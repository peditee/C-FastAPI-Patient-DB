from pydantic import BaseModel

class Patient(BaseModel):
    reference_number: int
    name: str
    date_of_birth: str
    address: str

    class Config:
        orm_mode = True
