"""BUILDING BASIC LOGER AND FUNCTIONS TO USE IN PIPELINE"""

import logging
import re
import pandas as pd
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


def clean_text(value):
    """Normalize one text value."""
    value = value.strip().lower()
    value = re.sub(r"\s+", " ", value)
    return value


def remove_iqr_outliers(df, column, threshold):
    """Remove IQR outliers from one column."""
    if column not in df.columns:
        logger.error(f"Column not found: {column}")
        raise ValueError(f"Column not found: {column}")

    q1 = df[column].quantile(0.25)
    q3 = df[column].quantile(0.75)
    iqr = q3 - q1

    lower_bound = q1 - threshold * iqr
    upper_bound = q3 + threshold * iqr

    before = df.shape[0]
    df = df[(df[column] >= lower_bound) & (df[column] <= upper_bound)]
    after = df.shape[0]

    logger.debug(
        f"IQR bounds for {column}: [{lower_bound}, {upper_bound}], removed {before - after} row(s)"
    )

    return df
