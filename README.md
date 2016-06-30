# mathsGenerator

# Installation:

Create new directory,

    $ mkdir mathsGenerator

Change directory into it,

    $ cd mathsGenerator

Set current directory as a virtual environment,

    $ virtualenv .

Activate virtual environment,

    $ source bin/activate     #works on Linux anyway!

Initialise directory as a local git repository,

    $ git init

Clone repository from git to here,

    $ git clone

Change directory into mathsGenerator,

    $ cd mathsGenerator

Install required python packages including django,

    $ pip install -r requirements.txt

Make sure to be in the same directory as manage.py 
Good idea to run migrations even though it will probably have no effect,

    $ python manage.py makemigrations

    $ python manage.py migrate

Run server,

    $ python manage.py runserver
