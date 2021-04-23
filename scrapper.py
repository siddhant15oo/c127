from selenium import webdriver
from bs4 import BeautifulSoup
import csv
import time


startURL='https://exoplanets.nasa.gov/discovery/exoplanet-catalog/'

browser=webdriver.Chrome('/Users/jaiagnani/sidds/web scraping/chromedriver')
browser.get(startURL)
time.sleep(15)

def scrape():
    headers=['Name','LightYearsFromEarth',"PlanetMass",'StellarMagnitude','Discovery_Date']
    planetdata=[]