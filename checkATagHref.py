import requests
from selenium import webdriver

driver=webdriver.Chrome(executable_path='INSERT chromedriver.exe PATH')

def checkATagHrefs(page):
    driver.get(page)
    atags = driver.find_elements_by_tag_name('a')
    hrefvalues = list(map(lambda atag: atag.get_attribute('href'), atags))

    links = []
    linksCount = []

    for href in hrefvalues:
        if href not in links:
            links += [href]
            linksCount += [[href,hrefvalues.count(href)]]
    print("--------------------------")
    print("testing:",page)
    for link in linksCount:
        try:
            r = requests.head(link[0])
            if r.status_code >= 400:
                print(link[0], r.status_code, " x", link[1])
        except:
            print(link)
    

pages = ["https://www.google.it/","https://www.python.org/"]

for page in pages:
    checkATagHrefs(page)
print("---END---")
