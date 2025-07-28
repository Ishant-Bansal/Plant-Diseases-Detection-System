# PlantCare AI - Plant Disease Detection System

A comprehensive web application for detecting plant diseases using artificial intelligence. Built with Flask, TensorFlow, and modern web technologies.

## 🌱 Features

- **AI-Powered Detection**: Advanced machine learning model to identify 38 different plant diseases
- **Instant Results**: Get disease diagnosis and confidence scores within seconds
- **Comprehensive Guide**: Detailed information about diseases, symptoms, and treatments
- **Responsive Design**: Works seamlessly on desktop, tablet, and mobile devices
- **User-Friendly Interface**: Modern, intuitive design with drag-and-drop file upload
- **Treatment Recommendations**: Do's and Don'ts for each detected disease

## 🚀 Supported Plants & Diseases

### Plants Covered:
- **Apple**: Scab, Black Rot, Cedar Apple Rust
- **Tomato**: Early Blight, Late Blight, Bacterial Spot, Leaf Mold
- **Potato**: Early Blight, Late Blight
- **Grape**: Black Rot, Leaf Blight, Esca
- **Corn**: Common Rust, Northern Leaf Blight, Gray Leaf Spot
- **Cherry**: Powdery Mildew
- **Peach**: Bacterial Spot
- **Pepper**: Bacterial Spot
- **Squash**: Powdery Mildew
- **Strawberry**: Leaf Scorch
- And many more...

## 🛠️ Technology Stack

### Backend:
- **Flask**: Python web framework
- **TensorFlow/Keras**: Machine learning model
- **NumPy**: Numerical computing
- **Pillow**: Image processing

### Frontend:
- **Bootstrap 5**: Responsive CSS framework
- **Font Awesome**: Icons
- **JavaScript**: Interactive features
- **HTML5/CSS3**: Modern web standards

### AI Model:
- **Architecture**: Convolutional Neural Network (CNN)
- **Input Size**: 128x128 pixels
- **Classes**: 38 plant diseases
- **Accuracy**: High precision detection

## 📦 Installation

### Prerequisites:
- Python 3.8 or higher
- pip (Python package installer)

### Step 1: Clone the Repository
```bash
git clone <repository-url>
cd plant-disease-detection
```

### Step 2: Create Virtual Environment
```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Run the Application
```bash
python app.py
```

The application will be available at `http://localhost:5000`

## 🎯 Usage

### 1. Home Page
- Learn about the system features
- View supported plants
- Access quick links to detection

### 2. Disease Detection
- Upload a plant leaf image
- Drag and drop or click to browse
- Get instant AI analysis
- View confidence scores and recommendations

### 3. Disease Guide
- Browse all supported diseases
- Search and filter by plant type
- Get detailed information about each disease

### 4. About & Contact
- Learn about the technology stack
- Contact support team
- Access FAQ section

## 📁 Project Structure

```
plant-disease-detection/
├── app.py                 # Main Flask application
├── disease_info.py        # Disease information dictionary
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
├── Plant_disease_model.h5 # Trained AI model
├── static/               # Static files
│   ├── style.css        # Custom CSS styles
│   ├── script.js        # JavaScript functionality
│   └── uploads/         # Uploaded images (auto-created)
├── templates/           # HTML templates
│   ├── base.html       # Base template
│   ├── home.html       # Home page
│   ├── predict.html    # Detection page
│   ├── diseases.html   # Disease guide
│   ├── disease_detail.html # Individual disease page
│   ├── about.html      # About page
│   ├── contact.html    # Contact page
│   └── faq.html        # FAQ page
└── DATASET/        https://www.kaggle.com/datasets/emmarex/plantdisease
    └── plantvillage/         # Plant disease images
```

## 🔧 Configuration

### Environment Variables
Create a `.env` file in the root directory:
```env
FLASK_ENV=development
SECRET_KEY=your-secret-key-here
UPLOAD_FOLDER=static/uploads
```

### Model Configuration
- The AI model is pre-trained and ready to use
- Model file: `Plant_disease_model.h5`
- Input image size: 128x128 pixels
- Supported formats: JPG, PNG, GIF, BMP, TIFF

## 📊 API Endpoints

### Web Routes:
- `GET /` - Home page
- `GET /predict` - Disease detection page
- `POST /predict` - Process image upload
- `GET /diseases` - Disease guide
- `GET /disease/<key>` - Individual disease details
- `GET /about` - About page
- `GET /contact` - Contact page
- `POST /contact` - Submit contact form
- `GET /faq` - FAQ page

### API Endpoints:
- `POST /api/predict` - JSON API for predictions

## 🎨 Customization

### Styling
- Modify `static/style.css` for custom styling
- Update color variables in CSS root
- Customize Bootstrap components

### Content
- Edit `disease_info.py` to add/modify diseases
- Update templates for content changes
- Modify JavaScript in `static/script.js`

### Model
- Replace `Plant_disease_model.h5` with your trained model
- Update class names in `app.py`
- Adjust image preprocessing as needed

## 🚀 Deployment

### Local Development:
```bash
python app.py
```

### Production Deployment:
1. Set up a production WSGI server (Gunicorn)
2. Configure environment variables
3. Set up reverse proxy (Nginx)
4. Enable HTTPS
5. Configure static file serving

### Docker Deployment:
```dockerfile
FROM python:3.9-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 5000
CMD ["python", "app.py"]
```

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Plant disease dataset contributors
- TensorFlow and Keras communities
- Bootstrap and Font Awesome teams
- Flask development community

## 📞 Support

For support and questions:
- Email: ishantbansal510@gmail.com
- Documentation: Check the FAQ page

## 🔮 Future Enhancements

- Mobile app development
- Real-time monitoring
- Weather integration
- Community features
- Advanced analytics
- Multi-language support

---

**PlantCare AI** - Empowering farmers with AI-driven plant health monitoring 🌱🤖 
