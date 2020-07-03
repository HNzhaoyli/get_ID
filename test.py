import torch
import torchvision
from torchvision import datasets,transforms
import os

image_datasets = datasets.ImageFolder(r'F:\Python  工程\market 1501\Market-1501-v15.09.15\pytorch\val')
print(image_datasets)
dataloader = torch.utils.data.DataLoader(image_datasets)


'''
print(path,v) #F:\Python  工程\market 1501\Market-1501-v15.09.15\pytorch\val\0002\0002_c1s1_000451_03.jpg 0
print('filename:',filename) #filename: 0002_c1s1_000451_03.jpg
'''
def get_id(img_path):
    camera_id = []
    labels = []
    for path, v in img_path:
        #filename = path.split('/')[-1]
        filename = os.path.basename(path)
        label = filename[0:4]
        camera = filename.split('c')[1]
        if label[0:2]=='-1':
            labels.append(-1)
        else:
            labels.append(int(label))
        camera_id.append(int(camera[0]))
    print(labels)
    return camera_id, labels

'''
# gallery_path是一个列表，包含了[（imgs,o）,(imgs,1),............]  imgs = path（绝对路径）+图片名字
#gallery_path: [('F:\\Python  工程\\market 1501\\Market-1501-v15.09.15\\pytorch\\val\\0002\\0002_c1s1_000451_03.jpg', 0),
'''
gallery_path = image_datasets.imgs
print('gallery_path:',gallery_path)


gallery_cam,gallery_label = get_id(gallery_path)
