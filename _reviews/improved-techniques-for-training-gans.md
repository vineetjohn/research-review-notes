---
layout: default
permalink: 'reviews/improved-techniques-for-training-gans.html'
title: 'Improved Techniques for Training GANs'
---

# Improved Techniques for Training GANs
---

## Idea

GANs are trained with a game theoretic setting where both the discriminator and the generator are trained to minimize their individual losses, thereby, potentially impacting the loss of the other entity and leading to training collapse. 

This paper tries to list the techniques/tricks that can be used to stabilize and improve GAN training.


## Method

The paper describes several different methods of improving the convergence of GANs
* **Feature Matching:** Instead of simply training the network to maximize the discriminator loss, run a discriminator on the generated distribution to encourage it to generate output that is close to the desired distribution. i.e. Train the generator to match expected feature values on an intermediate layer of the discriminator.
* **Minibatch Discrimination:** The collapse of GANs can be avoided to a better extent by having the discriminator look at multiple examples simultaneously as opposed to training it with each data-point in isolation.
* **Historical Averaging:** This is adding a loss term that computes the divergence of the current model parameters from the average model parameters from the previous $t$ epochs.
* **One-sided Label Smoothing:** Instead of predicting the discrete labels 0 and 1 in a classification problem, label smoothing sets the tragets to 0.1 and 0.9 and this reduces the vulnerability of neural networks to adversarial samples. In one-sided label smoothing, only the positive labels are smoothed.
* **Virtual batch normalization:** To avoid adding batch-bias by performing batch-norm over every batch, a preset batch is chosen as a reference batch and each data-point is normalized with respect to that.

The authors also propose using a pre-trained model (eg. The Inception model) and measuring the entropy of its predictions as a proxy of how confident the model is about the generated examples, which gives us an estimate of the image quality.
