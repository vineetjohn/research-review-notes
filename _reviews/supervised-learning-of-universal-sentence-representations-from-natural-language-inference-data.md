---
layout: default
permalink: 'reviews/supervised-learning-of-universal-sentence-representations-from-natural-language-inference-data.html'
title: 'Supervised Learning of Universal Sentence Representations from Natural Language Inference Data'
---

# Supervised Learning of Universal Sentence Representations from Natural Language Inference Data

---

## Idea

* The authors state the need for general purpose sentence embeddings similar to how word embeddings are used in several NLP tasks today. 
* They train their model on the Stanford Natural Language Inference (SNLI) corpus.
* The authors claim an improvement over the [SkipThought method](https://arxiv.org/abs/1506.06726) in learning generalized sentence embeddings that can be used for downstream tasks.


## Method

* The inspiration to train on a supervised task is taken from the fact that ImageNet, despite primarily being an object recognition model, learns features that can be used for a general computer vision task.
* After obtaining separate representations of the premise and hypothesis (2 sentences), the combined representation is a concatenation of:
    * Individual sentence representations
    * Element-wise product of the two representations
    * Element-wise subtraction of the two representations
* They try out the following architectural choices:
    * LSTM and GRU recurrent encoders
        * Only last hidden state used
    * BiLSTM network with mean/max pooling
        * All hidden states used
    * Self-attentive network
    * Hierarchical convolutional network
* The model is evaluated on a variety of tasks, including binary & multi-label classification, entailment, semantic relatedness, unsupervised textual similarity, paraphrase detection, image & caption retrieval.


## Observations

* This seems to be a very empirical paper. The main questions being answered is what neural network architecture, which task, and which dataset yields generalizable sentence embeddings.
* The BiLSTM with 4096 units and max pooling works best for the dev set, compared with other approaches.
* The authors observe that model convergence is quicker on Adam, but the results aren't as good.
* Combining the data from SNLI + MultiNLI improved the reported results.
* This approach outperformed SkipThought vectors on several benchmarks while being easier to train.

