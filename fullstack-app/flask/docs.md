# Flask routes documentation:

## `GET /read/{id}`
- returns: 
```json
{
    "username": 'string', 
    "email": 'string'
}
```

## `GET /list`
- returns an object with every user:
```json
{
    "0": {
        "username": "string",
        "email": "string"
    },
    "1": {
        "username": "john doe",
        "email": "john-doe@example.com"
    }, 
    .....
}
```

## `POST /update/{id}`
`body`:
```json
{
    "uid": int,             // required
    "username": "string",   // optional
    "email": "string"       // optional
}
```

Updates the username and/or email address associated with a user id
- returns: 
    - success: `200 OK`
    - failure: `400 Bad Request`

## `DELETE /delete/{id}`
`body`:
```json
{
    "id": int
}
```
- returns: 
    - success: `200 OK`
    - failure: `404 Resource not found`
