
# InfoGAN: Interpretable Representation Learning by Information Maximizing Generative Adversarial Nets

## Idea

The main idea is to be able to unsupervisedly learn interpretable representations about the semantics of an image from its latent code. This is done by maximinzing the mutual information between a fixed small subset of the generative noise variables in the GAN and the generated image.

## Background

* A vanilla GAN would use the latent space in an entangled manner, and the individial dimensions of the sampled noise $z$ would not correspond to distinct semantic features of the data.

## Method

* Latent code $c$ is the concatentation of all the possible latent variables $c_1, c_2 ... c_L$

## Observations
