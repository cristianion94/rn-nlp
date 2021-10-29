import nltk
# from nltk.corpus import wordnet as wn
# nltk.download('wordnet')

# from nltk.parse.generate import generate, demo_grammar
# from nltk import CFG
# grammar = CFG.fromstring(demo_grammar)
# print(grammar)

# Symbol	Meaning	Example
# S	sentence	the man walked
# NP	noun phrase	a dog
# VP	verb phrase	saw a park
# PP	prepositional phrase	with a telescope
# Det	determiner	the
# N	noun	dog
# V	verb	walked
# P	preposition	in
 
import nltk

groucho_grammar = nltk.CFG.fromstring("""
S -> NP VP
NP -> N | N CONJ N | Det N | 'I' | 'We' | 'us'
VP -> V NP | VP PP
PP -> P NP
V -> 'saw' | 'ate'
N -> 'lady' | 'hill' | 'octopus' | 'shells' | 'dinner' | 'Anna' | 'Peter'
P -> 'on' | 'for'
CONJ -> 'and'
Det -> 'the'
""")

sentences = [
    "I saw the lady on the hill",
    "We ate octopus and shells for dinner",
    "Anna and Peter saw us"
]

parser = nltk.ChartParser(groucho_grammar)

for sent in sentences:
    print("sent:", sent)
    s = sent.split(" ")
    for tree in parser.parse(s):
        print(tree)
    print("\n\n")


# import spacy
# from spacy import displacy

# # Load the language model
# nlp = spacy.load("en_core_web_sm")

# sentence = 'Deemed universities charge huge fees'

# # nlp function returns an object with individual token information, 
# # linguistic features and relationships
# doc = nlp(sentence)

# print ("{:<15} | {:<8} | {:<15} | {:<20}".format('Token','Relation','Head', 'Children'))
# print ("-" * 70)

# for token in doc:
#   # Print the token, dependency nature, head and all dependents of the token
#   print ("{:<15} | {:<8} | {:<15} | {:<20}"
#          .format(str(token.text), str(token.dep_), str(token.head.text), str([child for child in token.children])))
  
# # Use displayCy to visualize the dependency 
# displacy.render(doc, style='dep', jupyter=True, options={'distance': 120})