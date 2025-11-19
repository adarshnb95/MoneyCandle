from typing import List, Optional
import math


def calculate_daily_volatility(closing_prices: List[float]) -> Optional[float]:
    """
    Calculate simple volatility as standard deviation of daily returns.

    Returns volatility as a percentage (for example 2.5 means 2.5 percent).
    """
    if len(closing_prices) < 2:
        return None

    # daily returns: (P_t - P_(t-1)) / P_(t-1)
    returns = []
    for i in range(1, len(closing_prices)):
        prev_price = closing_prices[i - 1]
        curr_price = closing_prices[i]
        if prev_price == 0:
            continue
        r = (curr_price - prev_price) / prev_price
        returns.append(r)

    if len(returns) < 2:
        return None

    mean_return = sum(returns) / len(returns)
    squared_diffs = [(r - mean_return) ** 2 for r in returns]
    variance = sum(squared_diffs) / (len(returns) - 1)
    std_dev = math.sqrt(variance)

    # convert to percentage
    volatility_pct = std_dev * 100.0
    return volatility_pct
