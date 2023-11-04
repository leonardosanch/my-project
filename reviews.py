import requests

REVIEW_ID = 10
URL = f'http://localhost:8000/api/v1/reviews/{REVIEW_ID}'

REVIEW = {
    'review': 'Nueva review actualizamos el contenido',
    'score': 1
}

response = requests.put(URL, json=REVIEW)

if response.status_code == 200: 
    print('La reseña se actualizo de forma correcta.')
    print(response.json())
    
