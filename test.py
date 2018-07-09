from sqlalchemy import create_engine, Column, String, Integer      #注意添加没有的类型
from sqlalchemy.ext.declarative import declarative_base          
from sqlalchemy.orm import sessionmaker
from faker import Faker
import random

engine = create_engine('mysql://txuser:!QAZ2wsx3edc4r@10.201.251.35/tx_alert')
Base = declarative_base(engine)
session = sessionmaker(engine)()

class Test(Base):                                                
    __tablename__ = 'test'
    logid = Column(Integer, primary_key=True)
    name = Column(String(1024), unique=True, nullable=False)
    email = Column(String(128), unique=True, nullable=False)
    luanma = Column(String(128), unique=True, nullable=False)
    def __repr__(self):
        return '<Test: {}>'.format(self.name)
#Base.metadata.create_all()
#from faker import Faker
fake = Faker()
#rnum = random.randint(2,9) 
i = 1
while i < 100: 
    t = Test(name=fake.name(), email=fake.email(),luanma=fake.name())
    session.add(t)
    session.commit()
    i += 1