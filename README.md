# Django-Projects

[![Languages](https://img.shields.io/github/languages/top/ruskovin/Django-Projects)](https://github.com/ruskovin/Django-Projects)
[![Repo Size](https://img.shields.io/github/repo-size/ruskovin/Django-Projects)](https://github.com/ruskovin/Django-Projects)
[![Last Commit](https://img.shields.io/github/last-commit/ruskovin/Django-Projects)](https://github.com/ruskovin/Django-Projects)

## Overview

**Django-Projects** is a collection of my projects built using Django, showcasing different features and integrations of the Django web framework. The repository includes a range of project examples, from basic templates to more advanced applications with frontend and backend code.

## Repository Highlights

- **Django-based backend**: Core logic and APIs implemented with Python and Django.
- **Rich frontend**: Projects utilize JavaScript, SCSS, and CSS for interactive and responsive user interfaces.
- **Sample scripts**: Utilities and setup scripts in PowerShell and Batchfile, aiding development and deployment.

## Language Breakdown

| Language    | Percentage |
| ----------- | ---------- |
| JavaScript  | 50.9%      |
| SCSS        | 26.4%      |
| CSS         | 16.7%      |
| PowerShell  | 2.3%       |
| HTML        | 1.9%       |
| Python      | 1.7%       |
| Batchfile   | 0.1%       |

> *Note: This repository focuses heavily on frontend implementations with Django as the backend.*

## Getting Started

### Prerequisites

- [Python 3.x](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [Node.js and npm](https://nodejs.org/) (for frontend assets)
- Optionally: [Sass](https://sass-lang.com/) for SCSS compilation

### Installation

1. **Clone the repository**  
   ```bash
   git clone https://github.com/ruskovin/Django-Projects.git
   cd Django-Projects
   ```

2. **Backend setup**  
   - Create and activate a virtual environment:
     ```bash
     python -m venv venv
     source venv/bin/activate  # On Windows: venv\Scripts\activate
     ```
   - Install Python dependencies:
     ```bash
     pip install -r requirements.txt
     ```
   - Set up your database (migrations):
     ```bash
     python manage.py migrate
     ```

3. **Frontend setup**  
   - Install frontend dependencies:
     ```bash
     npm install
     ```
   - (If using SCSS) Compile styles:
     ```bash
     npm run build-css
     # or manually using sass:
     sass static/scss:static/css
     ```

4. **Run the server**
   ```bash
   python manage.py runserver
   ```

## Usage

- Access the Django server at `http://127.0.0.1:8000/`
- Explore different project folders for application-specific details.
- Each project may have its own README and setup instructions.

## Folder Structure

```
Django-Projects/
│
├── project_1/
│   ├── ...
├── project_2/
│   ├── ...
├── static/
│   ├── js/
│   ├── scss/
│   ├── css/
├── templates/
│   ├── ...
├── requirements.txt
├── manage.py
└── ...
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
- [Sass](https://sass-lang.com/)
- [Node.js](https://nodejs.org/)

---
> My Django projects showcasing different aspects of web development.
