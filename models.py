from sqlalchemy import Boolean, Column, Integer, String, TIMESTAMP

from database import Base


class RequestTexts(Base):
    __tablename__ = "request_texts"

    id = Column(Integer, primary_key=True, index=True)
    # creation_timestamp - timestamp at the moment of handling request
    text = Column(String)
    unique_words_count = Column(Integer)

    def __str__(self):
        return str({"id": self.id, "text": self.text, "uniqueWordsCount": self.unique_words_count})
