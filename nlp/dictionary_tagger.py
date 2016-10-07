import csv


class DictionaryTagger(object):
    def __init__(self, dictionary_paths):
        self.dictionary = {}
        self.max_key_size = 0
        
        for key, path in dictionary_paths.items():
            with open(path) as csvfile:
                dictionary = list(csv.reader(csvfile))
                self.dictionary[key] = [x[0] for x in dictionary]
                
    def tag(self, postagged_sentences):
        return [self.tag_sentence(sentence) for sentence in postagged_sentences]
    
    def tag_sentence(self, sentence):
        """
        Try to find expression for word or lemma in the dictionaries
        :param sentence: list of dictionaries of tagged tokens
        :return: list of dictionaries of tagged tokens with expressions
        """
        for word in sentence:
            for key, dictionary in self.dictionary.items():
                if word['word'] in dictionary or word['lemma'] in dictionary:
                    word['expression'] = key
                    # TODO - would be good if 'estimate' function also return list of words and expressions
                    break
                
        return sentence
