
# VIRTUAL ENV
# Virtualenv will isolate your Python/Django setup on a per-project basis. 
# This means that any changes you make to one website won't affect any others you're also developing. 
# Neat, right?

# Create Virtual ENV
# python -m venv myNewENV

# Activate Virtual ENV
# (while in project directory)
# myNewENV\Scripts\activate
# You will know it worked if your commandline is now prefixed with (myNewENV)

# Make sure your pip is updated
# python -m pip install --upgrade pip

# Add Django to the requirements.txt
# Django~=2.0.6
# pip install -r requirements.txt

# Create Django project
# django-admin.exe startproject mysite .

# Make some changes in settings.py now

# Create a database (with respect to DATABASE = {...} in settings.py)
# By default it will use sqlite3
# python manage.py migrate

# Run server
# python manage.py runserver

# Info Django that we made some changes in our model
# that will prepare a migration file for us
# python manage.py makemigrations blog

# To apply migration file to our database
# python manage.py migrate blog