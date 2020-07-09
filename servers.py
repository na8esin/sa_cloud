# HTTP通信を行うための標準ライブラリ
import urllib.request
import os
import json
# Base64を扱うための標準ライブラリ
import base64

def server_ids(zone):
    # 送信先のURL
    url = 'https://secure.sakura.ad.jp/cloud/zone/'
    url += zone+'/api/cloud/1.1/server/'
    data = get_sacloud_response(url)
    serverids = []
    for server in json.loads(data)['Servers']:
        serverids.append(server['ID'])

    return serverids

def get_sacloud_response(url, method="GET"):
    # Basic認証の情報
    user = os.environ['SAKURACLOUD_ACCESS_TOKEN']
    password = os.environ['SAKURACLOUD_ACCESS_TOKEN_SECRET']

    # Basic認証用の文字列を作成.
    basic_user_and_pasword = base64.b64encode(
                                '{}:{}'.format(user, password).encode('utf-8'))

    # Basic認証付きの、GETリクエストを作成する.
    request = urllib.request.Request(url, 
        headers={
            "Authorization": "Basic " + basic_user_and_pasword.decode('utf-8')},
        method=method)

    # 送信して、レスポンスを受け取る.
    with urllib.request.urlopen(request) as res:
        data = res.read()

    return data


