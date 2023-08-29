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

git clone https://github.com/ProgrammerAhmedO/Scraper.git
cd scraper

arduino
Copy code

2. **Install Dependencies:**

Ensure you have Python 3.9 installed or higher. Create and activate a virtual environment (optional but recommended), then install the required packages:
```python
pip install -r requirements.txt
```

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
```
3.1. Apply Migrations:
Apply the initial database migrations:
```python
python manage.py migrate
```
3.2. Create Superuser:
Create a superuser with the username "Puffin" and password "puffinpuffin123":
```python
python manage.py createsuperuser
```

## Usage:
   
4.1 Run the Development Server:
Start the development server:
```python
python manage.py runserver
```
The application will be accessible at http://localhost:8000/.
4.2. Access the Admin Panel:
Open the admin panel by visiting http://localhost:8000/admin/ and logging in with your superuser credentials.
4.3. Run the Web Scraper:
To run the web scraper manually, use the following command:
```python
python manage.py scrape_data
```
This will scrape data from a specified website, store it in the database, and display a success message.
<img width="922" alt="Screenshot 2023-08-29 at 1 43 01 PM" src="https://github.com/ProgrammerAhmedO/Scraper/assets/84571800/46902195-e5a4-4653-b558-269053b7b1a8">
<img width="1438" alt="Screenshot 2023-08-29 at 1 47 24 PM" src="https://github.com/ProgrammerAhmedO/Scraper/assets/84571800/5924a38f-4e65-4b8e-a698-e9d84a758b18">
<img width="1438" alt="Screenshot 2023-08-29 at 1 47 31 PM" src="https://github.com/ProgrammerAhmedO/Scraper/assets/84571800/cc9084ae-326f-44b6-bfe4-e4279c751a99">

## Usage (FastAPI Application):

1. **Run the Development Server:**

   Start the FastAPI development server:
   
   ```python
   uvicorn main:app --reload --port 8000
   ```
The application will be accessible at http://localhost:8000/.


## API Documentation

The API exposes the scraped data and supports filtering based on specific criteria. To access the API, use the following URL: **http://localhost:8000/api/data/.**
<img width="1438" alt="Screenshot 2023-08-29 at 1 43 36 PM" src="https://github.com/ProgrammerAhmedO/Scraper/assets/84571800/fbc9d036-0c33-40e5-8281-d2b3e84c5db5">

To filter the data, you can use query parameters. For example, to filter data with titles containing the word "example," use the URL: **http://localhost:8000/api/data/?title_contains=example.**
<img width="1438" alt="Screenshot 2023-08-29 at 1 44 13 PM" src="https://github.com/ProgrammerAhmedO/Scraper/assets/84571800/b5e37a64-822c-4e57-a937-cf82fe554917">


## Access the API (FastAPI Application):
The API exposes the scraped data and supports filtering based on specific criteria. To access the API, use the following URL: **http://localhost:8000/scraped_data/.**
To filter the data, you can use query parameters. For example, to filter data with titles containing the word "example," use the URL: **http://localhost:8000/scraped_data/?title=example.**

<img width="1438" alt="Screenshot 2023-08-29 at 10 12 43 PM" src="https://github.com/ProgrammerAhmedO/Scraper/assets/84571800/fb8980d2-d7a2-4b49-8541-39898cdf1459">
<img width="1438" alt="Screenshot 2023-08-29 at 10 12 59 PM" src="https://github.com/ProgrammerAhmedO/Scraper/assets/84571800/495d429f-de93-464c-86b0-954be2740e9b">

## Superuser Access

As mentioned earlier, a superuser account with the username **"Puffin"** and password **"puffinpuffin123"** has been created. You can use this account to access the Django admin panel and explore the application's functionality.
