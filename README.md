# Late Show API Challenge

## Setup Instructions

### PostgreSQL

- Install PostgreSQL and ensure it is running.
- Create a database for the application.
- Note the connection URL (e.g., `postgresql://user:password@localhost:5432/dbname`).

### Flask and Python Environment

- Ensure Python 3.7+ is installed.
- Install dependencies using pipenv or pip:

  ```bash
  pip install pipenv
  pipenv install
  pipenv shell
  ```

- Alternatively, install requirements manually if a requirements file is present.

### Environment Variables

Create a `.env` file in the project root with the following variables:

```
DATABASE_URL=your_postgresql_connection_url
JWT_SECRET_KEY=your_jwt_secret_key
```

## How to Run

### Database Migration

Run the following command to apply migrations:

```bash
flask db upgrade
```

### Seed the Database

To seed the database with initial data, run:

```bash
python server/seed.py
```

### Run the Application

Start the Flask application with:

```bash
flask run

```

or

```bash
python -m flask run
```

The API will be available at `http://localhost:5000`.

## Authentication Flow

### Register

- Endpoint: `POST /register`
- Request Body:

```json
{
  "username": "your_username",
  "password": "your_password"
}

```

- Response:

```json
{
  "message": "User registered"
}
```

### Login

- Endpoint: `POST /login`
- Request Body:

```json
{
  "username": "your_username",
  "password": "your_password"
}
```

- Response:

```json
{
  "access_token": "jwt_token_here"
}
```

### Token Usage

- Use the returned `access_token` as a Bearer token in the `Authorization` header for protected routes.
- Example:

```
Authorization: Bearer your_jwt_token
```

## Route List and Sample Requests/Responses

### Authentication

- `POST /register` - Register a new user.
- `POST /login` - Login and receive JWT token.

### Episodes

- `GET /episodes` - List all episodes.
  - Response:

  ```json
  [
    {
      "id": 1,
      "date": "2025-01-01",
      "number": 101
    },
    ...
  ]
  ```

- `GET /episodes/<id>` - Get episode details including appearances.
  - Response:

  ```json
  {
    "id": 1,
    "date": "2025-01-01",
    "number": 101,
    "appearances": [
      {
        "guest": "Emma Stone",
        "rating": 5
      },
      ...
    ]
  }
  ```

- `DELETE /episodes/<id>` - Delete an episode (requires authentication).
  - Response:

  ```json
  {
    "message": "Episode deleted"
  }
  ```

### Guests

- `GET /guests` - List all guests.
  - Response:

  ```json
  [
    {
      "id": 1,
      "name": "Emma Stone",
      "occupation": "Actor"
    },
    ...
  ]
  ```

### Appearances

- `POST /appearances` - Create an appearance (requires authentication).
- Request Body:

```json
{
  "rating": 5,
  "guest_id": 1,
  "episode_id": 1
}
```

- Response:

```json
{
  "message": "Appearance created"
}
```

## Postman Usage Guide

- Import the provided Postman collection file `challenge-4-lateshow.postman_collection.json` into Postman.
- The collection contains pre-configured requests for all API endpoints.
- To use authenticated routes, first perform the login request to obtain the JWT token.
- Set the token in the `Authorization` header as a Bearer token for subsequent requests.

## GitHub Repository

[[Repo link]](https://github.com/muthonii-pauline/late-show-api-challenge)
