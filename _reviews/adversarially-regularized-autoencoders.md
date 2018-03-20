---
layout: default
permalink: "reviews/adversarially-regularized-autoencoders.html"
title: 'Adversarially Regularized Autoencoders'
---

# Adversarially Regularized Autoencoders
---

## Idea
The authors attempt to learn disentangled representations for text using adversarially regularized autoencoders. 


## Method
* The ARAE proposed in this paper is a direct enhancement to a VAE.
* The adversarial discriminator/critic in this model provides a regularization that causes the generator to enforce a low Wasserstein distance metric between the true samples and the generated samples.
* Similar to several other papers, the generator is conditioned to reconstruct the unaligned text samples. It's denoted by $p_{\Psi}(x\|y,c) $ where $c$ is the content embedding and $y$ is the label.

### Experiments
* They emulate the experimental setup of [Style Transfer from Non-Parallel Text by Cross-Alignment](https://arxiv.org/abs/1705.09655) by using the Yelp positive/negative reviews corpus.
* 2 decoders are used, 1 each for positive and negative review decoding.
* 4 metrics are automatically tested, namely:
    * Transfer strength using a pre-trained classifier (FastText, which isn't actually a classifier, but an embedding method)
    * BLEU score
    * Perplexity and Reverse Perplexity, both of which are assesses using an RNN model. (This is just $2^{\mathcal{L}_{rec}}$)
* Human evaluations were also conducted to assess Transfer, Similarity and Naturalness.
* Similarly the authors also evaluate topic transfer, which tries to convert snippets of text from Politics, Science and Music to each other.


## Observations
* The model seems to outperform the model presented in the 'Style Transfer from Non-Parallel Text by Cross-Alignment' paper on both Transfer Strength and Content Preservation (as evaluated by BLEU scores)
* The authors do not state which BLEU score they use.
* The only novel offering this paper seems to provide by way of method is the usage of the Wasserstein-1 distance metric as a measure of distribution proximity as opposed to the Jensen-Shannon distance used in GANs.
* The authors state multiple times that they're operating on a discrete space and this makes it difficult for to estimate a sequence loss, but this estimation is usually done using a softmax approximation for the output space and an item-wise cross-entropy loss. Discrete autoencoders already exist.
