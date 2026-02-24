import os
import requests
import streamlit as st

st.set_page_config(page_title="K8s Namespace Provisioner", layout="centered")

st.title("Kubernetes Namespace Provisioner")
st.caption("Creates: Namespace + ResourceQuota + LimitRange via FastAPI")

# You can set this as an env var too:
# export API_BASE_URL="http://127.0.0.1:8000"
API_BASE_URL = os.getenv("API_BASE_URL", "http://127.0.0.1:8000").rstrip("/")

with st.sidebar:
    st.header("API Settings")
    api_url = st.text_input("FastAPI Base URL", value=API_BASE_URL)
    st.write("Endpoint used:")
    st.code(f"{api_url}/create-namespace", language="text")

    if st.button("Test /health"):
        try:
            r = requests.get(f"{api_url}/health", timeout=5)
            if r.ok:
                st.success(r.json())
            else:
                st.error(f"Health check failed: {r.status_code} - {r.text}")
        except Exception as e:
            st.error(f"Could not reach API: {e}")

st.divider()

ns = st.text_input("Namespace name", placeholder="e.g. student1")
col1, col2 = st.columns([1, 1])

with col1:
    create_btn = st.button("Create Environment", type="primary")

with col2:
    st.write("")  # spacing
    st.write("")  # spacing
    st.caption("Creates quota + limits with default values from API")

if create_btn:
    ns = (ns or "").strip()
    if not ns:
        st.warning("Please enter a namespace name.")
        st.stop()

    payload = {"namespace": ns}

    with st.spinner("Calling API..."):
        try:
            r = requests.post(f"{api_url}/create-namespace", json=payload, timeout=15)

            if r.ok:
                st.success("Done!")
                st.json(r.json())
            else:
                st.error(f"API Error: {r.status_code}")
                # Try to show JSON error if any
                try:
                    st.json(r.json())
                except Exception:
                    st.code(r.text)

        except requests.exceptions.RequestException as e:
            st.error(f"Request failed: {e}")

st.divider()
st.subheader("Quick usage")
st.code(
    "1) Start API: uvicorn app:app --reload\n"
    "2) Start UI:  streamlit run dashboard.py\n"
    "3) Enter namespace and click Create",
    language="text",
)
