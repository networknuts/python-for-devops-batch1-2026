import psutil
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel 

app = FastAPI()

# MEMORY CLASS
class Memory:
    def get(self):
        m = psutil.virtual_memory()
        return {
            "total": m.total,
            "used": m.used,
            "available": m.available,
            "percent": m.percent
        }

# DISK CLASS
class Disk:
    def __init__(self, path: str):
        self.path = path

    def get(self):
        try:
            d = psutil.disk_usage(self.path)
            return {
                "path": self.path,
                "total": d.total,
                "used": d.used,
                "free": d.free,
                "percent": d.percent
            }
        except Exception:
            raise HTTPException(status_code=400, detail="Invalid Path")

# USER REQUEST MODEL
class DiskRequest(BaseModel):
    path: str 

memory = Memory()

# ROUTES

@app.get("/memory")
def memory_data():
    return memory.get()

@app.post("/disk")
def disk_data(request: DiskRequest):
    disk = Disk(path=request.path)
    return disk.get()