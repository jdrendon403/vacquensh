from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime, timezone

class Batch(BaseModel):
    po: int = Field(min=0)
    start: Optional[datetime] = Field(default=datetime.now(timezone.utc))
    end: Optional[datetime] = None
    chamber: int = Field(min=1, max=2)


