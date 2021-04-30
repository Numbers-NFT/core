import translators as ts

def get_words(word):
    words = set()
    words.add(word)

    ts.bing("Hello", from_language="en", to_language="en")

    languages = ts._bing.language_map['en']
    size_languages = len(languages)
    index = 1

    for lang in languages:
        print(f"Getting translation ({index}/{size_languages})")
        words.add(ts.bing(word, from_language="en", to_language=lang))
        index+=1

    return words


if __name__ == "__main__":
    print(get_words("One"))