import torch
import numpy

a = numpy.array([1, 2, 3, 4, 5])
print(a)
a = torch.from_numpy(a)
print(a)
