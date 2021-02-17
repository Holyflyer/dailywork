# -*- coding: utf-8 -*-

import requests
import time

#userAgent = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
userAgent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36"
header = {
    "origin": "https://pt.m-team.cc",
    "Referer": "https://pt.m-team.cc/login.php",
    'User-Agent': userAgent,
}

def mteamLogin(account, password):
    # 模仿 登录
    print ("开始模拟登录M-TEAM")
    
    postUrl = "https://pt.m-team.cc/takelogin.php"
    postData = {
        "username": account,
        "password": password,
    }
    responseRes = requests.post(postUrl, data = postData, headers = header)
    # 无论是否登录成功，状态码一般都是 statusCode = 200
    print(f"statusCode = {responseRes.status_code}")
    print(f"text = {responseRes.text}")
    time.sleep(10)

if __name__ == "__main__":
    # 从返回结果来看，有登录成功
    mteamLogin("my_username", "my_password")

