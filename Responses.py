from datetime import  datetime
from gnewsclient import  gnewsclient
from textblob import  TextBlob

def sample_responses(input_text):
    user_message = str(input_text.lower())
    pol = TextBlob(user_message).sentiment.polarity

    if user_message in ("hello","hi","sup"):
        return "Hey! How is it going"

    if user_message in ("who are you","how are you?","who?"):
        return "I am Aman Bot"

    if user_message in ("time","time?"):
        now = datetime.now()
        date_time = now.strftime("%d/%m/%y, %H:%M")
        return str(date_time)

    if user_message in ("new","new?"):
        client = gnewsclient.NewsClient(language='english',
                                        location='india',
                                        topic='sports',
                                        max_results=3)

        news_list = client.get_news()
        news_1 = " "
        count = 1
        for item in news_list:
            news_1 = news_1 + str(count) + ". "
            news_1 = news_1 + item['title'] + "\n"
            count = count + 1
        return str(news_1)
    if pol<0:
        return "Sorru No offensive language !!"
    return "I dont get you !!"
