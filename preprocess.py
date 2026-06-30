import pandas as pd


class DataPreprocessor:

    @staticmethod
    def clean_train(df: pd.DataFrame):

        df = df.copy()

        # remove duplicates
        df = df.drop_duplicates()

        # sort chronologically
        df = df.sort_values("date")

        # missing sales
        if "unit_sales" in df.columns:
            df["unit_sales"] = df["unit_sales"].fillna(0)

        if "sales" in df.columns:
            df["sales"] = df["sales"].fillna(0)

        return df

    @staticmethod
    def clean_oil(df):

        df = df.copy()

        df["dcoilwtico"] = (
            df["dcoilwtico"]
            .interpolate()
            .bfill()
            .ffill()
        )

        return df

    @staticmethod
    def clean_transactions(df):

        df = df.copy()

        df["transactions"] = (
            df["transactions"]
            .fillna(0)
        )

        return df