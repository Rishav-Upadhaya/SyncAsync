# SyncAsync Django Project

This is a Django project that demonstrates the use of synchronous and asynchronous views. The project includes two apps: `movies` and `stories`, each with a simple model and database integration.

## Features

- **Synchronous Views**: Demonstrates blocking operations using Django's standard synchronous views.
- **Asynchronous Views**: Demonstrates non-blocking operations using Django's async views and `asgiref.sync` utilities.
- **Database Models**: Includes `Movie` and `Story` models with basic fields.
- **Admin Integration**: Models are registered in the Django admin for easy management.

## Requirements

- Python 3.8+
- Django 4.2+
- SQLite (default database)

## Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Rishav-Upadhaya/SyncAsync.git
   cd SyncAsync
   ```

2. **Install Dependencies**:
   Create a virtual environment and install the required packages:
   ```bash
   pip install django asyncio 
   ```

3. **Apply Migrations**:
   Run the following commands to set up the database:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. **Run the Development Server**:
   Start the Django development server:
   ```bash
   python manage.py runserver
   ```

5. **Access the Application**:
   Open your browser and navigate to:
   - Main View: [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
   - Synchronous View: [http://127.0.0.1:8000/sync/](http://127.0.0.1:8000/sync/)
   - Asynchronous View: [http://127.0.0.1:8000/async/](http://127.0.0.1:8000/async/)

## Project Structure

```
syncAsync/
├── movies/               # Movies app
├── stories/              # Stories app
├── syncAsync/            # Main project folder
├── manage.py             # Django management script
└── README.md             # Project documentation
```

## Models

### Movie
- `name`: A `CharField` to store the movie name.

### Story
- `name`: A `CharField` to store the story name.

## Views

- **Synchronous View**: Blocks execution while fetching movies and stories.
- **Asynchronous View**: Uses `asyncio.gather` to fetch movies and stories concurrently.

## License

This project is licensed under the MIT License. See the LICENSE file for details.