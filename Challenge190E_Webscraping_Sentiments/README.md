## Description

Webscraping is the delicate process of gathering information from a website (usually) without the assistance of an API. Without an API, it often involves finding what ID or CLASS a certain HTML element has and then targeting it. In our latest challenge, we'll need to do this (you're free to use an API, but, where's the fun in that!?) to find out the overall sentiment of a sample size of people.
We will be performing very basic sentiment analysis on a YouTube video of your choosing.

Your task is to scrape N (You decide but generally, the higher the sample, the more accurate) number of comments from a YouTube video of your choice and then analyse their sentiments based on a short list of happy/sad keywords
Analysis will be done by seeing how many Happy/Sad keywords are in each comment. If a comment contains more sad keywords than happy, then it can be deemed sad.
Here's a basic list of keywords for you to test against. I've ommited expletives to please all readers...
happy = ['love','loved','like','liked','awesome','amazing','good','great','excellent']
sad = ['hate','hated','dislike','disliked','awful','terrible','bad','painful','worst']
Feel free to share a bigger list of keywords if you find one. A larger one would be much appreciated if you can find one.

### Input
On console input, you should pass the URL of your video to be analysed.

### Output
The output should consist of a statement stating something along the lines of -
"From a sample size of" N "Persons. This sentence is mostly" [Happy|Sad] "It contained" X "amount of Happy keywords and" X "amount of sad keywords. The general feelings towards this video were" [Happy|Sad]