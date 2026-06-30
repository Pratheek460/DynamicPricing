from revenue_forecaster import (
    RevenueForecaster
)

demand = 500

price = 120

cost = 70

revenue = (
    RevenueForecaster
    .forecast_revenue(
        demand,
        price
    )
)

profit = (
    RevenueForecaster
    .forecast_profit(
        demand,
        price,
        cost
    )
)

print("Revenue:", revenue)

print("Profit:", profit)