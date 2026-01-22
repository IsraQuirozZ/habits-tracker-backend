from pydantic import BaseModel, validator
from typing import Optional
from datetime import datetime
import re

# Validaciones aquí
class HabitBase(BaseModel):
    name: str 
    description: Optional[str] = None

    @validator('name')
    def validate_name(cls, v: str) -> str:

        if not v or not v.strip():
            raise ValueError ('El campo no puede estar vacío')

        v = v.strip()

        if len(v) < 3:
            raise ValueError('Debe tener al menos 2 caracteres')
        
        if len(v) > 100:
            raise ValueError('No puede exceder 100 caracteres')

        # Solo letras, espacios, tildes y caracteres especiales del español
        if not re.match(r'^[a-zA-ZáéíóúÁÉÍÓÚñÑüÜ\s]+$', v):
            raise ValueError('Solo se permiten letras y espacios')
        
        return v.title()
    
    @validator('description')
    def validate_description(cls, v: str) -> str:
        v = v.strip()

        if len(v) > 250:
            raise ValueError('No puede exceder 100 caracteres')
        
        return v.title()

class HabitCreate(HabitBase):
    pass


class HabitResponse(HabitBase):
    id: int
    is_active: bool
    created_at: datetime

    class Config:
        orm_mode = True
