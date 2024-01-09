import torch

a = torch.randn(7, 7)
b = torch.randn(1, 7)
b = b.permute(1,0)
print(a)
print(b)

out = torch.matmul(a, b)
print(f'output =\n {out}')
