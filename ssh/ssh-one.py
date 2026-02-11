import paramiko

def ssh_execute(host, username, password, cmd):
    """
    Connect to a linux server using SSH and execute a command
    """
    client = paramiko.SSHClient() #initialize ssh
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy()) #add server to your known_hosts
    client.connect(hostname=host, username=username, password=password) #make the connection
    print(f"Server: {host}")
    stdin, stdout, stderr = client.exec_command(cmd) #execute a command
    output = stdout.read().decode()
    err = stderr.read().decode()
    return output, err

response_output, response_error = ssh_execute("192.168.159.70","aryan","networknuts","lsblk")

print(f"Output:\n {response_output}")
print(f"Error:\n {response_error}")
