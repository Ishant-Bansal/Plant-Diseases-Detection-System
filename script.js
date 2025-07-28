// PlantCare AI - Main JavaScript File

document.addEventListener('DOMContentLoaded', function() {
    // Initialize all components
    initAnimations();
    initFormValidation();
    initTooltips();
    initScrollEffects();
    initFileUpload(); // <-- Yeh line add karo!
});

// Animation Functions
function initAnimations() {
    // Fade in elements on scroll
    const observerOptions = {
        threshold: 0.1,
        rootMargin: '0px 0px -50px 0px'
    };

    const observer = new IntersectionObserver(function(entries) {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                entry.target.classList.add('fade-in-up');
            }
        });
    }, observerOptions);

    // Observe elements for animation
    document.querySelectorAll('.feature-card, .step-card, .plant-card, .tech-card, .info-card').forEach(el => {
        observer.observe(el);
    });
}

// Form Validation
function initFormValidation() {
    const forms = document.querySelectorAll('form');
    
    forms.forEach(form => {
        form.addEventListener('submit', function(e) {
            if (!form.checkValidity()) {
                e.preventDefault();
                e.stopPropagation();
            }
            form.classList.add('was-validated');
        });
    });
}

// Tooltips
function initTooltips() {
    const tooltipTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="tooltip"]'));
    tooltipTriggerList.map(function (tooltipTriggerEl) {
        return new bootstrap.Tooltip(tooltipTriggerEl);
    });
}

// Scroll Effects
function initScrollEffects() {
    // Navbar background on scroll
    window.addEventListener('scroll', function() {
        const navbar = document.querySelector('.navbar');
        if (window.scrollY > 50) {
            navbar.classList.add('navbar-scrolled');
        } else {
            navbar.classList.remove('navbar-scrolled');
        }
    });

    // Smooth scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
}

// File Upload Functions
function initFileUpload() {
    const fileInput = document.getElementById('fileInput');
    const uploadArea = document.getElementById('uploadArea');
    const submitBtn = document.getElementById('submitBtn');

    if (fileInput && uploadArea) {
        // File input change handler
        fileInput.addEventListener('change', function(e) {
            const file = e.target.files[0];
            if (file) {
                updateUploadArea(file);
                if (submitBtn) submitBtn.disabled = false;
            }
        });

        // Drag and drop functionality
        uploadArea.addEventListener('dragover', function(e) {
            e.preventDefault();
            uploadArea.classList.add('dragover');
        });

        uploadArea.addEventListener('dragleave', function(e) {
            e.preventDefault();
            uploadArea.classList.remove('dragover');
        });

        uploadArea.addEventListener('drop', function(e) {
            e.preventDefault();
            e.stopPropagation();
            const files = e.dataTransfer.files;
            if (files && files.length > 0) {
                fileInput.files = files;
                fileInput.dispatchEvent(new Event('change', { bubbles: true }));
            }
            uploadArea.classList.remove('dragover');
        });
    }
}

function updateUploadArea(file) {
    // Sirf file ka naam update karo
    const fileName = document.getElementById('fileName');
    if (fileName) {
        fileName.innerText = file.name;
    }
}

function resetUpload() {
    const fileInput = document.getElementById('fileInput');
    const uploadArea = document.getElementById('uploadArea');
    const submitBtn = document.getElementById('submitBtn');
    
    if (fileInput) fileInput.value = '';
    if (submitBtn) submitBtn.disabled = true;
    
    if (uploadArea) {
        uploadArea.innerHTML = `
            <div class="upload-content text-center">
                <i class="fas fa-cloud-upload-alt upload-icon"></i>
                <h4>Upload Plant Image</h4>
                <p class="text-muted">Drag and drop your image here or click to browse</p>
                <p id="fileName" style="color: #888; font-size: 0.95em; margin-bottom: 0.5em;"></p>
                <input type="file" name="file" id="fileInput" class="file-input" accept="image/*" required>
                <label for="fileInput" class="btn btn-primary">
                    <i class="fas fa-upload me-2"></i>Choose Image
                </label>
            </div>
        `;
    }
}

// Search and Filter Functions
function initSearchFilter() {
    const searchInput = document.getElementById('searchInput');
    const filterSelect = document.getElementById('filterSelect');
    const diseaseCards = document.querySelectorAll('.disease-card');
    const noResults = document.getElementById('noResults');

    function filterDiseases() {
        const searchTerm = searchInput ? searchInput.value.toLowerCase() : '';
        const filterValue = filterSelect ? filterSelect.value.toLowerCase() : '';
        let visibleCount = 0;

        diseaseCards.forEach(card => {
            const diseaseName = card.dataset.name || '';
            const plantType = card.dataset.plant || '';
            
            const matchesSearch = diseaseName.includes(searchTerm);
            const matchesFilter = !filterValue || plantType.includes(filterValue);
            
            if (matchesSearch && matchesFilter) {
                card.style.display = 'block';
                visibleCount++;
            } else {
                card.style.display = 'none';
            }
        });

        // Show/hide no results message
        if (noResults) {
            if (visibleCount === 0) {
                noResults.classList.remove('d-none');
            } else {
                noResults.classList.add('d-none');
            }
        }
    }

    if (searchInput) searchInput.addEventListener('input', filterDiseases);
    if (filterSelect) filterSelect.addEventListener('change', filterDiseases);
}

// Loading States
function showLoading(element) {
    if (element) {
        element.classList.add('loading');
        element.disabled = true;
    }
}

function hideLoading(element) {
    if (element) {
        element.classList.remove('loading');
        element.disabled = false;
    }
}

// Alert Functions
function showAlert(message, type = 'info') {
    const alertContainer = document.createElement('div');
    alertContainer.className = `alert alert-${type} alert-dismissible fade show`;
    alertContainer.innerHTML = `
        ${message}
        <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
    `;
    
    // Insert at the top of the main content
    const mainContent = document.querySelector('.main-content');
    if (mainContent) {
        mainContent.insertBefore(alertContainer, mainContent.firstChild);
    }
    
    // Auto dismiss after 5 seconds
    setTimeout(() => {
        if (alertContainer.parentNode) {
            alertContainer.remove();
        }
    }, 5000);
}

// Utility Functions
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

function throttle(func, limit) {
    let inThrottle;
    return function() {
        const args = arguments;
        const context = this;
        if (!inThrottle) {
            func.apply(context, args);
            inThrottle = true;
            setTimeout(() => inThrottle = false, limit);
        }
    };
}

// Initialize components when DOM is ready
document.addEventListener('DOMContentLoaded', function() {
    initFileUpload();
    initSearchFilter();
    
    // Add loading states to forms
    document.querySelectorAll('form').forEach(form => {
        form.addEventListener('submit', function() {
            const submitBtn = form.querySelector('button[type="submit"]');
            if (submitBtn) {
                showLoading(submitBtn);
                submitBtn.innerHTML = '<i class="fas fa-spinner fa-spin me-2"></i>Processing...';
            }
        });
    });
});

// Export functions for global use
window.PlantCareAI = {
    showAlert,
    showLoading,
    hideLoading,
    resetUpload,
    debounce,
    throttle
}; 