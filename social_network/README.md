# Image Social Network CRUD API with Django REST framework
This API is based on 
[Django REST framework](https://www.django-rest-framework.org), a powerful and flexible toolkit for building Web APIs. 

## Requirements
* Django 5.0.2
* Django REST framework 3.14.0
* Pillow 10.2.0
* Psycopg2-binary 2.9.9
* Geopy 2.4.1

## Installation
After you cloned the repository, you want to create a virtual environment, so you have a clean python installation. You can do this by running the command:
```
python -m venv env
```
You can install all the required dependencies by running:
```
pip install -r requirements.txt
```
## Structure
In a RESTful API, endpoints (URLs) define the structure of the API and how end users access data from our application using the HTTP methods - GET, POST, PUT, DELETE. 
In our case, we have one several resources, posts, comments and likes, so we will use the following URLS - /api/posts/ and /api/posts/<id> and so on for /api/likes/ and /api/comments/ for collections and elements, respectively:

| Endpoint | HTTP Method | Result |
| -------- | ----------- | ------ |
| /api/posts/ | GET | Get all posts |
| /api/posts/:id | GET | Get a single post |
| /api/posts/ | POST | Create a new post |
| /api/posts/:id | PUT | Update a post |
| /api/posts/:id | DELETE | Delete a  post |

The structure of posts model is the following:
```
{   user : set automatically,
    text : 'post text', 
    uploaded_images : image files (optional),
    created_at : set automatically,
    location : 'text explaination'(optional) }
```

Users can leave comments to posts with the following HTTP Methods:
| Endpoint | HTTP Method | Result |
| -------- | ----------- | ------ |
| /api/comments/ | GET | Get all comments |
| /api/comments/:id | GET | Get a single comment |
| /api/comments/ | POST | Create a new comment |
| /api/comments/:id | PUT | Update a comment |
| /api/comments/:id | DELETE | Delete a comment |

Comments structure:
```
{   user : set automatically,
    post : id of a post,
    text : 'text of a comment'
}
```

And process likes:

| Endpoint | HTTP Method | Result |
| -------- | ----------- | ------ |
| /api/likes/ | GET | Get all likes |
| /api/likes/:id | GET | Get a single like |
| /api/likes/ | POST | Create a new like |
| /api/likes/:id | PUT | Update like |
| /api/likes/:id | DELETE | Delete like |

Likes structure:
```
{   user : set automatically,
    post : id of a post,
}
```

To create, update or delete an element an access token shoul be obtained via /admin/ panel. To view the elements no tokens are needed.


