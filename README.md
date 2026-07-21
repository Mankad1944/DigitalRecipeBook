# 🍬 Digital Recipe Book for Family & Friends
### Traditional Indian Sweets Recipe Management System

![License](https://img.shields.io/badge/License-MIT-green.svg)
![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Django](https://img.shields.io/badge/Django-Framework-success.svg)
![MySQL](https://img.shields.io/badge/Database-MySQL-orange.svg)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen.svg)

---

## 📖 Project Overview

**Digital Recipe Book for Family & Friends (Indian Sweets)** is a web-based application developed to preserve and organize traditional Indian sweet recipes in a digital format. The platform allows family members and friends to securely store, manage, search, and share recipes while maintaining a structured and user-friendly experience.

The application eliminates the dependency on handwritten recipe books by providing a centralized digital repository accessible anytime.

---

## ✨ Features

### 👤 User Features

- User Registration & Login
- Secure Authentication
- View All Recipes
- Search Recipes
- Filter by Category
- View Detailed Recipe
- Save Favorite Recipes
- User Profile Management
- Responsive Interface

### 👨‍🍳 Recipe Management

- Add New Recipes
- Edit Existing Recipes
- Delete Recipes
- Upload Recipe Images
- Ingredients Management
- Step-by-Step Cooking Instructions
- Preparation Time
- Cooking Time
- Serving Size
- Difficulty Level

### 🍮 Categories

- Barfi
- Ladoo
- Halwa
- Peda
- Kheer
- Gulab Jamun
- Rasgulla
- Modak
- Jalebi
- Festival Specials
- Other Traditional Indian Sweets

### 🔍 Search & Filter

- Search by Recipe Name
- Search by Ingredients
- Category Filter
- Difficulty Filter

---

## 🛠️ Technology Stack

### Frontend

- HTML5
- CSS3
- Bootstrap
- JavaScript

### Backend

- Python
- Django Framework

### Database

- MySQL

### Development Tools

- Visual Studio Code
- Git
- GitHub

---

## 📂 Project Structure

```
Digital-Recipe-Book/
│
├── recipebook/
│   ├── settings.py
│   ├── urls.py
│   └── ...
│
├── recipes/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   ├── admin.py
│   ├── forms.py
│   └── templates/
│
├── static/
│   ├── css/
│   ├── js/
│   └── images/
│
├── media/
│   └── recipe_images/
│
├── templates/
│
├── requirements.txt
│
├── manage.py
│
└── README.md
```

---

## 💾 Database

The application uses **MySQL** for storing:

- User Information
- Recipe Details
- Ingredients
- Categories
- Recipe Images
- Favorite Recipes

---

## 📸 Main Modules

### 🏠 Home

- Featured Recipes
- Latest Recipes
- Search Bar

### 📚 Recipes

- Recipe Listing
- Recipe Details
- Category View

### ❤️ Favorites

- Save Favorite Recipes
- Remove Favorites

### 👤 User Profile

- Personal Details
- Saved Recipes

### 🔐 Authentication

- Register
- Login
- Logout

### ⚙️ Admin Panel

- Manage Users
- Manage Recipes
- Manage Categories
- Manage Images

---

## 🚀 Installation

### 1. Clone Repository

```bash
git clone https://github.com/yourusername/Digital-Recipe-Book.git
```

### 2. Navigate to Project

```bash
cd Digital-Recipe-Book
```

### 3. Create Virtual Environment

```bash
python -m venv venv
```

### 4. Activate Virtual Environment

Windows

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
source venv/bin/activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Configure Database

Update your `settings.py`

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'recipe_db',
        'USER': 'root',
        'PASSWORD': 'your_password',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```

### 7. Apply Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 8. Create Superuser

```bash
python manage.py createsuperuser
```

### 9. Run Server

```bash
python manage.py runserver
```

Open:

```
http://127.0.0.1:8000/
```

---

## 📷 Screenshots

Add screenshots here.

Example:

```
screenshots/
├── home.png
├── login.png
├── recipes.png
├── recipe-details.png
├── favorites.png
└── admin-dashboard.png
```

---

## 🎯 Learning Outcomes

This project helped in understanding:

- Django MVC Architecture
- CRUD Operations
- Authentication System
- File Upload Handling
- MySQL Integration
- Template Rendering
- Bootstrap Responsive Design
- Database Relationships
- Version Control using Git

---

## 🔮 Future Enhancements

- Recipe Rating System
- User Comments
- Video Recipes
- Nutrition Information
- Shopping List Generator
- Meal Planner
- PDF Recipe Export
- Multi-language Support
- Dark Mode
- Mobile Application
- Recipe Recommendation System
- AI-powered Ingredient Suggestions

---

## 🤝 Contributing

Contributions are welcome.

1. Fork the repository
2. Create a new feature branch
3. Commit your changes
4. Push to your branch
5. Create a Pull Request

---

## 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Brijesh Mankad**

MCA Student | Full Stack Developer | Python & Django Enthusiast

GitHub: https://github.com/yourusername

LinkedIn: https://linkedin.com/in/yourprofile

---

## 🙏 Acknowledgements

- Django Documentation
- Bootstrap Documentation
- MySQL Documentation
- Python Community
- Family & Friends for sharing traditional Indian sweet recipes

---

⭐ If you found this project useful, consider giving it a star on GitHub!
