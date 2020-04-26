from pickle_api import get_pickle
import os

def get_data_from_archive(root_dir, date_time_string):

    pickled_folder = os.path.join(root_dir, "data", date_time_string)
    file_list = os.listdir(pickled_folder)

    for single_file in file_list:
        try:
            if single_file.startswith("trends"):
                trends = get_pickle(os.path.join(pickled_folder, single_file))
        except:
            pass

    trend_dict = {}
    for single_trend in trends[0]["trends"]:
        if single_trend['tweet_volume'] == None:
            pass
        else:
            tweet_volume = single_trend['tweet_volume']
            trend_dict[single_trend['name']] = tweet_volume

    trend_map = []
    for trend_key in trend_dict.keys():
        trend_map.append([trend_dict[trend_key], trend_key])
    trend_map.sort(reverse=True)
    status_dict = {}

    for i_num, _ in enumerate(trend_map):
        try:
            status_dict[i_num] = get_pickle(os.path.join(pickled_folder, "statuses." + str(i_num) + ".pkl"))
        except:
            pass

    return trends, trend_map, status_dict
