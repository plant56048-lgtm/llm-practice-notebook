# llm-practice-notebook
Daily hands-on practice code from an LLM course: 1 hour a day, building from prompts to working LLM apps.
# LLM Practice Daily

My hands-on practice code from an 8-hour LLM course.
I'm spending **1 hour per day** for 8 days, and each day's folder has the code I wrote plus short notes on what I learned.

## Day 1: Bigram Language Model

Built a simple **bigram language model** from scratch using pure Python (no libraries).

**What it does:**
- Splits a sample text into words
- Counts how often each word is followed by every other word (`pair_counts`)
- Converts those counts into probabilities (`pair_probs`) — e.g. what's the chance "king" is followed by "loved"?
- Generates new text by randomly picking the next word, weighted by these probabilities

**Why it matters:** This is the core idea behind how language models predict the next token — real LLMs do the same thing, just with billions of parameters and far more context instead of just one previous word.

**Example output:**
```
the king loved the queen and...
```
## Day 2: N-gram Language Model

Extended the Day 1 bigram language model into a **general n-gram language model** using pure Python.

**What I learned:**

- Generalized the model to support different values of `n`
- Built **bigram, trigram, and fourgram models** using the same function
- Used `(n-1)` previous words as the **context** to predict the next word
- Converted word counts into probabilities for each context
- Generated text by randomly sampling the next word based on its probability

**How it works:**

For an **n-gram model**, the previous `n-1` words are used to predict the next word.

For example:

```text
Bigram:
Context → "king"
Target  → "loved"

Trigram:
Context → "king loved"
Target  → "the"

Fourgram:
Context → "king loved the"
Target  → "queen"
```

The model stores these relationships as:

```text
(context) → possible next words → probabilities
```

For example:

```text
("king", "loved") → {
    "the": probability,
    ...
}
```

**Generation:**

During text generation, the model:

1. Takes the starting words
2. Extracts the last `n-1` words as the current context
3. Looks up possible next words
4. Uses their probabilities to randomly choose the next word
5. Adds the selected word to the output
6. Repeats the process

**Bigram vs Trigram vs Fourgram:**

- **Bigram:** Uses only 1 previous word as context
- **Trigram:** Uses 2 previous words
- **Fourgram:** Uses 3 previous words

As the context gets larger, the generated text can become more consistent because the model has more information about what came before. However, larger n-grams also need more training data to cover different contexts.

**Example:**

```text
BIGRAM OUTPUT:
the king loved the queen...

TRIGRAM OUTPUT:
the king loved the queen and...

FOURGRAM OUTPUT:
the king loved the queen and the king...
```

**Why it matters:**

This shows how adding more context can improve next-word prediction. Modern LLMs use much more sophisticated architectures and learn far more complex patterns, but the basic idea of **using previous context to predict what comes next** is an important foundation.



## Day 3: Vector Similarity & Word Embeddings

Explored how similarity between words is measured mathematically — the foundation of how LLMs represent meaning as vectors.

**What it does:**
- Implements `dot_product()` and `vector_size()` (magnitude) from scratch
- Builds `cosine_similarity()` = dot product ÷ (magnitude A × magnitude B)
- Tests dot product alone first — shows it's misleading when vectors differ in scale (e.g. `rajat` vs `rahul`, same direction but 10x bigger, dot product way overstates difference)
- Switches to cosine similarity, which normalizes for scale and only measures *direction* — so `rajat` vs `rahul` correctly comes out ~1.0 (nearly identical)
- Applies this to toy 5-dimensional "word embeddings" for king, queen, cricket, potato — finds king/queen highly similar, king/potato strongly dissimilar
- Writes `find_best_word_in_llm()`: given a target vector, ranks a vocabulary by cosine similarity — a tiny version of how an LLM picks the most relevant next token

**Key insight:** Cosine similarity cares about *direction*, not magnitude. Two vectors pointing the same way are "similar" even if one is 10x longer — this is why embeddings compare words by angle, not raw size.

**Example output:**
```
king:0.997
queen:0.997
cricket:0.236
potato:-0.653
```
## Day 4: Why LLMs Use Matrix Multiplication

Compared a plain Python loop against NumPy's matrix multiplication (`@`) to see why real LLMs can't afford to score words one at a time.

**What it does:**
- Scores 3 cricketers against an "ideal captain" profile two ways:
  - A nested loop, computing each dot product by hand
  - `cricketers @ ideal_captain` — the same scores, computed as one matrix-vector multiplication
- Both give identical results, but the matrix version is one line instead of a loop
- Scales the same idea up to realistic LLM size: a 100,000-word vocabulary, each word a 4096-dimensional vector (`vocabulary`), scored against one `requirements` vector
- Times the loop version vs `vocabulary @ requirements` on this larger data

**Key insight:** A real LLM vocabulary × embedding size is 100,000 × 4096 — looping through that in pure Python took **~350 seconds**. The matrix multiplication version does the exact same math in a fraction of a second, because NumPy runs it in optimized, vectorized C/BLAS code instead of Python's interpreter loop. This is why every LLM operation (attention, next-token scoring, etc.) is written as matrix multiplication, not loops — at billions of parameters, loops are simply too slow to ever finish.

**Example output:**
```
one at a time (loop):
Virat: 208
Bumrah: 189
Rohit: 179

All at once (Matrix)
Virat: 208
Bumrah: 189
Rohit: 179

The loop time is: 349.887...
0.012... (matrix time)
```
