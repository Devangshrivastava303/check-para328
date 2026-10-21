from pydantic import BaseModel
from typing import Optional

class Askrequest(BaseModel):
    prompt: str
    model: Optional[str]  = None

class Askresponse(BaseModel):
    model:str
    answer: str
    latency_ms: int
    tokens: int 

