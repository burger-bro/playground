import torch
print(torch.backends.mps.is_available())
print(torch.backends.mps.is_built())

N = 1000000000

device = torch.device("mps")

cpu_a = torch.randn([1, N])
cpu_b = torch.randn([N, 1])

gpu_a = torch.randn([1, N], device=device)
gpu_b = torch.randn([N, 1], device=device)

def cpu_run():
    c = torch.matmul(cpu_a, cpu_b)
    return c

def gpu_run():
    c = torch.matmul(gpu_a, gpu_b)
    return c

import timeit
cpu_time = timeit.timeit(cpu_run, number=3)
gpu_time = timeit.timeit(gpu_run, number=3)
print(cpu_time, gpu_time)








