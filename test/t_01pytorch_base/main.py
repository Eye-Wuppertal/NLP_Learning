

from __future__ import print_function
import torch

# 按间距中的绿色按钮以运行脚本。
if __name__ == '__main__':
    # x1 = torch.empty(5, 3)
    # print(x1)
    # x2 = torch.rand(5, 3)
    # print(x2)
    # x3 = torch.zeros(5, 3, dtype=torch.long)
    # print(x3)
    # x4 = torch.tensor([[1.11, 2.34], [1, 2]])
    # print(x4)
    # # 利用news_methods方法得到一个张量
    # x5 = x3.new_ones(5, 3, dtype=torch.double)
    # print(x5)
    #
    # # 利用randn_like方法得到相同张量尺寸的一个新张量, 并且采用随机初始化来对其赋值
    # x6 = torch.randn_like(x5, dtype=torch.float)
    # print(x6)

    x = torch.ones(2, 2, requires_grad=True)  # 追踪在这个类上定义的所有操作
    print(x)
    y = x+2
    print(y)
    z = y*y*3
    print(z)
    # a = z.mean()  # 得平均数，具有squeeze()功效，消除指定维度
    # print(a)
    z.backward(torch.ones(2, 2, dtype=torch.float))
    print(x.grad)
