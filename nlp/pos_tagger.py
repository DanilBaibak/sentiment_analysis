import nltk
from nltk.corpus import wordnet as wn


class POSTagger(object):
    def __init__(self):
        self.lmtzr = nltk.stem.wordnet.WordNetLemmatizer()
        
    def is_noun(self, tag):
        return tag in ['NN', 'NNS', 'NNP', 'NNPS']

    def is_verb(self, tag):
        return tag in ['VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']

    def is_adverb(self, tag):
        return tag in ['RB', 'RBR', 'RBS']

    def is_adjective(self, tag):
        return tag in ['JJ', 'JJR', 'JJS']

    def penn_to_wn(self, tag):
        """
        Transform tag of the word to the wordnet
        :param tag: tag of the word
        :return: wordnet
        """
        if self.is_adjective(tag):
            return wn.ADJ
    
        if self.is_noun(tag):
            return wn.NOUN
    
        if self.is_adverb(tag):
            return wn.ADV
    
        if self.is_verb(tag):
            return wn.VERB
            
        return wn.NOUN

    def pos_tag(self, sentences):
        """
        :param sentences: list of lists of words
            e.g.: [['this', 'is', 'a', 'sentence']]
        :return: list of dictionaries of tagged tokens. Each tagged tokens has a form, a lemma, a postag, and a lexpression
            e.g: [[{'expression': None, 'lemma': 'This', 'word': 'this', 'postag': 'DT'},
                {'expression': None, 'lemma': 'be', 'word': 'is', 'postag': 'VBZ'},
                {'expression': None, 'lemma': 'a', 'word': 'a', 'postag': 'DT'},
                {'expression': None, 'lemma': 'sentence', 'word': 'sentence', 'postag': 'NN'},
                {'expression': None, 'lemma': '.', 'word': '.', 'postag': '.'}]]
        """
        tagged_text = []
        pos = [nltk.pos_tag(sentence) for sentence in sentences]        
        for sentence in pos:
            tagged_sentence = []
            for word, postag in sentence:
                tagged_sentence.append({
                    'word': word.lower(), 
                    'lemma': self.lmtzr.lemmatize(word, self.penn_to_wn(postag)), 
                    'postag': postag, 
                    'expression': None
                })
                
            tagged_text.append(tagged_sentence)

        return tagged_text
