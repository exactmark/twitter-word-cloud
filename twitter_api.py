import twitter
import json
from pickle_api import store_pickle


# Modified from https://github.com/mikhailklassen/Mining-the-Social-Web-3rd-Edition
class twitter_obj():

    def __init__(self):
        from auth import OAUTH_TOKEN_SECRET, OAUTH_TOKEN, CONSUMER_SECRET, CONSUMER_KEY

        auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET,
                                   CONSUMER_KEY, CONSUMER_SECRET)

        self.twitter_api = twitter.Twitter(auth=auth)

    def get_us_trends(self):
        US_WOE_ID = 23424977
        return self.get_region_trends(US_WOE_ID)

    def get_world_trends(self):
        WORLD_WOE_ID = 1
        return self.get_region_trends(WORLD_WOE_ID)

    def get_region_trends(self, region_id):
        trends = self.twitter_api.trends.place(_id=region_id)
        # for trend in trends[0]['trends']:
        #     print(trend['name'])
        return trends

    def get_dumps_for_topic(self,topic,count_arg=100):
        q = topic
        count = count_arg
        
        # Import unquote to prevent url encoding errors in next_results
        from urllib.parse import unquote
        
        # See https://dev.twitter.com/rest/reference/get/search/tweets
        
        search_results = self.twitter_api.search.tweets(q=q, count=count)
        
        statuses = search_results['statuses']
        
        
        # Iterate through 5 more batches of results by following the cursor
        for _ in range(5):
            # print('Length of statuses', len(statuses))
            try:
                next_results = search_results['search_metadata']['next_results']
            except KeyError as e: # No more results when next_results doesn't exist
                break
                
            # Create a dictionary from next_results, which has the following form:
            # ?max_id=847960489447628799&q=%23RIPSelena&count=100&include_entities=1
            kwargs = dict([ kv.split('=') for kv in unquote(next_results[1:]).split("&") ])
            
            search_results = self.twitter_api.search.tweets(**kwargs)
            statuses += search_results['statuses']

        return statuses
        # store_pickle(statuses, "pickled_statuses.pkl")
