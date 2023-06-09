from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional
from games import Games, Review, User, session

from fastapi.middleware.cors import CORSMiddleware
app=FastAPI()

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:3000",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
class GamesSchema(BaseModel):
    title:str
    descriptive:str
    genre:str
    release_date:str
    developer:str
    url:str
    platforms:str
    class Config:
        orm_mode=True
class  updateGameSchema(BaseModel):
    title:Optional[str] = None
    descriptive:Optional[str] = None
    genre:Optional[str] = None
    release_date:Optional[str] = None
    developer:Optional[str] = None
    url:Optional[str] = None
    platforms:Optional[str] = None
    class Config:
        orm_mode=True


        
@app.get('/')
def get_all_games() -> List[GamesSchema]:
    games= session.query(Games).all()
    return games
@app.post('/data')
def add_data(game: GamesSchema) -> GamesSchema:
    gm = Games(**dict(game))
    session.add(gm)
    session.commit()
    return game
@app.patch('/patch_endpoint/{id}')
def update_data(id: int, data:updateGameSchema) -> GamesSchema:
    existing_data= session.query(Games).get(id)
    if existing_data is None:
        return {"error":"Data not found"}
    for field, value in data.dict(exclude_unset=True).items():
        setattr(existing_data, field, value)
        session.commit()
        return{"message":"Data update successfully"}
@app.delete('/delete/{id}')
def delete_all(id:int) -> None:
    game = session.query(Games).filter_by(id_no=id).first()
    session.delete(game)
    session.commit()    
    
@app.put('/updateall/{id}')
def update_all(id:int, data:updateGameSchema) -> GamesSchema :
    pts=session.query(Games).get(id)
    if pts is None:
    # no values
      return {"error":"data not found"}   
    pts.title = data.title
    pts.descriptive = data.descriptive
    pts.genre = data.genre
    pts.release_date = data.release_date
    pts.developer = data.developer
    pts.url = data.url
    pts.platforms = data.platforms
    session.commit()
    return pts



class ReviewModel(BaseModel):
    rating: str
    comments: str


@app.get('/get_review')
def get_reviews():
    reviews = session.query(Review).all()
    return reviews


@app.post('/reviews')
def add_review(review: ReviewModel):
    new_review = Review(**review.dict())
    session.add(new_review)
    session.commit()
    return new_review
@app.delete('/delete_review/{id}')
def delete_all(id:int) -> None:
    rev = session.query(Review).filter_by(id_no=id).first()
    session.delete(rev)
    session.commit()   

class UserName(BaseModel):
    username: str
    email: str
    password: str


@app.get('/users')
def get_users():
    users = session.query(User).all()
    return users


@app.post('/users')
def add_user(user: UserName):
    new_user = User(**user.dict())
    session.add(new_user)
    session.commit()
    return new_user
@app.delete('/delete_usr/{id}')
def delete_all(id:int) -> None:
    usr = session.query(User).filter_by(id_no=id).first()
    session.delete(usr)
    session.commit()

@app.patch("/users/{id}")
def update_user(id: int, user: UserName):
    existing_user = session.query(User).filter(User.username == id).first()
    if existing_user:
        for field, value in user.dict(exclude_unset=True).items():
            setattr(existing_user, field, value)
        session.commit()
        return existing_user
