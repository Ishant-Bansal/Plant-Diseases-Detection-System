from flask import Flask, request, render_template, redirect, url_for, flash, jsonify
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import os
import uuid
from werkzeug.utils import secure_filename
from disease_info import DISEASE_INFO, HEALTHY_PLANTS
import re

app = Flask(__name__)
app.secret_key = 'your-secret-key-here'

# Configuration
UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'bmp', 'tiff'}

# Create upload folder if it doesn't exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Load the pre-trained model
model = load_model("Plant_disease_model.h5")

# Class names (same as your original)
class_names = [
    'Apple___Apple_scab', 'Apple___Black_rot', 'Apple___Cedar_apple_rust', 'Apple___healthy',
    'Blueberry___healthy', 'Cherry_(including_sour)___healthy', 'Cherry_(including_sour)___Powdery_mildew',
    'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot', 'Corn_(maize)___Common_rust_',
    'Corn_(maize)___healthy', 'Corn_(maize)___Northern_Leaf_Blight', 'Grape___Black_rot',
    'Grape___Esca_(Black_Measles)', 'Grape___healthy', 'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)',
    'Orange___Haunglongbing_(Citrus_greening)', 'Peach___Bacterial_spot', 'Peach___healthy',
    'Pepper,_bell___Bacterial_spot', 'Pepper,_bell___healthy', 'Potato___Early_blight',
    'Potato___healthy', 'Potato___Late_blight', 'Raspberry___healthy', 'Soybean___healthy',
    'Squash___Powdery_mildew', 'Strawberry___healthy', 'Strawberry___Leaf_scorch',
    'Tomato___Bacterial_spot', 'Tomato___Early_blight', 'Tomato___healthy', 'Tomato___Late_blight',
    'Tomato___Leaf_Mold', 'Tomato___Septoria_leaf_spot', 'Tomato___Spider_mites Two-spotted_spider_mite',
    'Tomato___Target_Spot', 'Tomato___Tomato_mosaic_virus', 'Tomato___Tomato_Yellow_Leaf_Curl_Virus'
]

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def predict_disease(image_path):
    """Predict disease from image using the loaded model"""
    try:
        # Load and preprocess image
        img = image.load_img(image_path, target_size=(128, 128))
        img_array = image.img_to_array(img) / 255.0
        img_array = np.expand_dims(img_array, axis=0)
        
        # Make prediction
        prediction_array = model.predict(img_array)
        predicted_class = class_names[np.argmax(prediction_array)]
        confidence = float(np.max(prediction_array)) * 100
        
        return predicted_class, confidence
    except Exception as e:
        return None, 0

def parse_response(text):
    description = re.search(r"Description:(.*?)(?:Severity:|$)", text, re.DOTALL)
    severity = re.search(r"Severity:(.*?)(?:Do's:|$)", text, re.DOTALL)
    dos = re.search(r"Do's:(.*?)(?:Don'ts:|$)", text, re.DOTALL)
    donts = re.search(r"Don'ts:(.*?)(?:Treatment:|$)", text, re.DOTALL)
    treatment = re.search(r"Treatment:(.*)", text, re.DOTALL)

    def clean(val):
        return val.group(1).strip() if val else ""

    dos_list = [d.strip('- ').strip() for d in clean(dos).split('\n') if d.strip()] if dos else []
    donts_list = [d.strip('- ').strip() for d in clean(donts).split('\n') if d.strip()] if donts else []

    return {
        "description": clean(description),
        "severity": clean(severity),
        "dos": dos_list,
        "donts": donts_list,
        "treatment": clean(treatment)
    }

@app.route('/')
def home():
    """Home page with introduction and call to action"""
    return render_template('home.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    """Prediction page with image upload and results"""
    prediction = None
    confidence = 0
    disease_info = None
    img_path = None
    error = None
    
    if request.method == 'POST':
        # Check if file was uploaded
        if 'file' not in request.files:
            error = 'No file selected'
            return render_template('predict.html', error=error)
        
        file = request.files['file']
        
        # Check if file is empty
        if file.filename == '':
            error = 'No file selected'
            return render_template('predict.html', error=error)
        
        # Check if file is allowed
        if file and allowed_file(file.filename):
            # Generate unique filename
            filename = secure_filename(file.filename)
            unique_filename = f"{uuid.uuid4()}_{filename}"
            img_path = f"uploads/{unique_filename}"  # Only uploads/filename, not static/uploads/filename
            
            # Save file
            file.save(os.path.join(UPLOAD_FOLDER, unique_filename))
            
            # Make prediction
            full_img_path = os.path.join('static', img_path)
            prediction, confidence = predict_disease(full_img_path)
            
            if prediction:
                # Get disease information
                if prediction in DISEASE_INFO:
                    disease_info = DISEASE_INFO[prediction]
                elif prediction in HEALTHY_PLANTS:
                    disease_info = HEALTHY_PLANTS[prediction]
                else:
                    disease_info = {
                        'name': prediction.replace('___', ' - '),
                        'description': 'Disease information not available.',
                        'dos': ['Consult with a plant expert'],
                        'donts': ['Don\'t ignore the symptoms'],
                        'severity': 'Unknown',
                        'treatment': 'Consult with a plant expert'
                    }
            else:
                error = 'Error processing image. Please try again.'
        else:
            error = 'Invalid file type. Please upload an image file (PNG, JPG, JPEG, GIF, BMP, TIFF).'
    
    return render_template('predict.html', 
                         prediction=prediction, 
                         confidence=confidence, 
                         disease_info=disease_info, 
                         img_path=img_path, 
                         error=error)

@app.route('/diseases')
def diseases():
    """Diseases information page"""
    # Get all diseases from the dictionary
    all_diseases = list(DISEASE_INFO.keys())
    return render_template('diseases.html', diseases=all_diseases, disease_info=DISEASE_INFO)

@app.route('/disease/<disease_key>')
def disease_detail(disease_key):
    """Individual disease detail page"""
    if disease_key in DISEASE_INFO:
        disease = DISEASE_INFO[disease_key]
        return render_template('disease_detail.html', disease=disease, disease_key=disease_key)
    else:
        flash('Disease not found', 'error')
        return redirect(url_for('diseases'))

@app.route('/about')
def about():
    """About page with project details"""
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    """Contact page with contact form"""
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        message = request.form.get('message')
        
        # Here you would typically save to database or send email
        # For now, we'll just flash a success message
        flash('Thank you for your message! We will get back to you soon.', 'success')
        return redirect(url_for('contact'))
    
    return render_template('contact.html')

@app.route('/faq')
def faq():
    """FAQ page"""
    return render_template('faq.html')

@app.route('/api/predict', methods=['POST'])
def api_predict():
    """API endpoint for predictions"""
    if 'file' not in request.files:
        return jsonify({'error': 'No file provided'}), 400
    
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No file selected'}), 400
    
    if file and allowed_file(file.filename):
        # Generate unique filename
        filename = secure_filename(file.filename)
        unique_filename = f"{uuid.uuid4()}_{filename}"
        img_path = os.path.join(UPLOAD_FOLDER, unique_filename)
        
        # Save file
        file.save(img_path)
        
        # Make prediction
        full_img_path = os.path.join('static', img_path)
        prediction, confidence = predict_disease(full_img_path)
        
        if prediction:
            return jsonify({
                'prediction': prediction,
                'confidence': confidence,
                'image_path': img_path
            })
        else:
            return jsonify({'error': 'Error processing image'}), 500
    else:
        return jsonify({'error': 'Invalid file type'}), 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
