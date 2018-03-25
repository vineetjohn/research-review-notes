---
layout: default
permalink: "reviews/disentangled-representations-for-manipulation-of-sentiment-in-text.html"
title: 'Disentangled Representations for Manipulation of Sentiment in Text'
---

# Disentangled Representations for Manipulation of Sentiment in Text

## Idea

The main idea of the paper is to change the style (sentiment) of a body of text while retaining its content

## Method

* This system uses a CNN for text encoding and an RNN for decoding.
* MMD is a metric that calculates the distance between the means of 2 different probability distribution. This is estimated in this paper using a Gaussian kernel.
* In the case of sentiment, 2 distinct probability distributions $P_{source}$ and $P_{target}$ are learned. The style transfer is achieved by traversing the manifold between these 2 distributions.
* The initial training phase just uses an autoencoder-like setup to recreate the original sentences.
* After the initial training, the CNN is trained to classify sentiment, thus, causing the distribution of the encoded sentences to diverge based on whether the sentence is positive or negative.
* Decoding is done by conditioning the start of the sentence on a start-of-sentence token and the sentence's encoding. The sentence generation ends when an EOS (end-of-sentence) token is generated.
* The traversal across the manifold between the positive and negative distributions is done to transfer the sentiment of text.

## Observations

* It is not clear how the representations are disentangled. It seems like the sentence encoding itself encodes information about the sentiment and hence, the representations rely on the entanglement to generate the manifold which is traversed.
* No quantitative evaluations were performed citing lack of evaluation metrics.
