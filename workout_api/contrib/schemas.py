from typing import Annotated
from pydantic import UUID4, BaseModel, Field
from datetime import datetime

class BaseSchema(BaseModel):
    class Config:
        extra = 'forbid'
        from_attributes = True
        
class OutMixin(BaseModel):
    id: Annotated[UUID4, Field(description='Identificado')] 
    created_at: Annotated[datetime, Field(description='data de criação')]
    