
# Controlling Linguistic Style Aspects in Neural Language Generation

## Idea

The authors control multiple aspects of the text i.e. content and style via attribute vectors and generate modified bodies of text using a conditioned neural language model.

## Background

As opposed to the method used in [Toward Controlled Generation of Text](https://arxiv.org/abs/1703.00955), this one doesn't use variational auto-encoders.

## Method

* The authors rely on a conditioned LSTM-based neural language model to generate sentences with modified content and style. A movie review dataset from Rotten Tomatoes is used for the task.
* Multiple style and content attributes can be manipulated and used for training/generation at the same time i.e. combinations of the attributes can also be used.
* The labels attributed to the training set are known entities.
* Simple rules, heuristics and lexicons are used to derive some of the labels that the training data is annotated with.
* The system of multi-label conditioning is compared to dedicated language models for each attribute.
* A few of the metrics like sentiment and professional reviews are evaluated using human annotations.

## Observations

* The dedicated language models work better than the single conditioned language models but it doesn't scale to multiple attributes, which the authors cite as a desirable property to have.
* The authors state the sentiment was difficult to model since the perplexity of sentence conditioned with sentiment is lesser compared to conditioned sentences of other attributes. This could also be attributed to the fact that it takes lesser changes to model sentiment than it does to model the other attributes.
* Although the authors use manual annotation to label the sentiment of the generated sentences, a good generalizable sentiment analysis classifier might have been quicker.
