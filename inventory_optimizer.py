class InventoryOptimizer:

    @staticmethod
    def reorder_quantity(
        current_stock,
        predicted_demand,
        safety_stock=0.2
    ):

        safety_inventory = (
            predicted_demand * safety_stock
        )

        required_stock = (
            predicted_demand +
            safety_inventory
        )

        reorder = max(
            0,
            required_stock - current_stock
        )

        return {
            "current_stock": current_stock,
            "predicted_demand": predicted_demand,
            "safety_stock": round(
                safety_inventory,
                2
            ),
            "reorder_quantity": round(
                reorder,
                2
            )
        }