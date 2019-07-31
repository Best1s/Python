import requests
r = requests.get("http://120.78.133.37:8080/login")
#print(r.content)
#print(r.text)
#r = chardet.detect(r.content)

print(r.status_code)
print(r.headers)
print(r.headers.get('content-type'))
print(r.headers['content-type'])