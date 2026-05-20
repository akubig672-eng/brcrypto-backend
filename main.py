from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Brcrypto API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "Brcrypto Mining API", "status": "live", "version": "1.0.0"}

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.get("/mining/status")
def mining_status():
    return {"active": True, "hashrate": "0 H/s", "workers": 0, "earnings": 0.0}

@app.post("/mining/start")
def start_mining():
    return {"message": "Mining started", "status": "active"}

@app.post("/mining/stop")
def stop_mining():
    return {"message": "Mining stopped", "status": "inactive"}
