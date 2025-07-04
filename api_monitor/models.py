from sqlalchemy import Column, Integer, String, DateTime, Text, create_engine
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class SystemInfo(Base):
    __tablename__ = 'system_info'
    
    id = Column(Integer, primary_key=True)
    timestamp = Column(DateTime)
    ip_address = Column(String)
    processor = Column(String)
    os_name = Column(String)
    os_version = Column(String)
    running_processes = Column(Text)  
    logged_in_users = Column(Text)        