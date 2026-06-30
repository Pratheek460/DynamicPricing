from pydantic import BaseModel


class DemandRequest(BaseModel):
    store_nbr: int
    item_nbr: int


class PriceRequest(BaseModel):
    current_price: float
    cost: float
    predicted_demand: float


class InventoryRequest(BaseModel):
    current_stock: float
    predicted_demand: float