from sqlalchemy import Column, String, JSON, Float, Integer
from .base import BaseModel

class LLMUsage(BaseModel):
    __tablename__ = "llm_usage"
    
    model_name = Column(String, index=True)
    prompt = Column(String)
    response = Column(String)
    metadata = Column(JSON)
    tokens_used = Column(Integer)
    processing_time = Column(Float)
    cost = Column(Float) 