import torch

# reshaping and viewing
a = torch.tensor([[1, 2, 3, 4],
                  [5, 6, 7, 8]])
print(f'tensor a = \n{a}')
print(f'\nshape of tensor = {a.shape}')
print(f'\nreshaped tensor = \n{a.reshape([1,8])}\n')
print(f'\nresize tensor = \n{a.resize_(1,8)}\n\n')


# stacking
x = torch.tensor([10, 20, 30, 40])
y = torch.tensor([50, 60, 70, 80])

print(f'x = {x}')
print(f'y = {y}')

print('\nstacking tensor')
t = torch.stack((x,y))
print(t)

print("\njoin tensors dimension 0:")
t = torch.stack((x, y), dim=0)
print(t)

print("join tensors dimension 1:")
t = torch.stack((x, y), dim=1)
print(t)

# squeezing and unsqueezing
sq = torch.squeeze(a)
print(f'\nsize of tensor squeezed a = {sq.shape}')
unsq = torch.unsqueeze(sq, 0)
print(f'\nsize of tensor unsqueezed a = {unsq.shape}')



