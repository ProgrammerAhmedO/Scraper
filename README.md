# Base Scraper App

The Base Scraper App is a Django-based web application that demonstrates the process of web scraping, data storage in a PostgreSQL database, and API creation using Django REST Framework. The application provides an API to access the scraped data and supports filtering based on specific criteria.

Please note that this project is intended as a learning exercise and demonstration of concepts. As of now, the project is not deployed to a hosting provider, so you can run it locally to explore its functionality.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [API Documentation](#api-documentation)
- [Superuser Access](#superuser-access)

## Features

- Web scraper that collects data from a website of your choice.
- Data storage in a PostgreSQL database.
- Exposes data through a REST API using Django REST Framework.
- Supports filtering of data based on specific criteria.
- Easy installation and setup.

## Installation

1. **Clone the Repository:**

git clone https://github.com/your-username/scraper.git
cd scraper

arduino
Copy code

2. **Install Dependencies:**

Ensure you have Python 3.x installed. Create and activate a virtual environment (optional but recommended), then install the required packages:

pip install -r requirements.txt

bash
Copy code

3. **Database Configuration:**

Update the database settings in `scraper/settings.py`:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'Puffin',
        'USER': 'postgres',
        'PASSWORD': 'puffinpuffin123',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
Apply Migrations:
Apply the initial database migrations:
Copy code
python manage.py migrate
Create Superuser:
Create a superuser with the username "Puffin" and password "puffinpuffin123":
Copy code
python manage.py createsuperuser
Usage

Run the Development Server:
Start the development server:
Copy code
python manage.py runserver
The application will be accessible at http://localhost:8000/.
Access the Admin Panel:
Open the admin panel by visiting http://localhost:8000/admin/ and logging in with your superuser credentials.
Run the Web Scraper:
To run the web scraper manually, use the following command:
Copy code
python manage.py scrape_data
This will scrape data from a specified website, store it in the database, and display a success message.
API Documentation

The API exposes the scraped data and supports filtering based on specific criteria. To access the API, use the following URL: http://localhost:8000/api/data/.

To filter the data, you can use query parameters. For example, to filter data with titles containing the word "example," use the URL: http://localhost:8000/api/data/?title_contains=example.

Superuser Access

As mentioned earlier, a superuser account with the username "Puffin" and password "puffinpuffin123" has been created. You can use this account to access the Django admin panel and explore the application's functionality.
