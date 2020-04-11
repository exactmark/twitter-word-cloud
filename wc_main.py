import pickle
from twitter_api import twitter_obj

my_api = twitter_obj()
trends = my_api.get_us_trends()

print(my_api)
print()
print(trends)
print()

