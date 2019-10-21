import requests
from bs4 import BeautifulSoup
from collections import deque
import datetime

visited = set(["http://toscrape.com/"])
#Queue with seed set
dq = deque([["http://toscrape.com/", "", 0]])
#["http://mentalfloss.com/article/53792/17-ancient-abandoned-websites-still-work", "", 0], ["http://www.fabpedigree.com/james/mathmen.htm", "", 0], ["http://scratchpads.eu/explore/sites-list", "", 0]])

#Maximum depth to go through
max_depth = 2

#Index tracker
i = 0

#File that holds the list of the URL mapping
urlfile = open("index.txt", "w+")

while dq:

    #The Queue to implement the depth first search
    base, path, depth = dq.popleft()

    
    if depth < max_depth:
        try:
            soup = BeautifulSoup(requests.get(base + path).text, "html.parser")

            for link in soup.find_all("a"):
                
                #Get the "href"s from the html code
                href = link.get("href")

                #If the link had not been visited
                if href not in visited:
                    #Add the link to the visited list
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

            #Print html
            for html in soup.find_all("div"):
                print(html)



                
        except:
            pass

urlfile.close()
