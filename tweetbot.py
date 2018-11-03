#!/usr/bin/python2.7
# encoding: utf-8

import tweepy

# Autenticação

cons_key = 'consumer_key_numbers'
cons_sec = 'consumer_key_secret'
acc_token = 'access_token_numers'
token_sec = 'access_token_secret'

auth = tweepy.OAuthHandler(cons_key, cons_sec)
auth.set_access_token(acc_token, token_sec)
api = tweepy.API(auth)

user = api.me()
print(user.name)

#Envia um tweet
#api.update_status('Testing Tweepy Lib')


# Pesquisa por Tweets e Retweeta a partir de duas variaveis
def main():
	search = ("Cyberpunk art", "Photo")
	
	numerotweets = 5
	for tweet in tweepy.Cursor(api.search, search).items(numerotweets):
		try:
			tweet.retweet()
			print("Tweet Retweeted!")
		except tweepy.TweepError as e:
			print(e.reason)
		except StopIteration:
			break
main()
