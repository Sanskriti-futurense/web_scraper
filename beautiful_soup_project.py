import bs4
import requests
from bs4 import BeautifulSoup
import pandas as pd
from requests.api import head
import csv

page = requests.get("https://market.todaypricerates.com/Pakur-vegetables-price-in-Jharkhand")
# print(page.text)
headers=[]
fillings = []

soup = BeautifulSoup(page._content, "html.parser")
results = soup.find("div", {"class":"Table"})
# print(results.prettify())
headers = [header.text for header in results.find("div", class_="Heading").find_all("div", class_="Cellth")]
# print(headers)
for th in results.find_all("div", class_="Row"):
#     veg_elements = results.find("div", class_="Heading").find_all("div", class_="Cellth")
#     headers.append(",".join(th.text.strip().split()))
#     rows = results.find("div", class_="Row").find_all("div", class_="Cell")
      fillings.append([val.text for val in th.find_all("div", class_="Cell")])

with open('D:\output_file(1).csv', 'w', encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    writer.writerows(th for th in fillings if th)
# print(fillings)
# pd.DataFrame([fillings], columns=[headers]).to_csv(r"D:\new_veg_elts(3).csv")