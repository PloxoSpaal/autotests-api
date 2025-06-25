import httpx


login_body = {
  "email": "user121@example.com",
  "password": "string"
}
link = 'http://localhost:8000'
login_response = httpx.post(link+'/api/v1/authentication/login',json=login_body)
access_token = login_response.json()['token']['accessToken']
users_me_headers = {"Authorization": f"Bearer {access_token}"}
user_response = httpx.get(link+'/api/v1/users/me',headers=users_me_headers)
print(user_response.json())
print(user_response.status_code)