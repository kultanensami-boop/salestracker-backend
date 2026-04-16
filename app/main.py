from app.database import Base, engine

# Luo tietokantataulut automaattisesti
Base.metadata.create_all(bind=engine)

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import events

app = FastAPI(
    title="SalesTracker Backend",
    description="Backend for SalesTracker application",
    version="1.0.0"
)

# CORS (salli frontin yhteydet)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # myöhemmin rajoitetaan
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(events.router)

@app.get("/")
def root():
    return {"status": "ok", "message": "SalesTracker backend running"}

