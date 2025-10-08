# ALX Travel App

A Django-based RESTful API for managing travel listings, bookings, and reviews. This project is designed for learning and demonstration purposes as part of the ALX ProDev program.

## Features

- **Listings**: Create, view, and manage travel accommodation listings.
- **Bookings**: Book listings and manage reservations.
- **Reviews**: Leave ratings and comments for listings.
- **API Documentation**: Interactive Swagger docs available at `/swagger/`.
- **Seed Command**: Populate the database with sample listings for development.

## Tech Stack

- Python 3.10+
- Django 5.2.5
- Django REST Framework
- MySQL
- Celery & RabbitMQ (for async tasks)
- drf-yasg (Swagger API docs)
- django-cors-headers

## Getting Started

### Prerequisites

- Python 3.10+
- MySQL
- RabbitMQ (for Celery)
- [pipenv](https://pipenv.pypa.io/en/latest/) or `pip`

### Installation

1. **Clone the repository:**
    ```bash
    git clone <repo-url>
    cd alx_travel_app_0x00/alx_travel_app
    ```

2. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3. **Configure environment variables:**
    - Copy `.env` from the sample or edit with your DB credentials.

4. **Apply migrations:**
    ```bash
    python manage.py migrate
    ```

5. **Seed the database (optional):**
    ```bash
    python manage.py seed
    ```

6. **Run the development server:**
    ```bash
    python manage.py runserver
    ```

7. **Access API docs:**
    - Visit [http://localhost:8000/swagger/](http://localhost:8000/swagger/)

## Usage

- **Listings API:** `/api/`
- **Hello World Endpoint:** `/api/hello/`
- **Swagger Docs:** `/swagger/`

## Project Structure

```
alx_travel_app/
    manage.py
    .env
    requirement.txt
    alx_travel_app/
        settings.py
        urls.py
        wsgi.py
        ...
    listings/
        models.py
        serializers.py
        views.py
        urls.py
        management/
            commands/
                seed.py
```

## Development

- Add new models in [`listings/models.py`](alx_travel_app/listings/models.py)
- Register models in [`listings/admin.py`](alx_travel_app/listings/admin.py)
- Add API endpoints in [`listings/views.py`](alx_travel_app/listings/views.py) and [`listings/urls.py`](alx_travel_app/listings/urls.py)
- Update serializers in [`listings/serializers.py`](alx_travel_app/listings/serializers.py)

## License

This project is for educational purposes.

## Author

ALX ProDev Program
