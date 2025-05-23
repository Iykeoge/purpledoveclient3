from pydantic import BaseModel, field_validator
from typing import Optional
from uuid import UUID

# Base schema for transactions
class TransactionBase(BaseModel):
    user_id: UUID
    first_name: str
    last_name: str
    email: str
    phone_number: str
    country: str
    company_name: str
    organization: str
    domain_name: str
    plan: str
    quantity: int
    amount: float
    training_and_setup: bool
    payment_reference: str
    transaction_id: str
    message: Optional[str] = "Payment successful"
    payment_status: str





class TransactionPayload(BaseModel):
    user_id: UUID
    first_name: str
    last_name: str
    email: str
    phone: str
    country: str
    company_name: str
    organization: str
    site_name: str
    plan: str
    quantity: int
    amount: float
    valid_from: str
    valid_upto: str
    training_and_setup: bool
    payment_reference: Optional[str] = None
    transaction_id: Optional[int] = None
    message: Optional[str] = "Payment successful"
    payment_status: Optional[str] = None

    @field_validator('payment_reference', 'transaction_id', 'payment_status')
    @classmethod
    def validate_payment_fields(cls, v, info):
        # Get the current field name
        field_name = info.field_name
        
        # Access the data dict with all values so far
        data = info.data
        
        plan = data.get('plan', '')
        if plan and plan.lower() != 'free' and v is None:
            raise ValueError(f"{field_name} is required for non-free plans")
        return v
    
    
# class TransactionPayload(BaseModel):
#     user_id: UUID
#     first_name: str
#     last_name: str
#     email: str
#     phone: str
#     country: str
#     company_name: str
#     organization: str
#     site_name: str
#     plan: str
#     quantity: int
#     amount: float
#     valid_from: str
#     valid_upto: str
#     training_and_setup: bool
#     payment_reference: str
#     transaction_id: int
#     message: Optional[str] = "Payment successful"
#     payment_status: str

# Schema for creating transactions
class TransactionCreate(TransactionBase):
    pass

# Schema for updating transactions (with optional fields)
class TransactionUpdate(BaseModel):
    plan: Optional[str] = None
    payment_status: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[str] = None
    phone_number: Optional[str] = None
    country: Optional[str] = None
    company_name: Optional[str] = None
    organization: Optional[str] = None
    domain_name: Optional[str] = None
    quantity: Optional[int] = None
    amount: Optional[float] = None
    training_and_setup: Optional[bool] = None
    payment_reference: Optional[str] = None
    transaction_id: Optional[str] = None
    message: Optional[str] = None
