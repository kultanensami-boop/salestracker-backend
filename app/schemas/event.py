from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class EventCreate(BaseModel):
    categories: List[str]
    comment: Optional[str] = None
    url: Optional[str] = None

class EventResponse(EventCreate):
    id: int
    user_id: int
    timestamp: datetime

    class Config:
        orm_mode = True

