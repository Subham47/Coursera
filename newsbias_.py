from textblob import TextBlob

def csv_reader(filename):
    news=[]
    file=open(filename,encoding="utf8")
    for row in file:
        news.append(row)
    file.close()
    return news

def rating_each_row(news):
    for i in range(len(news)):
        edu=TextBlob(news[i])
        x=edu.sentiment.polarity
        if x<0:
            news[i]+"left"
        elif x==0:
            news[i]+"neutral"
        elif x>0 and x<=1:
            news[i]+"right"

def print():
    for i in range(len(news)):
        print(news[i])

def main_loop():
    news=csv_reader("data1.csv")
    rating_each_row(news)
    print()

if __name__=='__main__':
    main_loop()