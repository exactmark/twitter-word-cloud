import twitter


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
        for trend in trends[0]['trends']:
            print(trend['name'])
        return trends
