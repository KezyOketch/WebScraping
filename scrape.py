import requests
from bs4 import BeautifulSoup
from collections import deque
import datetime

visited = set(["http://mentalfloss.com/article/53792/17-ancient-abandoned-websites-still-work"])
dq = deque([["http://mentalfloss.com/article/53792/17-ancient-abandoned-websites-still-work", "", 0]])
max_depth = 2
i = 0
urlfile = open("index.txt", "w+")

while dq:
    base, path, depth = dq.popleft()
    #                         ^^^^ removing "left" makes this a DFS (stack)

    if depth < max_depth:
        try:
            soup = BeautifulSoup(requests.get(base + path).text, "html.parser")

            for link in soup.find_all("a"):
                href = link.get("href")

                if href not in visited:
                    visited.add(href)
                    if href.startswith("http"):
                        ts = datetime.datetime.now()
                        ts.strftime("%m/%d/%Y")
                        line = str(i) + ".html " + str(ts) + " " + href + "\n"
                        urlfile.write(line)
                        i += 1 

                    if href.startswith("http"):
                        dq.append([href, "", depth + 1])
                    else:
                        dq.append([base, href, depth + 1])
                        
        except:
            pass

urlfile.close()
