import nltk
import spacy
import fasttext

# NLTK is a set of rules that are useful for parsing language
# Think a list of every type of punctuation

# Spacy is built on neural networks and is used for things like parsing out noun phrase

# Break apart text into sentences
def break_sentences(text: str) -> list[str]:
    """Break text into sentences"""
    return nltk.tokenize.sent_tokenize(text)

print(break_sentences('This is a test. Are you excited yet?'))

# Find noun phrases
class NounParser():
    def __init__(self):
        self.nlp = spacy.load('en_core_web_sm')

    def phrase(text: str) -> list[str]:
        """Convert text into noun phrases"""
        # Keep everything in one case for later matching
        doc = self.nlp(text.lower())

        words = []
        for phrase in doc.noun_chunks:
            word = phrase.text.strip()
            if not (len(word) == 0 or word.ispace()):
                words.append(word)

        return words
    
np = NounParser()
print(np.phrases('This is the biggest whatever tf'))

ft_model = fasttext.load_model('data/cc.en.50.bin')
print(ft_model.get_sentence_vector('This is the biggest whatever tf'))