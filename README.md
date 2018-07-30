# card_service

## 查询余额
|URL|Header|Method|
| --- | -- | -- |
|/api/card/balance/ | None| GET|

**URL Params:**
```
   sid : string // 学号
```

**POST Data: None**

**RETURN Data:**
```
{
    "model": {
        "balance": "5.16",
        "consumeTotal": "228",
        "dataSum": "41",
        "deptName": "",
        "img": "",
        "name": "",
        "smtDealdatetimeTxt": "2018-07-15 07:08:34",
        "userId": ""
    },
    "msg": "",
    "result": true
}
```

**Status Code :**
```
200 // 成功
404 // 学号不正确
```

***

## 查询流水
|URL|Header|Method|
| --- | -- | -- |
|/api/card/account/| None| GET|

**URL Params:**
```
    sid : string // 学号
    startTime : string  // 这种格式 2018-04-28
    endTime : string
```

**POST Data: None**

**RETURN Data:**
```
{
    "list": [
        {
            "data": [
                {
                    "date": "04月28日",
                    "smtDealDateTimeTxt": "2018-04-28 11:47:18",
                    "smtDealName": "消费",
                    "smtInMoney": "181.2",
                    "smtOrgName": "黄焖鸡米饭",
                    "smtOutMoney": "169.2",
                    "smtTransMoney": "12.0",
                    "time": "11:47"
                },
                {
                    "date": "04月28日",
                    "smtDealDateTimeTxt": "2018-04-28 07:46:13",
                    "smtDealName": "消费",
                    "smtInMoney": "192.4",
                    "smtOrgName": "二楼",
                    "smtOutMoney": "181.2",
                    "smtTransMoney": "11.2",
                    "time": "07:46"
                }
            ],
            "title": "2018-04"
        }
    ],
    "msg": "",
    "result": true
}
```

**Status Code :**
```
200 // 成功
404 // 时间格式错误，不存在
```

