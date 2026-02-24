from fastapi import FastAPI, HTTPException
from kubernetes import client, config
from kubernetes.client.rest import ApiException

# ---------------------------
# Load Kubernetes Config
# ---------------------------
try:
    config.load_incluster_config()
except:
    config.load_kube_config()

v1 = client.CoreV1Api()

app = FastAPI()


@app.get("/namespaces")
def get_namespaces():
    try:
        ns_list = v1.list_namespace()

        namespaces = []
        for ns in ns_list.items:
            namespaces.append({
                "name": ns.metadata.name,
                "status": ns.status.phase
            })

        return {
            "count": len(namespaces),
            "namespaces": namespaces
        }

    except ApiException as e:
        raise HTTPException(
            status_code=500,
            detail=f"Kubernetes API error: {e}"
        )
