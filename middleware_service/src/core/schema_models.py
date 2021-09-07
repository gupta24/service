from pydantic import BaseModel
from datetime import date
from typing import List, Optional
from fastapi_utils.api_model import APIModel


class MonthlyEarning(APIModel):
    date: str
    value: float


class ClientRequestData(APIModel):
    email: str
    earning: List[MonthlyEarning] = []


class ClientSignatureWithData(APIModel):
    customer_data: ClientRequestData
