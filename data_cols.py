from pydantic import BaseModel

class data_cols(BaseModel):
    Gender: float
    Age: float
    Height: float
    Weight: float
    family_history_with_overweight: float
    FAVC: float
    CAEC: float
    SMOKE: float
    CH2O: float
    CALC: float
    MTRANS: float
