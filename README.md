educa
================================

### This is an e-learning platform with own content management system (CMS)


### Implemented:
* Created fixtures for models
* Used model inheritance
* Created custom model fields
* Used class-based views and mixins
* Built formsets
* Created a CMS
* Created public views for displaying course information
* Built a student registration system
* Manage student enrollment onto courses
* Render diverse content for course modules
* Installed and configured Memcached
* Cache content using the Django cache framework
* Monitor Memcached using the django-memcache-status
* Installed Django REST framework
* Created serializers for your models
* Built a RESTful API
* Created nested serializers
* Built custom API views
* Handled API authentication
* Added permissions to API views
* Created a custom permission
* Implemented viewsets and routers
* Used the Requests library to consume the API
* Added Channels to project
* Built a WebSocket consumer and appropriate routing
* Implemented a WebSocket client
* Enabled a channel layer with Redis
* Made consumer fully asynchronous

### The going_live branch is used to set up a production environment on an online server so that it can be accessed over the Internet

### Implemented:
* Configured project settings for a production environment
* Used a PostgreSQL database
* Set up a web server with uWSGI and NGINX
* Serve static assets through NGINX
* Secure connections using SSL
* Used Daphne to serve Django Channels
* Created a custom middleware
* Implemented custom management commands


### Getting Started:
1. to start the server use: python manage.py runserver (stop Ctrl + C)
2. in terminal Ubuntu to start Memcached run: memcached -l 127.0.0.1:11211 (stop Ctrl + C)
3. in terminal Ubuntu to start the Redis server: sudo service redis-server start (stop  sudo service redis-server stop)

for the going_live branch
1. to start the server use: python manage.py runserver --settings=educa.settings.pro (or local)
2. to start NGINX run: sudo nginx (stop sudo nginx -s quit or sudo nginx –s stop)


### Additional Programs:
for Windows
- Windows 10 with WSL
- Ubuntu 18.04 
- redis-cli 4.0.9
- Memcached 1.5.6
for going_live branch
- PostgreSQL 11
- NGINX 1.14.0-0ubuntu1.9
- additional packages uWSGI==2.0.18 and daphne==2.4.1

## Required packages:

* Python 3.9
* virtualenv + pip
* Git