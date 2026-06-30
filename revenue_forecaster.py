class RevenueForecaster:

    @staticmethod
    def forecast_revenue(
        demand,
        price
    ):

        return demand * price

    @staticmethod
    def forecast_profit(
        demand,
        price,
        cost
    ):

        revenue = demand * price

        cost_total = (
            demand * cost
        )

        return revenue - cost_total