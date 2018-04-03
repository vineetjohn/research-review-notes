---
layout: default
permalink: 'reviews/generating-sentences-by-editing-prototypes.html'
title: 'Generating Sentences by Editing Prototypes'
---

# Generating Sentences by Editing Prototypes
---

## Idea

The authors propose a prototype-then-edit model that involves modifying a source sentence by attending to the source sequence with a randomly sampled attention vector.

## Method

* The formulation described in the paper stems from the observation that sentences in a large corpus can be viewed as minor transformations of the other sentences in the corpus.
* The method involves sampling a random prototype from the training set to condition on. To avoid an intractable sum over all the possible sentences in the training set, since each of them have a uniform probability of being picked, only prototypes $x'$ in the neighbourhood of the final output $x$, following the rationale that only a subset of the total prototypes could possible be edited into $x$.
* The neighbourhood of candidate prototypes is calculated using a word-edit distance metric - Jaccard Distance.
* The prototype vector is attended to while decoding.
* The other component of the latent space is the random vector that is analogous to $z$ in a VAE setup. Unlike most applications of VAE, the sampling is done from a prior that is not a simple Gaussian distribution.

### Experiments
* A vocab size of $10K$ was used and the named-entities (proper nouns) were replaced by their base common nouns.
* Corpora used for the experiments were Yelp review and BillionWord
* The encoder used a 3 layer bidirectional LSTM and the decoder uses a 3 layer LSTM model with attention.

## Observations
* The perplexity results outperforms a vanilla neural language model and a 5-gram Kneser-Ney language model used in an ensemble for the Yelp corpus.
* Qualitative results indicate that multiple edits performed on a single sentence prevents degeneration to generic sentences.
