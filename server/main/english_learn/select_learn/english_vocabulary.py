from functools import lru_cache
import pprint
import requests

import nltk
from nltk.stem.porter import PorterStemmer
from nltk import pos_tag
porter_stemmer = PorterStemmer()

POS_DEFINITIONS = {
    "CC":	"coordinating conjunction",
    "CD":	"cardinal digit",
    "DT":	"determiner",
    "EX":	"existential there",
    "FW":	"foreign word",
    "IN":	"preposition/subordinating conjunction",
    "JJ":	"This NLTK POS Tag is an adjective (large)",
    "JJR":	"adjective, comparative (larger)",
    "JJS":	"adjective, superlative (largest)",
    "LS":	"list market",
    "MD":	"modal (could, will)",
    "NN":	"noun, singular (cat, tree)",
    "NNS":	"noun plural (desks)",
    "NNP":	"proper noun, singular (sarah)",
    "NNPS":	"proper noun, plural (indians or americans)",
    "PDT":	"predeterminer (all, both, half)",
    "POS":	"possessive ending (parent\ ‘s)",
    "PRP":	"personal pronoun (hers, herself, him, himself)",
    "PRP$":	"possessive pronoun (her, his, mine, my, our )",
    "RB":	"adverb (occasionally, swiftly)",
    "RBR":	"adverb, comparative (greater)",
    "RBS":	"adverb, superlative (biggest)",
    "RP":	"particle (about)",
    "TO":	"infinite marker (to)",
    "UH":	"interjection (goodbye)",
    "VB":	"verb (ask)",
    "VBG":	"verb gerund (judging)",
    "VBD":	"verb past tense (pleaded)",
    "VBN":	"verb past participle (reunified)",
    "VBP":	"verb, present tense not 3rd person singular(wrap)",
    "VBZ":	"verb, present tense with 3rd person singular (bases)",
    "WDT":	"wh-determiner (that, what)",
    "WP":	"wh- pronoun (who)",
    "WRB":	"wh- adverb (how)"
}

DEFINITIONS_AMOUNT = 3


def parse_definition_request(definitions_request):
    definitions = []
    sound_link = ""
    definitions_request = definitions_request.json()
    # pprint.pprint(definitions)
    count = 0
    for i in range(len(definitions_request)):
        if len(sound_link) == 0 and len(definitions_request[i]["phonetics"]) > 0:
            # print(definitions_request[i]["phonetics"])
            if definitions_request[i]["phonetics"][0].get("audio", False):
                sound_link = definitions_request[i]["phonetics"][0]['audio']

        for meaning in definitions_request[i]['meanings']:
            for definition in meaning['definitions']:
                # top definitions
                if count < DEFINITIONS_AMOUNT:
                    # print(definition['definition'])
                    definitions.append(definition['definition'])
                    count += 1
                else:
                    break

    return {
        "definitions": definitions,
        "sound_link": sound_link
    }


@lru_cache(maxsize=100000)
def request_definition(word):
    return requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}")


@lru_cache(maxsize=100000)
def get_definition(word):
    word = word.lower().strip()

    definitions = {
        "definitions": [],
        "sound_link": ""
    }
    definitions_request = request_definition(word)

    if definitions_request.status_code == 200:
        definitions = parse_definition_request(definitions_request)
    else:
        # stem word
        word = porter_stemmer.stem(word)
        # get definition stem word
        definitions_request = request_definition(word)

        if definitions_request.status_code == 200:
            definitions = parse_definition_request(definitions_request)

    return definitions


@lru_cache(maxsize=100000)
def get_word_POS(sentence, word):

    tokens = nltk.word_tokenize(sentence)
    pos_tags = nltk.pos_tag(tokens)
    pos_tag = ""
    for item in pos_tags:
        if word in item[0]:
            pos_tag = item[1]
            break
    pos_definition = POS_DEFINITIONS.get(pos_tag, "No pos definition")

    return pos_definition
