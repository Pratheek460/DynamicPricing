const API =
    "http://127.0.0.1:8000";


async function predictDemand() {

    const response =
        await fetch(
            API + "/predict-demand",
            {
                method: "POST"
            }
        );

    const data =
        await response.json();

    document
        .getElementById(
            "demandResult"
        )
        .innerText =
        JSON.stringify(
            data,
            null,
            2
        );
}


async function recommendPrice() {

    const response =
        await fetch(
            API + "/recommend-price",
            {
                method: "POST",

                headers: {
                    "Content-Type":
                    "application/json"
                },

                body: JSON.stringify({

                    current_price:
                    Number(
                        document
                        .getElementById(
                            "price"
                        ).value
                    ),

                    cost:
                    Number(
                        document
                        .getElementById(
                            "cost"
                        ).value
                    ),

                    predicted_demand:
                    Number(
                        document
                        .getElementById(
                            "demand"
                        ).value
                    )
                })
            }
        );

    const data =
        await response.json();

    document
        .getElementById(
            "priceResult"
        )
        .innerText =
        JSON.stringify(
            data,
            null,
            2
        );
}


async function inventoryPlan() {

    const response =
        await fetch(
            API + "/inventory",
            {
                method: "POST",

                headers: {
                    "Content-Type":
                    "application/json"
                },

                body: JSON.stringify({

                    current_stock:
                    Number(
                        document
                        .getElementById(
                            "stock"
                        ).value
                    ),

                    predicted_demand:
                    Number(
                        document
                        .getElementById(
                            "inventoryDemand"
                        ).value
                    )
                })
            }
        );

    const data =
        await response.json();

    document
        .getElementById(
            "inventoryResult"
        )
        .innerText =
        JSON.stringify(
            data,
            null,
            2
        );
}