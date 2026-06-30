from ingestion.loader import DataLoader
from ingestion.preprocess import DataPreprocessor
from ingestion.merge_dataset import build_master_dataframe

print("RUN_PIPELINE: Starting data processing pipeline...")
loader = DataLoader()

print("Loading datasets...")

train = loader.load_train()
stores = loader.load_stores()
items = loader.load_items()
oil = loader.load_oil()
transactions = loader.load_transactions()
holidays = loader.load_holidays()

print("Cleaning data...")

train = DataPreprocessor.clean_train(train)
oil = DataPreprocessor.clean_oil(oil)
transactions = DataPreprocessor.clean_transactions(
    transactions
)

print("Merging datasets...")

master_df = build_master_dataframe(
    train,
    stores,
    items,
    oil,
    holidays,
    transactions
)

print(master_df.head())

print(master_df.shape)

master_df.to_parquet(
    "data/processed/master.parquet",
    index=False
)

print("Saved Successfully")