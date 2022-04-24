from sqlalchemy import Boolean, Column, Integer, String, TIMESTAMP

from database import Base


class Requests(Base):
    __tablename__ = "requests"

    id = Column(Integer, primary_key=True, index=True)
    # email = Column(String, unique=True, index=True)
    # hashed_password = Column(String)
    # is_active = Column(Boolean, default=True)

    # creation_timestamp
    text = Column(String)
    unique_words_count = Column(Integer)
