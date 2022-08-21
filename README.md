# AutoEncoders
Implementing variatons of Autoencoding algorithms 

## Introduction 

Autoencoders are a specific type of feedforward neural networks where the input is the same as the output. They compress the input into a lower-dimensional code and then reconstruct the output from this representation. The code is a compact “summary” or “compression” of the input, also called the latent-space representation.

An autoencoder consists of 3 components: 
1. *encoder* : compresses the input and produces the code
2. *code* 
3. *decoder* : reconstructs the input only using this code.

![image1](images/autoencoder.png)

To build an autoencoder, we need :
1. Encoding Method
2. Decoding Method
3. Loss Function to compare the outputs with the target

## Architecture

![image2](images/architecture.png)

## Model 1 : 

Attempting to convert black and white images to colorful ones via training black and white encoded images to decode to a colorful one.

### Dataset Creation :
COCO-2017's validation dataset has been used over here to limited GPU capacity. Two different attempts are made via different model architecture. 

1. The first model involves resizing images to dimensions of 256 and then converting them to black and white

2. The second model involves resizing images to dimesions of 160x160.