import requests

balance_url = "http://weixin.ccnu.edu.cn/App/weixin/CardInfoAjax"
detail_query_url = "http://weixin.ccnu.edu.cn/App/weixin/queryTrans"

def get_balance(sid):
    """
    get balance
    :param sid: student id
    :return: balance in json
    """
    headers = {
        "User-Agent" : "Mozilla/5.0 (iPhone; CPU iPhone OS 11_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E216 MicroMessenger/6.6.6 NetType/WIFI Language/zh_CN",
        "Cookie" : "wxqyuserid=%s" % sid,
    }

    r = requests.get(balance_url,headers=headers)
    return r.json()

def detail_query(sid,startTime,endTime):
    """
    校园卡流水明细
    :param sid: 学号
    :param startTime: 起始时间
    :param endTime: 结束时间
    :return: json  data
    """
    headers = {
        "User-Agent" : "Mozilla/5.0 (iPhone; CPU iPhone OS 11_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E216 MicroMessenger/6.6.6 NetType/WIFI Language/zh_CN",
        "Cookie": "wxqyuserid=%s" % sid,
    }
    params = {
        "page": 1,
        "pageSize": 200,
        "startTime": startTime,
        "endTime": endTime,
    }
    r = requests.get(detail_query_url, params=params, headers=headers)
    return r.json()

if __name__ == '__main__':
    print(get_balance(201621081))
    detail_query(2016210813,"2018-04-28","2018-05-03")
