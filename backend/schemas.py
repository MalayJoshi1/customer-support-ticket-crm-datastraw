from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional, List

class NoteResponse(BaseModel):
    id: int
    ticket_id: str
    note_text: str
    created_at: datetime

    class Config:
        from_attributes = True

class TicketCreate(BaseModel):
    customer_name: str
    customer_email: EmailStr
    subject: str
    description: str

class TicketUpdate(BaseModel):
    status: str
    notes: Optional[str] = None

class TicketListResponse(BaseModel):
    id: int
    ticket_id: str
    customer_name: str
    customer_email: str
    subject: str
    status: str
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True

class TicketDetailResponse(BaseModel):
    id: int
    ticket_id: str
    customer_name: str
    customer_email: str
    subject: str
    description: str
    status: str
    created_at: datetime
    updated_at: Optional[datetime] = None
    notes: List[NoteResponse] = []

    class Config:
        from_attributes = True