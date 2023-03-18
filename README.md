# README #

### What is this repository for? ###

* This repository is for the backend of niflr store edge device
* Python version used: 3.9.13

### Databse Configuration: ###

```python
DATABASES = {  
    'default': {  
        'ENGINE': 'django.db.backends.postgresql_psycopg2',  
        'NAME': "postgres",  
        'PASSWORD': "12345",  
        'USER': "postgres",  
        'HOST': "localhost",  
        'PORT': "1234",  
    }  
}  
```

### Set up procedure ###

* clone the repository
* execute command: "pip3 install -r requirements.txt" for installing all the required libraries
* execute command: "python3 manage.py makemigrations niflr_edge_store" for generating migration files
* execute command: "python3 manage.py migrate" for migration
* For creating a new superuser, execute command: "python3 manage.py createsuperuser --email admin@example.com --username admin", replace email and username as per requirement
* execute command: "python3 manage.py runserver" for starting the server
* default url for server: "http://127.0.0.1:8000/"

### Database Structure ###

```python
niflr_edge_store-backend  
    |-- camera  
        |-- Videos (stores path to 5 minutes (variable) clips of each camera live feed)  
        |-- Cameras (stores details of all the cameras inside a particular store)  
        |-- Scanners (stores details of all the scanners (QR Code Scanner) inside a particular store)  
    |-- iot   
        |-- weight changes (stores details of each weight change event - both picking and putting back products by all types of user)    
        |-- machines (stores details of all the machines inside a particular store)     
        |-- machine sessions (generates new session after every 5 minutes (variable))   
    |-- ticket   
        |-- tickets (stores data of all the tickets generated)
    |-- user   
        |-- user sessions (stores all the events related to login and logout of all the users, user can be a customer, admin or operations' person)   
        |-- user details (local record of all the user details)   
        |-- carts (carts stores data related to the mapping of user id and product, which user has picked what product)   
        |-- store mode changes (stores changes in store mode, i.e. Customer, Refillment or Maintenance)
    |-- niflr_edge_stre (contains celery, settings and master control of urls)   
```
### Code Structure ###

* Each folder consists of models (fields in each table), serializers, views and urls
* weight.log file stores all the logs related to weight change events and heartbeat.log stores each heartbeat event

### Machine or Instrument Onboarding ###

* Details of new camera, scanner, or machine can be added to the database directly from Django admin panel "http://127.0.0.1:8000/admin/"

### Ticket Details ###

* Tickets are generated as soon as some user logs out of the store (after scanning QR Code), number of tickets generated for each user is equal to the number of machines present in the store. Each ticket stores the following data: TktID, Start_Time (Login Time of User), End_Time (Logout time of user), all Weight Change Events occuring in that specific time period for a specific machine, User_ID, Video links of all the videos captured in the time period, Machine_ID and Status of ticket (To be reviewed, review under process, review complete)

### Comments ###

* Should we generate tickets based on Start Time and End Time or based on Store Sessions ???