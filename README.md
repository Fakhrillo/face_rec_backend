# Face Recognition System Backend

This project is a Django REST API backend for a face recognition system. It uses the face_recognition library for comparing face encodings and handling user information with the ability to add and verify users based on facial data.


## Features

 - **User registration with face recognition:** Users can be added to the database with their image and are recognized when they upload the same or similar image.
 - **Face comparison:** The system compares uploaded images to the stored known images and returns the closest match if any.
 - **REST API:** Supports POST requests to interact with the backend for user registration and verification.


## Requirements
 - Python 3.x
 - Django
 - Django REST Framework
 - Pillow (for image handling)
 - face_recognition (for facial encoding and comparison)
 - NumPy (for handling face encodings)


## Setup

1. Clone the repository:
    ```sh
    git clone https://github.com/Fakhrillo/face_rec_backend.git
    cd face_rec_backend
    ```

2. Create and activate a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Apply database migrations:
    ```sh
    python manage.py migrate
    ```

5. Run the Django development server:
    ```sh
    python manage.py runserver
    ```

6. Your API is now accessible at http://127.0.0.1:8000/.


## API Endpoints

### 1. User Registration (/user/)
### 2. User Face Check (/user-check/)


## Known Issues
 - Ensure that the uploaded images have faces. If no face is detected, an error might be raised.
 - Images should be clear and well-lit for better recognition accuracy.


## License
This project is licensed under the MIT License.