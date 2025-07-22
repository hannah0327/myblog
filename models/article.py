from routes import db
from datetime import datetime
from sqlalchemy import Integer, String, BLOB, TIMESTAMP
from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import func

class Article(db.Model):
    __tablename__ = 'articles'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    __content: Mapped[bytes] = mapped_column(BLOB, name="content", nullable=False)
    create_time: Mapped[datetime] = mapped_column(TIMESTAMP, nullable=False, server_default=func.now())
    update_time: Mapped[datetime] = mapped_column(TIMESTAMP, nullable=True, server_default=func.now(), onupdate=func.now())

    # GET 方法 to retrieve content as a string
    @property
    def content(self):
        return self.__content.decode('utf-8')
    
    # SET 方法 to set content from a string
    @content.setter
    def content(self, content_value: str):
        self.__content = content_value.encode('utf-8')