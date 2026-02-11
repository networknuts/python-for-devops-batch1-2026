from fabric import Connection

def conn(hostname, username, pkey, cmd):
    response = Connection(
        host=hostname,
        user=username,
        connect_kwargs={
            "key_filename": pkey
        }
    )
    result = response.run(cmd)

conn("192.168.159.9", "student", "/home/aryan/.ssh/id_rsa", "uptime")
