"""
Pydantic schemas for order operations.
"""

import uuid
from decimal import Decimal

from pydantic import BaseModel, Field


class OrderCreate(BaseModel):
    """Schema for creating a new order"""

    user_id: uuid.UUID = Field(..., description="ID of the user placing the order")
    price: Decimal = Field(..., description="Price of the order")
    token: str = Field(..., description="Token symbol for the order")
    position: uuid.UUID = Field(..., description="Position ID related to the order")


class OrderResponse(BaseModel):
    """Schema for order response"""

    id: uuid.UUID
    user_id: uuid.UUID
    price: Decimal
    token: str
    position: uuid.UUID

    class Config:
        """Pydantic model configuration"""

        from_attributes = True
