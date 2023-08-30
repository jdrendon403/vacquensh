from pydantic import BaseModel, Field
from typing import List, Optional
from datetime import datetime, timezone

class Step(BaseModel):
    fnc: int = Field(min=0, max=1)
    temp: float = Field(min=100.0, max=1000.0)
    rate: float = Field(min=0.0, max=25.0)
    time: int = Field(min=0, max=18000)
    difftemp: float = Field(min=0.0, max=50.0)
    fanspeed: float = Field(min=0.0, max=100.0)


class Recipe(BaseModel):
    id: Optional[int] = None
    name: str = Field(min_length=5)
    version: Optional[int] = Field(min=0)
    lastmod: Optional[datetime] = Field(default=datetime.now(timezone.utc))
    status: bool
    recipe: List[Step]