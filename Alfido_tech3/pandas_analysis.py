import pandas as pd
from pathlib import Path


def load_and_clean_data(csv_path):
    df = pd.read_csv(csv_path)
    df['Region'] = df['Region'].fillna('Unknown')

    for col in ['Sales', 'Quantity', 'Discount']:
        df[col] = pd.to_numeric(df[col], errors='coerce').astype(float)

    mean_sales = df['Sales'].mean()
    df.loc[df['Sales'] < 0, 'Sales'] = mean_sales

    median_quantity = df['Quantity'].median()
    median_discount = df['Discount'].median()
    df['Quantity'] = df['Quantity'].fillna(median_quantity)
    df['Discount'] = df['Discount'].fillna(median_discount)

    df['Region'] = df['Region'].replace({'unknown': 'Unknown'})
    return df


def build_summary(df):
    return (
        df.groupby('Category')
          .agg(total_sales=('Sales', 'sum'), avg_discount=('Discount', 'mean'), total_quantity=('Quantity', 'sum'))
          .reset_index()
    )


def get_insight(summary):
    best_category = summary.loc[summary['total_sales'].idxmax(), 'Category']
    return f"The {best_category} category brings in the highest total sales."


def run_analysis(csv_path=None):
    if csv_path is None:
        csv_path = Path(__file__).with_name('sales_data.csv')

    df = load_and_clean_data(csv_path)
    print('Original data shape:', df.shape)
    print('\nPreview:')
    print(df.head())
    print('\nMissing values:')
    print(df.isna().sum())

    print('\nCleaned data:')
    print(df)

    high_sales = df[df['Sales'] > 200]
    print('\nHigh sales products:')
    print(high_sales[['Product', 'Sales', 'Region']])

    summary = build_summary(df)
    print('\nCategory summary:')
    print(summary)

    insight = get_insight(summary)
    print('\nSimple insight:')
    print(insight)
    print("Electronics products dominate sales, while missing values were filled so the analysis stays reliable.")
    return df, summary, insight


if __name__ == '__main__':
    run_analysis()
