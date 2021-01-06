# Sentiment-Analysis-Hackathon

This was built for the [2020 Hack.GT Hackathon](https://2020.hack.gt/) and is meant to run sentiment analysis on twitter tweets
To run this install the modules and run main.py then open the HTML file in your browser of choice also add your api keys

## Inspiration
Getting a constant stream of thoughts from people is now possible with Twitter’s API and to process them automatically is not very hard so I thought, why not put them together. We used this "thought processing" to analyze how people thought about Donald Trump and Joe Biden (as there is an election coming very soon)

## What it does
This takes in a live stream of tweets that have the key words "Trump" or "Biden" in them and will analyze them to see if they are positive or negative then it will aggregate all this information and display it in an easy to understand way. It also can analyze this data LIVE.

## How We Built it
We Built this using the Tweepy API, a twitter API wrapper, the textblob python package to analyze the tweets and the leaflet.js package to display the data aggregated live.

## Challenges we ran into
Our original plan was to program a bot that analyzed tweets to buy and sell stocks based on if they had a good sentiment or a bad one (good or bad vibes), but we had a issue which was that the markets were closed and we couldn't test out our bot which took us too long to realize. So then we pivoted and decided to made a program that could give data about candidates perception and favorability faster than any poll could, with in one or two seconds any tweet about Joe Biden or Donald Trump would be analyzed giving a sentiment value and categorized then displayed to a user giving live useful data about a candidate.

## Accomplishments that we're proud of
We are proud that we got the thing running and functional. We are also proud that we have it all running live and that this program could be useful to anyone who wants to know the current political standing of a candidate.

## What we learned
That you can't make a Stock Market trading bot on the weekend and that even if your idea doesn't work that doesnt mean its a waste of time and you can always make something cool out of it.

## What's next for Sentiment Analysis Hackathon
We are hoping to run this during a debate to see the live perception of people change as candidates talk, We also hope to see this used in other applications or for people who just want to see how the candidates stand in each state in an unconventional form that would still give them useful information.
