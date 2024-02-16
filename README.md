# TuComida

## About

This project is a web page for TuComida.

## How to run

1. Clone the repository
2. Configure the environment variables:
    - crete a .env file in the root of the project for database variables

    ```bash
    PS_HOST="xxxxx"
    PS_DBNAME="xxxxx"
    PS_USER="xxxxx"
    PS_PASSWORD="xxxxxx"
    PS_PORT="xxxx"
    ```
3. just run app.py

## Populate the database

for insert user values to test the app ensure hash the password with the following code:

```python
from werkzeug.security import check_password_hash, generate_password_hash

# generate a hash
pswh = generate_password_hash("MyStrongPassword!")
print("MY HASH: ", pswh)

# if you want check the hash
print("CHECK HASH: ", check_password_hash("My hashed pass", "MyStrongPassword!"))
```
then you can use the hash to insert the user password in the database.


