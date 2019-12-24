# Tech-Reviews 

## About
It is project made using django framework. Basically it is website where users can check tech products reviews and they can also write reviews for the products. Anyone can use the source code. You can also make changes where necessary and add new files to expand the project.

## To run locally, do the usual  [on windows]:

#### 1. Create a Python 3.8 virtualenv

#### 2. Install django :

    pip install django
  
#### 3. Go to directory of project and activate virtual env :

    cd directory_of_project
    workon virtual_env_name
  
#### 4. Download and install PostgreSQL and pgAdmin 

#### 5. Create new database in pgAdmin and change DATABASES field in settings.py file in TechReviews
    
    # settings.py file
    DATABASES = {    # change this if you want to run this project on your device.
    'default': {                  
        'ENGINE': 'django.db.backends.postgresql',  
        'NAME': 'db_name',              # your database name              
        'USER': 'postgres',             # username of pgAdmin      
        'PASSWORD': '1234',             # password of pgAdmin
        'HOST':'localhost'
    }
    }

#### 6. Now execute following commands on command prompt

    python manage.py makemigrations
    python manage.py migrate

#### 7. Start server
     
    python manage.py runserver
   
#### 8. Now search http://127.0.0.1:8000/  in the browser.   
Right now only admin can add new product. So you have to add products and those products will be displayed on home screen.
#### 9. To add product 

        python manage.py createsuperuser
Now go to Go to http://127.0.0.1:8000/admin and login to add new products.       
