"""BUILDING BASIC LOGER AND FUNCTIONS TO USE IN PIPELINE"""
import logging

logger = logging.getLogger(__name__)


def show_overview(df):
    """Display basic information about a DataFrame."""
    logger.debug(f"showing overview for dataframe with a shape {df.shape}")
    print(f"shape: {df.shape}")
    print(df.head(5))
    print(f"columns: {list(df.columns)}")
    print(f"Data Types: \n{df.dtypes}")


def remove_duplicates(df):
    """Remove exact duplicate rows."""
    before = df.shape[0]
    df = df.drop_duplicates()
    after = df.shape[0]
    logger.debug(f"Removed duplicates: {before} rows -> {after} rows")
    return df

def drop_missing_rows(df):
    """Remove rows containing missing values."""
    before = df.shape[0]
    df = df.dropna()
    after = df.shape[0]
    logger.debug(f"Dropped missing rows: {before} rows -> {after} rows")
    return df

    # Drop rows containing one or more missing values.
    # Log a DEBUG message containing the before and after row counts.
    # Return the resulting DataFrame.
