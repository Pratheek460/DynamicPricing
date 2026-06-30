import pandas as pd


class PricingEngine:

    @staticmethod
    def calculate_revenue(
        price,
        demand
    ):
        return price * demand

    @staticmethod
    def calculate_profit(
        price,
        demand,
        cost
    ):
        revenue = price * demand

        return revenue - (
            cost * demand
        )

    @staticmethod
    def simulate_prices(
        current_price,
        predicted_demand,
        cost
    ):

        results = []

        price_range = [
            current_price * 0.8,
            current_price * 0.9,
            current_price,
            current_price * 1.1,
            current_price * 1.2
        ]

        for price in price_range:

            revenue = (
                PricingEngine
                .calculate_revenue(
                    price,
                    predicted_demand
                )
            )

            profit = (
                PricingEngine
                .calculate_profit(
                    price,
                    predicted_demand,
                    cost
                )
            )

            results.append(
                {
                    "price": round(price, 2),
                    "revenue": round(revenue, 2),
                    "profit": round(profit, 2)
                }
            )

        return pd.DataFrame(results)