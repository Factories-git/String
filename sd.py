def build_ngram_model(corpus):
    ngram_model = {}

    for sentence in corpus:
        for i in range(len(sentence) - 1):
            current_char = sentence[i]
            next_char = sentence[i + 1]

            if current_char not in ngram_model:
                ngram_model[current_char] = {}

            if next_char not in ngram_model[current_char]:
                ngram_model[current_char][next_char] = 0

            ngram_model[current_char][next_char] += 1

    # Choose the most frequent next character for each character
    for current_char in ngram_model:
        next_chars = ngram_model[current_char]
        most_frequent_char = min(next_chars, key=lambda k: (-next_chars[k], k))
        ngram_model[current_char] = most_frequent_char

    return ngram_model

corpus = ['[i-love-you]','my-name-is-james','[gist-algorithm-masters]']
print(build_ngram_model(corpus))