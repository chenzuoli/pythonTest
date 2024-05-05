from SQLAlchemy import Column, Integer, Boolean, String, DateTime

class User:
    __table__name = "users"
    id = Column(Integer, primary_key=True)