from db.base_class import Base
from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship
from .blog import Blog

class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(100),nullable=False,unique=True,index=True)
    password = Column(String(50), nullable = False)
    is_active = Column(Boolean,default=True)
    is_admin = Column(Boolean,default=False)
    blogs = relationship("Blog",back_populates="author")