import requests

REVIEW_ID = 10
URL = f'http://localhost:8000/api/v1/reviews/{REVIEW_ID}'

response = requests.delete(URL)

if response.status_code == 200: 
    print('La reseña fue eliminada de forma correcta.')
    print(response.json())
else: 
    
    print(response.content)
    
