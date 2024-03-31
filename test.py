import argparse
from PIL import Image
from models import *
import torch
import torchvision.transforms as tfs
import torchvision.utils as vutils
abs=os.getcwd()+'/'
import time

# record start time
start_time = time.time()

parser=argparse.ArgumentParser()
parser.add_argument('--task',type=str,default='its',help='its or ots')
parser.add_argument('--test_imgs',type=str,default='test_imgs',help='Test imgs folder')
opt=parser.parse_args()
dataset=opt.task
img_dir=abs+opt.test_imgs+'/'
output_dir=abs+f'pred_{dataset}/'
print("pred_dir:",output_dir)
if not os.path.exists(output_dir):
    os.mkdir(output_dir)
model_dir=abs+f'trained_models/{dataset}_train_Transformation.pk'
device='cuda' if torch.cuda.is_available() else 'cpu'
ckp=torch.load(model_dir,map_location=device)
net=Transformation()
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
    vutils.save_image(ts,output_dir+im.split('.')[0]+'_transformation.jpg')

# record end time
end_time = time.time()
# record running time
total_time = end_time - start_time
print(f"Total running time of the program: {total_time} s")