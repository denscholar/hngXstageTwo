# HNGX stage 2 Project

This is a Django-based RESTful API for managing and interacting with persons' data.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.6 or higher installed
- Pip package manager installed
- Virtualenv (optional but recommended)
- PostgreSQL (or any other database of your choice) installed and configured

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/denscholar/hngXstageTwo.git

2. Navigate to the project directory:
   ```bash
   cd HngStageTwo

3. Create a virtual environment (optional but recommended):
   ```bash
   virtualenv venv

4. Activate the virtual environment:
   - On Windows:
   ```bash
   venv\Scripts\activate

   ```
   - On macOS and Linux:
   ```bash
   source venv/bin/activate

5. Install the project dependencies:
   ```bash
   pip install -r requirements.txt

# Configuration
1. Create a PostgreSQL database and configure the database settings in settings.py:
   ```bash
   DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'yourdbname',
        'USER': 'yourdbuser',
        'PASSWORD': 'yourdbpassword',
        'HOST': 'localhost',  # Change if your database is hosted elsewhere
        'PORT': '',           # Leave empty for default PostgreSQL port
    }
}
2. Set up other project configurations such as secret keys, allowed hosts, etc., in settings.py.

# Running the API

1. Run database migrations:
   ```bash
   python manage.py migrate

2.Start the development server:
```bash
python manage.py runserver
```

The API should now be running at http://localhost:8000/.

