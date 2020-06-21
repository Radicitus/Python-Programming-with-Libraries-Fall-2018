import twitter
import re
import geocoder
import time
import json
from datetime import datetime, timedelta

with open('credentials.json', 'r') as credentials_file:
    credentials = json.load(credentials_file)

api = twitter.Api(consumer_key=credentials['CONSUMER_KEY'],
                  consumer_secret=credentials['CONSUMER_SECRET'],
                  access_token_key=credentials['ACCESS_TOKEN'],
                  access_token_secret=credentials['ACCESS_TOKEN_SECRET'],
                  tweet_mode='extended',
                  sleep_on_rate_limit=False)


def filterTimeline(kw):
    keyword = kw.lower()
    result = api.GetHomeTimeline(exclude_replies=True)
    tweets = [s.full_text for s in result]
    for tweet in tweets:
        try:
            word_list = re.sub("[^\w]", " ", tweet).split()
            for word in word_list:
                word_lower = word.lower()
                if word_lower == keyword:
                    raise Exception
            print(tweet + "\n")
        except:
            continue


def commonWord(username):
    real_user_name = api.GetUser(screen_name=username).screen_name
    sw = (real_user_name, username.lower(), 'u', 'co', 'all', 'just', 'being', 'over', 'both', 'through', 'yourselves', 'its', 'before', 'herself', 'had', 'should', 'to', 'only', 'under', 'ours', 'has', 'do', 'them', 'his', 'very', 'they', 'not', 'during', 'now', 'him', 'nor', 'did', 'this', 'she', 'each', 'further', 'where', 'few', 'because', 'doing', 'some', 'are', 'our', 'ourselves', 'out', 'what', 'for', 'while', 'does', 'above', 'between', 't', 'be', 'we', 'who', 'were', 'here', 'hers', 'by', 'on', 'about', 'of', 'against', 's', 'or', 'own', 'into', 'yourself', 'down', 'your', 'from', 'her', 'their', 'there', 'been', 'whom', 'too', 'themselves', 'was', 'until', 'more', 'himself', 'that', 'but', 'don', 'with', 'than', 'those', 'he', 'me', 'myself', 'these', 'up', 'will', 'below', 'can', 'theirs', 'my', 'and', 'then', 'is', 'am', 'it', 'an', 'as', 'itself', 'at', 'have', 'in', 'any', 'if', 'again', 'no', 'when', 'same', 'how', 'other', 'which', 'you', 'after', 'most', 'such', 'why', 'a', 'off', 'i', 'yours', 'so', 'the', 'having', 'once', 'https')
    tweet_id = None
    list_spaces = []
    for i in range(10):
        stream = api.GetUserTimeline(screen_name=username,
                                     count=200,
                                     include_rts=False,
                                     exclude_replies=True,
                                     max_id=tweet_id)
        list_spaces.extend([s.full_text for s in stream])
        tweet_id = stream[len(stream) - 1].id_str
    list_no_spaces = []
    for string in list_spaces:
        word_list = re.sub("[^\w]", " ", string).split()
        list_no_spaces.extend([word.lower() for word in word_list])
    final_list = []
    for word in list_no_spaces:
        if word not in sw and not word.isnumeric():
            final_list.append(word)
    final_count = 0
    final_word = ""
    for word in final_list:
        count = 0
        is_word = word
        for run in final_list:
            if run == word:
                count += 1
        if count > final_count:
            final_count = count
            final_word = is_word
    return final_word


def searchArea(kw, location=geocoder.ip('me')):
    start = time.strftime("%m/%d/%Y")
    start = datetime.strptime(start, "%m/%d/%Y")
    date = str(start - timedelta(days=7))
    keyword = kw.lower()
    g = geocoder.mapquest(location, key=credentials['MapquestKey'])
    current_location = str(g.latlng[0]) + "," + str(g.latlng[1])
    count = 0
    tweets = []
    last_tweet_id = None
    more_tweets = True
    check_tweet_id = '69'
    while more_tweets:
        try:
            tweets_to_add = api.GetSearch(geocode=(current_location + ",5mi"),
                                          since=date[:10],
                                          include_entities=False,
                                          count=100,
                                          max_id=last_tweet_id)
            last_tweet_id = tweets_to_add[len(tweets_to_add) - 1].id_str
            if check_tweet_id == last_tweet_id:
                raise Exception
            list_add = [s.full_text for s in tweets_to_add]
            for tweet in list_add:
                word_list = re.sub("[^\w]", " ", tweet).split()
                for word in word_list:
                    word_check = word.lower()
                    if word_check == keyword:
                        count += 1
                        break
                tweets.append(tweet)
            check_tweet_id = last_tweet_id
        except:
            more_tweets = False
    return count
