#-*- coding: utf-8 -*-
import requests
proxies = {
  "http":"http://0.10.1.10:3128",
  "http":"http://10.10.1.10:1080"
}
requests.get('http://example.org',proxies=proxies)