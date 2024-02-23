from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium import webdriver
from textblob import TextBlob
from bs4 import BeautifulSoup
from datetime import datetime
import chromedriver_binary
from requests import get
import pandas as pd
import time, sys, re

class tweets:

    """
    Collects tweets of the social-media content in Twitter when hashtag is given.
    :param tweets: Unique identification keyword for every social-media tweets in Twitter.
    :returns: Returns all the tweets.
    """

    def __init__(self, keyword, ChromeOptions=None, BS4parser='lxml'):
        start_time = datetime.now()
        if ChromeOptions is not None:
            options = ChromeOptions
        else:
            options = Options()
        options.headless = True
        options=options
        browser = webdriver.Chrome(options=options)
        browser.get("https://twitter.com/search?q=" + keyword)

        while browser.find_element(By.TAG_NAME, 'div'):
            browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            time_delta = datetime.now() - start_time
            sys.stdout.write('\r' + str("calculating time") + "  " + str(time_delta.seconds) +  "  " + "seconds taken to parse all the tweets from twitter" + '\r')
            sys.stdout.flush()
            if time_delta.seconds >= 150:
                break

        soup = BeautifulSoup(browser.page_source, BS4parser)
        browser.quit()

        tweets_count = soup.select('.TweetTextSize')
        sys.stdout.write('\r' + "\n" + str("total tweets are") + " : " + str(len(tweets_count)) + '\r')
        sys.stdout.flush()

        analyser = SentimentIntensityAnalyzer()
        neu_sum, neg_sum, compound_sum, pos_sum, count = 0,0,0,0,0

        self.tweets = [' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", item.text).split()) for item in tweets_count]
        sentiment_score = [analyser.polarity_scores(self.tweets[i])['compound'] for i in range(len(self.tweets))]
        polarity_score = [analyser.polarity_scores(self.tweets[i]) for i in range(len(self.tweets))]

        sentiment = []
        for item in tweets_count:
            analysis = TextBlob(' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", item.text).split()))
            # set sentiment
            if analysis.sentiment.polarity > 0:
                sentiment.append('positive')
            elif analysis.sentiment.polarity == 0:
                sentiment.append('neutral')
            else:
                sentiment.append('negative')

        self.tweets_df = pd.DataFrame({'tweets' : self.tweets, 'sentiment' : sentiment, 'sentiment_score' : sentiment_score, 'polarity_scorce' : polarity_score})

        for i in range(len(self.tweets)):
            count += 1
            score = analyser.polarity_scores(self.tweets[i])
            neu_sum += score['neu']
            neg_sum += score['neg']
            pos_sum += score['pos']

        if count:
            self.final_sentiment_scores = {"neu" : round(neu_sum / count, 3), "neg" : round(neg_sum / count, 3), "pos" : round(pos_sum / count, 3), "compound" : round(compound_sum / count, 3)}
        else:
            self.final_sentiment_scores = None
