import multiprocessing
bind = "192.168.178.99:8000"
workers = multiprocessing.cpu_count() * 2 + 1