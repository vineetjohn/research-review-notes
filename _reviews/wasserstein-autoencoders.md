---
layout: default
permalink: 'reviews/wasserstein-autoencoders.html'
title: 'Wasserstein Autoencoders'
---

# Wasserstein Autoencoders
---

## Idea
Wasserstein Autoencoders (WAE) are proposed as an alternative to Variational Autoencoders (VAE) as a method of getting the encoded data distribution to match the prior, which can be used for generative modeling. The main idea is to use the Wasserstein distance metric to penalize the distance between the encoded distribution and the prior, as opposed to the KL-divergence term used in VAEs.

## Background
* Optimal Transport (OT) cost is a way of measuring the distance between probability distributions.
* f-divergences like the KL-divergence is apparently a stronger notion of distance and it often maxes out, provided no useful gradients, something that OT costs are supposed to address by their weaker topology.
* Classic f-divergences include the Kulback-Liebler divergence (KL-divergence) and the Jensen-Shannon divergence.

## Method
* The authors propose 2 separate regularizers, (1) the Wasserstein adversarial loss, and (2) a maximum mean discrepancy regularization, which is known to work well to match standard normal distributions in high dimensions. These approaches are called WAE-GAN and WAE-MMD respectively.
* The WAE-MMD model eliminates adversary training entirely and optimizes a min-min objective. A positive definite kernel is required to compute pairwise distances between the $n$ samples of the prior and encoded distributions.
* The WAE-GAN model optimizes the same adversarial objective as the regular GAN, except that the objective is defined on the latent space instead of the actual input/output space. The divergence is calculated by $D_{JS}$ which is the Jensen-Shannon divergence. This is evaluated empirically by averaging the divergence of $n$ samples.
* The authors explain the difference between VAEs and WAEs as being the absence of the mutual information term $\mathbb{I}_Q(X, Z)$ in WAEs.

## Observations
* The WAE-GAN algorithm seems faster as it only needs to do $O(n)$ computations as opposed to the WAE-MMD metric which requires $O(n^2)$
* "Typically Z has no more than 100 dimensions and $P_Z$ is Gaussian"
* WAE-GAN seems to have performed better on the quantitative image quality metrics
