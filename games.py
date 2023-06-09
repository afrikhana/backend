from sqlalchemy import String, Column, Integer, create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class Games(Base):
    __tablename__ = 'game'

    id_no = Column(Integer, primary_key = True, autoincrement=True)
    title = Column(String(40), nullable=False)
    descriptive= Column(String(500), nullable=False)
    genre= Column(String(30), nullable=False)
    release_date= Column(String(30), nullable=False)
    developer=Column(String(40), nullable=False)
    url=Column(String(100), nullable=False)
    platforms= Column(String(40), nullable=False)
    # reviews = relationship('Review', back_populates='game')

class Review(Base):
    __tablename__ = 'reviews'

    id_no = Column(Integer, primary_key=True, autoincrement=True)
    rating = Column(String)
    comments = Column(String)
    # game_id = Column(Integer, ForeignKey('games.id_no'))
    # user_id = Column(Integer, ForeignKey('users.id_no'))
    # game = relationship('Games', back_populates='reviews')

class User(Base):
    __tablename__ = 'users'

    id_no = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)
    password= Column(String(20),nullable=False)

engine= create_engine('sqlite:///db.db')
Base.metadata.create_all(engine)
Session= sessionmaker(bind=engine)
session=Session()