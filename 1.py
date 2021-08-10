from urllib.request import urlopen

from lxml import etree

with open("data.txt", "r") as f:
    lines = f.read().splitlines()

with open("otus.txt", "a+") as file:
    for index, line in enumerate(lines):
        try:
            lnk = f"https://www.blockchain.com/ru/btc/tx/{line}"
            response = urlopen(lnk)
            tree = etree.parse(response, etree.HTMLParser())
            d = tree.xpath('//*[@id="__next"]/div[3]/div/div[4]/div/div/div[2]/div/div[10]/div[2]/span')
            file.write(f"{line} {d[0].text}\n")
            print(index)
        except Exception:
            file.write(f"{line} error\n")
