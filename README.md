# MoneyCandle

MoneyCandle is a stock volatility tracker that helps users keep an eye on price swings without staring at charts all day. It pulls market data, calculates volatility, and lets users configure alerts when a stock moves beyond a custom threshold.

## Why this exists

Most retail investors either:

- Check prices too often and still miss big moves, or  
- Set generic price alerts that do not match their risk tolerance.

MoneyCandle focuses on **volatility bands** and **personalized alerts**, so users can track meaningful movements for the stocks they actually care about.

## Core features (MVP)

- Search and track stocks by ticker symbol
- Fetch intraday or daily price data from a market data API
- Compute simple volatility metrics (for example: standard deviation over the last N days)
- Allow users to set alert rules per ticker (for example: "alert me if daily change > 3 percent")
- REST API for:
  - Listing tracked tickers
  - Getting volatility metrics
  - Managing alert rules
- Health check endpoint for monitoring and deployment

## Future ideas

- User accounts and authentication
- Push notifications or email alerts
- Support for watchlists and portfolios
- Different volatility models (ATR, Bollinger band like ranges, intraday volatility)
- Android app or web dashboard that talks to this backend
- Historical alert history and simple analytics

## Architecture (initial)

This repository contains the backend service built with FastAPI.

High level components:

- **API layer (FastAPI)**  
  Exposes endpoints for health checks, stock lookup, volatility metrics, and alert rules.

- **Market data service**  
  Thin wrapper over an external market data API (for example Alpha Vantage, Finnhub, or any other provider). Responsible for:
  - Symbol lookup
  - Fetching price time series
  - Normalizing the data into a common format

- **Volatility and alert logic**  
  Services that:
  - Compute volatility from historical prices
  - Evaluate user alert rules against the latest prices
  - Trigger notifications (in later versions)

- **Persistence layer (to be added)**  
  Database to store:
  - Tracked tickers
  - User alert rules
  - Alert history

## Tech stack

- Python  
- FastAPI  
- Uvicorn  
- httpx (for calling market data APIs)  
- SQLAlchemy or another ORM (for persistence, in a later iteration)  

## Getting started

### Prerequisites

- Python 3.9 or later
- A market data API key (for example Alpha Vantage or Finnhub)

### Installation

```bash
git clone https://github.com/<your-username>/moneycandle.git
cd moneycandle
python -m venv venv
# Windows
venv\Scripts\activate
# Mac/Linux
# source venv/bin/activate

pip install -r requirements.txt
