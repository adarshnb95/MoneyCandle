from fastapi import APIRouter

router = APIRouter()

@router.get("/{symbol}/volatility")
def get_volatility(symbol: str):
    # Temporary placeholder response
    # Later: call market_data service, compute volatility, return metrics
    return {
        "symbol": symbol.upper(),
        "volatility_window_days": 14,
        "volatility": None,
        "status": "not_implemented",
    }
