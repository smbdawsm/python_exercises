import psutil as ps

print(f'CPU INFO \n Cores - {ps.cpu_count()} Frequency - {ps.cpu_freq()} \n CPU % utilization - {ps.cpu_percent()}')
print(f'All INFO of RAM \n {ps.virtual_memory()}, \n swap memory: {ps.swap_memory()}')
print(f'File system mounted on "/" \n {ps.disk_usage("/")}')

for el,v  in ps.net_if_addrs().items():
    print(f'Interface: {el} ---- {v}')
    print(f'{"*"*100}')

print(ps.net_io_counters())
print(ps.test())
