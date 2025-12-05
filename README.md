📈 MoneyCandle

Real-time Stock Price Alerts · FastAPI Backend + Android App

MoneyCandle is a full-stack project that tracks stock prices in real time, lets users create price alerts, and checks which alerts would be triggered. The system includes:

A FastAPI backend with PostgreSQL

A Kotlin Android app using Retrofit + Coroutines

Future support for push notifications and background workers

Both backend and Android clients live in this single repository.

🗂 Repository Structure
MoneyCandle/
│
├── app/                     # FastAPI backend source
│   ├── db.py
│   ├── main.py
│   ├── models.py
│   ├── schemas/
│   └── routers/
│
├── android/                 # Android app root
│   └── MoneyCandle/         # Android Studio project folder
│
├── tests/                   # Backend tests
├── requirements.txt         # Backend dependencies
├── .gitignore
└── README.md

🚀 Backend (FastAPI)
Features

Create stock price alerts (above/below target)

List existing alerts

Check triggered alerts

PostgreSQL-based persistent storage

Automatic DB schema creation

Tech Stack

FastAPI

PostgreSQL (Docker)

SQLAlchemy

Pydantic v2

Uvicorn

🧩 Backend Setup
1) Start PostgreSQL using Docker
docker run --name moneycandle-postgres ^
  -e POSTGRES_PASSWORD=supersecret ^
  -p 5433:5432 ^
  -d postgres:16

2) Install backend dependencies
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt

3) Create .env
DATABASE_URL=postgresql+psycopg2://postgres:supersecret@localhost:5433/postgres

4) Run the backend
uvicorn app.main:app --reload


API Docs:
👉 http://127.0.0.1:8000/docs

📱 Android App
Features (in progress)

View alerts

Create alerts

Check which alerts are triggered

Clean Retrofit API integration

Tech Stack

Kotlin

Android Studio

Retrofit + Moshi

Coroutines

📱 Android Setup
1) Open the Android project

In Android Studio, open:

android/MoneyCandle/

2) Set base URL

Inside ApiClient.kt:

private const val BASE_URL = "http://10.0.2.2:8000/"

3) Dependencies used
implementation "com.squareup.retrofit2:retrofit:2.11.0"
implementation "com.squareup.retrofit2:converter-moshi:2.11.0"
implementation "com.squareup.okhttp3:logging-interceptor:4.12.0"
implementation "com.squareup.moshi:moshi:1.15.0"
implementation "com.squareup.moshi:moshi-kotlin:1.15.0"
implementation "org.jetbrains.kotlinx:kotlinx-coroutines-android:1.8.1"

🧪 Example API Usage in Android
Create an alert
ApiClient.api.createAlert(
    CreateAlertRequest(
        symbol = "AAPL",
        targetPrice = 220.0,
        direction = AlertDirection.ABOVE
    )
)

List alerts
val alerts = ApiClient.api.getAlerts()

Check triggered alerts
ApiClient.api.checkAlerts(
    AlertCheckRequest(
        prices = listOf(PriceSnapshot("AAPL", 225.0))
    )
)

🛣 Roadmap
Backend

Real stock prices via external API

Background job scheduler

User accounts + JWT

Push notifications (FCM)

Android

Alert list UI

Create alert screen

Background polling worker

Push notification support

🤝 Contributing

This is a personal project but suggestions and improvements are welcome.

📜 License

MIT License — see LICENSE.