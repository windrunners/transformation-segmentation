import torch.nn as nn
import torch

def default_conv(in_channels, out_channels, kernel_size, bias=True):
    return nn.Conv2d(in_channels, out_channels, kernel_size,padding=(kernel_size//2), bias=bias)

class PALayer(nn.Module):
    def __init__(self, channel):
        super(PALayer, self).__init__()
        self.pa = nn.Sequential(
                nn.Conv2d(channel, channel // 8, 1, padding=0, bias=True),
                nn.ReLU(inplace=True),
                nn.Conv2d(channel // 8, 1, 1, padding=0, bias=True),
                nn.Sigmoid()
        )
    def forward(self, x):
        y = self.pa(x)
        return x * y

class CALayer(nn.Module):
    def __init__(self, channel):
        super(CALayer, self).__init__()
        self.avg_pool = nn.AdaptiveAvgPool2d(1)
        self.ca = nn.Sequential(
                nn.Conv2d(channel, channel // 8, 1, padding=0, bias=True),
                nn.ReLU(inplace=True),
                nn.Conv2d(channel // 8, channel, 1, padding=0, bias=True),
                nn.Sigmoid()
        )

    def forward(self, x):
        y = self.avg_pool(x)
        y = self.ca(y)
        return x * y

class SALayer(nn.Module):
    def __init__(self, channel):
        super().__init__()
        self.conv = nn.Conv2d(2, 1, 1, padding=0, bias=True)
        self.sigmoid = nn.Sigmoid()

    def forward(self, x):
        max_result, _ = torch.max(x, dim=1, keepdim=True)
        avg_result = torch.mean(x, dim=1, keepdim=True)
        result = torch.cat([max_result, avg_result], 1)
        output = self.conv(result)
        output = self.sigmoid(output)
        return output * x

class Block(nn.Module):
    def __init__(self, conv, dim, kernel_size,):
        super(Block, self).__init__()
        self.conv1=conv(dim, dim, kernel_size, bias=True)
        self.act1=nn.ReLU(inplace=True)
        self.conv2=conv(dim, dim, kernel_size, bias=True)

    def forward(self, x):
        res=self.act1(self.conv1(x))
        res=self.conv2(res)
        res += x
        return res


class Transformation(nn.Module):
    def __init__(self, conv=default_conv):
        super(Transformation, self).__init__()
        self.dim=64
        kernel_size=3
        pre_process = [conv(3, self.dim, kernel_size)]
        self.g1 = Block(conv, self.dim, kernel_size)
        self.g2 = Block(conv, self.dim, kernel_size)
        self.g3 = Block(conv, self.dim, kernel_size)
        self.calayer = CALayer(self.dim)
        self.palayer = PALayer(self.dim)
        self.salayer = SALayer(self.dim)

        post_precess = [
            conv(self.dim, self.dim, kernel_size),
            conv(self.dim, 3, kernel_size)]

        self.pre = nn.Sequential(*pre_process)
        self.post = nn.Sequential(*post_precess)

    def forward(self, x1):
        x = self.pre(x1)
        out1 = self.g1(x)
        out2 = self.g2(out1) + x
        out3 = self.g2(out2) + out1
        out = self.calayer(out3)
        out = self.palayer(out)
        out = self.salayer(out)
        x = self.post(out)
        return x + x1

if __name__ == "__main__":
    net = Transformation()
    print(net)