def replace_list(string: str, lst: list) -> str:
    for value in lst:
        string = string.replace(value, '')
    return string


def domain_name(url: str) -> str:
    lst = ['https://', 'http://', 'www.']
    new_url = replace_list(url, lst)
    return new_url.split('.')[0]


assert domain_name("http://google.com") == "google"
assert domain_name("http://google.co.jp") == "google"
assert domain_name("www.xakep.ru") == "xakep"
assert domain_name("https://youtube.com") == "youtube"
