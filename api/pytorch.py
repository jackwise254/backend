import torch

# print(torch.__version__)
my_tensor = torch.tensor([[1,2,3], [4,5,6]], dtype=torch.float32, device='cpu', requires_grad=True)

x = torch.diag(torch.ones(3))

print(x)