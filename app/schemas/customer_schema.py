from pydantic import BaseModel, EmailStr
from typing import Optional

class CustomerSchema(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    address: Optional[str] = None

    class config:
        orm_mode = True

