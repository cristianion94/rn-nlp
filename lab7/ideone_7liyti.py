fullDict = {
    "MascN": {
        "Cat": "Chat",
        "Book": "Livre",
        "Sugar": "Sucre"
    },
    "FemN": {
        "Cane": "Canne",
        "Woman": "Femme",
        "Table": "Table",
        "Saw": "Scie"
    },
    "V": {
        "Sleeps": "Dort",
        "Reads": "Lit",
        "Walks": "Marche",
        "Cut": "A coupé",
        "Saw": "A Vu",
        "Is": "Est"
    },
    "DET": {
        "The": "Le",
        "A": "Un"
    },
    "ADJ": {
        "Red": "Rouge",
        "Happy": "Heureuse",
        "Cane": "De Canne"
    },
    "CONJ": {
        "And": "Et",
        "Or": "Ou"
    },
    "PREP": {
        "With": "Avec",
        "To": "A",
        "From": "De",
        "Under": "Sous"
    }
}

translate = {
    "Cane": "Canne",
    "Cat": "Chat",
    "Book": "Livre",
    "Sugar": "Sucre",
    "Woman": "Femme",
    "Table": "Table",
    "Sleeps": "Dort",
    "Reads": "Lit",
    "Walks": "Marche",
    "Cut": "A coupé",
    "Is": "Est",
    "Red": "Rouge",
    "Happy": "Heureuse",
    "And": "Et",
    "Or": "Ou",
    "With": "Avec",
    "To": "A",
    "From": "De",
    "Under": "Sous"
}

categories = {
    "Cat": "MascN",
    "Book": "MascN",
    "Sugar": "MascN",
    "Woman": "FemN",
    "Table": "FemN",
    "Sleeps": "V",
    "Reads": "V",
    "Walks": "V",
    "Cut": "V",
    "Is": "V",
    "The": "DET",
    "Red": "ADJ",
    "Happy": "ADJ",
    "And": "CONJ",
    "Or": "CONJ",
    "With": "PREP",
    "To": "PREP",
    "From": "PREP",
    "Under": "PREP"
}

rules = {
    ("ADJ", "MascN"): ("MascN", "ADJ"),
    ("ADJ", "FemN"): ("FemN", "ADJ"),
    ("the", "MascN"): ("Le", "MascN"),
    ("the", "FemN"): ("La", "FemN"),
    ("The", "MascN"): ("Le", "MascN"),
    ("The", "FemN"): ("La", "FemN"),
    ("a", "MascN"): ("Un", "MascN"),
    ("a", "FemN"): ("Une", "FemN"),
    ("A", "MascN"): ("Un", "MascN"),
    ("A", "FemN"): ("Une", "FemN"),
    ("DET", "saw"): ("DET", "Scie"),
    ("saw", "DET"): ("A Vu", "DET"),
    ("DET", "cane"): ("DET", "Canne"),
    ("MascN", "cane"): ("MascN", "De Canne"),
    ("FemN", "cane"): ("FemN", "De Canne")
}

# print(rules[("ADJ", "N")])

sentencesToTranslate = [
    "A book is under the table.",
    "Mary cut the sugar cane with a saw.",
    "Mary cut the sugar cane and is happy.",
    "The woman with a red cane saw a cat under the table and walks to the cat."
]

for sentence in sentencesToTranslate:
    sentence = sentence.split(" ")
    sentence[len(sentence) - 1] = sentence[len(sentence) - 1][:-1]
    print(sentence)

    tmp = ["" for _ in range(len(sentence))]
    translated = [False for _ in range(len(sentence))]

    for i in range(len(sentence) - 1):
        if translated[i] == False and translated[i + 1] == False:
            w1 = sentence[i]
            w2 = sentence[i + 1]
            categorie1 = w1
            categorie2 = w2
            if w1.capitalize() in categories and w1.lower() != "the":
                categorie1 = categories[w1.capitalize()]
            if w2.capitalize() in categories and w2.lower() != "the":
                categorie2 = categories[w2.capitalize()]
            if (categorie1, categorie2) in rules:
                result1, result2 = rules[(categorie1, categorie2)]
                if categorie1 == result1:
                    if categorie2 == result2:
                        tmp[i] = translate[w1.capitalize()]
                        tmp[i + 1] = translate[w2.capitalize()]
                        translated[i] = True
                        translated[i + 1] = True
                    else:
                        tmp[i] = translate[w1.capitalize()]
                        tmp[i + 1] = result2
                        translated[i] = True
                        translated[i + 1] = True
                elif categorie1 == result2:
                    if categorie2 == result1:
                        tmp[i] = translate[w2.capitalize()]
                        tmp[i + 1] = translate[w1.capitalize()]
                        translated[i] = True
                        translated[i + 1] = True
                    else:
                        tmp[i] = result2
                        tmp[i + 1] = translate[w1.capitalize()]
                        translated[i] = True
                        translated[i + 1] = True
                else: # 1 != 1 and 1 != 3
                    if categorie2 == result2: # 1-> 1 translated, 2 -> 2
                        tmp[i] = result1
                        tmp[i + 1] = translate[w2.capitalize()]
                        translated[i] = True
                        translated[i + 1] = True
                    else: # 1-> 2 translated, 2 -> 1
                        tmp[i] = translate[w2.capitalize()]
                        tmp[i + 1] = result1
                        translated[i] = True
                        translated[i + 1] = True
    for i in range(len(sentence)):
        if not translated[i] and sentence[i].capitalize() in translate:
            tmp[i] = translate[sentence[i].capitalize()]
        elif not translated[i]:
            tmp[i] = sentence[i]
    #print(tmp)
    print(' '.join(tmp))