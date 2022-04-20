import torch
import numpy as np

x1 = torch.from_numpy(2 * np.ones((2, 2), dtype=np.float32))
x1.requires_grad_(True)
w1 = torch.from_numpy(5 * np.ones((2, 2), dtype=np.float32))
w1.requires_grad_(True)
print("x1 =", x1)
print("w1 =", w1)

x2 = x1 * w1
w2 = torch.from_numpy(6 * np.ones((2, 2), dtype=np.float32))
w2.requires_grad_(True)
print("x2 =", x2)
print("w2 =", w2)

y = x2 * w2
Y = torch.from_numpy(10 * np.ones((2, 2), dtype=np.float32))
print("y =", y)
print("Y =", Y)

L = Y - y
print("L =", L)

L.backward(torch.ones(2, 2, dtype=torch.float))

print(x1.grad)
print(w1.grad)
print(w2.grad)


