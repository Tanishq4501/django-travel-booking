<div align="center">

# 🚀 TravelCo - Django Booking Platform

**A modern, full-stack travel booking application built with Django, featuring a stunning dark-themed interface styled with Tailwind CSS. Deployed live on Render.**

![TravelCo Banner](https://placehold.co/1200x400/0a0a0a/e5e7eb?text=TravelCo&font=manrope)

</div>

<p align="center">
  <a href="https://django-travel-booking.onrender.com/" target="_blank"><img src="https://img.shields.io/badge/Live_Demo-Visit_Site-brightgreen?style=for-the-badge&logo=render" alt="Live Demo"></a>
  <img src="https://img.shields.io/badge/Django-5.x-092E20?style=for-the-badge&logo=django" alt="Django Version">
  <img src="https://img.shields.io/badge/PostgreSQL-Render-336791?style=for-the-badge&logo=postgresql" alt="PostgreSQL">
  <img src="https://img.shields.io/badge/Tailwind_CSS-3.x-blueviolet?style=for-the-badge&logo=tailwind-css" alt="Tailwind CSS">
</p>

---

## ✨ Live Application Access

The application is fully deployed and live on Render.

-   **Live Site URL**: **[https://django-travel-booking.onrender.com/](https://django-travel-booking.onrender.com/)**

### 🔑 Admin Panel Access

You can access the admin dashboard to manage travel options and bookings.

-   **Admin Panel URL**: **[https://django-travel-booking.onrender.com/admin/](https://django-travel-booking.onrender.com/admin/)**
-   **Username**: `admin`
-   **Password**: `kyrogen568`

---

## 🌟 Features

-   **🎫 Multi-Modal Booking**: Book flights, trains, and bus journeys through a sleek, modern UI.
-   **🔐 User Authentication**: Secure signup, login, and logout functionality.
-   **🔍 Smart Search & Filtering**: Find travel options by source, destination, and transport type.
-   **📅 Booking Management**: View, track, and cancel your bookings in a dedicated dashboard.
-   **💳 Dynamic Pricing**: Real-time cost calculation when booking multiple seats.
-   **📱 Fully Responsive Design**: A professional and aesthetic interface that works beautifully across all devices.

---

## 📸 Screenshots

| Homepage & Filters                                                                                             | My Bookings Dashboard                                                                                              |
| :-------------------------------------------------------------------------------------------------------------: | :-------------------------------------------------------------------------------------------------------------------: |
| ![](https://github.com/Tanishq4501/django-travel-booking/blob/main/ss/home.PNG)                                  | ![](https://github.com/Tanishq4501/django-travel-booking/blob/main/ss/my-bookings.PNG)                                 |
| **Login & Signup** | **Booking Process** |
| ![](https://github.com/Tanishq4501/django-travel-booking/blob/main/ss/login.PNG)                                 | ![](https://github.com/Tanishq4501/django-travel-booking/blob/main/ss/booking.PNG)                                     |

---

## 🛠️ Technology Stack

| Category     | Technology                                                                                                                                                                                                                                                                                                                                                      |
| :----------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Backend** | <img src="https://img.shields.io/badge/Python-3.11-3776AB?style=flat-square&logo=python&logoColor=white" /> <img src="https://img.shields.io/badge/Django-5.x-092E20?style=flat-square&logo=django&logoColor=white" />                                                                                                                                              |
| **Database** | <img src="https://img.shields.io/badge/PostgreSQL-Live-336791?style=flat-square&logo=postgresql&logoColor=white" /> <img src="https://img.shields.io/badge/MySQL-Local-4479A1?style=flat-square&logo=mysql&logoColor=white" />                                                                                                                                    |
| **Frontend** | <img src="https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white" /> <img src="https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=flat-square&logo=tailwind-css&logoColor=white" />                                                                                                                                             |
| **Deployment** | <img src="https://img.shields.io/badge/Render-46E3B7?style=flat-square&logo=render&logoColor=white" /> <img src="https://img.shields.io/badge/Gunicorn-499848?style=flat-square&logo=gunicorn&logoColor=white" /> <img src="https://img.shields.io/badge/WhiteNoise-FFFFFF?style=flat-square&logo=python&logoColor=black" /> |

---

## 🚀 Local Development Setup

This project is configured for dual-database environments. It uses **MySQL** for local development and automatically switches to **PostgreSQL** in the deployed Render environment.

### Prerequisites
-   Python 3.11+
-   MySQL Server (for local development)
-   Git

### Installation Steps

1.  **Clone the repository**
    ```bash
    git clone [https://github.com/Tanishq4501/django-travel-booking.git](https://github.com/Tanishq4501/django-travel-booking.git)
    cd django-travel-booking
    ```

2.  **Create a virtual environment**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  **Install dependencies**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up the local database**
    -   Ensure your local MySQL server is running.
    -   Create a database (e.g., `travel_db`).
    -   Update the `DATABASES` configuration in `travel_booking/settings.py` with your local MySQL credentials.

5.  **Run migrations and start the server**
    ```bash
    python manage.py migrate
    python manage.py runserver
    ```

The application will be available at `http://127.0.0.1:8000`.

---

## 🤝 Contributing

We welcome contributions! Please fork the repository, create a feature branch, and open a pull request.

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

**Tanishq**
-   GitHub: [@Tanishq4501](https://github.com/Tanishq4501)
-   Email: tanishqchoudhary5689@gmail.com

---

<div align="center">
  **⭐ Show Your Support! If this project helped you, please consider giving it a star on GitHub! ⭐**
</div>
