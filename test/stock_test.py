from pandas import DataFrame

from app.stocks import fetch_stock_data, format_usd


def test_usd_formatting():
    # it should apply USD formatting:
    assert format_usd(4.50) == "$4.50"

    # it should display two decimal places:
    assert format_usd(4.5) == "$4.50"

    # it should round to two places:
    assert format_usd(4.55555) == "$4.56"

    # it should display thousands separators:
    assert format_usd(1234567890.5555555) == "$1,234,567,890.56"


def test_fetch_stock_data():
    df = fetch_stock_data()
    assert isinstance(df, DataFrame)
    assert "timestamp" in df.columns
    assert "adjusted_close" in df.columns
