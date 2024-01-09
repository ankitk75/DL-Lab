import torch

# q8
a = torch.randn(2, 3)
b = torch.randn(2, 3)

b = b.permute(1,0)
ans = torch.matmul(a, b)
print(ans)

# q9
min