import pandas as pd
import numpy as np


class FeatureEngineer:

    @staticmethod
    def create_time_features(df):

        df = df.copy()

        df["day"] = df["date"].dt.day

        df["day_of_week"] = df["date"].dt.dayofweek

        df["week"] = df["date"].dt.isocalendar().week.astype(int)

        df["month"] = df["date"].dt.month

        df["quarter"] = df["date"].dt.quarter

        df["year"] = df["date"].dt.year

        df["is_weekend"] = (
            df["day_of_week"] >= 5
        ).astype(int)

        return df

    @staticmethod
    def create_holiday_feature(df):

        df = df.copy()

        if "type_y" in df.columns:
            df["is_holiday"] = (
                df["type_y"]
                .notna()
                .astype(int)
            )
        else:
            df["is_holiday"] = 0

        return df

    @staticmethod
    def create_transaction_features(df):

        df = df.copy()

        if "transactions" in df.columns:
            df["transactions"] = (
                df["transactions"]
                .fillna(0)
            )

        return df

    @staticmethod
    def create_oil_features(df):

        df = df.copy()

        if "dcoilwtico" in df.columns:
            df["dcoilwtico"] = (
                df["dcoilwtico"]
                .fillna(
                    df["dcoilwtico"].median()
                )
            )

        return df

    @staticmethod
    def create_lag_features(df):

        df = df.copy()

        target_col = "unit_sales"

        df = df.sort_values(
            ["store_nbr", "item_nbr", "date"]
        )

        grouped = df.groupby(
            ["store_nbr", "item_nbr"]
        )

        df["lag_1"] = grouped[target_col].shift(1)

        df["lag_7"] = grouped[target_col].shift(7)

        df["lag_14"] = grouped[target_col].shift(14)

        df["lag_30"] = grouped[target_col].shift(30)

        return df

    @staticmethod
    def create_rolling_features(df):

        df = df.copy()

        grouped = (
            df.groupby(
                ["store_nbr", "item_nbr"]
            )["unit_sales"]
        )

        df["rolling_mean_7"] = (
            grouped
            .transform(
                lambda x:
                x.shift(1)
                 .rolling(7)
                 .mean()
            )
        )

        df["rolling_mean_30"] = (
            grouped
            .transform(
                lambda x:
                x.shift(1)
                 .rolling(30)
                 .mean()
            )
        )

        df["rolling_std_7"] = (
            grouped
            .transform(
                lambda x:
                x.shift(1)
                 .rolling(7)
                 .std()
            )
        )

        return df

    @staticmethod
    def fill_missing(df):

        df = df.copy()

        numeric_cols = df.select_dtypes(
            include=np.number
        ).columns

        df[numeric_cols] = (
            df[numeric_cols]
            .fillna(0)
        )

        return df


def build_features(df):

    print("Creating Time Features...")
    df = FeatureEngineer.create_time_features(df)

    print("Creating Holiday Features...")
    df = FeatureEngineer.create_holiday_feature(df)

    print("Creating Transaction Features...")
    df = FeatureEngineer.create_transaction_features(df)

    print("Creating Oil Features...")
    df = FeatureEngineer.create_oil_features(df)

    print("Creating Lag Features...")
    df = FeatureEngineer.create_lag_features(df)

    print("Creating Rolling Features...")
    df = FeatureEngineer.create_rolling_features(df)

    print("Filling Missing Values...")
    df = FeatureEngineer.fill_missing(df)

    return df