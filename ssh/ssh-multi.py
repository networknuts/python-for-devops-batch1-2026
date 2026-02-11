import paramiko

def ssh_execute(host, username, pkey, cmd, timeout=10):
    """
    Connect to a linux server using SSH and execute a command
    """
    client = paramiko.SSHClient() #initialize ssh
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) #add server to your known_hosts
    try:
        client.connect(hostname=host, username=username, pkey=pkey, timeout=timeout)
        stdin, stdout, stderr = client.exec_command(cmd)
        output = stdout.read().decode().strip()
        error = stderr.read().decode().strip()

        return output, error
    except Exception as connection_error:
        return "Connection failed", connection_error
    finally:
        client.close()


def perform_execution(file_path):
    """
    Read server IPs/hostnames from a file
    """
    f = open(file_path)
    for server in f.readlines():
        print("="*10)
        output, error = ssh_execute(server.strip(), "student", "/home/aryan/.ssh/id_rsa", "lsblk")
        if output:
            print(f"Output: {output} ")
        if error:
            print(f"Error: {error}")
    f.close()


perform_execution("vm_list.txt")