from bs4 import BeautifulSoup
import requests 

# websites = "https://subslikescript.com/movie/Titanic-120338"
root = "https://subslikescript.com/"
websites = f"{root}movies_letter-A"
result = requests.get(websites)
context = result.text

soup = BeautifulSoup(context,"lxml")
pagination = soup.find("ul",class_="pagination")
all_items = pagination.find_all("li",class_="page-item")
pages =all_items[3].text
print(pages) 
for page in range(1,int(pages)):
    # https://subslikescript.com/movies_letter-A?page=1
    url = f"{root}movies_letter-A?page={page}"
    result = requests.get(url)
    context = result.text
    soup = BeautifulSoup(context,"lxml")
    box = soup.find("article",class_="main-article")
    links = box.find_all("a",href=True)
    for link in links:
        # https://subslikescript.com/movie/A_1000000000000000_Ransom-4926482
        try:
            website = root + link["href"]
            result = requests.get(website)
            context = result.text
            soup = BeautifulSoup(context,"lxml")
            box = soup.find("article",class_="main-article")
            title = box.find("h1").get_text()
            transcript = box.find("div",class_="full-script")
            with open(f"{title}.txt","w",encoding="utf-8") as file:
                file.write(transcript)
        except:
            pass
        
        # print(link["href"])
    

# print(links)

# print(all_items) 
# print(pagination)
# print(soup.prettify)
# box  = soup.find("article",class_="main-article")

# links = box.find_all("a",href=True)


# for link in links:
#     try:
#         website = root + link["href"]
#         results  = requests.get(website)
#         content = results.text
#         soup = BeautifulSoup(content,"lxml")
#         box = soup.find("article",class_="main-article")
#         title = box.find("h1").get_text()
#         transcript = box.find("div",class_="full-script").get_text()
#         with open(f"{title}.txt","w",encoding="utf-8") as file:
#             file.write(transcript)
#     except:
#         pass
