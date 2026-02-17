import subprocess

result = subprocess.run(["cat","/etc/hosts"], capture_output=True)
print(result.stdout.decode())