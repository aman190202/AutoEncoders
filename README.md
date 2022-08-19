# AutoEncoders
Learning all about autoencoders

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

