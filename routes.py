import joblib
import pandas as pd

from fastapi import APIRouter


from src.api.schemas import (
    DemandRequest,
    InventoryRequest,
    PriceRequest
)

from src.pricing.pricing_engine import (
    PricingEngine
)

from src.inventory.inventory_optimizer import (
    InventoryOptimizer
)

from src.revenue.revenue_forecaster import (
    RevenueForecaster
)


router = APIRouter()

model = joblib.load(
    "models/demand_forecast_xgb.pkl"
)


@router.get("/")
def home():

    return {
        "message":
        "Dynamic Pricing API Running"
    }


@router.post("/recommend-price")
def recommend_price(
    request: PriceRequest
):

    result = PricingEngine.simulate_prices(
        current_price=request.current_price,
        predicted_demand=request.predicted_demand,
        cost=request.cost
    )

    best_price = result.loc[
        result["profit"].idxmax()
    ]

    return {
        "recommended_price":
        float(best_price["price"]),

        "expected_profit":
        float(best_price["profit"])
    }


@router.post("/predict-demand")
def predict_demand(
    request: DemandRequest
):

    df = pd.read_parquet(
        "data/processed/features.parquet"
    )

    filtered = df[
        (df["store_nbr"] == request.store_nbr)
        &
        (df["item_nbr"] == request.item_nbr)
    ]

    if filtered.empty:

        return {
            "error":
            "Store/Item combination not found"
        }

    latest = (
        filtered
        .sort_values("date")
        .tail(1)
    )

    drop_cols = [
        "id",
        "date",
        "unit_sales",
        "type_y"
    ]

    for col in latest.select_dtypes(
        include="object"
    ).columns:

        latest[col] = (
            latest[col]
            .astype("category")
            .cat.codes
        )

    X = latest.drop(
        columns=[
            c
            for c in drop_cols
            if c in latest.columns
        ]
    )

    prediction = model.predict(X)

    return {
        "store_nbr":
        request.store_nbr,

        "item_nbr":
        request.item_nbr,

        "predicted_demand":
        float(prediction[0])
    }



@router.post("/inventory")
def inventory_plan(
    request: InventoryRequest
):

    return (
        InventoryOptimizer
        .reorder_quantity(
            current_stock=request.current_stock,
            predicted_demand=request.predicted_demand
        )
    )

@router.post("/revenue")
def revenue_forecast(
    request: PriceRequest
):

    revenue = (
        RevenueForecaster
        .forecast_revenue(
            request.predicted_demand,
            request.current_price
        )
    )

    profit = (
        RevenueForecaster
        .forecast_profit(
            request.predicted_demand,
            request.current_price,
            request.cost
        )
    )

    return {
        "revenue": revenue,
        "profit": profit
    }