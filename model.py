from sqlalchemy import Column, Integer, String, Date, ForeignKey, Float, Boolean, DateTime, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship,sessionmaker

Base = declarative_base()
engine = create_engine('sqlite:///database.db')

DBSession = sessionmaker(bind=engine, autoflush=False)
session = DBSession()

class Messages(Base):
	__tablename__ = 'messages'
	id = Column(Integer,primary_key=True)
	name = Column(String)
	message = Column (String) 

Base.metadata.create_all(engine)