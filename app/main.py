from fastapi import FastAPI
import os, time

app = FastAPI()

@app.get("/health")
def health():
    return {"ok": True, "ts": int(time.time())}

@app.get("/export/latest")
def export_latest():
    # placeholder JSON voor TradingView inputs
    return {
        "weights": [1/13]*13,
        "thresholds": {"long": 0.6, "short": 0.6},
        "calibration": {"a": 1.0, "b": 0.0}
    }
