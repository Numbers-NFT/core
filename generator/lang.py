languages = ['ca', 'uk', 'tlh-Latn', 'is', 'bs', 'sm', 'kmr', 'gu', 'ps', 'pt', 'yua', 'af', 'hi', 'sq', 'es',
             'lzh', 'pt-PT', 'fil', 'te', 'ne', 'fi', 'mww', 'ga', 'hu', 'de', 'sr-Latn', 'ku', 'lo', 'mr',
             'lt', 'prs', 'nb', 'bg', 'or', 'fr', 'fj', 'sk', 'ta', 'kn', 'az', 'id', 'sr-Cyrl', 'hr', 'ar', 'el',
             'ru', 'cs', 'vi', 'bn', 'fa', 'yue', 'kk', 'he', 'mg', 'fr-CA', 'mt', 'mi', 'ty', 'ht',
             'ml', 'to', 'sv', 'cy', 'ms', 'zh-Hans', 'sl', 'tr', 'et', 'otq', 'ur', 'da', 'hy', 'nl', 'pa', 'zh-Hant',
             'ja', 'lv', 'th', 'it', 'as', 'pl', 'ko', 'sw']

lang_dict = {'ca': 'Setanta-quatre', 'uk': 'сімдесят чотири', 'tlh-Latn': 'loS', 'is': 'sjötíu og fjórir',
             'bs': 'sedamdeset četiri', 'sm': 'fitusefulu-fa', 'kmr': 'heftê û çar', 'gu': '૭૪', 'ps': 'څلور اویا',
             'pt': 'setenta e quatro', 'yua': "setenta yéetel kantúulo'on", 'af': 'Vier-en-sewentig', 'hi': 'चौहत्तर',
             'ti': 'ሰብዓን ኣርባዕተን', 'sq': '74', 'es': 'setenta y cuatro', 'lzh': '七十四', 'pt-PT': 'setenta e quatro',
             'fil': "pitumpu't apat na", 'ro': 'șaptezeci și patru', 'te': 'డెబ్బై నాలుగు', 'iu': '744',
             'ne': 'पचहत्तर', 'fi': 'seitsemänkymmentäneljä', 'mww': 'xyacaum plaub', 'ga': 'seachtó a ceathair',
             'hu': 'hetvennégy', 'de': 'vierundsiebzig', 'sr-Latn': 'sedamdeset četiri', 'ku': 'حەفتاو چوار',
             'lo': 'ເຈັດສິບສີ່', 'mr': 'चौहत्तर', 'lt': 'septyniasdešimt keturi', 'prs': 'هفتاد و چهار',
             'nb': 'syttifire', 'bg': 'седемдесет и четири', 'or': '74', 'en': 'seventy-four',
             'fr': 'soixante-quatorze', 'fj': 'vitusagavulu-va', 'sk': 'sedemdesiatštyri', 'ta': 'எழுபத்து நான்கு',
             'kn': 'ಎಪ್ಪತ್ತನಾಲ್ಕು', 'az': 'yetmiş dörd', 'id': 'tujuh puluh empat', 'sr-Cyrl': 'седамдесет четири',
             'hr': 'sedamdeset i četiri', 'ar': 'أربعة وسبعون', 'el': 'εβδομήντα τέσσερα', 'ru': 'семьдесят четыре',
             'cs': 'sedmdesát čtyři', 'vi': 'Bảy mươi bốn', 'bn': 'চুয়াত্তর', 'fa': 'هفتاد و چهار', 'yue': '七十四',
             'kk': 'жетпіс төрт', 'he': 'שבעים וארבע', 'mg': 'efatra am fitopolo', 'fr-CA': 'soixante-quatorze',
             'mt': 'erbgħa u sebgħin', 'mi': 'whitu tekau mā whā', 'am': 'ሰባ አራት', 'my': 'ခုနစ်ဆယ်လေးယောက်',
             'ty': 'hitu ahuru ma maha', 'ht': 'katsannk', 'km': 'ចិតសិបបួន', 'ml': 'എഴുപത്തിനാല്',
             'to': 'fitungofulu mā fā', 'sv': 'sjuttiofyra', 'cy': 'saith deg pedwar', 'ms': 'tujuh puluh empat',
             'zh-Hans': '七十四', 'sl': '74', 'tr': 'yetmiş dört', 'et': 'seitsekümmend neli',
             'otq': "setenta ya 're̲t'a ma goho", 'ur': 'چوہتر', 'da': '74', 'hy': 'յոթանասունչորս',
             'nl': 'vierenzeventig', 'pa': '74', 'zh-Hant': '七十四', 'ja': '74', 'lv': 'septiņdesmit četri',
             'th': 'เจ็ดสิบสี่', 'it': 'settantaquattro', 'as': 'চব্বিশ', 'pl': 'siedemdziesiąt cztery', 'ko': '74',
             'sw': 'sabini na nne'}

if __name__ == "__main__":

    final_list = list()

    for l in languages:
        if lang_dict[l] != '74':
            final_list.append(l)

    print(len(final_list))
    print(final_list)