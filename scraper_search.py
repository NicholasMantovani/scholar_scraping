from tabulate import tabulate;
import requests;
from bs4 import BeautifulSoup;

URL = "https://scholar.google.com/citations?view_op=search_authors&mauthors=dick";

page = requests.get(URL);

soup = BeautifulSoup(page.text, "html.parser");

profiles = soup.find(id="gsc_sa_ccl");

list_profiles = profiles.findAll("div", class_="gsc_1usr")

class Profile:
    def __init__(self, name, desc, email, citato):
        self.name = name
        self.desc = desc
        self.email = email
        self.citato = citato
    def __repr__(self) -> str: return str(" " + self.name) + str(" " + self.desc) + str(" " + self.email) + str(" " + self.citato) 

profiles = [];

for profile in list_profiles:
    name = profile.find("h3", class_="gs_ai_name").text
    desc = profile.find("div", class_="gs_ai_aff").text
    email = profile.find("div", class_="gs_ai_eml").text
    citato = profile.find("div", class_="gs_ai_cby").text
    profiles.append({"name": name, "desc": desc, "email": email, "citato": citato })

print(profiles)