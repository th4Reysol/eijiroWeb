from bs4 import BeautifulSoup
import os
import requests
import csv 

csvPath="computer_terms.csv"
url = "https://eow.alc.co.jp/lbl_com.html"
getUrl = requests.get(url)
getUrl.encoding = getUrl.apparent_encoding
getText = BeautifulSoup(getUrl.content, "html.parser")

ensligh_words =[word.get_text() for word in getText.select("ul.words>li>a")]

with open(csvPath, "w", newline='')as f:
    for word in ensligh_words:
        f.write(word+'\n')



