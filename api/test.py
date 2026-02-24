import psutil

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
        except Exception as e:
            return {
                "Error": e
            }