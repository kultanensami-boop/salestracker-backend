from sqlalchemy import Column, Integer, String, DateTime, JSON, ForeignKey
from sqlalchemy.sql import func
from app.database import Base

class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, index=True)  # myöhemmin ForeignKey
    timestamp = Column(DateTime(timezone=True), server_default=func.now())
    categories = Column(JSON, nullable=False)
    comment = Column(String, nullable=True)
    url = Column(String, nullable=True)

