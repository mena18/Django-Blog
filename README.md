Django Blog
===================
this is a Full featured blog build with python and Django where People can read articles and comment on them or share the article with friends 


Features
-------------
- Articles/Posts
	- [X] Author can write/edit/delete articles using django admin dashboard
	- [X] Article are displayed in descending order with 20 word maximum for the body  and the full body displayed in the detailed article after clicking Read me
	- [X] Pagination used to display 3 articles per page 
	- [X] article images are resized to (600,300) when article created automatically   
- Tags 
	- [X] you can create articles with different tags 
	- [X] tags are used to get similar articles by getting the articles that contains the same tags
	- [X] when clicking on and tags you can view all articles with the same tag
- Search
	- [X] you can search articles by title 
	- [ ] improve the search by allowing search by tags or search by body of the article
- Subscribing
    - [X] users can Subscribe to the blog and receive an email for every new created article
    
- Sharing posts
    - [X] users can share article  with friend  by adding their email and the article link will be sent to them
- Most commented posts
    - [X] you can view the 5 most Commented articles (using template tags so it's easy to use the same block in and other template ) 
- Comments
	- [X] user can leave a comment on any article 
- Sub Comments 
	- [X] user can reply on other users comments 
	- [X] you can view or hide the reply form for each comment 
- Admin Dashboard 
	- [X] you can work with all models (Posts,comments,users,tags) in the software using Django Dashboard
	- [X] adding some customization to allow searching and filtering for the models

- Authors
	- [ ] Author can write/edit/delete Articles from the home page with normal forms instead  of using django dashboard
	- [ ] Add Author section in the detailed page to show information about the author 

- users
	- [ ] register and login in the blog 
	- [ ] receive regular email gradually as they are Technically subscribing 
	- [ ] can comment without saying their name or email
	- [ ] can have profile image 
	- [ ] edit and delete comments


----------------------

Visuals
-------------

![alt_text](https://raw.githubusercontent.com/mena18/Django-Blog/master/screenShots/Home_page.png)

----------

![alt_text](https://raw.githubusercontent.com/mena18/Django-Blog/master/screenShots/post_detail.png)


----------

Prerequisites
-------------
Before you begin, ensure you have met the following requirements:

- you have installed python3.6 or above

-------------- 

Installation and usage
-------------

1- fork or download this repository and then open the folder in your CLi

2- install all the dependencies 

On Linux and macOS:
``` bash
pip3 install -r requirements.txt
```
On Windows:

``` bash
pip install -r requirements.txt
```

> **Notes:**

 > - you can use virtual environment "venv" if you want to install all the requirements inside virtual environment instead of installing them directly on your operating system you [click here for more inforation](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)
 
 >- please contact me if you have problems in the Installation process  


----------------------

Usage 
------------
 after installing all the requirements run the app

On Linux and macOS:
``` bash
python3 manage.py runserver
```
On Windows:

``` bash
python manage.py runserver
```
----------
you should see something like this in the console 

![alt_text](https://raw.githubusercontent.com/mena18/Django-Blog/master/screenShots/running.png)
this mean the server is running and you can continue next step 

open your browser and write that link to view the project
``` bash
http://127.0.0.1:8000/
```
to add new articles from the admin panel write 
``` bash
http://127.0.0.1:8000/admin
```
- username = admin
- password = 123

You can change the username and password or add new users (must be superuser to add articles)


----------------------




Dependencies
-------------------



- Front End
	- Bootstrap 4
	- mdbootstrap


- Back End
	- Django3
	- django-taggit
	- Pillow

----------------------

License
--------------

Django Blog is open source software licensed as MIT.
