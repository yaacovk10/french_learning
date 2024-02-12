# French Learning Application Backend

This Django REST Framework project serves as the backend for a French learning application, providing interactive lessons, exercises, user authentication, and more.

## Features

- **User Authentication**: Secure login and password management using JWT tokens.
- **Lessons Management**: CRUD operations for managing lessons.
- **Words Management**: CRUD operations for managing words associated with lessons, including fetching words by lesson.
- **Speech Synthesis and Recognition**: Integration with Web Speech API for text-to-speech and speech-to-text functionalities to aid in learning pronunciation.
- **Image Fetching**: Utilization of the Pexels API to fetch relevant images for words.

## Technologies

- **Django 5.0.1**: High-level Python web framework for rapid development.
- **Django REST Framework**: Powerful toolkit for building Web APIs.
- **SQLite**: Default database for development.
- **JWT Authentication**: For secure handling of user authentication.

## Setup and Installation

1. **Clone the repository:**
   ```bash
   git clone https://your-repository-url.git
   cd your-project-directory


2. **Create and activate a virtual environment** python -m venv venv
source venv/bin/activate

3. **Install required dependencies:**
pip install -r requirements.txt

4. **Apply migrations to create the database schema:**
python manage.py migrate

5. **Run the development server:**
python manage.py runserver


**API Endpoints**
- Login: POST /login/ - Obtain JWT tokens for authentication.
- Update Password: PUT /update_password/ - Update user password.
- Lessons:
    - GET /lessons/ - Fetch all lessons.
    - POST /lessons/ - Create a new lesson.
    - GET /lessons/<int:pk>/ - Fetch a specific lesson.
    - PUT /lessons/<int:pk>/ - Update a specific lesson.
    - DELETE /lessons/<int:pk>/ - Delete a specific lesson.
- Words:
    - GET /words/ - Fetch all words or words by lesson using lesson_id query parameter.
    - POST /words/ - Create a new word.
    - GET /words/<int:pk>/ - Fetch a specific word.
    - PUT /words/<int:pk>/ - Update a specific word.
    - DELETE /words/<int:pk>/ - Delete a specific word.
