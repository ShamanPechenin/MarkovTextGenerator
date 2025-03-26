from random import choice


def tokenize_text(text):
    text = text.replace(".", "")
    words = text.split()
    tokens = []
    token_pairs = {}
    for i in range(len(words) // token_size):
        token = " ".join(words[i * token_size:(i + 1) * token_size])
        tokens.append(token)
        if i < 1:
            continue
        if tokens[-2] in token_pairs.keys():
            token_pairs[tokens[-2]].append(token)
        else:
            token_pairs[tokens[-2]] = [token]

    return words, tokens, token_pairs


def find_token_from_string(text):
    start = text.split()
    if len(start) > 1:
        tokenized_start = []
        for i in range(len(start) // token_size):
            tokenized_start.append(" ".join(start[i * token_size:(i + 1) * token_size]))
    else:
        tokenized_start = start

    if tokenized_start[-1] in token_pairs:
        first_token = tokenized_start[-1]
    else:
        first_token = ""
        for token in tokens:
            if start[-1].lower() in token.lower():
                first_token = token
                break
        if first_token == "":
            first_token = choice(words)
    return first_token


def generate_token_chain(first_token):
    chain = [first_token]

    for i in range(max_size):
        try:
            chain.append(choice(token_pairs[chain[-1]]))
        except:
            break
    return chain


if __name__ == "__main__":
    token_size = 2
    start = "Дорогие товарищи"
    max_size = 30

    with open("dataNY1.txt", "r", encoding="utf-8") as file:
        data = file.read()

    words, tokens, token_pairs = tokenize_text(data)
    first_token = find_token_from_string(start)
    chain = generate_token_chain(first_token)
    res = ' '.join(chain)
    print(res)
