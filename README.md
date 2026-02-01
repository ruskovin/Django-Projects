# Django-Projects

[![Languages](https://img.shields.io/github/languages/top/ruskovin/Django-Projects)](https://github.com/ruskovin/Django-Projects)
[![Repo Size](https://img.shields.io/github/repo-size/ruskovin/Django-Projects)](https://github.com/ruskovin/Django-Projects)
[![Last Commit](https://img.shields.io/github/last-commit/ruskovin/Django-Projects)](https://github.com/ruskovin/Django-Projects)

## Overview

**Django-Projects** is a collection of Django projects showcasing different features and integrations of the Django web framework. This repository contains five distinct applications, each demonstrating various aspects of Django development, from basic CRUD operations to more advanced features like APIs and e-commerce functionality.

## Projects in This Repository

### 1. Blog
A full-featured blog application with a Django backend and Bootstrap frontend.
- **Location**: `/Blog`
- **Features**: Blog post creation, reading, and management with API support

### 2. Ecommerce
An e-commerce platform built with Django.
- **Location**: `/Ecommerce`
- **Features**: Product catalog, shopping cart functionality

### 3. Social Network
A social networking application.
- **Location**: `/social_network/social`
- **Features**: User profiles, social interactions

### 4. Todo List
A simple todo list application.
- **Location**: `/todo-list/todolist`
- **Features**: Task management with create, read, update, and delete operations

### 5. Weather App
A weather information application that displays weather data for cities worldwide.
- **Location**: `/weather_app/weatherApp`
- **Features**: City weather lookup using Django

## Technology Stack

- **Backend**: Python, Django
- **Frontend**: HTML, CSS, JavaScript, Bootstrap
- **Database**: SQLite (default Django database)
- **Additional Tools**: Node.js and npm for frontend dependencies (in some projects)

## Getting Started

### Prerequisites

- [Python 3.x](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [Node.js and npm](https://nodejs.org/) (for frontend assets in some projects)

### Installation

Each project in this repository is a standalone Django application. To run any project:

1. **Clone the repository**  
   ```bash
   git clone https://github.com/ruskovin/Django-Projects.git
   cd Django-Projects
   ```

2. **Navigate to the project you want to run**  
   ```bash
   # For Blog project:
   cd Blog
   
   # For Ecommerce project:
   cd Ecommerce
   
   # For Social Network:
   cd social_network/social
   
   # For Todo List:
   cd todo-list/todolist
   
   # For Weather App:
   cd weather_app/weatherApp
   ```

3. **Set up a virtual environment** (recommended)  
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

4. **Install dependencies**  
   ```bash
   # Install Django and project-specific dependencies
   pip install django
   # Some projects may have a requirements.txt file
   pip install -r requirements.txt  # if available
   
   # For projects with frontend dependencies (Blog, Todo List):
   npm install  # if package.json exists
   ```

5. **Run migrations and start the server**
   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

6. **Access the application**  
   Open your browser and navigate to `http://127.0.0.1:8000/`

## Usage

Each project is independent and can be run separately:

1. Navigate to the project folder you want to explore
2. Follow the installation steps above for that specific project
3. Access the application at `http://127.0.0.1:8000/`
4. Some projects may have their own README files with additional details

## Folder Structure

```
Django-Projects/
│
├── Blog/                    # Blog application
│   ├── manage.py
│   ├── BlogAPP/
│   ├── myblog/
│   └── myblog_api/
│
├── Ecommerce/              # E-commerce application
│   ├── manage.py
│   ├── Ecommerce/
│   ├── e_commerce_app/
│   └── templates/
│
├── social_network/         # Social networking app
│   └── social/
│       ├── manage.py
│       └── social/
│
├── todo-list/              # Todo list application
│   └── todolist/
│       ├── manage.py
│       ├── tasks/
│       └── todolist/
│
├── weather_app/            # Weather information app
│   └── weatherApp/
│       ├── manage.py
│       ├── weather/
│       └── weatherApp/
│
└── README.md
```

## Contributing

Contributions, issues, and feature requests are welcome!

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a pull request

## License

This repository is for educational and demonstration purposes. See individual project folders for licensing information.

## Acknowledgments

- [Django](https://www.djangoproject.com/)
- [Bootstrap](https://getbootstrap.com/)
- [Node.js](https://nodejs.org/)

---
> My Django projects showcasing different aspects of web development.
