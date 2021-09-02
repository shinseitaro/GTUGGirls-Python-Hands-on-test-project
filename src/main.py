import time
import argparse
import download
import scraping


from requests_html import HTMLSession
from logzero import logger

def run():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--download', action="store_true",  help="ページをダウンロード")

    args = parser.parse_args()

    if args.download:
        logger.info("開店閉店情報を10ページダウンロードしてきます")
        pages = range(1, 11)
        session = HTMLSession()
        for i in pages:
        # 閉店URL
            url_close = f'https://kaiten-heiten.com/category/kantou_koushinetsu/tokyo/page/{i}/?s=%E3%80%90%E9%96%89%E5%BA%97%E3%80%91'
            # 開店URL
            url_open = f'https://kaiten-heiten.com/category/kantou_koushinetsu/tokyo/page/{i}/?s=%E3%80%90%E9%96%8B%E5%BA%97%E3%80%91'
            target = "download"
            overwrite = True
            download.downloader(session, url_close, target, overwrite)
            time.sleep(3)
            download.downloader(session, url_open, target, overwrite)
            time.sleep(3)

if __name__ == "__main__":
    run()
