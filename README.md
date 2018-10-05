# CorrelationOneChallenge
A backend DB and API built with Django for candidates completing online assessments. 

## Technologies used
* [Django] (https://www.djangoproject.com/)
* [DRF] (www.django-rest-framework.org/)

## Installation
* Before beginning, make sure you have Python and virtualenv installed on your computer.

* Next, git clone this repo:
    ```bash
       $ git clone https://github.com/talaltoukan/CorrelationOneChallenge
    ```

* ### Dependencies
    1. cd into the cloned repo:
        ```bash
           $ cd CorrelationOneChallenge
        ```

    2. Create and run your virtual environment:
        ```bash
           $ virtualenv venv -p python
           $ source venv/bin/activate
        ```

    3. Install the dependencies needed to run the app:
        ```bash
           $ pip install Django
           $ pip install djangorestframework
           $ pip install Pillow

        ```

    4. Run DB migrations:
        ```bash
           $ python manage.py makemigrations assessment
           $ python manage.py migrate
        ```
* ### Run It
    Now it's ready to run:
    ```bash
       $ python manage.py runserver
    ```

    Access the API service by using:
    ```
       http://localhost:8000/assessment/
    ```

