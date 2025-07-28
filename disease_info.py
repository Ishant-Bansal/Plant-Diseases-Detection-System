# Disease Information Dictionary
# Contains detailed information about common plant diseases

DISEASE_INFO = {
    'Apple___Apple_scab': {
        'name': 'Apple Scab',
        'description': 'A fungal disease caused by Venturia inaequalis that affects apple trees, causing dark, scabby lesions on leaves and fruit.',
        'symptoms': [
            'Dark, olive-green to brown spots on leaves',
            'Scabby, corky lesions on fruit',
            'Distorted or stunted fruit growth',
            'Premature leaf drop in severe cases'
        ],
        'dos': [
            'Remove and destroy fallen leaves and infected fruit',
            'Apply fungicides during the growing season',
            'Prune trees to improve air circulation',
            'Plant resistant apple varieties',
            'Maintain proper tree spacing'
        ],
        'donts': [
            'Don\'t leave fallen leaves on the ground over winter',
            'Don\'t plant susceptible varieties in wet areas',
            'Don\'t overhead water trees',
            'Don\'t ignore early symptoms'
        ],
        'severity': 'Moderate to High',
        'treatment': 'Fungicide application and cultural practices'
    },
    
    'Apple___Black_rot': {
        'name': 'Apple Black Rot',
        'description': 'A fungal disease caused by Botryosphaeria obtusa that affects apple trees, causing fruit rot and cankers on branches.',
        'symptoms': [
            'Circular, sunken lesions on fruit',
            'Black, mummified fruit',
            'Cankers on branches and trunk',
            'Yellowing and browning of leaves'
        ],
        'dos': [
            'Remove and destroy infected fruit and branches',
            'Prune out cankers during dormancy',
            'Apply fungicides during bloom',
            'Maintain tree vigor through proper fertilization',
            'Control insect pests that create wounds'
        ],
        'donts': [
            'Don\'t leave mummified fruit on trees',
            'Don\'t make pruning cuts during wet weather',
            'Don\'t over-fertilize with nitrogen',
            'Don\'t ignore branch cankers'
        ],
        'severity': 'High',
        'treatment': 'Pruning, fungicides, and cultural control'
    },
    
    'Apple___Cedar_apple_rust': {
        'name': 'Cedar Apple Rust',
        'description': 'A fungal disease caused by Gymnosporangium juniperi-virginianae that requires both apple trees and cedar trees to complete its life cycle.',
        'symptoms': [
            'Bright orange-yellow spots on leaves',
            'Circular lesions with red borders',
            'Orange gelatinous growths on cedar trees',
            'Fruit deformation and drop'
        ],
        'dos': [
            'Remove cedar trees within 2 miles if possible',
            'Apply fungicides during spring',
            'Plant resistant apple varieties',
            'Prune to improve air circulation',
            'Monitor for early symptoms'
        ],
        'donts': [
            'Don\'t plant apple trees near cedar trees',
            'Don\'t ignore cedar galls in the area',
            'Don\'t apply fungicides too late',
            'Don\'t plant susceptible varieties'
        ],
        'severity': 'Moderate',
        'treatment': 'Fungicides and cultural practices'
    },
    
    'Potato___Early_blight': {
        'name': 'Potato Early Blight',
        'description': 'A fungal disease caused by Alternaria solani that affects potato plants, causing dark brown lesions on leaves and stems.',
        'symptoms': [
            'Dark brown, target-like lesions on leaves',
            'Concentric rings in lesions',
            'Yellowing and death of lower leaves',
            'Lesions on stems and tubers'
        ],
        'dos': [
            'Remove and destroy infected plant debris',
            'Apply fungicides preventively',
            'Maintain adequate plant spacing',
            'Use certified disease-free seed',
            'Rotate crops annually'
        ],
        'donts': [
            'Don\'t overhead water plants',
            'Don\'t plant in poorly drained soil',
            'Don\'t ignore early symptoms',
            'Don\'t save seed from infected plants'
        ],
        'severity': 'Moderate',
        'treatment': 'Fungicides and cultural practices'
    },
    
    'Potato___Late_blight': {
        'name': 'Potato Late Blight',
        'description': 'A devastating fungal disease caused by Phytophthora infestans that can rapidly destroy entire potato crops.',
        'symptoms': [
            'Water-soaked lesions on leaves',
            'White fungal growth on leaf undersides',
            'Rapid leaf death and defoliation',
            'Brown, firm rot on tubers'
        ],
        'dos': [
            'Apply fungicides preventively',
            'Remove infected plants immediately',
            'Use resistant potato varieties',
            'Ensure good air circulation',
            'Monitor weather conditions'
        ],
        'donts': [
            'Don\'t plant in wet, cool conditions',
            'Don\'t overhead water during outbreaks',
            'Don\'t ignore early symptoms',
            'Don\'t save tubers from infected plants'
        ],
        'severity': 'Very High',
        'treatment': 'Immediate fungicide application and removal of infected plants'
    },
    
    'Tomato___Early_blight': {
        'name': 'Tomato Early Blight',
        'description': 'A fungal disease caused by Alternaria solani that affects tomato plants, causing dark brown lesions and defoliation.',
        'symptoms': [
            'Dark brown, target-like spots on leaves',
            'Concentric rings in lesions',
            'Yellowing and death of lower leaves',
            'Lesions on stems and fruit'
        ],
        'dos': [
            'Remove infected leaves and debris',
            'Apply fungicides preventively',
            'Mulch around plants',
            'Avoid overhead watering',
            'Use resistant varieties'
        ],
        'donts': [
            'Don\'t water from above',
            'Don\'t plant too close together',
            'Don\'t ignore early symptoms',
            'Don\'t save seed from infected plants'
        ],
        'severity': 'Moderate',
        'treatment': 'Fungicides and cultural practices'
    },
    
    'Tomato___Late_blight': {
        'name': 'Tomato Late Blight',
        'description': 'A devastating fungal disease caused by Phytophthora infestans that can rapidly destroy tomato crops.',
        'symptoms': [
            'Water-soaked, gray-green lesions',
            'White fungal growth on leaf undersides',
            'Rapid leaf death and defoliation',
            'Firm, brown rot on fruit'
        ],
        'dos': [
            'Remove infected plants immediately',
            'Apply fungicides preventively',
            'Use resistant varieties',
            'Ensure good air circulation',
            'Monitor weather conditions'
        ],
        'donts': [
            'Don\'t plant in wet, cool conditions',
            'Don\'t overhead water during outbreaks',
            'Don\'t ignore early symptoms',
            'Don\'t save seed from infected plants'
        ],
        'severity': 'Very High',
        'treatment': 'Immediate fungicide application and removal of infected plants'
    },
    
    'Tomato___Bacterial_spot': {
        'name': 'Tomato Bacterial Spot',
        'description': 'A bacterial disease caused by Xanthomonas spp. that affects tomato plants, causing small, dark lesions on leaves and fruit.',
        'symptoms': [
            'Small, dark, water-soaked spots on leaves',
            'Yellow halos around lesions',
            'Lesions on stems and fruit',
            'Fruit deformation and drop'
        ],
        'dos': [
            'Use certified disease-free seed',
            'Apply copper-based bactericides',
            'Remove infected plants',
            'Avoid overhead watering',
            'Rotate crops'
        ],
        'donts': [
            'Don\'t work in wet fields',
            'Don\'t save seed from infected plants',
            'Don\'t overhead water',
            'Don\'t ignore early symptoms'
        ],
        'severity': 'High',
        'treatment': 'Bactericides and cultural practices'
    },
    
    'Grape___Black_rot': {
        'name': 'Grape Black Rot',
        'description': 'A fungal disease caused by Guignardia bidwellii that affects grapevines, causing fruit rot and leaf spots.',
        'symptoms': [
            'Circular, tan lesions on leaves',
            'Black, shriveled berries',
            'Hard, black mummies on clusters',
            'Reddish-brown lesions on shoots'
        ],
        'dos': [
            'Remove and destroy infected plant parts',
            'Apply fungicides during growing season',
            'Prune to improve air circulation',
            'Use resistant varieties',
            'Monitor for early symptoms'
        ],
        'donts': [
            'Don\'t leave mummified berries on vines',
            'Don\'t plant in poorly drained soil',
            'Don\'t overhead water',
            'Don\'t ignore early symptoms'
        ],
        'severity': 'High',
        'treatment': 'Fungicides and cultural practices'
    },
    
    'Corn_(maize)___Common_rust_': {
        'name': 'Corn Common Rust',
        'description': 'A fungal disease caused by Puccinia sorghi that affects corn plants, causing reddish-brown pustules on leaves.',
        'symptoms': [
            'Reddish-brown pustules on leaves',
            'Circular to oval lesions',
            'Yellow halos around lesions',
            'Premature leaf death'
        ],
        'dos': [
            'Plant resistant hybrids',
            'Apply fungicides if needed',
            'Monitor for early symptoms',
            'Maintain proper plant spacing',
            'Rotate crops'
        ],
        'donts': [
            'Don\'t plant susceptible varieties',
            'Don\'t ignore early symptoms',
            'Don\'t plant too close together',
            'Don\'t save seed from infected plants'
        ],
        'severity': 'Moderate',
        'treatment': 'Resistant varieties and fungicides'
    },
    
    'Cherry_(including_sour)___Powdery_mildew': {
        'name': 'Cherry Powdery Mildew',
        'description': 'A fungal disease caused by Podosphaera clandestina that affects cherry trees, causing white powdery growth on leaves and fruit.',
        'symptoms': [
            'White powdery growth on leaves',
            'Distorted and stunted leaves',
            'Reduced fruit quality',
            'Premature leaf drop'
        ],
        'dos': [
            'Apply fungicides during growing season',
            'Prune to improve air circulation',
            'Remove infected plant parts',
            'Use resistant varieties',
            'Monitor for early symptoms'
        ],
        'donts': [
            'Don\'t plant in shady, humid areas',
            'Don\'t overhead water',
            'Don\'t ignore early symptoms',
            'Don\'t plant susceptible varieties'
        ],
        'severity': 'Moderate',
        'treatment': 'Fungicides and cultural practices'
    },
    
    'Peach___Bacterial_spot': {
        'name': 'Peach Bacterial Spot',
        'description': 'A bacterial disease caused by Xanthomonas arboricola that affects peach trees, causing lesions on leaves, fruit, and twigs.',
        'symptoms': [
            'Small, angular lesions on leaves',
            'Corky, scabby lesions on fruit',
            'Lesions on twigs and branches',
            'Fruit deformation and drop'
        ],
        'dos': [
            'Apply copper-based bactericides',
            'Prune infected branches',
            'Use resistant varieties',
            'Maintain tree vigor',
            'Monitor for early symptoms'
        ],
        'donts': [
            'Don\'t work in wet conditions',
            'Don\'t overhead water',
            'Don\'t ignore early symptoms',
            'Don\'t plant susceptible varieties'
        ],
        'severity': 'High',
        'treatment': 'Bactericides and cultural practices'
    },
    
    'Pepper,_bell___Bacterial_spot': {
        'name': 'Bell Pepper Bacterial Spot',
        'description': 'A bacterial disease caused by Xanthomonas spp. that affects pepper plants, causing small, dark lesions on leaves and fruit.',
        'symptoms': [
            'Small, dark, water-soaked spots',
            'Yellow halos around lesions',
            'Lesions on stems and fruit',
            'Fruit deformation and drop'
        ],
        'dos': [
            'Use certified disease-free seed',
            'Apply copper-based bactericides',
            'Remove infected plants',
            'Avoid overhead watering',
            'Rotate crops'
        ],
        'donts': [
            'Don\'t work in wet fields',
            'Don\'t save seed from infected plants',
            'Don\'t overhead water',
            'Don\'t ignore early symptoms'
        ],
        'severity': 'High',
        'treatment': 'Bactericides and cultural practices'
    },
    
    'Squash___Powdery_mildew': {
        'name': 'Squash Powdery Mildew',
        'description': 'A fungal disease caused by Podosphaera xanthii that affects squash plants, causing white powdery growth on leaves.',
        'symptoms': [
            'White powdery growth on leaves',
            'Yellowing and death of leaves',
            'Reduced fruit quality',
            'Premature plant death'
        ],
        'dos': [
            'Apply fungicides during growing season',
            'Remove infected plant parts',
            'Use resistant varieties',
            'Maintain proper spacing',
            'Monitor for early symptoms'
        ],
        'donts': [
            'Don\'t plant in shady, humid areas',
            'Don\'t overhead water',
            'Don\'t ignore early symptoms',
            'Don\'t plant susceptible varieties'
        ],
        'severity': 'Moderate',
        'treatment': 'Fungicides and cultural practices'
    },
    
    'Strawberry___Leaf_scorch': {
        'name': 'Strawberry Leaf Scorch',
        'description': 'A fungal disease caused by Diplocarpon earliana that affects strawberry plants, causing reddish-purple lesions on leaves.',
        'symptoms': [
            'Reddish-purple lesions on leaves',
            'Dark spots with purple borders',
            'Yellowing and death of leaves',
            'Reduced fruit quality'
        ],
        'dos': [
            'Remove infected leaves',
            'Apply fungicides during growing season',
            'Use resistant varieties',
            'Maintain proper spacing',
            'Monitor for early symptoms'
        ],
        'donts': [
            'Don\'t overhead water',
            'Don\'t plant too close together',
            'Don\'t ignore early symptoms',
            'Don\'t plant susceptible varieties'
        ],
        'severity': 'Moderate',
        'treatment': 'Fungicides and cultural practices'
    }
}

# Healthy plant information
HEALTHY_PLANTS = {
    'Apple___healthy': {
        'name': 'Healthy Apple',
        'description': 'This apple tree shows no signs of disease and is in good health.',
        'care_tips': [
            'Maintain regular watering schedule',
            'Apply balanced fertilizer in spring',
            'Prune annually for shape and health',
            'Monitor for pests and diseases',
            'Ensure good air circulation'
        ]
    },
    'Potato___healthy': {
        'name': 'Healthy Potato',
        'description': 'This potato plant shows no signs of disease and is growing well.',
        'care_tips': [
            'Maintain consistent soil moisture',
            'Hill soil around plants as they grow',
            'Monitor for pests and diseases',
            'Harvest when foliage begins to yellow',
            'Store in cool, dark conditions'
        ]
    },
    'Tomato___healthy': {
        'name': 'Healthy Tomato',
        'description': 'This tomato plant shows no signs of disease and is thriving.',
        'care_tips': [
            'Provide consistent watering',
            'Support plants with cages or stakes',
            'Remove suckers for indeterminate varieties',
            'Monitor for pests and diseases',
            'Harvest when fruit is fully colored'
        ]
    }
} 