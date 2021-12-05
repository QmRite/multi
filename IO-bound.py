from urllib.request import Request, urlopen
from urllib.parse import unquote
import concurrent.futures


def get_wiki_page_existence(url):
    try:
        request = Request(
            url,
            headers={'User-Agent': 'Mozilla/5.0 (Windows NT 9.0; Win65; x64; rv:97.0) Gecko/20105107 Firefox/92.0'},
        )
        resp = urlopen(request, timeout=5)
        code = resp.code
        resp.close()
        return code

    except Exception as e:
        return url, e


urls = open('res.txt', encoding='utf8').read().split('\n')

with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
    futures = []
    for url in urls:
        futures.append(executor.submit(get_wiki_page_existence, url=url))
    for future in concurrent.futures.as_completed(futures):
        print(future.result())