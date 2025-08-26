# TravelCo Booking System

A modern, space-themed Django web application for booking flights, trains, and bus journeys with an immersive cosmic user interface.

[![Django](https://img.shields.io/badge/Django-4.x-092E20?style=for-the-badge&logo=django&logoColor=white)](https://djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org/)
[![Bootstrap](https://img.shields.io/badge/Bootstrap-5.3-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white)](https://getbootstrap.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](LICENSE)

---

## 🌟 Features

### ✨ Core Functionality
- **🎫 Multi-Modal Booking**: Book flights, trains, and bus journeys
- **🔐 User Authentication**: Secure signup, login, and logout
- **🔍 Smart Search & Filtering**: Find travel options by source, destination, and transport type
- **📅 Booking Management**: View, track, and cancel bookings
- **💳 Dynamic Pricing**: Real-time cost calculation with multiple seats
- **📱 Responsive Design**: Works seamlessly on desktop, tablet, and mobile

### 🎨 Design Features
- **⚡ Smooth Animations**: CSS3 animations and transitions for enhanced UX
- **🎯 Interactive Elements**: Hover effects, loading states, and micro-interactions
- **🎪 Modern Typography**: Google Fonts integration with Orbitron and Space Grotesk
- **🌈 Gradient UI**: Beautiful gradient backgrounds and buttons

---

## 📸 Screenshots

### 🏠 Home Page - Mission Control Center
<!-- Add screenshot here showing:
   - Navigation bar with cosmic branding
   - Search filters section
   - Travel options cards with gradient effects
   - Black hole inspired background
-->
*[Screenshot placeholder - Show the main dashboard with available travel options and search functionality]*

---

### 🔑 Authentication Pages
<!-- Add screenshots here showing:
   - Login page with floating labels and cosmic particles
   - Signup page with password strength indicator
   - Form validation states
-->
*[Screenshot placeholder - Show the login/signup forms with cosmic styling and interactive elements]*

---

### 🎫 Booking Process
<!-- Add screenshot here showing:
   - Mission overview with route visualization
   - Booking form with seat selector
   - Cost calculator and terms section
-->
*[Screenshot placeholder - Show the booking confirmation page with route visualization and cost breakdown]*

---

### 📱 My Bookings Dashboard
<!-- Add screenshot here showing:
   - List of user bookings
   - Booking status badges
   - Cancel booking functionality
-->
*[Screenshot placeholder - Show the user's booking history with status indicators and management options]*

---

## 🛠️ Technology Stack

| Technology | Purpose | Version |
|------------|---------|---------|
| **Django** | Backend Framework | 4.x |
| **Python** | Programming Language | 3.8+ |
| **SQLite** | Database | Default |
| **Bootstrap** | CSS Framework | 5.3.2 |
| **HTML5/CSS3** | Frontend | Latest |
| **JavaScript** | Client-side Logic | ES6+ |
| **Font Awesome** | Icons | 6.4.0 |
| **Google Fonts** | Typography | Orbitron, Space Grotesk |

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Tanishq4501/django-travel-booking.git
   cd django-travel-booking
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the database**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a superuser** (Optional)
   ```bash
   python manage.py createsuperuser
   ```

6. **Load sample data** (Optional)
   ```bash
   python manage.py loaddata sample_data.json
   ```

7. **Run the development server**
   ```bash
   python manage.py runserver
   ```

8. **Access the application**
   Open your browser and navigate to `http://127.0.0.1:8000`

---

## 📁 Project Structure

```
django-travel-booking/
│
├── 📁 travel_booking/          # Main project directory
│   ├── 📄 __init__.py
│   ├── 📄 settings.py         # Django settings
│   ├── 📄 urls.py            # Main URL configuration
│   └── 📄 wsgi.py            # WSGI configuration
│
├── 📁 booking/                # Main app directory
│   ├── 📁 migrations/        # Database migrations
│   ├── 📁 templates/         # HTML templates
│   │   ├── 📄 base.html      # Base template with cosmic theme
│   │   ├── 📄 home.html      # Homepage
│   │   ├── 📄 login.html     # Login page
│   │   ├── 📄 signup.html    # Registration page
│   │   ├── 📄 book_travel.html    # Booking page
│   │   └── 📄 my_bookings.html    # User bookings
│   ├── 📄 models.py          # Data models
│   ├── 📄 views.py           # View functions
│   ├── 📄 urls.py            # App URL patterns
│   └── 📄 forms.py           # Django forms
│
├── 📁 static/                # Static files (CSS, JS, images)
├── 📁 media/                 # Media files
├── 📄 manage.py              # Django management script
├── 📄 requirements.txt       # Python dependencies
└── 📄 README.md              # This file
```

---

## 🎮 Usage Guide

### 🏠 Home Page Navigation
1. **Browse Travel Options**: View all available flights, trains, and buses
2. **Filter Results**: Use the Mission Control Center to filter by:
   - Launch Point (Source)
   - Destination
   - Vessel Type (Flight/Train/Bus)
3. **Book Journey**: Click "Launch Mission" on any travel option

### 👤 User Management
1. **Create Account**: Click "Join Mission" to register
2. **Login**: Use "Launch In" to access your account
3. **Profile**: View your details in the navigation area

### 🎫 Booking Process
1. **Select Travel Option**: Choose from available missions
2. **Configure Booking**: 
   - Select number of crew members (seats)
   - Review mission details and route
   - Check cost breakdown
3. **Confirm Booking**: Complete the mission registration
4. **Track Bookings**: View all bookings in "My Journeys"

---

## 🎨 Customization

### Theme Configuration
The cosmic theme uses CSS custom properties for easy customization:

```css
:root {
    --cosmic-black: #0a0a0a;
    --void-black: #1a1a1a;
    --stellar-gray: #2d2d2d;
    --accent-blue: #64ffda;
    --accent-purple: #bb86fc;
    /* Modify these values to change the theme */
}
```

### Adding New Features
1. **Models**: Define new data models in `booking/models.py`
2. **Views**: Add view functions in `booking/views.py`
3. **Templates**: Create HTML templates in `booking/templates/`
4. **URLs**: Configure routing in `booking/urls.py`

---

## 🔧 Configuration

### Environment Variables
Create a `.env` file in the root directory:

```env
DEBUG=True
SECRET_KEY=your-secret-key-here
DATABASE_URL=sqlite:///db.sqlite3
ALLOWED_HOSTS=localhost,127.0.0.1
```

### Database Configuration
By default, the project uses SQLite. To use PostgreSQL or MySQL:

1. Install the appropriate database adapter
2. Update `DATABASES` in `settings.py`
3. Run migrations: `python manage.py migrate`

---

## 🧪 Testing

Run the test suite:
```bash
python manage.py test
```

Run with coverage:
```bash
pip install coverage
coverage run manage.py test
coverage report
```

---

## 🚀 Deployment

### Heroku Deployment
1. Install Heroku CLI
2. Create a Heroku app: `heroku create your-app-name`
3. Set environment variables: `heroku config:set DEBUG=False`
4. Deploy: `git push heroku main`

### Docker Deployment
```dockerfile
# Dockerfile example
FROM python:3.9
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
```

---

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/AmazingFeature`
3. **Commit changes**: `git commit -m 'Add some AmazingFeature'`
4. **Push to branch**: `git push origin feature/AmazingFeature`
5. **Open a Pull Request**

### Development Guidelines
- Follow PEP 8 style guide
- Write descriptive commit messages
- Add tests for new features
- Update documentation as needed

---

## 🐛 Known Issues

- [ ] Mobile responsiveness could be improved on very small screens
- [ ] Date picker styling needs refinement
- [ ] Search functionality could include more advanced filters

---

## 🗺️ Roadmap

### Phase 1 (Current)
- [x] Basic booking functionality
- [x] User authentication
- [x] Responsive design
- [x] Cosmic theme implementation

### Phase 2 (Planned)
- [ ] Payment integration
- [ ] Email notifications
- [ ] Advanced search filters
- [ ] Booking history export
- [ ] Multi-language support

### Phase 3 (Future)
- [ ] Real-time seat availability
- [ ] Interactive route maps
- [ ] Mobile app development
- [ ] AI-powered recommendations
- [ ] Social sharing features

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

**Tanishq**
- GitHub: [@Tanishq4501](https://github.com/Tanishq4501)
- Email: [tanishqchoudhary5689@gmail.com]

---

## 🙏 Acknowledgments

- Django community for the amazing framework
- Bootstrap team for the responsive CSS framework
- Font Awesome for the beautiful icons
- Google Fonts for the typography
- All contributors and testers

---

## 📞 Support

If you encounter any issues or have questions:

1. Check the [Issues](https://github.com/Tanishq4501/django-travel-booking/issues) page
2. Create a new issue with detailed information
3. Join our community discussions
4. Email support: [tanishqchoudhary5689@gmail.com]

---

## ⭐ Show Your Support

If this project helped you, please consider giving it a ⭐ star on GitHub!

---

<div align="center">

**🌌 Made with ❤️ and cosmic inspiration 🚀**

*Embark on extraordinary journeys across the universe*

</div>
