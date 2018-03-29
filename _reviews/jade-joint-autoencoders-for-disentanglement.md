---
layout: default
permalink: "reviews/jade-joint-autoencoders-for-disentanglement.html"
title: 'JADE - Joint Autoencoders for Dis-Entanglement'
---

# JADE: Joint Autoencoders for Dis-Entanglement
---

## Idea
The authors motivate the idea of using an auxilliary dataset that has abundant labeled samples to supplement a dataset that has only a few labeled samples, as long as the two datasets have at least one factor of variation in common. This is done by distentangling the content representation from the style using a variational autoencoder.

## Method
* The authors make the assumption that the distributions $X$, with limited data, and $Y$ with abundant data, have the generative priors $P(z_1, z_2)$ and $P(z_3, z_4)$ respectively.
* Assuming that $z_2$ and $z_4$ are the content representations of each dataset respectively, we want to train a classifier that is trained to distinguish between the two, and train encoders for each dataset that encoder $y_2$ and $y_4$ in such a way that they are indistinguishable from each other.
* This forces the content to be stored specifically in $z_2$ and $z_4$. Now, since the set of $Y$ labeled examples is abundant, we have several $(z_4, label)$ pairs to train a new content classifier on, and now since $z_2$ and $z_4$ are interchangeable, we can use this dataset to augment the existing labels for the scarce dataset of $z_2, l$ pairs.

## Observations
* Even though the objective is to augment training of data scarce regimes with abundant data from another dataset, there are assumptions about the other dataset, including the very presence of such a dataset, and the fact that there should be at least one factor of variation in common.
* It'd have been interesting if the authors did an exploratory evaluation on the pancreatic and breast cancer datasets as well, as motivated in the introduction, instead of evaluating only on MNIST and SVHN.

