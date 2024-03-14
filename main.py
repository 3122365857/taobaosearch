import js2py
import requests as rq
url = "https://h5api.m.taobao.com/h5/mtop.relationrecommend.wirelessrecommend.recommend/2.0/"
cookie2 = "" # cookie2
token = "" #_m_h5_tk
t = token.split("_")[0]
token_enc = ""#_m_h5_tk_enc
sgcookie = ""# sgcookie
data = {
    "jsv": "2.6.2",
    "appKey": "12574478",
    "api": "mtop.relationrecommend.WirelessRecommend.recommend",
    "v": "2.0",
    "type": "jsonp",
    "dataType": "jsonp",
    "callback": "mtopjsonp2"
}
x5sec="" #读取过量数据后需要验证码，手动输入后即可
headers = {
    "Cookie": "cookie2={}; _m_h5_tk={}; _m_h5_tk_enc={};sgcookie={}; x5sec={}".format(cookie2, token, token_enc, sgcookie,x5sec),
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/124.0",

}
import tqdm
import time

i = 1
context = js2py.EvalJs()
with open("taobao.js", 'r', encoding="utf-8") as f:
    js = f.read()
context.execute(js)
start_page = 1
end_page = 100
with tqdm.tqdm(total=end_page-start_page+1) as pbar:
    for i in range(start_page, end_page+1):
        result = context.exec("篮球鞋", t, i, 12574478)
        data["data"] = result["data"]
        data["t"] = result["time"]
        data["sign"] = result["sign"]
        response = rq.get(url, headers=headers, params=data)
        with open(f"data/{i}.json", 'w') as f:
            f.write(response.text[12:-1])
        if "FAIL_SYS_USER_VALIDATE" in response.text:
            print("需要验证码")
            x5sec = input("输入x5sec")
            headers = {
                "Cookie": "cookie2={}; _m_h5_tk={}; _m_h5_tk_enc={};sgcookie={}; x5sec={}".format(cookie2, token,
                                                                                                  token_enc, sgcookie,
                                                                                                  x5sec),
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/124.0",

            }
        pbar.update(1)
        time.sleep(5)

