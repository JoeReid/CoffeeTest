from .          import Base
from sqlalchemy import Column, Integer, Unicode

class Member(Base):
    __tablename__= "member"
    id           = Column(Integer(),  primary_key=True)
    name         = Column(Unicode(),  nullable=False)
