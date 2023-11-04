from typing import List

from fastapi import FastAPI
from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import status

from fastapi.security import OAuth2PasswordRequestForm

from .database import User
from .database import Movie 
from .database import UserReview
from .routers import user_router
from .routers import review_router
from .routers import movie_router

from .common import create_access_token

from .database import Database as connection




app = FastAPI(title='Proyecto para reseñar peliculas',
              description='En este proyecto seremos capaces de reseñar peliculas.',
              version='1')

api_v1 = APIRouter(prefix='/api/v1')


api_v1.include_router(user_router)
api_v1.include_router(review_router)
api_v1.include_router(movie_router)

@api_v1.post('/auth')
async def auth(data: OAuth2PasswordRequestForm = Depends()):
    user = User.authenticate(data.username, data.password)
  
    if user:
        return{
            'access_token': create_access_token(user),
            'token_type': 'Bearer'
            
        }
    else:
        raise HTTPException(
            status_code = status.HTTP_401_UNAUTHORIZED,
            detail='Username o Password incorrectos',
            headers={'WWW-Authenticate': 'Bearer'}
            
        )
        
    
    

app.include_router(api_v1)


@app.on_event('startup')
def startup():
    if connection.is_closed():
        connection.connect()
        
    connection.create_tables([User, Movie, UserReview])
        
        
        
@app.on_event('shutdown')
def shutdown():
    if not connection.is_closed():
        connection.close()
        
        
        





    
