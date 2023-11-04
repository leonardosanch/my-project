from fastapi import APIRouter

from ..database import Movie

from datetime import datetime

from ..schemas import MovieResponseModel
from ..schemas import MovieRequestModel


router = APIRouter(prefix='/movies')

    
@router.post('/movies',response_model=MovieResponseModel)
async def create_movie(movie: MovieRequestModel):  
     
    movie = Movie.create(
        title = movie.title,
        created_at = datetime.now()
    )
    return movie    