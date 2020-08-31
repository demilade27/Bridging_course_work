## For every django framework installed, the above command is required !

## pip install pipenv : to create virtual machine to run python django on every project

## pipenv shell : to create new shell

## pipenv install django

### Create a nw project, A project is the overall website /application

## django-admin startproject projectname

## django-admin startproject projectname

## TO RUN THE SERVER : Before runing ur server , make sure your in the same folder as manage.py

## python manage.py runserver

## python manage.py migrate

### A PROJECT IS THE WHOLE APPLICATON ,WHILE AN APP IS PART OF THE WHOLE PROJECT, OR A PART OF THE PROJECTpython manage

## python manage.py startapp app_name

BEFORE MIGRATION: GO TO SETTINGS AND LOCATE INSTALLED_APPS, add the project app
python manage.py makemigrations djangoapp

python manage.py migrate
$ pa_autoconfigure_django.py --python=3.6 https://github.com/demilade27/Bridging_course_work.git

MANIPULATE THE SHELL:
python manage.py shell

CREATE SUPER USER:
python manage.py createsuperuser

PIPENV VS ENV

# Don't feel obligated to use pipenv. It is generally recommended to help people who are intimidated by virtualenvs, and is not appropriate for all use cases. It actually relies on pip and virtualenv, so virtualenv is not going away. There are also some common criticisms of pipenv. See this blog post for some examples.

# virtualenv (venv), on the other hand, is bundled with python itself, so is certainly more stable, widespread and canonically correct. So you won't run into problems like this.

USING A VENV

# python -m venv myvenv

# myvenv\Scripts\activate

# pip install --upgrade pip

# python -m pip install django~=1.11.0 - LTS-2017

### Remember to run everything in the virtualenv. If you don't see a prefix (myvenv) in your

### console, you need to activate your virtualenv. We explained how to do that in the Django

### installation chapter in the Working with virtualenv part. Typing myvenv\Scripts\activate

### on Windows or source myvenv/bin/activate on Mac OS X or Linux will do this for you.

# django-admin.exe startproject mysite .

### manage.py is a script that helps with management of the site. With it we will be able (amongst other things) to start a web server on our computer without installing anything else.

### The settings.py file contains the configuration of your website. Remember when we talked about a mail carrier checking where to deliver a letter? urls.py file contains a list of patterns used by urlresolver .

## CREATE DB:

To create a database for our blog, let's run the following in the console: python manage.py
migrate (we need to be in the djangogirls directory that contains the manage.py file).

Creating an application

## Starting the web server

You need to be in the directory that contains the manage.py file (the djangogirls directory). In
the console, we can start the web server by running python manage.py runserver :

Create a model/object
python manage.py startapp blog

CREATING TABLES/MAKING MIGRATION FILES:
python manage.py makemigrations model_name

APPLYING THE MIGRATIONS
c

ADMIN:
TO HAVE ACCESS TO THE ADMIN WE NEED TO RUN THE COMMAND:
python manage.py createsuperuser
