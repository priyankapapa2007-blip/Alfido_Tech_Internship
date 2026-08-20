from pathlib import Path
import pandas_analysis as pa


def test_cleaning_and_summary():
    df = pa.load_and_clean_data(Path('sales_data.csv'))

    assert df.shape[0] == 10
    assert df['Region'].isna().sum() == 0
    assert df['Quantity'].isna().sum() == 0
    assert df['Discount'].isna().sum() == 0
    assert df.loc[df['Product'] == 'Camera', 'Sales'].iloc[0] > 0

    summary = pa.build_summary(df)
    assert summary['Category'].tolist() == ['Audio', 'Electronics', 'Mobile', 'Office']
    assert summary.loc[summary['Category'] == 'Electronics', 'total_sales'].iloc[0] > 0

    insight = pa.get_insight(summary)
    assert 'Electronics' in insight


def test_high_sales_filter():
    df = pa.load_and_clean_data(Path('sales_data.csv'))
    high_sales = df[df['Sales'] > 200]

    assert len(high_sales) == 7
    assert high_sales['Product'].tolist() == ['Laptop', 'Monitor', 'Phone', 'Tablet', 'Speaker', 'Camera', 'Printer']
    assert high_sales['Sales'].min() > 200
