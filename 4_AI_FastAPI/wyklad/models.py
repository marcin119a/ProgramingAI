from pydantic import BaseModel, Field
from typing import Optional

class PricePrediction(BaseModel):
   area_m2: float
   rooms: int
   locality: str
   photos: int

class OfferFilters(BaseModel):
   locality: Optional[str] = Field(None, description="Filtruj po lokalizacji (np. 'Bałuty', 'Śródmieście')")
   rooms: Optional[int] = Field(None, description="Filtruj po liczbie pokoi")
   min_price: Optional[float] = Field(None, description="Minimalna cena")
   max_price: Optional[float] = Field(None, description="Maksymalna cena")