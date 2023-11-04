import requests
URL = 'http://localhost:8000/api/v1/users/login'

USER = {
    'username': 'eduardo_gpg',
    'password': 'password'
}

response = requests.post(URL, json=USER)

if response.status_code == 200:
    print('Usuario autenticado de forma exitosa.')
    
    print(response.json())
    
    print(response.cookies)
    print(response.cookies.get_dict())
    
    user_id = response.cookies.get_dict().get('user_id')
    
    print(user_id)