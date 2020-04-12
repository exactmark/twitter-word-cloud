from twitter_api import twitter_obj
from pickle_api import store_pickle, get_pickle
from word_cloud_api import create_wordcloud_file_from_dict
from text_mod_api import normalize_string_to_dict
from datetime import datetime
from simple_html_api import create_table_from_trend_dicts,append_table_to_index
import os,time

# get dictionary onstartup
# import nltk
# nltk.download('punkt')
# nltk.download('stopwords')


root_dir="page"

# for loop goes here
while True:
    now = datetime.now()
    time_iter = now.strftime("%Y%m%d%H%M%S")
    time_iter_str = now.strftime("%Y/%m/%d, %H:%M:%S")

    my_api = twitter_obj()
    trends = my_api.get_us_trends()

    trend_dict = {}
    trend_url_dict={}

    for single_trend in trends[0]["trends"]:
        # print(single_trend)
        if single_trend['tweet_volume'] == None:
            pass
        else:
            tweet_volume = single_trend['tweet_volume']
            trend_dict[single_trend['name']] = tweet_volume
            trend_url_dict[single_trend['name']]=single_trend['url']

    os.makedirs( os.path.join(root_dir, "imgs", str(time_iter)))

    create_wordcloud_file_from_dict(trend_dict, os.path.join(root_dir, "imgs", str(time_iter),"trend_cloud.png"))

    trend_list = []
    for trend_key in trend_dict.keys():
        trend_list.append([trend_dict[trend_key],trend_key])
    trend_list.sort(reverse=True)
    trend_list=trend_list[:10]

    new_table = create_table_from_trend_dicts(time_iter,time_iter_str,trend_list,trend_url_dict,root_dir)
    # print(new_table)

    for trend_index,single_trend_obj in enumerate( trend_list):
        trend_name=single_trend_obj[1]
        statuses = my_api.get_dumps_for_topic(trend_name)

        # statuses = get_pickle('pickled_statuses.pkl')

        long_text = " ".join([single_status["text"] for single_status in statuses])

        text_word_dict = normalize_string_to_dict(long_text)

        image_path = os.path.join(root_dir,"imgs",str(time_iter),str(trend_index)+".png")
        print("creating "+os.path.normpath(image_path))
        create_wordcloud_file_from_dict(text_word_dict, os.path.normpath(image_path))

    append_table_to_index(root_dir,new_table)

    time.sleep(3600)
