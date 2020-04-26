from wordcloud import WordCloud


def create_wordcloud(text):
    print("starting generation")
    wordcloud = WordCloud().fit_words(text).to_file('wordcloud.png')
    print('wordcloud success')


def create_wordcloud_file_from_dict(text_dict, file_path):
    wordcloud = WordCloud().fit_words(text_dict).to_file(file_path)
