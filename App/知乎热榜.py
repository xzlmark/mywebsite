import requests
from parsel import Selector


def get_anynew():
    url = 'https://www.anyknew.com/api/v1/sites/zhihu'
    response = requests.get(url)
    infos = response.json()
    for info in infos['data']['site']['subs']:
        for i in info['items']:
            print(i['iid'])
            print(f'https://www.anyknew.com/go/{i["iid"]}')


def get_banyuetan():
    url = 'http://www.banyuetan.org/'
    response = requests.get(url)
    sel = Selector(response.text)
    infos = sel.xpath('//div[@class="hot_tt"]/h3')
    title = infos.xpath('./a/text()').get()
    print(title)
    href = infos.xpath('./a/@href').get()
    print(href)


def get_people():
    url = 'http://opinion.people.com.cn/GB/8213/49160/49219/'
    response = requests.get(url)
    response.encoding='gb2312'
    sel = Selector(response.text)
    infos = sel.xpath('//td[@class="t10l14bl"]/a')
    for info in infos:
        title = info.xpath('./text()').get()
        print(title)
        href = 'http://opinion.people.com.cn'+info.xpath('./@href').get()
        print(href)


def get_xinhuawang():
    url = 'http://www.xinhuanet.com/'
    headers = {
        'user-agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36'
    }
    response = requests.get(url,headers=headers)
    response.encoding = 'utf-8'
    sel = Selector(response.text)
    infos = sel.xpath('//div[@id="hpart1"]//span[@id="syhistoryid"]/a')
    title = infos.xpath('./text()').get()
    href = infos.xpath('./@href').get()
    print(title)
    print(href)

if __name__ == '__main__':

    get_xinhuawang()
