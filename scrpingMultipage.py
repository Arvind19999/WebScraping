from bs4 import BeautifulSoup
import requests 

# websites = "https://subslikescript.com/movie/Titanic-120338"
root = "https://subslikescript.com/"
websites = f"{root}movies"
result = requests.get(websites)
context = result.text

soup = BeautifulSoup(context,"lxml")


box  = soup.find("article",class_="main-article")

links = box.find_all("a",href=True)


for link in links:
    try:
        website = root + link["href"]
        results  = requests.get(website)
        content = results.text
        soup = BeautifulSoup(content,"lxml")
        box = soup.find("article",class_="main-article")
        title = box.find("h1").get_text()
        transcript = box.find("div",class_="full-script").get_text()
        with open(f"{title}.txt","w",encoding="utf-8") as file:
            file.write(transcript)
    except:
        pass
