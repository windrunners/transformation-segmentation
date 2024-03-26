# transformation-segmentation

## 1 Introduction
With the continuous development of science and technology, the application of robotics in the industrial field has gradually become a key factor to promote production efficiency and quality improvement. Among them, the application of weld grinding automation has brought significant changes to the industrial field. Robotic weld grinding automation is the use of advanced machine learning, visual recognition, and motion control techniques to enable robots to accurately perceive the position and shape of the weld and automatically execute the grinding process. 
To this end, we developed a new transformation segmentation algorithm to solve the problem of weld segmentation in smoke environment.

## 2 Prepare data for training and verification
A. training datasets  
RESIDE: <https://sites.google.com/view/reside-dehaze-datasets> or 
<https://www.cvmart.net/dataSets/detail/560?channel_id=op10&utm_source=cvmartmp&utm_campaign=datasets&utm_medium=article>

B. test datasets  
smoke weld:  
link: <https://pan.baidu.com/s/15uuiMYRz7TFb1rPKC0WO4Q>  password: lqui

## 3 train and test for transformation net
A. train  
Run the "train.py" file.  

B. test  
Run the "test.py" file.  

## 4 Segmentation net based on pre-training model
### A. SAM  
link: <https://github.com/facebookresearch/segment-anything>  
### B. FastSAM
link: <https://github.com/CASIA-IVA-Lab/FastSAM>

## 5 Performance test for segmented images
We used matlab program for verification. The address of the matlab program used is as follows:  
link: <https://github.com/windrunners/segmentation-verification>

## 6 Detailed steps
A. 
B.
C.
D.
E.
F.
G.
H.


## 7 Citation
'''
@article{zhang2024Weld,
    title={Weld image segmentation in industrial smoke scene},
    author={Zhang, Xu and Zheng, Qingchun and Zhu, Peihao and  Zhao, Yangyang and Liu Jiwei},
    journal={Proceedings of the Romanian Academy, Series A: Mathematics, Physics, Technical Sciences, Information Science},
    year={2024},
    publisher={IEEE}
}
'''





