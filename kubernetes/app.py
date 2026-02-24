from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from kubernetes import client, config
from kubernetes.client.rest import ApiException

# ---------------------------
# Load kube config
# ---------------------------
try:
    config.load_incluster_config()
except:
    config.load_kube_config()

v1 = client.CoreV1Api()

app = FastAPI()


class NamespaceRequest(BaseModel):
    namespace: str


@app.post("/create-namespace")
def create_namespace(data: NamespaceRequest):

    ns_name = data.namespace

    # ---------------------------
    # 1. Create Namespace
    # ---------------------------
    namespace_body = client.V1Namespace(
        metadata=client.V1ObjectMeta(name=ns_name)
    )

    try:
        v1.create_namespace(namespace_body)
    except ApiException as e:
        if e.status != 409:  # 409 = already exists
            raise HTTPException(status_code=500, detail=str(e))

    # ---------------------------
    # 2. Create ResourceQuota
    # ---------------------------
    quota_body = client.V1ResourceQuota(
        metadata=client.V1ObjectMeta(
            name="basic-quota",
            namespace=ns_name
        ),
        spec=client.V1ResourceQuotaSpec(
            hard={
                "pods": "5",
                "requests.cpu": "1",
                "requests.memory": "1Gi",
                "limits.cpu": "2",
                "limits.memory": "2Gi"
            }
        )
    )

    try:
        v1.create_namespaced_resource_quota(ns_name, quota_body)
    except ApiException:
        pass  # ignore if already exists

    # ---------------------------
    # 3. Create LimitRange
    # ---------------------------
    limit_body = client.V1LimitRange(
        metadata=client.V1ObjectMeta(
            name="basic-limits",
            namespace=ns_name
        ),
        spec=client.V1LimitRangeSpec(
            limits=[
                client.V1LimitRangeItem(
                    type="Container",
                    default={
                        "cpu": "500m",
                        "memory": "512Mi"
                    },
                    default_request={
                        "cpu": "200m",
                        "memory": "256Mi"
                    }
                )
            ]
        )
    )

    try:
        v1.create_namespaced_limit_range(ns_name, limit_body)
    except ApiException:
        pass

    return {
        "message": f"Namespace '{ns_name}' created with quota and limitrange"
    }
