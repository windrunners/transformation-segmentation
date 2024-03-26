import os,argparse
import numpy as np
from PIL import Image
from models import *
import torch
import torch.nn as nn
import torchvision.transforms as tfs 
import torchvision.utils as vutils
import matplotlib.pyplot as plt
from torchvision.utils import make_grid
abs=os.getcwd()+'/'
import time

# 记录开始时间
start_time = time.time()

parser=argparse.ArgumentParser()
parser.add_argument('--task',type=str,default='its',help='its or ots')
parser.add_argument('--test_imgs',type=str,default='test_imgs',help='Test imgs folder')
opt=parser.parse_args()
dataset=opt.task
gps=3
blocks=19
img_dir=abs+opt.test_imgs+'/'
output_dir=abs+f'pred_FFA_{dataset}/'
print("pred_dir:",output_dir)
if not os.path.exists(output_dir):
    os.mkdir(output_dir)
model_dir=abs+f'trained_models/{dataset}_train_ffa_{gps}_{blocks}.pk'
device='cuda' if torch.cuda.is_available() else 'cpu'
ckp=torch.load(model_dir,map_location=device)
net=FFA(gps=gps,blocks=blocks)
# net=nn.DataParallel(net)
net.load_state_dict(ckp['model'])
net.eval()
for im in os.listdir(img_dir):
    print(f'\r {im}',end='',flush=True)
    haze = Image.open(img_dir+im)
    haze1= tfs.Compose([
        tfs.ToTensor(),
        tfs.Normalize(mean=[0.64, 0.6, 0.58],std=[0.14,0.15, 0.152])
    ])(haze)[None,::]
    haze_no=tfs.ToTensor()(haze)[None,::]
    with torch.no_grad():
        pred = net(haze1)
    ts=torch.squeeze(pred.clamp(0,1).cpu())
    # tensorShow([haze_no,pred.clamp(0,1).cpu()],['haze','pred'])
    vutils.save_image(ts,output_dir+im.split('.')[0]+'_FFA.jpg')

# 记录结束时间
end_time = time.time()
# 计算运行时间
total_time = end_time - start_time
print(f"程序运行总时间: {total_time} 秒")