text = """
the king loved playing cricket in the royal garden every evening
the queen loved playing chess in the grand palace every afternoon
the king and the queen walked in the royal garden together
the people loved the king because the king loved the people
the king loved the queen and the queen loved the king dearly
the royal garden was beautiful in the evening light
the grand palace had a chess room where the queen played every day
"""

words = text.lower().split()

def build_ngram_model(words, n=2):
    counts = {}
    for i in range(len(words)-n+1):
        context = tuple(words[i:i+n-1])
        target = words[i+n-1] 

        if context not in counts:
            counts[context] = {}
        if target not in counts[context]:
            counts[context][target] = 0
        counts[context][target] += 1
    probs = {}
    for context in counts:
        total = sum(counts[context].values())
        probs[context] = {}
        for target in counts[context]:
            probs[context][target] = counts[context][target]/total

    return probs
bigram=build_ngram_model(words, 2)
trigram=build_ngram_model(words, 3)
fourgram=build_ngram_model(words, 4)

'''print("BIGRAM - after - loved:")
for w, p in sorted(bigram[("loved",)].items(), key = lambda x: -x[1])[:5]:
    print(f"  {w}:{p: .1%}")
print("TRIGRAM - after - king, loved:")
for w, p in sorted(trigram[("king", "loved")].items(), key = lambda x: -x[1])[:5]:
    print(f"  {w}:{p: .1%}")'''

import random
def generate_ngram(model, n, start_words, num_words = 10): 
    output = list(start_words)

    for _ in range(num_words):
        context = tuple(output[-(n-1):])
        if context not in model: 
            break

        options = list(model[context].keys())
        probs = list(model[context].values())

        next_word = random.choices(options, weights = probs, k=1)[0]
        output.append(next_word)
    return " ".join(output)

print("BIGRAM-OUTPUT")
for i in range(3):
    print(f"{generate_ngram(bigram, 2, ['the'])}")

print("TRIGRAM-OUTPUT")
for i in range(3):
    print(f"{generate_ngram(trigram, 3, ['the','king'])}")

print("FOURGRAM-OUTPUT")
for i in range(3):
    print(f"{generate_ngram(fourgram, 4, ['the','king','loved'])}")
