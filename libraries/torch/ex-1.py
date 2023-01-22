import torch

x = torch.Tensor([3.0]).double() ; x.requires_grad = True
a = torch.Tensor([4.0]).double() ; a.requires_grad = True
b = torch.Tensor([2.0]).double() ; b.requires_grad = True
c = torch.Tensor([5.0]).double() ; c.requires_grad = True

y = a * x**2  +  b * x  +  c

print(y.data.item())
y.backward()
print(x.grad.item())  # 2ax + b = 2*4*3 + 2 = 24+2 = 26
#print(x.grad)
