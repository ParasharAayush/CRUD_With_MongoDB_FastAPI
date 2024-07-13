
# CRUD Operations with MongoDB and FastAPI


In this project we have developed a complete application that performs CRUD (Create, Read, Update, Delete) operations on a MongoDB database using Python. We have implemented wrapper functions for each CRUD operation and integrated these functions with the FastAPI framework to expose these operations as RESTful APIs.


## Table of Contents
- [Requirements](#requirements)
- [Installation](#installation)
- [Setup MongoDB](#setup-mongodb)
- [Running the Application](#running-the-application)
- [API Endpoints](#api-endpoints)
- [Testing with Postman](#testing-with-postman)
- [Error Handling](#error-handling)
- [Contributing](#contributing)
## Requirements
- Python 3.8+
- MongoDB
- FastAPI
- Uvicorn
- pymongo
## Installation
1. Clone the repository:
```shell
git clone https://github.com/ParasharAayush/CRUD_With_MongoDB_FastAPI.git
cd CRUD_With_MongoDB_FastAPI
```
2. Install the required packages:
```shell
pip install fastapi uvicorn pymongo
```



## Setup MongoDB
1. Install MongoDB:
Follow the MongoDB installation guide for your operating system.

2. Start MongoDB:

Ensure MongoDB is running. You can start it using:

```shell
mongod
```
3. Create Database and Collection:
Connect to MongoDB using the MongoDB shell:
```shell
mongo
```

4. Create a database and collection:
```shell
use testdb
db.items.insertOne({ name: "Sample Item", description: "This is a sample item." })
```
## Running the Application
1. Start the FastAPI application using Uvicorn:
```shell
uvicorn main:app --reload
```
2. The application will be available at http://127.0.0.1:8000
## API Endpoints
1. Create an Item:
URL: '/items/'\
Method: 'POST'\
Request Body:
```shell
{
    "name": "Item1",
    "description": "Description1"
}
```
Response:
```shell
{
    "id": "6692c7f8dac7f446a6a726fa"
}
```
2. Read an Item:
URL: '/items/{name}'\
Method: 'GET'\
Response:
```shell
{
    "_id": "6692c7f8dac7f446a6a726fa",
    "name": "Item1",
    "description": "Description1"
}
```
3. Read All Items
URL: '/items/'\
Method: 'GET'\
Response:
```shell
{
    {
        "_id": "6692b2703d8aef282fc4e49b",
        "name": "Sample Item",
        "description": "This is a sample item."
    },
    {
        "_id": "6692c7f8dac7f446a6a726fa",
        "name": "Item1",
        "description": "Description1"
    }
}
```
4. Update an Item
URL: '/items/{name}'\
Method: 'PUT'\
Request Body:
```shell
{
    "description": "Updated Description"
}
```
Response:
```shell
{
    "updated": 1
}
```
5. Delete an Item
URL: '/items/{name}'\
Method: 'DELETE'\
Response:
```shell
{
    "deleted": 1
}
```


## Testing with Postman
1. Create an Item:
Method: 'POST'\
URL: 'http://127.0.0.1:8000/items/' \
Body:
```shell
{
    "name": "Item1",
    "description": "Description1"
}
```
2. Read an Item:
Method: 'GET'\
URL: 'http://127.0.0.1:8000/items/item1'

3. Read All Items:
Method: 'GET'\
URL: 'http://127.0.0.1:8000/items/'

4. Update an Item:
Method: 'PUT'\
URL: 'http://127.0.0.1:8000/items/Item1' \
Body: 
```shell
{
    "updated": 1
}
```

5. Delete an Item:
Method: 'DELETE'\
URL: 'http://127.0.0.1:8000/items/Item1'





## Error Handling
The application includes basic error handling to manage database connection issues and data validation errors. If an error occurs, the API will return an appropriate HTTP status code and error message.
## Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your changes.
