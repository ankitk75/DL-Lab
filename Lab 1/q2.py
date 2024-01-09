import torch

a = torch.tensor([[1, 2, 3, 4],
                  [5, 6, 7, 8]])

print(a)
print(a.shape)

a = a.permute(1, 0)

print(f'after: {a.shape}')
