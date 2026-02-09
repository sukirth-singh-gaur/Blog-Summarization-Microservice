import subprocess
import os

def start():
    # Start RQ worker
    worker = subprocess.Popen(
        ["python", "-m", "app.worker"]
    )

    # Start API
    api = subprocess.Popen(
        [
            "uvicorn",
            "app.api:app",
            "--host", "0.0.0.0",
            "--port", os.getenv("PORT", "8000")
        ]
    )

    worker.wait()
    api.wait()

if __name__ == "__main__":
    start()
