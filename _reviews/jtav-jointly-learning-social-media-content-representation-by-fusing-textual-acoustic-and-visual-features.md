---
layout: default
permalink: 'reviews/jtav-jointly-learning-social-media-content-representation-by-fusing-textual-acoustic-and-visual-features.html'
title: 'JTAV: Jointly Learning Social Media Content Representation by Fusing Textual, Acoustic, and Visual Features'
---

# JTAV: Jointly Learning Social Media Content Representation by Fusing Textual, Acoustic, and Visual Features
---

## Idea
The authors propose to learn the 'content' of social media, by fusing together 3 distinct content modes: textual, acoustic and visual.
They claim that jointly learning features from all 3 of these outperforms systems that rely on single- or bi-modal learning.
Their approach involves learning single-modal features and then fusing together the features learned from different modes.

## Background
* Bi-modal learning has already been explored in previous work.
* This comprises learning representations of each single-modal attribute independently.
* These representations/embeddings can then be fused by learning a common embedding space.

## Method
An attention-based network attBiGRU is used for text information, a DCRNN for acoustic information, and a fine-tuned general framework called DenseNet for visual features.

Text information is divided into two parts:
* Protagonist
* Supporting Players
of which the supporting players attend to the representation of the protagonist.
Here, the protagonist is simply the largest body of text in the instance of data (e.g. blog post, song) and the supporting players refer to the auxiliary pieces of text (e.g. comments, reviews).

## Observations
* The addition of text and audio don't seem to give a huge boost over the performance already achieved by just images. (i.e. 0.58 vs. 0.62)
