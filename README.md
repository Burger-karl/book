created a Functional REST CRUD API using Django, Django rest framework

start by creating a base folder

in the base folder, we create a virtual environment using the command 'virtualenv bookapp'

install all dependencies including django and django rest framework in the virtual env

create a django project 'book'

in the django project dir, create an app 'book_api'

configure the settings.py file, add the project app 'book_api' and rest_framework to the 'installed apps' object.

Also, configure the settings.py file, add the Postgresql Database which is used in this project

Open your pgAdmin app and create a new database

configure the project 'book' urls.py file, and include the project app 'book_api' urls.py file.

create the api models in the models.py file and migrate to the database using the command 'python manage.py makemigrations book_api' and 'python manage.py migrate'.

create a serializer.py file in the app 'book_api' dir, which will be used to convert complex data types.

create the logic for POST, GET, PUT AND DELETE in the views.py file.

create a urls.py file in the app dir 'book_api', create the routes using the class views created in the views.py file.

run the CRUD project using the command 'python manage.py runserver'.

Postman App was used for testing the crud api, In testing the CRUD api;

POST request is to create a new book and call the REST endpoint '/api/'.

GET request is to read a book and call the REST endpoint '/api/id'. The 'id' is passed as an argument to the endpoint.

PUT request is to update a particular book and call the REST endpoint '/api/id'. The 'id' is passed as an argument to the endpoint.

DELETE request is to delete a particular book and call the REST endpoint '/api/id'. The 'id' is passed as an argument to the endpoint. 



UML DIGARAM






![Blank board](https://github.com/Burger-karl/book/assets/116649077/e6d74f93-e246-4759-bac4-83a490644d8b)






