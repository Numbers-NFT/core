from wordcloud import WordCloud
from translator import get_words
import numpy as np
from PIL import Image
import os

#english, dec, bin, hex
NUMBERS = [
    ('One', '1', '1', '1')
]

FONTS = [
    "OrelegaOne-Regular.ttf",
    "ZenDots-Regular.ttf"
]

word_list = get_words(NUMBERS[0][0])

text = " ".join(wordList)
print(text)

src_dir = os.getcwd()
imagePath = src_dir + "/apple.png"
font = src_dir + "/SimHei.ttf"
resultPath = src_dir + "/output.png"

bg = np.array(Image.open(imagePath))
wc = WordCloud(
    mask=bg,
    background_color="white",
    max_font_size=150,
    min_font_size=5,
    max_words=5000,
    random_state=40,
    font_path=font,
).generate(text)
wc.to_file(resultPath)