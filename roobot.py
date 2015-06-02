import tweepy, time, sys
#enter the corresponding information from your Twitter application:
CONSUMER_KEY = '0KwR0AuLS5TS5IIHISd5TKS2P'#keep the quotes, replace this with your consumer key
CONSUMER_SECRET = 'TohC48AtQubiLpcf2gvaPaPLKF8sD9iRrzEo1VaqrYhGSoXPQF'#keep the quotes, replace this with your consumer secret key
ACCESS_KEY = '2920410575-6aP8zpZ13VINsRRhE18Nra66uNVPr9uw5cMzGNz'#keep the quotes, replace this with your access token
ACCESS_SECRET = '4VyvKt2zcshY2AgonGz08qlxqd9lTh0MuKuyXG57byx2x'#keep the quotes, replace this with your access token secret
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

last_retweet = 1;
last_mention = 1;
#gather the initial tweets, and find the most recent and retweet
statuses = api.home_timeline(count = 5);
mentions = api.mentions_timeline(count = 1);
#    print "id: %s\n" % status.id
for status in statuses:
    try:
        api.retweet(status.id);
    except tweepy.TweepError:
        break;
    last_retweet = max(status.id,last_retweet);
#retweets all new mentions
for mention in mentions:
    try:
        api.retweet(mention.id);
    except tweepy.TweepError:
        break;
    last_mention = max(mention.id,last_mention);

#pause for a minute
time.sleep(60);
#loop that will keep running, after initial start up to continue reading tweets
while True :
    print "start of loop\n\n\n"
    statuses = api.home_timeline(since_id = last_retweet);
    mentions = api.mentions_timeline(since_id = last_mention);
    #retweet and set last_retweet to most recent status id for all new statuses
    for status in statuses:
        try:
            api.retweet(status.id);
            break;
        except tweepy.TweepError:
            break;
        last_retweet = max(status.id,last_retweet);

    for mention in mentions:
        try:
            api.retweet(mention.id);
        except tweepy.TweepError:
            break;
        last_mention = max(mention.id,last_mention);

    #sleep for one minute so not to make too many timeline requests
    #max is 15 per minute    
    time.sleep(61);
    



print "%s\n" % api.rate_limit_status();




