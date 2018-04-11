---
layout: default
permalink: 'reviews/word-translation-without-parallel-data.html'
title: 'Word Translation Without Parallel Data'
---

# Word Translation Without Parallel Data
---

## Idea
The main idea of the paper is to separately and unsupervisedly learn word embeddings from 2 different languages using a method like Word2Vec and then align the embedding spaces of the 2 languages using adversarial training. This allows the similar words in each language to be mapped to roughly the same point on the manifold. This manifold can then be queried using one language's words and the corresponding word in the other languages closest in the embedding space should be the transalated word. In this way, the authors propose building an unsupervised bilingual dictionary.

## Method
* The Procrustes method using aligned words as anchor points and tries to reduce an energy function that corresponds to a spring system between anchor points.
* The authors come up with a custom metric of distance computation (CSLS) that evaluates the mean of cosine distances of a word to the K-nearest words in the other language to minimize the hubness problem of embeddings i.e. some words are the nearest neighbours of many points while some are not the nearest neighbour for any point.
* The model enforces an additional constraint to ensure the the linear transformation from the source language embedding manifold to the target languange embedding manifold done by the network is done by an orthogonal matrix.

### Experiments
* Fastext pre-trained vectors were used to translate the words into the embedding space.
* The authors also evaluate this method on a low-resource language pair i.e. English-Esperanto, and acheive results comparable to supervised methods.

## Observations
* This method albeit unsupervised, outperformed several supervised methods of generation bilingual lexicons, and should probably be considered a stepping stone towards non-parallel neural machine translation capabilities.
* The authors don't elaborate on how exactly they extract word-translation pairs for evaluation while accounting for polysemy.
* The adversarial objective to align the 2 monolingual embedding spaces seems to be adept at learn cross-lingual embeddings without parallel data and the Procrustes refinement approach ensures high-quality word mappings.

