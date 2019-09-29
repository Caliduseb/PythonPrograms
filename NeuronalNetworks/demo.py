import torch, random
import torch.nn as nn
import torch.nn.functional as F
from torch.autograd import Variable
import torch.optim as optim


class MeinNetz(nn.Module):

    def __init__(self):
        super(MeinNetz, self).__init__()
        self.lin1 = nn.Linear(10, 10)
        self.lin2 = nn.Linear(10, 10)
        self.lin3 = nn.Linear(10, 10)

    def forward(self, x):
        x = F.relu(self.lin1(x))
        x = self.lin3(x)
        return x

    def num_flat_features(self, x):
        size = x.size()[1:]
        num = 1
        for i in size:
            num *= i
        return num


l1 = []
l2 = []

for i1 in range(10):
    for i2 in range(10):
        numb = random.randint(0, 1)
        l2.append(numb)
    l1.append(l2)
    l2 = []

for o1 in l1:
    o2 = o1

netz = MeinNetz()
for i in range(100):
    x = [0, 1, 0, 0, 0, 1, 0, 1, 0, 0]
    inputy = Variable(torch.Tensor([x for _ in range(10)]))
    out = netz(inputy)
    x = [1, 0, 1, 1, 1, 0, 1, 0, 1, 1]
    target = Variable(torch.Tensor([x for _ in range(10)]))
    criterion = nn.MSELoss()
    loss = criterion(out, target)
    netz.zero_grad()
    loss.backward()
    optimizer = optim.SGD(netz.parameters(), lr=0.10)
    optimizer.step()
