import requests

site = "https://wafflesshop.herokuapp.com/"
cookies = {"flavour": "7499aced43869b27f505701e4edc737f0cc346add1240d4ba86fbfa251e0fc35"}


def fuzzer():
    initial_arr = []

    return ['img', 'order']


items = fuzzer()
for i in items:
    path = site + i
    r = requests.get(path, cookies=cookies)
    if r.status_code != 404:
        print(path)


# print(r.status_code)
# print(r.content)
