from twitter_api import twitter_obj
from pickle_api import store_pickle, get_pickle
from word_cloud_api import create_wordcloud_file_from_dict
from text_mod_api import normalize_string_to_dict

# get dictionary if first run...
# import nltk
# nltk.download('punkt')
# nltk.download('stopwords')



my_api = twitter_obj()
trends = my_api.get_us_trends()

print(my_api)
print()
print(trends)
print()

# Storing pickle so we don't overdo the scrape
# store_pickle(trends,"pickled_trends.pkl")

# Get pickled
# pickled_trends = get_pickle('pickled_trends.pkl')

# print(pickled_trends)

trend_dict = {}

for single_trend in trends[0]["trends"]:
    # print(single_trend)
    if single_trend['tweet_volume'] == None:
        pass
    else:
        tweet_volume = single_trend['tweet_volume']
        trend_dict[single_trend['name']] = tweet_volume

print(trend_dict)

create_wordcloud_file_from_dict(trend_dict, "trend_cloud.png")

statuses = my_api.get_dumps_for_topic(trends[0]["trends"][0]["name"])

# statuses = get_pickle('pickled_statuses.pkl')

print(statuses[0])

long_text = " ".join([single_status["text"] for single_status in statuses])

# word_list = []
#
# for single_text in texts_list:
#     word_list+=single_text.split(" ")
#
text_word_dict = normalize_string_to_dict(long_text)

create_wordcloud_file_from_dict(text_word_dict, "trend_word.png")
