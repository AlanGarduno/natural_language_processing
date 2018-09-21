import write
from bs4   import BeautifulSoup
import re

def split_into_articles(fname):
    f = open(fname,'r',encoding='UTF-8')
    text = f.read()
    f.close()
    text = text.replace('\x97', '')

    articles = re.split('<h3>', text)
    arts = []
    for article in articles:
        soup = BeautifulSoup(article,'lxml')
        text = soup.get_text()
        text = text.replace('\x97', '')
        arts.append(text)
    return arts

def main():
    arts = split_into_articles('e960401.html')
    articles = arts[1:]
    print(len(arts))
    write.writeList(articles, 'articles.txt')

if __name__ == '__main__':
    main()