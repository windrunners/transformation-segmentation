# transformation-segmentation

## 1 Introduction
With the continuous development of science and technology, the application of robotics in the industrial field has gradually become a key factor to promote production efficiency and quality improvement. Among them, the application of weld grinding automation has brought significant changes to the industrial field. Robotic weld grinding automation is the use of advanced machine learning, visual recognition, and motion control techniques to enable robots to accurately perceive the position and shape of the weld and automatically execute the grinding process. 
To this end, we developed a new transformation segmentation algorithm to solve the problem of weld segmentation in smoke environment.

## 2 Method
In view of the complex working conditions in the weld field, this paper proposes a method for weld image segmentation. The proposed large model of weld segmentation can adapt to different smoke environments and has good adaptability to multiple smoke concentrations. Compared with the combination of defogging and large segmentation models, the proposed algorithm has higher accuracy of weld segmentation.

![image](https://github.com/windrunners/transformation-segmentation/blob/main/method/method.png)


## 3 Prepare data for training and verification
A. training datasets  
RESIDE: <https://sites.google.com/view/reside-dehaze-datasets> or 
<https://www.cvmart.net/dataSets/detail/560?channel_id=op10&utm_source=cvmartmp&utm_campaign=datasets&utm_medium=article>

B. test datasets  
smoke weld:  
link: <https://pan.baidu.com/s/15uuiMYRz7TFb1rPKC0WO4Q>  password: lqui

## 4 train and test for feature transformation
A. train  
Run the "train.py" file.  

B. test  
Run the "test.py" file.  

## 5 Segmentation net based on pre-training model
### A. SAM  
link: <https://github.com/facebookresearch/segment-anything>  
### B. FastSAM
link: <https://github.com/CASIA-IVA-Lab/FastSAM>

## 6 Performance test for segmented images
We used matlab program for verification. The address of the matlab program used is as follows:  
link: <https://github.com/windrunners/segmentation-verification>

## 7 Detailed steps
A. Download the programs and data linked above.  
B. Execute the training task of feature transformation.  
C. The image with smoke is transformed to generate intermediate potential features.  
D. Unsupervised segmentation is performed using the pre-trained model SAM or FastSAM.  
E. Continue to implement segmentation performance verification using the performance test program.
F. Generate test data, obtain data distribution and deviation.

## 8 Citation
```
@article{zhang2024Weld,
    title={Weld image segmentation in industrial smoke scene},
    author={Zhang, Xu and Zheng, Qingchun and Zhu, Peihao and  Zhao, Yangyang and Liu Jiwei},
    journal={Proceedings of the Romanian Academy, Series A: Mathematics, Physics, Technical Sciences, Information Science},
    year={2024}
}
```






