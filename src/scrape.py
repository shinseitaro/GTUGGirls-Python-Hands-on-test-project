import glob
from bs4 import BeautifulSoup


def get_details(soup ):
    """
    soup: soup.select_one("article") もしくは、soup.select("article")[0] を想定
    """
    soup_a = soup.select_one("a")
    name = soup_a.get("title")
    post_time = soup_a.select_one("span.post_time").get_text()
    url = soup_a.get("href")
    category = soup_a.select_one("span.post_cat").get_text()

    category_tag = [cat for cat in  soup.get("class") if cat.find("category") > -1]# 

    return {
        "name":name, 
        "post_time":post_time,
        "url":url,
        "category":category,
        "category_tag":category_tag,}


def fetch_all(soup):
    articles = soup.select("article")
    return [get_details(article) for article in articles]
        


if __name__ == '__main__':
    fname = "download/【閉店】/_category_kantou_koushinetsu_tokyo_page_1_.html"
    html = open(fname).read()
    soup = BeautifulSoup(html, 'html.parser')

    print(fetch_all(soup))