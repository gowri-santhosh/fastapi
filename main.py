from fastapi import FastAPI, HTTPException
from data import movies_list
from genre import GenreEnum
from movie_model import MovieBaseModel

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/pagination")
async def pagination(offset: int = 1, limit : int = 10):
    all_movies = list(movies_list.values())
    mv_cnt = len(all_movies)
    start = (offset - 1) * limit
    end = start + limit
    if start >= mv_cnt:
        return None
    return all_movies[start:end]


@app.get("/movies/{name}")
async def search_movies(name: str):
    if name not in movies_list:
        raise HTTPException(status_code=404, detail=f"{name} not found")
    return movies_list[name]


@app.get("/movies/genre/{genre}")
async def search_genre(genre: GenreEnum):
    data = list(movies_list.values())
    genre_movies = []
    for i in data:
        if i["genre"] == genre.value:
            genre_movies.append(i)
    return genre_movies


@app.post("/movies")
async def create_movie(movie: MovieBaseModel):
    movies_list[movie.name] = movie.model_dump()
    return {"message": f"Movie {movie.name} created"}


@app.delete("/delete_movies/{name}")
async def delete_movie(name: str):
    if name not in movies_list:
        raise HTTPException(status_code=404, detail=f"{name} not found")
    del movies_list[name]
    return {"message": f"Movie {name} deleted"}


@app.put("/update_movies/{name}")
async def update_movie(movie: MovieBaseModel):
    if movie.name not in movies_list:
        raise HTTPException(status_code=404, detail=f"{movie.name} not found")
    movies_list[movie.name] = movie.model_dump()
    return {"message": f"Movie {movie.name} updated"}
