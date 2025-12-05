# 📈 MoneyCandle
Real-time Stock Price Alerts · FastAPI Backend + Android App

MoneyCandle is a full-stack project that tracks stock prices, lets users create price alerts, and checks which alerts get triggered.

This repository contains:

- A **FastAPI backend** with PostgreSQL  
- A **Kotlin Android app** using Retrofit + Coroutines  

---

## 🗂 Repository Structure

```
MoneyCandle/
├── app/                     # FastAPI backend
│   ├── db.py
│   ├── main.py
│   ├── models.py
│   ├── schemas/
│   └── routers/
├── android/
│   └── MoneyCandle/         # Android Studio project
├── tests/
├── requirements.txt
├── .gitignore
└── README.md
```

---

## 🚀 Backend (FastAPI)

### Features
- Create stock price alerts  
- List existing alerts  
- Check triggered alerts  
- Persistent storage via PostgreSQL  

### Tech Stack
- FastAPI  
- SQLAlchemy  
- Pydantic v2  
- PostgreSQL (Docker)  
- Uvicorn  

---

## 🧩 Backend Setup

### 1. Start PostgreSQL using Docker

```bash
docker run --name moneycandle-postgres ^
  -e POSTGRES_PASSWORD=supersecret ^
  -p 5433:5432 ^
  -d postgres:16
```

### 2. Install backend dependencies

```bash
python -m venv venv
.env\Scriptsctivate
pip install -r requirements.txt
```

### 3. Create `.env`

```
DATABASE_URL=postgresql+psycopg2://postgres:supersecret@localhost:5433/postgres
```

### 4. Run backend

```bash
uvicorn app.main:app --reload
```

API Documentation → http://127.0.0.1:8000/docs  

---

## 📱 Android App

### Features (in progress)
- View price alerts  
- Create new alerts  
- Check triggered alerts via backend API  

### Tech Stack
- Kotlin  
- Retrofit + Moshi  
- Coroutines  
- Android Studio  

---

## 📱 Android Setup

### 1. Open project

Open:

```
android/MoneyCandle/
```

### 2. Set backend URL

Inside `ApiClient.kt`:

```kotlin
private const val BASE_URL = "http://10.0.2.2:8000/"
```

### 3. Dependencies used

```gradle
implementation "com.squareup.retrofit2:retrofit:2.11.0"
implementation "com.squareup.retrofit2:converter-moshi:2.11.0"
implementation "com.squareup.okhttp3:logging-interceptor:4.12.0"
implementation "com.squareup.moshi:moshi:1.15.0"
implementation "com.squareup.moshi:moshi-kotlin:1.15.0"
implementation "org.jetbrains.kotlinx:kotlinx-coroutines-android:1.8.1"
```

---

## 🛣 Roadmap

### Backend  
- Real market price integration  
- Background job scheduler  
- Push notifications  
- User authentication  

### Android  
- Alerts UI  
- Create new alert screen  
- Background polling  
- Push notifications  

---

## 📜 License  
MIT License
