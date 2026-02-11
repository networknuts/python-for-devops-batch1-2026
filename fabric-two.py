from fabric import Connection

def run_on_hosts(host_file, command):
    f = open(host_file,"r")
    for server in f.readlines():
        print(f"===== {server.strip()} =====")
        try:
            conn = Connection(
                host=server.strip(),
                user="student",
                connect_kwargs={
                    "key_filename": "/home/aryan/.ssh/id_rsa"
                }
            )
            result = conn.run(command)
        except Exception as connection_error:
            print(f"Connection failed: {connection_error}")

run_on_hosts("vm_list.txt", "uptime")