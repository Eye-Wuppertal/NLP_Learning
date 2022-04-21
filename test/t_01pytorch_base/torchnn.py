# 导入若干工具包
import torch
import torch.nn as nn
import torch.nn.functional as F


# 定义一个简单的网络类
class Net(nn.Module):

    def __init__(self):
        super(Net, self).__init__()
        # 定义第一层卷积神经网络, 输入通道维度=1, 输出通道维度=6, 卷积核大小3*3
        self.conv1 = nn.Conv2d(1, 6, 3)
        # 定义第二层卷积神经网络, 输入通道维度=6, 输出通道维度=16, 卷积核大小3*3
        self.conv2 = nn.Conv2d(6, 16, 3)
        # 定义三层全连接网络
        self.fc1 = nn.Linear(16 * 6 * 6, 120)
        self.fc2 = nn.Linear(120, 84)
        self.fc3 = nn.Linear(84, 10) # 后面10个分类

    def forward(self, x):
        # 任意卷积层后面要加激活层、池化层
        # 在(2, 2)的池化窗口下执行最大池化操作
        x = F.max_pool2d(F.relu(self.conv1(x)), (2, 2))
        x = F.max_pool2d(F.relu(self.conv2(x)), 2)
        # 经过卷积层的处理后，张量要进入全连接层，进入前需要调整张量的形状
        x = x.view(-1, self.num_flat_features(x))
        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return x

    def num_flat_features(self, x):
        # 计算size, 除了第0个维度上的batch_size
        size = x.size()[1:]
        num_features = 1
        for s in size:
            num_features *= s
        return num_features


net = Net()
# print(net)

params = list(net.parameters())
# print(len(params))
# print(params[0].size())
input = torch.randn(1, 1, 32, 32)
out = net(input)
# print(out)
# print(out.size())
target = torch.randn(10)
target = target.view(1, -1)
criterion = nn.MSELoss()

loss = criterion(out, target)
print(loss)
loss.backward()

