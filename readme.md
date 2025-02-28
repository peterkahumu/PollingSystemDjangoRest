# Polling System API

A Django REST Framework (DRF) based API for creating and managing polls, choices, and votes. This API supports authentication using token-based authentication.

## Features
- User authentication with token-based authentication
- CRUD operations for polls
- CRUD operations for choices within a poll
- Voting system with constraints to prevent duplicate votes
- User registration and login endpoints
- Admin panel for managing polls and choices

## Installation

### Prerequisites
- Python 3.12+
- Django 5.1.1
- Django REST Framework

### Clone the Repository
```bash
git clone <repository_url>
cd polling-system
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Apply Migrations
```bash
python manage.py migrate
```

### Create a Superuser
```bash
python manage.py createsuperuser
```

### Run the Server
```bash
python manage.py runserver
```

## API Endpoints

### Authentication
#### Register a new user
```http
POST /users/
```
**Request Body:**
```json
{
  "username": "example_user",
  "email": "user@example.com",
  "password": "securepassword"
}
```
**Response:**
```json
{
  "username": "example_user",
  "email": "user@example.com"
}
```

#### Login
```http
POST /login/
```
**Request Body:**
```json
{
  "username": "example_user",
  "password": "securepassword"
}
```
**Response:**
```json
{
  "token": "your_auth_token"
}
```

### Polls
#### List all polls
```http
GET /polls/
```
#### Create a new poll (Authenticated)
```http
POST /polls/
```
**Request Body:**
```json
{
  "question": "What is your favorite programming language?",
  "created_by": 1
}
```

#### Retrieve a specific poll
```http
GET /polls/{id}/
```

#### Delete a poll (Only creator can delete)
```http
DELETE /polls/{id}/
```

### Choices
#### List choices for a poll
```http
GET /polls/{poll_id}/choices/
```

#### Create a choice (Only poll creator can create)
```http
POST /polls/{poll_id}/choices/
```
**Request Body:**
```json
{
  "choice_text": "Python"
}
```

### Voting
#### Cast a vote
```http
POST /polls/{poll_id}/choices/{choice_id}/vote/
```
**Request Body:**
```json
{
  "voted_by": 1
}
```

## Admin Panel
The Django admin panel is available at:
```http
/admin/
```
Use the superuser credentials to access the panel and manage polls, choices, and votes.

## Project Structure
```
polling-system/
│-- PollingSystem/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│-- polls/
│   ├── migrations/
│   ├── admin.py
│   ├── apiviews.py
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   ├── views.py
│-- manage.py
```

## Security Considerations
- Ensure `DEBUG = False` in production.
- Use environment variables to store sensitive information like `SECRET_KEY`.
- Use proper authentication and permission classes.

## Contributing
1. Fork the repository.
2. Create a new branch.
3. Make changes and commit them.
4. Push to your fork.
5. Create a pull request.

## License
This project is open-source under the MIT License.

