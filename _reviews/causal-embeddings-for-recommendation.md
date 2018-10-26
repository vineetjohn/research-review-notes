---
layout: default
permalink: 'reviews/causal-embeddings-for-recommendation.html'
title: 'Causal Embeddings for Recommendation'
---

# Causal Embeddings for Recommendation
---

## Idea
The authors argue that recommendation systems that optimize for time-spent are indirect optimization methods compared to approaches that just predict items based on a user's past. They learn a recommendation policy that tries to infer the desired outcome from organic user behavior.

The idea presented is a riff on simple matrix factorization methods and uses the outcome of randomized recommendations' outcomes to create user and item representations.

## Background
Previous approaches to item recommendations are broadly classified into 2 categories:
1. Item-to-item similarity systems, that learn embeddings for items and use a distance metric like cosine similarity to identify similar items
2. User-item sequence embeddings, which tries to predict the next item which the user intends to purchase.

## Method
* The authors attempt to jointly factorize the matrix of control observations and the matrix of treatment observations.
* They utilize an algorithm the call the 'CausE' algorithm, that generates the recommendations.

## Observations
* The proposed algorithms outperformed the baselines compared against for the MovieLens and Netflix datasets.
