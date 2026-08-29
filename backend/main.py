from fastapi import FastAPI

app = FastAPI(
    title="VAYU-AI",
    description="Agentic AI based Air Pollution-Weather Coupled Forecasting System for Delhi NCR",
    version="1.0"
)


@app.get("/")
def home():
    return {
        "project": "VAYU-AI",
        "status": "running",
        "message": "Air Pollution-Weather Forecasting Agent"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }
