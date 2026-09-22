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
