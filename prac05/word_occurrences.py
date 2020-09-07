def main():
    words = {}
    string = input("Text: ")
    split_string = string.split(" ")
    for word in split_string:
        words[word] = 0
    for word in split_string:
        if word in split_string:
            words[word] += 1
    word_keys = list(words.keys())
    word_keys.sort()
    longest_name = get_longest_name(word_keys)
    for key in word_keys:
        print(f"{key:{longest_name}} : {words[key]}")


def get_longest_name(lst):
    longest_name = 0
    for value in lst:
        if len(value) > longest_name:
            longest_name = len(value)
    return longest_name


main()
