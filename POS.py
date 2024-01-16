from enum import Enum

class PartOfSpeech(Enum):
    NOUN = "noun"
    VERB = "verb"
    ADJECTIVE = "adjective"
    ADVERB = "adverb"

class WordDefinition:
    def __init__(self, word, part_of_speech, definition, synonyms=None, antonyms=None, examples=None):
        self.word = word
        self.part_of_speech = part_of_speech
        self.definition = definition
        self.synonyms = synonyms or []
        self.antonyms = antonyms or []
        self.examples = examples or []

class LexicalDatabase:
    def __init__(self):
        self.word_definitions = {}

    def add_word_definition(self, word_definition):
        self.word_definitions[word_definition.word] = word_definition

    def lookup_word_definition(self, word):
        if word in self.word_definitions:
            return self.word_definitions[word]
        else:
            return None

    def lookup_synonyms(self, word):
        if word in self.word_definitions:
            return self.word_definitions[word].synonyms
        else:
            return []

    def lookup_antonyms(self, word):
        if word in self.word_definitions:
            return self.word_definitions[word].antonyms
        else:
            return []

    def lookup_examples(self, word):
        if word in self.word_definitions:
            return self.word_definitions[word].examples
        else:
            return []


lexical_database = LexicalDatabase()

word_definition_1 = WordDefinition("apple", PartOfSpeech.NOUN, "A round fruit with red or green skin and a white inside.",
                                   synonyms=["fruit", "pomaceous fruit"],
                                   antonyms=["orange"],
                                   examples=["I ate an apple for breakfast.",
                                             "The apple tree is in bloom."])
lexical_database.add_word_definition(word_definition_1)

word_definition_2 = WordDefinition("run", PartOfSpeech.VERB, "To move quickly on foot.",
                                   synonyms=["jog", "sprint"],
                                   antonyms=["walk"],
                                   examples=["I like to run in the morning.",
                                             "The dog ran after the ball."])
lexical_database.add_word_definition(word_definition_2)

print(lexical_database.lookup_word_definition("apple").definition)
# Output: A round fruit with red or green skin and a white inside.

print(lexical_database.lookup_synonyms("apple"))
# Output: ['fruit', 'pomaceous fruit']

print(lexical_database.lookup_antonyms("run"))
# Output: ['walk']

print(lexical_database.lookup_examples("run"))
# Output: ['I like to run in the morning.', 'The dog ran after the ball.']