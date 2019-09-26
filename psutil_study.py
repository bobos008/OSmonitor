# coding=utf-8

import psutil

"""
获取CPU各项数据
1. 用户时间以及百分比
2. 系统时间以及百分比
3. 空闲时间以及百分比
4. cpu的硬件信息
"""
# 获取cpu时间
cpu_core_time = psutil.cpu_times()
print(cpu_core_time)

# 获取cpu时间百分比
cpu_core_time_percent = psutil.cpu_times_percent()
print(cpu_core_time_percent)

# 获取cpu使用率
cpu_core_percent = psutil.cpu_percent(1)
print(cpu_core_percent, "%")

# 每个核心线程数
cpu_core_count = psutil.cpu_count()
print(cpu_core_count)

# 获取cpu核心数
cpu_thread_count = psutil.cpu_count(logical=False)
print(cpu_thread_count)

# 获取cpu温度
temperatures = psutil.sensors_temperatures()
print(temperatures["coretemp"][0])

"""
获取内存信息
"""
memory = psutil.virtual_memory()
print(memory)

"""
获取硬盘信息
"""
disks_data = psutil.disk_partitions()
print(disks_data)
i = 0
disk_count = len(disks_data)
total_disk = 0
used_disk = 0
free_disk = 0
while True:
    if i >= disk_count:
        break
    print(disks_data[i])
    #disk_info = psutil.disk_usage(disks_data[i].device)
    disk_info = psutil.disk_usage(disks_data[i].mountpoint)
    total_disk += float(disk_info.total)/1024/1024/1024
    used_disk += float(disk_info.used)/1024/1024/1024
    free_disk += float(disk_info.free)/1024/1024/1024
    i += 1
print(round(total_disk, 2))
print(round(used_disk, 2))
print(round(free_disk, 2))
