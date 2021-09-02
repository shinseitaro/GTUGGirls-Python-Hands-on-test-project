import time
import sys
import os
import random

from requests_html import HTMLSession
from yarl import URL
from logzero import logger


def downloader(session, url, target, overwrite):
    r = session.get(url)
    if r.status_code !=200:
        logger.error(f"GET {url} return {r.status_code}")
        return 0
    else:    
        query = URL(url).query['s'] 
        path = URL(url).path.replace("/", "_") + ".html"
        dirname = os.path.join(target, query)
        if not os.path.exists(dirname):
            os.makedirs(dirname)
        html = os.path.join(dirname, path)
        if (os.path.exists(html) and overwrite) or (not os.path.exists(html)):
            try:
                r = session.get(url)
                with open(html, 'wb') as fout:
                    fout.write(r.content)
                    logger.info(f"SUCCESSFULLY DOWNLOWD: {url}, {html}")
                return 1 
            except:
                logger.error(f"ERROR: {sys.exc_info()}")
                return 0 


if __name__ == '__main__':

    session = HTMLSession()
    pages = range(1, 103) #56
    for i in pages:
        #閉店URL
        #url = f'https://kaiten-heiten.com/category/kantou_koushinetsu/tokyo/page/{i}/?s=%E3%80%90%E9%96%89%E5%BA%97%E3%80%91'
        #開店URL
        url = f'https://kaiten-heiten.com/category/kantou_koushinetsu/tokyo/page/{i}/?s=%E3%80%90%E9%96%8B%E5%BA%97%E3%80%91'
        target = "download"
        overwrite = True
        downloader(session, url, target, overwrite)
        time.sleep(random.randint(2,4))
       
        

        



