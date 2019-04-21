from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup


def get_title(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        print(e)
        return None
    except URLError as e:
        print('The server could not be found!')
        return None
    else:
        try:
            print('It Worked!')
            bs = BeautifulSoup(html.read(), 'html.parser')
            h1 = bs.body.h1
            print(h1)
        except AttributeError as e:
            return None
        return h1


title = get_title('http://www.pythonscraping.com/pages/page1.html')
if title is None:
    print('Title could not be found')
else:
    print(title)

