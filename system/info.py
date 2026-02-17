# SYSTEM RELATED INFORMATION
# BASIC INFO - HOSTNAME, KERNEL, ARCHITECTURE, BOOT TIME
# CPU - NUMBER OF CORES, PHYSICAL CORES, VIRTUAL CORES
# MEMORY - TOTAL, AVAILABLE, USED, PERCENTAGE
# SWAP - TOTAL, AVAILABLE, USED, PERCENTAGE - YOUR JOB
# DISK - NUMBER OF DEVICES, NUMBER OF PARTITIONS, TOTAL SIZE, USED SIZE, AVAILABLE SIZE, PERCENTAGE
# NETWORK - NETWORK INTERFACES, IPV4, IPV6, NETMASK, BROADCAST
# PROCESSES - NUMBER OF PROCESSES RUNNING, NAME OF PROCESS, PID OF PROCESS

import platform
import time
import humanize
import psutil 

print("="*40, "SYSTEM INFORMATION", "="*40)
hostname = platform.node()
system = platform.system()
kernel = platform.release()
boot_time = psutil.boot_time()
print(f"Hostname: {hostname}")
print(f"System Type: {system}")
print(f"Kernel: {kernel}")
print(f"Boot time: {time.ctime(boot_time)}")

print("="*40, "CPU INFORMATION", "="*40)
cpu_count = psutil.cpu_count()
cpu_usage_percentage = psutil.cpu_percent()
print(f"Total CPU: {cpu_count}")
print(f"CPU Usage: {cpu_usage_percentage}%")

print("="*40, "MEMORY INFORMATION", "="*40)
memory_usage = psutil.virtual_memory()
print(f"Total Memory: {humanize.naturalsize(memory_usage.total)}")
print(f"Available Memory: {humanize.naturalsize(memory_usage.available)}")
print(f"Used Memory: {humanize.naturalsize(memory_usage.used)}")
print(f"Memory Percentage Usage: {memory_usage.percent}%")

print("="*40, "DISK INFORMATION", "="*40)
devices = psutil.disk_partitions()
for device in devices:
    print(f"Device Name: {device.device}")
    print(f"\tMountpath: {device.mountpoint}")
    print(f"\tFilesystem: {device.fstype}")
    device_size = psutil.disk_usage(device.mountpoint)
    print(f"\tTotal Size: {humanize.naturalsize(device_size.total)}")
    print(f"\tUsed Size: {humanize.naturalsize(device_size.used)}")
    print(f"\tFree Size: {humanize.naturalsize(device_size.free)}")
    print(f"\tPercentage Usage: {device_size.percent}%")
    print("-------")

print("="*40, "NETWORK INFORMATION", "="*40)
network_devices = psutil.net_if_addrs()
for network_name, network_data in network_devices.items():
    print(f"Interface Name: {network_name}")
    for network in network_data:
        if str(network.family) == "AddressFamily.AF_INET":
            print(f"\tIPV4: {network.address}")
            print(f"\tNetmask: {network.netmask}")
            print(f"\tBroadcast: {network.broadcast}")
    print("--------")

print("="*40, "PROCESS INFORMATION", "="*40)
n = 0
for proc in psutil.process_iter(['pid', 'name', 'username']):
    print(f"Process: {proc.info['name']} | PID: {proc.info['pid']} | Process Owner: {proc.info['username']}")
    n = n + 1
print(f"Total processes: {n}")