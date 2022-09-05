import http
import requests
from items import ArticleList
from items import Article


# 获取仓库的文章列表
def get_article_list(get_list_url, headers):
    response = requests.get(url=get_list_url, headers=headers)
    list = []
    if response.status_code == http.HTTPStatus.UNAUTHORIZED:
        raise Exception("错误的token, 请重试")
    elif response.status_code == http.HTTPStatus.NOT_FOUND:
        raise Exception("错误的仓库的唯一名称, 请重试")
    elif response.status_code == http.HTTPStatus.OK:
        content = response.json()
        data = content.get("data")

        for article in data:
            title = article.get("title")
            slug = article.get("slug")
            list.append(ArticleList(title, slug))
    else:
        raise Exception(response.text)
    return list


def get_article(get_article_url, headers):
    response = requests.get(url=get_article_url, headers=headers)
    content = response.json()
    data = content.get("data")
    title = data.get("title")
    body = data.get("body_html")
    if body== None:
        raise Exception("正文缺失")
    return Article(title, body)

def download_article(article):
    with open(article.title+".html",'w',encoding='utf-8') as fp:
        fp.write(article.body)

def main():
    base_url = "https://www.yuque.com/api/v2/repos/"
    namespace = input("请输入仓库的唯一名称（例：yuque/developer）：")
    token = input("请输入token（在语雀的账号设置页面获取）：")

    get_list_url = base_url + namespace + "/docs"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36',
        'X-Auth-Token': token
    }
    list = get_article_list(get_list_url, headers)
    for item in list:
        get_article_url = get_list_url + "/" + item.slug
        article = get_article(get_article_url,headers)
        download_article(article)


if __name__ == '__main__':
    main()
