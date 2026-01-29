from fastapi import FastAPI

app = FastAPI(
    title="Hinsight Dashboard API",
    version="0.1.0",
)

@app.get("/hinsight")
def health_check() -> dict:
    return {"status": "ok"}
