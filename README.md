# Sentiment analysis
[Rule-based](https://en.wikipedia.org/wiki/Rule-based_system) library for [sentiment analysis](https://en.wikipedia.org/wiki/Sentiment_analysis). The main idea, that library returns mark of the _sentiment_ (3, -5, etc), but not only trend - _positive_ or _negative_. The way how _sentiment mark_ is calculated is just summarization of positive and negative adjectives, paying attention to the increment, decrement and inverter words. 

Current version of the library works only with **english** text.

# Main features
The library handles:
- _increment_ and _decrement_ words (like _less_, _greatly_, etc.)
- _inverter_ words (like _not_, etc.)
- _comparative_ and _superlative_ form

The **vocabulary** of the adjectives can strongly influence on the sentiment mark. So you can use different vocabularies of the _positive_ and _negative_ adjectives depends of the context of documents.

# Installation
For installation the best way use [conda](http://conda.pydata.org/docs/using/index.html). After installation **conda** just run:
```sh
conda env create -f env.yml
```
After the installation was done successfully, activate your enviroment:
```sh
source activate sa
```
> For using **conda** and **environments**, please read full documentation of [conda](http://conda.pydata.org/docs/using/index.html).

# Example
```sh
from sentiment_analysis.estimator import Estimator

estimator = Estimator()
print(estimator.estimate('The staff is amazing, friendly and helpful.'))
```
