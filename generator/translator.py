import time

import translators as ts


def get_words(word):
    print("Translation for word:" + word)
    words = dict()

    words[word] = 1
    print("Started get_words for: " + word)

    languages = ['ca', 'uk', 'tlh-Latn', 'is', 'bs', 'sm', 'kmr', 'gu', 'ps', 'pt', 'yua', 'af', 'hi', 'es', 'lzh',
                 'pt-PT', 'fil', 'te', 'ne', 'fi', 'mww', 'ga', 'hu', 'de', 'sr-Latn', 'ku', 'lo', 'mr', 'lt', 'prs',
                 'nb', 'bg', 'fr', 'fj', 'sk', 'ta', 'kn', 'az', 'id', 'sr-Cyrl', 'hr', 'ar', 'el', 'ru', 'cs', 'vi',
                 'bn', 'fa', 'yue', 'kk', 'he', 'mg', 'fr-CA', 'mt', 'mi', 'ty', 'ht', 'ml', 'to', 'sv', 'cy', 'ms',
                 'zh-Hans', 'tr', 'et', 'otq', 'ur', 'hy', 'nl', 'zh-Hant', 'lv', 'th', 'it', 'as', 'pl', 'sw']

    print(languages)
    size_languages = len(languages)
    index = 1

    for lang in languages:
        is_done = False
        internal_sleep = 1
        while not is_done:
            try:
                print(f"Getting translation ({index}/{size_languages}) with internal_sleep={internal_sleep} ")
                time.sleep(internal_sleep)
                try:
                    words[ts.bing(word, from_language="en", to_language=lang)] = 1
                except KeyError:
                    print("No translation for:" + lang)
                index += 1
                internal_sleep = 1
                is_done = True
            except IOError as e:
                print(e)
                is_done = False
                internal_sleep = internal_sleep * 2
                print("Błąd w pętli for z pobieraniem tłumaczenia, ponawiam")

    return words


if __name__ == "__main__":
    print(get_words("seventy-four"))
