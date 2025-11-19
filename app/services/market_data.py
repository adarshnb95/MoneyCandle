from typing import List, Dict
import httpx

from app.core.config import settings


class MarketDataError(Exception):
    pass


async def fetch_daily_prices(symbol: str, limit: int = 30) -> List[Dict]:
    """
    Fetch recent daily prices for a symbol.

    Returns a list of dicts:
    [
        {"date": "2025-11-14", "close": 245.12},
        ...
    ]
    """
    if settings.market_data_provider != "alpha_vantage":
        raise MarketDataError("Unsupported market data provider")

    if not settings.market_data_api_key:
        raise MarketDataError("MARKET_DATA_API_KEY is not configured")

    url = "https://www.alphavantage.co/query"
    params = {
        "function": "TIME_SERIES_DAILY_ADJUSTED",
        "symbol": symbol,
        "apikey": settings.market_data_api_key,
    }

    try:
        # Slightly higher timeout to be safe on slower responses
        async with httpx.AsyncClient(timeout=20.0) as client:
            response = await client.get(url, params=params)
    except httpx.RequestError as exc:
        # This catches ConnectTimeout, network errors, DNS, etc.
        raise MarketDataError(f"Could not reach market data provider: {exc}") from exc

    if response.status_code != 200:
        raise MarketDataError(f"Market data request failed with status {response.status_code}")

    data = response.json()

    key = "Time Series (Daily)"
    if key not in data:
        # Alpha Vantage sometimes sends "Note" or "Error Message" when throttled
        note = data.get("Note") or data.get("Error Message") or "missing time series"
        raise MarketDataError(f"Unexpected response from market data provider: {note}")

    time_series = data[key]

    dates_sorted = sorted(time_series.keys(), reverse=True)[:limit]

    prices = []
    for d in dates_sorted:
        close_price = float(time_series[d]["4. close"])
        prices.append({"date": d, "close": close_price})

    if not prices:
        raise MarketDataError("No price data available")

    return prices
