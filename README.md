# Weather Application

This Django application integrates with the OpenWeatherMap API to fetch weather data for specified cities, stores it in a PostgreSQL database, and provides a REST API for accessing and managing the data. The application also uses Celery to periodically update weather data for a list of cities.

## Features

- Fetch weather data from the OpenWeatherMap API.
- Store weather data in a PostgreSQL database.
- Expose RESTful endpoints for fetching and managing weather data.
- Use Celery to periodically update weather data for a predefined list of cities (e.g., London and New York).
- Optional: Docker and Docker Compose for containerized deployment.
- Optional: Swagger UI for API documentation.

## Requirements

- Python 3.x
- Django
- PostgreSQL
- Celery
- Redis (for Celery broker)
- Docker and Docker Compose (optional)

## Getting Started

### Setup
1. **Deployment using pip and virtual environment**
1.1. **Clone the repository:**

   git clone https://github.com/yourusername/weather_app.git
   cd weather_app

1.2. **Set up a virtual environment:**

    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

1.3 **Install the required packages:**
    pip install -r requirements.txt

1.4 **Set up PostgreSQL:**

    Ensure PostgreSQL is installed and running.

    Create a database for the application:

    psql -U postgres
    CREATE DATABASE weather_db;
    CREATE USER your_db_user WITH PASSWORD 'your_db_password';
    ALTER ROLE your_db_user SET client_encoding TO 'utf8';
    ALTER ROLE your_db_user SET default_transaction_isolation TO 'read committed';
    ALTER ROLE your_db_user SET timezone TO 'UTC';
    GRANT ALL PRIVILEGES ON DATABASE weather_db TO your_db_user;

1.5 **Openweather config**

    Update DATABASES settings in weather_app/settings.py with your PostgreSQL credentials.

    Add your OpenWeatherMap API key to weather_app/settings.py:

    OPENWEATHER_API_KEY = 'your_openweather_api_key'

1.6 **Run Migrations**

    python manage.py migrate

1.7 **Create a superuser - optional:**

    python manage.py createsuperuser

1.8 **Run the development server:**

    python manage.py runserver

    Access the application at http://localhost:8000.

### API Endpoints

    Fetch weather data for a city:
    GET /api/weather/<city>/

    json
    {
    "city": "London",
    "temperature": 15.5,
    "description": "Clear sky",
    "timestamp": "2024-07-09T12:00:00Z"
    }

    Update weather data for a city:
    POST /api/weather/<city>/

    json
    {
    "message": "Weather data for London has been updated."
    }

    Fetch all weather data:
    GET /api/weather/

    json

    [
        {
            "city": "London",
            "temperature": 15.5,
            "description": "Clear sky",
            "timestamp": "2024-07-09T12:00:00Z"
        },
        {
            "city": "New York",
            "temperature": 25.0,
            "description": "Sunny",
            "timestamp": "2024-07-09T12:00:00Z"
        }
    ]

    Update weather data by ID:
    PUT /api/weather/<id>/

    json

    {
        "message": "Weather data with ID 1 has been updated."
    }

    Delete weather data by ID:
    DELETE /api/weather/<id>/

    json
    {
        "message": "Weather data with ID 1 has been deleted."
    }

## Running Celery

1. **Ensure Redis is installed and running.**

2. **Start the Celery worker:**

    celery -A config worker -l info
    
3. **Start the Celery beat:**

    celery -A config beat -l info

## 2. Optional: Docker Deployment

**Ensure Docker and Docker Compose are installed.**

**Build and start the containers:**

    docker-compose up --build

Access the application at http://localhost:8000.

## 3.Optional: Swagger Documentation
Access the Swagger UI for API documentation at http://localhost:8000/swagger/.








