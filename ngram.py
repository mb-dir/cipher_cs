from math import log10

class ngram(object):
    def __init__(self, ngramfile, sep=' '):
        ''' Load a file containing ngrams and counts, calculate log probabilities '''
        self.ngrams = {}
        with open(ngramfile, 'r') as f:
            for line in f:
                key, count = line.strip().split(sep)
                self.ngrams[key] = int(count)
        self.L = len(key)
        self.N = sum(self.ngrams.values())

        for key in self.ngrams.keys():
            self.ngrams[key] = log10(float(self.ngrams[key]) / self.N)
        self.floor = log10(0.01 / self.N)

    def score(self, text):
        ''' Compute the score of text '''
        score = 0
        ngrams = self.ngrams.__getitem__
        for i in range(len(text) - self.L + 1):
            if text[i:i + self.L] in self.ngrams:
                score += ngrams(text[i:i + self.L])
            else:
                score += self.floor
        return score