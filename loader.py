from pathlib import Path
import pandas as pd


class DataLoader:

    def __init__(self):

        BASE_DIR = Path(__file__).resolve().parent.parent.parent

        self.data_dir = BASE_DIR / "data" / "raw"

        print(f"Dataset Path: {self.data_dir}")

    def load_train(self):
        return pd.read_csv(
            self.data_dir / "train.csv",
            parse_dates=["date"],
            nrows=500000
        )

    def load_test(self):
        return pd.read_csv(
            self.data_dir / "test.csv",
            parse_dates=["date"]
        )

    def load_stores(self):
        return pd.read_csv(
            self.data_dir / "stores.csv"
        )

    def load_items(self):
        return pd.read_csv(
            self.data_dir / "items.csv"
        )

    def load_oil(self):
        return pd.read_csv(
            self.data_dir / "oil.csv",
            parse_dates=["date"]
        )

    def load_transactions(self):
        return pd.read_csv(
            self.data_dir / "transactions.csv",
            parse_dates=["date"]
        )

    def load_holidays(self):
        return pd.read_csv(
            self.data_dir / "holidays_events.csv",
            parse_dates=["date"]
        )