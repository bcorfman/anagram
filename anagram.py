from collections_extended import bag


def read_word_list(wordlist_filename: str = "wordlist.txt") -> list:
    with open(wordlist_filename) as wordlist:
        return [word.lower().strip() for word in wordlist.readlines()]


def anagrams(search_word: str, word_list: list) -> list:
    letters_in_search_word = bag(search_word)
    candidate_word_list = [
        word for word in word_list if bag(word).issubset(letters_in_search_word)
    ]
    solutions = []
    for i, first_word in enumerate(candidate_word_list):
        first_bag = bag(first_word)
        for j in range(i + 1, len(candidate_word_list)):
            second_word = candidate_word_list[j]
            if first_bag + bag(second_word) == letters_in_search_word:
                solutions.append(f"{first_word} {second_word}")
                solutions.append(f"{second_word} {first_word}")
    return solutions


def main():
    for pairs in anagrams("documenting", read_word_list()):
        print(pairs)


if __name__ == "__main__":
    main()
