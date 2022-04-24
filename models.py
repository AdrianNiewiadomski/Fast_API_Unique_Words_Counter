from sqlalchemy import Column, Integer, String, TIMESTAMP

from database import Base


class RequestTexts(Base):
    __tablename__ = "request_texts"

    id = Column(Integer, primary_key=True, index=True)
    creation_timestamp = Column(TIMESTAMP)
    text = Column(String)
    unique_words_count = Column(Integer)
