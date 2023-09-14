# API Documentation

This documentation provides information on how to use the the Project API.

# ER design for the project:


<img width="533" alt="Screenshot 2023-09-14 144322" src="https://github.com/denscholar/hngXstageTwo/assets/48631109/16020bbd-7af0-4d9e-9059-5d10cc40f864">



## API Endpoints

### List all Persons

- **URL**: `/api/`
- **Method**: `GET`
- **Description**: Get a list of all persons.

**Request**

No request data is required.

**Response**

```json
Status: 200 OK
Content-Type: application/json

[
  {
    "id": 1,
    "name": "John Doe",
    "age": "30",
    "email": "john@example.com",
    "house_address": "123 Main St",
    "occupation": "Software Engineer",
    "interest": "Coding"
  },
  {
    "id": 2,
    "name": "Jane Smith",
    "age": "25",
    "email": "jane@example.com",
    "house_address": "456 Elm St",
    "occupation": "Designer",
    "interest": "Art"
  }
]

```


### Create a New Person
- **URL**: `/api/`
- **Method**: `POST`
- **Description**: Create a new person.

**Request**

No request data is required.

```json
Status: 200 OK
Content-Type: application/json

{
  "name": "Alice Johnson",
  "age": 28,
  "email": "alice@example.com",
  "house_address": "789 Oak St",
  "occupation": "Data Scientist",
  "interest": "Machine Learning"
}

Status: 201 Created
Content-Type: application/json

{
  "message": "Person successfully added"
}
```


### Retrieve a Person by id or name
- **URL**: `/api/<str:id_or_name>/`
- **Method**: `GET`
- **Description**: Retrieve a person by their id or name.

**Request**

```json
Status: 200 OK
Content-Type: application/json

{
  "id": 1,
  "name": "John Doe",
  "age": 30,
  "email": "john@example.com",
  "house_address": "123 Main St",
  "occupation": "Software Engineer",
  "interest": "Coding"
}
```


### Update a Person by id or name
- **URL**: `/api/<str:id_or_name>/`
- **Method**: `PUT`
- **Description**: Update a person by their id or name.

**Request**

```json
Content-Type: application/json

{
  "name": "Updated Name",
  "age": 35
}
```
**Response**
Status: 200 OK
Content-Type: application/json
```json
{
  "message": "Person updated"
}

```

### Delete a Person by id or name
- **URL**: `/api/<str:id_or_name>/`
- **Method**: `DELETE`
- **Description**: Delete a person by their id or name.

**Request**

```json
Content-Type: application/json

{
  "name": "Updated Name",
  "age": 35
}
```

Request

No request data is required.


**Response**

```json
Status: 204 No Content
Content-Type: application/json
{
  "message": "Person updated"
}

```
# Known Limitations
This API does not provide user authentication and authorization. It's recommended to implement proper authentication and authorization mechanisms in a production environment.
Error handling and validation messages in responses may be limited in some cases. Custom error messages and handling can be enhanced further.


# Local Setup and Deployment
Follow the instructions in the README.md file for setting up and running the API locally. For deployment, configure a production server, set environment variables, and serve the API using a WSGI server.

