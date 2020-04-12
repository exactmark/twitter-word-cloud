import numpy as np
# import pandas as pd
from os import path
# from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

import matplotlib.pyplot as plt
# % matplotlib inline


def create_wordcloud(text):
    print("starting generation")
    wordcloud=WordCloud().fit_words(text).to_file('wordcloud.png')
    print('wordcloud success')
    # plt.imshow(wordcloud,interpolation='bilinear')
    # plt.axis('off')
    # plt.show()
    
def create_wordcloud_file_from_dict(text_dict,file_path):
    wordcloud=WordCloud().fit_words(text_dict).to_file(file_path)
    
    