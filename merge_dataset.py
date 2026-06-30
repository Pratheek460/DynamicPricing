def build_master_dataframe(
        train,
        stores,
        items,
        oil,
        holidays,
        transactions
):

    df = train.copy()

    df = df.merge(
        stores,
        on="store_nbr",
        how="left"
    )

    df = df.merge(
        items,
        on="item_nbr",
        how="left"
    )

    df = df.merge(
        oil,
        on="date",
        how="left"
    )

    df = df.merge(
        transactions,
        on=["date", "store_nbr"],
        how="left"
    )

    holidays = holidays[
        [
            "date",
            "type",
            "locale",
            "transferred"
        ]
    ]

    df = df.merge(
        holidays,
        on="date",
        how="left"
    )

    return df