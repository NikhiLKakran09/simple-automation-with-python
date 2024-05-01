
import requests
import webbrowser as web

topic = "romantic songs"
url = f"https://www.youtube.com/results?q={topic}"
count = 0
cont = requests.get(url)
data = cont.content
data = str(data)
lst = data.split('"')
for i in lst:
    count += 1
    #print(i)
    if i == "WEB_PAGE_TYPE_WATCH":
        break
if lst[count - 5] == "/results":
    raise Exception("No Video Found for this Topic!")
web.open(f"https://www.youtube.com{lst[count - 5]}")
