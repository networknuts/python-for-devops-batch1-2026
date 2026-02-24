import paramiko
from scp import SCPClient

# =========================
# CONFIGURATION
# =========================
LINUX_HOST = "192.168.1.50"      # Linux machine IP
USERNAME = "ubuntu"              # Linux username
PASSWORD = "your_password"       # OR use key file
LOCAL_FILE = r"C:\Users\Aryan\Desktop\test.txt"
REMOTE_PATH = "/home/ubuntu/test.txt"

# =========================
# SSH CONNECTION FUNCTION
# =========================
def create_ssh_client(host, user, password):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=host, username=user, password=password)
    return ssh

# =========================
# MAIN
# =========================
try:
    ssh = create_ssh_client(LINUX_HOST, USERNAME, PASSWORD)

    with SCPClient(ssh.get_transport()) as scp:
        scp.put(LOCAL_FILE, REMOTE_PATH)
        print("✅ File copied successfully!")

    ssh.close()

except Exception as e:
    print("❌ Error:", str(e))
