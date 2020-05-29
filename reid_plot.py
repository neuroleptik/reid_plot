#!/usr/bin/env python
# coding: utf-8
import matplotlib.pyplot as plt
import argparse
import torch
from PIL import Image
import torchvision.transforms as T
import os.path
from os import path

# preprocessing of image before inference
# argument : path to an image
# return : a tensor of features 
def preprocess_and_infer(path_to_img):
        
        image = Image.open(path_to_img).convert('RGB')
        paths.append(image)
        image = preprocess(image)
        images = image.unsqueeze(0).to(device)
        with torch.no_grad():
            features = model(images)

        return features
    
    
if __name__ == "__main__":
    # Get the args 
    parser = argparse.ArgumentParser()
    parser.add_argument("input_images1", help="first png or jpg file",type=str)
    parser.add_argument("input_images2", help="second png or jpg file",type=str)
    args = parser.parse_args()

    if not path.exists(args.input_images1) :
        print("Error : "+args.input_images1+" bad file name or path")
        exit()
    if not path.exists(args.input_images2) :
        print("Error : "+args.input_images2+" bad file name or path")
        exit()


    # Var definition 
    pixel_mean=[0.485, 0.456, 0.406]
    pixel_std=[0.229, 0.224, 0.225]
    paths = []
    seuil = 12.0
    min_dist = 2.46
    max_dist = 15
    preprocess = T.Compose([T.Resize((256,128)),
                            T.ToTensor(),
                            T.Normalize(mean=pixel_mean, std=pixel_std)])
    
    # Load model
    model = torch.load('extractor_osnet_x1.pth') 
    model.eval()
    device = torch.device('cuda')
    model.to(device)
    
    # Preprocess and infer 2 images
    features = preprocess_and_infer(args.input_images1)
    features2 = preprocess_and_infer(args.input_images2)

    #Compare two tensors 
    distance = float(torch.dist(features,features2))
    fiablility = 100-(((distance-min_dist)/(max_dist-min_dist))*100)
    
    # Prepare figure 
    figure = plt.figure()
    figure.add_subplot(1,2, 1)
    plt.imshow(paths[0])
    figure.add_subplot(1,2, 2)
    plt.imshow(paths[1])
    
    # Compare with seuil variable which is a experimental variable about threshold number 
    # Save to results dir
    if distance > seuil:
        figure.suptitle('no reID')
        plt.savefig('./results/output_.png')
    else:
        figure.suptitle('reID precision : '+str(round(100-(((distance-min_dist)/(max_dist-min_dist))*100),2))+' %')
        plt.savefig('./results/output_'+args.input_images1+'_'+args.input_images2+'.png')
    
    plt.close(figure)