import httpx
from random import randrange


link = 'http://localhost:8000'
create_user_body = {
  "email": f"user{randrange(1,100)}{randrange(1,100)}{randrange(1,100)}{randrange(1,100)}@example.com",
  "password": "string",
  "lastName": "string",
  "firstName": "string",
  "middleName": "string"
}
create_user_response = httpx.post(link + '/api/v1/users',json=create_user_body)
print(create_user_response.status_code)
first_email = create_user_body['email']
login_body = {
  "email": create_user_response.json()['user']['email'],
  "password": create_user_body['password']
}
login_user_response = httpx.post(link + '/api/v1/authentication/login', json=login_body)
access_token = login_user_response.json()['token']['accessToken']
print(login_user_response.status_code)
user_id = create_user_response.json()['user']['id']
update_user_body = {
  "email": f"user{randrange(1,100)}{randrange(1,100)}{randrange(1,100)}{randrange(1,100)}@example.com",
  "lastName": "string",
  "firstName": "string",
  "middleName": "string"
}
update_user_headers = {"Authorization": f"Bearer {access_token}"}
second_email = update_user_body['email']
update_user_response = httpx.patch(link + f'/api/v1/users/{user_id}', json=update_user_body, headers=update_user_headers)
print(update_user_response.status_code)