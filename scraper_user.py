from tabulate import tabulate;
import requests;
from bs4 import BeautifulSoup;

URL = "https://scholar.google.com/citations?user=hm57p1wAAAAJ&hl=en";

page = requests.get(URL);

soup = BeautifulSoup(page.text, "html.parser");

job_elements = soup.find_all("td", class_="gsc_rsb_std");

print(job_elements[2].text)

table = soup.find(id="gsc_rsb_st")

table_head = table.find("thead");

table_head_tr = table_head.find("tr")

table_head_ths = table_head_tr.findAll("th")

table_head_out = []
for head_th in table_head_ths:
    table_head_out.append(head_th.text)

table_body = table.find("tbody");

table_trs = table_body.find_all("tr")

all_table = []

for tr in table_trs:
    table_tds = tr.findAll("td")
    row = [];
    for td in table_tds:
        row.append(td.text)
    all_table.append(row)

print(tabulate(all_table, table_head_out))