# Django Redis Serialization Demonstration

This is a simple Django project that serves as a demonstration of how to serialize Python objects using `pickle`, save them in Redis, and then retrieve and use them in subsequent `GET` requests. The project showcases the basic steps involved in serializing data and storing it in a Redis cache for later retrieval.

## Project Overview

- **Objective**: To demonstrate the serialization of Python objects and their storage in Redis for later retrieval.

- **Technology Stack**:
  - Django: Python web framework.
  - Redis: In-memory data store.
  - `pickle`: Python module for object serialization.

## Getting Started

Follow these steps to get the project up and running on your local machine.

1. **Clone the Repository**:

   ```bash
   git clone [<repository_url>](https://github.com/m-moein98/picky)
   cd picky
   ```

2. **Install Dependencies**:

   Use `pip` to install the required Python packages listed in the `requirements.txt` file:

   ```bash
   pip install -r requirements.txt
   ```

3. **Run Migrations**:

   Apply the database migrations to set up the database:

   ```bash
   python manage.py migrate
   ```

4. **Run the Development Server**:

   Start the Django development server:

   ```bash
   python manage.py runserver
   ```

   The project will be accessible at `http://127.0.0.1:8000/`.

## Usage

This project provides two API endpoints to demonstrate the serialization and storage of data in Redis:

- **POST `/serialize-and-save/`**:
  - This endpoint allows you to serialize a Python object using `pickle` and save it in Redis. The data can be sent as JSON in the request body.

- **GET `/retrieve-and-use/`**:
  - This endpoint retrieves the serialized data from Redis and demonstrates how to use it in the response.

Here's a step-by-step guide on how to use the endpoints:

1. **POST Data**:
   - Send a POST request to `http://127.0.0.1:8000/fruit/` with JSON data in the request body. For example:

   ```json
   {
    "name": "apple",
    "calories": 1000
    }
   ```

   This data will be serialized and stored in Redis.

2. **GET Data**:
   - Send a GET request to `http://127.0.0.1:8000/fruit/1`.
   - The data previously serialized and stored in Redis will be retrieved and used in the response.

## Project Structure

- `fruit/`: The Django app containing the views and API endpoints for serialization and retrieval.
- `picky/`: The project's main configuration.
- `requirements.txt`: Lists the project's dependencies.

## Dependencies

- Django: The web framework.
- `django-redis`: A Django cache backend for Redis.
- Redis server: The in-memory data store.

## Conclusion

This Django project serves as a simple demonstration of how to serialize Python objects using `pickle`, save them in Redis, and retrieve and use them in subsequent requests. It can be used as a reference for understanding the basic concepts of data serialization and caching in Django with Redis. Feel free to explore the code and adapt it to your specific use case.

**Note**: This project is for educational purposes and may not be suitable for production use. Care should be taken when serializing and deserializing data, especially when it comes to security and data integrity.