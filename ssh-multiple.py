import paramiko

def ssh_execute(host, username, pkey, cmd, timeout=7):
    """
    Connect to a linux vm using key based auth
    """
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        key = paramiko.RSAKey.from_private_key_file(pkey)
        client.connect(hostname=host, username=username, pkey=key, timeout=timeout)
        stdin, stdout, stderr = client.exec_command(cmd)
        output = stdout.read().decode()
        error = stderr.read().decode()
        return output, error
    except Exception as connection_error:
        return "Connection failed", connection_error
    finally:
        client.close()

def perform_execute(file_path):
    """
    Extract IPs from file and run above ssh_execute function on them
    """
    f = open(file_path)
    for server in f.readlines():
        print("="*10)
        print(f"Server: {server}")
        output, error = ssh_execute(server.strip(), "student", "/home/aryan/.ssh/id_rsa", "lsblk")
        print(f"Output:\n {output}")
        print(f"Error:\n {error}")
    f.close()

perform_execute("vm_list.txt")