from .spider import get_balance, detail_query
from flask import Flask
from flask import jsonify, request

app = Flask(__name__)


@app.route("/api/card/balance/",methods=['GET'])
def balance():
    """
    获取账户余额
    :return:
    """
    sid = request.args.get('sid')
    r = get_balance(sid)
    if r['result'] != True:
        return jsonify({
            'msg' : '一卡通不存在！',
        }), 404

    return jsonify(r), 200


@app.route("/api/card/account/",methods=['GET'])
def account():
    """
    获取流水账单
    :return:
    """
    sid = request.args.get('sid')
    start = request.args.get('startTime')
    end = request.args.get('endTime')
    r = detail_query(sid,start,end)
    if r['result'] != True:
        return jsonify({
            'msg' : '该字符串未被识别为有效的 DateTime。',
        }), 404
    return jsonify(r), 200
