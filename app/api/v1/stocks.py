from fastapi import APIRouter, HTTPException, Query

from app.services.market_data import fetch_daily_prices, MarketDataError
from app.services.volatility import calculate_daily_volatility

router = APIRouter()


@router.get("/{symbol}/volatility")
async def get_volatility(
    symbol: str,
    window: int = Query(14, ge=2, le=60, description="Number of recent trading days to use"),
):
    """
    Compute simple daily volatility for a symbol over the last 'window' days.
    """
    try:
        prices = await fetch_daily_prices(symbol, limit=window + 5)
    except MarketDataError as e:
        raise HTTPException(status_code=502, detail=str(e))

    if not prices:
        raise HTTPException(status_code=404, detail="No price data found for symbol")

    # Use the most recent 'window' closing prices
    closing_prices = [p["close"] for p in prices[:window]]

    volatility = calculate_daily_volatility(closing_prices)
    if volatility is None:
        raise HTTPException(status_code=400, detail="Not enough data to compute volatility")

    return {
        "symbol": symbol.upper(),
        "window_days": window,
        "closing_prices_used": len(closing_prices),
        "volatility_percent": round(volatility, 3),
    }
