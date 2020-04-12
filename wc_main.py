
from twitter_api import twitter_obj
from pickle_api import store_pickle, get_pickle
from word_cloud_api import create_wordcloud_file_from_dict

if True:
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

word_dicts={}

for single_trend in trends[0]["trends"]:
    # print(single_trend)
    if single_trend['tweet_volume']==None:
        tweet_volume=10
    else:
        tweet_volume=single_trend['tweet_volume']
    word_dicts[single_trend['name']]=tweet_volume
    
print(word_dicts)
    
create_wordcloud_file_from_dict(word_dicts,"newfunc3.png")

my_api.get_dumps_for_topic(trends[0]["trends"][0]["name"])
