from fastapi import FastAPI
import socket
import os
import time
import psutil

app = FastAPI()

APP_VERSION = os.getenv("APP_VERSION", "1.0.0")

@app.get("/")
def root():
    return {"message": "DevOps API running 🚀"}

@app.get("/health")
def health():
    return {
        "status": "healthy",
        "hostname": socket.gethostname(),
        "version": APP_VERSION
    }

@app.get("/readiness")
def readiness():
    return {"status": "ready"}

@app.get("/system")
def system_info():
    return {
        "cpu_usage_percent": psutil.cpu_percent(interval=1),
        "memory_usage_percent": psutil.virtual_memory().percent,
        "pod_name": socket.gethostname()
    }

@app.get("/stress")
def stress(seconds: int = 5):
    end_time = time.time() + seconds
    while time.time() < end_time:
        pass
    return {"message": f"CPU stressed for {seconds} seconds"}