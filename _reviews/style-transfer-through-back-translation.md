---
layout: default
permalink: 'reviews/style-transfer-through-back-translation.html'
title: 'Style Transfer Through Back-Translation'
---

# Style Transfer Through Back-Translation
---

## Idea

The authors state that learning a language translation model better preserves the meaning of a sentence and reduces it's stylistic properties, allowing for adversarial generation of text in the different style as the original. They also claim to have improved automatic evaluation of style transfer, and manual evaluation of content preservation.

## Method

* Based on [previous work](https://arxiv.org/abs/1610.05461) that concludes that machine translation strips sentences of their stylistic content, hence, translating to another language and back should be the preliminary step before conditioned generation on a new style. They use author style as the framework for evaluation.
* The authors use a multi-decoder model i.e. one model per style, similar to previous work done for text style transfer.
* The output of the decoders are sent to a classifier, with the objective of checking if the generated sentence has the attributes that the decoder needs to include while producing it. This is an additional training signal to guide the decoder.
* The model loss is a linear combination of the reconstruction and classifier losses.
* An attention vector is also used for alignment between the original sentence and the style transferred decoded sentence.


## Observations

* Content preservation was evaluated manually. Although style transfer evaluation is trivial, this metric seems more difficult to find an automated metric for.
* One of the main motivations given for style transfer in text is to alleviate bias by synthesizing training data. However, if that was the objective, wouldn't it be better to simply train the model with the bias such that it isn't able to differentiate between two distributions of the same content with different style distributions?
* This model seems to have performed better for longer sentences, and also outperformed the cross-alignment paper for style transfer on political slant and sentiment.
