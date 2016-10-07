from .nlp.dictionary_tagger import DictionaryTagger
from .nlp.pos_tagger import POSTagger
from .nlp.splitter import Splitter
import os


class Estimator(object):
    def __init__(self):
        # set root path for the project
        os.chdir(os.path.dirname(os.path.abspath(__file__)))

        self.dicttagger = DictionaryTagger({
            'positive': 'expressions/positive.csv',
            'negative': 'expressions/negative.csv',
            'inv': 'expressions/inv.csv',
            'inc': 'expressions/inc.csv',
            'dec': 'expressions/dec.csv'
        })
        self.splitter = Splitter()
        self.postagger = POSTagger()

    def value_of(self, sentiment):
        """
        Translate sentimental to the number value
        :param sentiment: string
        :return: int
        """
        if sentiment == 'positive':
            return 1

        if sentiment == 'negative':
            return -1

        return 0

    def sentence_score(self, sentence_tokens, previous_token, acum_score):
        """
        :param sentence_tokens: tokenized sentence
            e.g.: [[('I', 'I', ['PRP']), ('was', 'was', ['VBD']), ('in', 'in', ['IN'])]
        :param previous_token: token
        :param acum_score: int - the sentimental score of the text
        :return: the sentimental score
        """
        if not sentence_tokens:
            return acum_score
        else:
            current_token = sentence_tokens[0]
            expression = current_token['expression']
            token_postag = current_token['postag']

            token_score = self.value_of(expression)

            # check if the current adjective has comparative or superlative form
            if token_postag == 'JJR':
                token_score *= 2.0
            elif token_postag == 'JJS':
                token_score *= 3.0

            # check if previous the token is the increment or decrement or inverter
            if previous_token is not None:
                previous_expression = previous_token['expression']
                previous_token_postag = previous_token['postag']

                if previous_expression == 'inc':
                    if previous_token_postag == 'RBS':
                        token_score *= 3.0
                    else:
                        token_score *= 2.0
                elif previous_expression == 'dec':
                    if previous_token_postag == 'RBS':
                        token_score /= 3.0
                    else:
                        token_score /= 2.0
                elif previous_expression == 'inv':
                    token_score *= -1.0

            return self.sentence_score(sentence_tokens[1:], current_token, acum_score + token_score)

    def sentiment_score(self, review):
        return sum([self.sentence_score(sentence, None, 0.0) for sentence in review])

    def estimate(self, text):
        """
        Make sentimental estimation for the current text
        :param text: text for the estimation
            e.g.: The staff is amazing, friendly and helpful.
        :return: sentimental score
            e.g: 3
        """
        splitted_sentences = self.splitter.split(text)
        pos_tagged_sentences = self.postagger.pos_tag(splitted_sentences)
        dict_tagged_sentences = self.dicttagger.tag(pos_tagged_sentences)

        return self.sentiment_score(dict_tagged_sentences)
