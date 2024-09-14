# Interactive App Tutor - Backend

## Installation

Set up a virtual environment with by running

```bash
python -m venv .venv
```

in the command line. Now you can activate it with

```bash
source .venv/bin/activate
```

Install the dependencies

```bash
pip install -r requirements.txt
```

## Running the backend

If running the backend for the first time, you need to migrate changes to the database

```bash
python manage.py makemigrations
python manage.py migrate
```

NOTE: When using sqlite make sure this file actually exists, even if blank - Django will populate it later when migrating.

Now you can run the server, using

```bash
python manage.py runserver
```

## Accessing the Admin page

1. Create an Admin User:

Before you can access the admin panel, you'll need to create an admin user. Open a terminal in your project directory and run the following command:

```bash
python manage.py createsuperuser
```

This command will prompt you to set a username, email address, and password for your admin account. Choose a strong password and keep it secure, as it will be used to access sensitive administrative features.

2. Accessing the Admin Panel:

Once you've created an admin user, you can access the admin panel by opening http://localhost:8085/admin in your web browser. Login using the username and password you created in step 1.

3. Managing Data:

The admin panel allows you to add, edit, and delete data within your project's database. You can manage different models (data structures) and their associated fields through the admin interface.

## More Information

For more information, view the [User Manual](./User_Manual.pdf)
