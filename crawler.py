# import these two modules bs4 for selecting HTML tags easily
from bs4 import BeautifulSoup
# requests module is easy to operate some people use urllib but I prefer this one because it is easy to use.
import requests


# I put here my own blog url ,you can change it.
url="http://mentalfloss.com/article/53792/17-ancient-abandoned-websites-still-work"

#Requests module use to data from given url
source=requests.get(url)

# BeautifulSoup is used for getting HTML structure from requests response.(craete your soup)
soup=BeautifulSoup(source.text,features = "lxml")
links = []
# Find function is used to find a single element if there are more than once it always returns the first element.
title=soup.find('title') # place your html tagg in parentheses that you want to find from html.
print("this is with html tags :",title)

qwery=soup.find('h1') # here i find first h1 tagg in my website using find operation.

#use .text for extract only text without any html tags
print("this is without html tags:",qwery.text) 


links=soup.find('a') #i extarcted link using "a" tag
print(links)


# ## extarct data from innerhtml 

# here i extarcted href data from anchor tag.
print(links['href']) 

# similarly i got class details from a anchor tag
print(links['class'])


# ## findall operation in Bs4

# findall function is used to fetch all tags at a single time.
many_link=soup.find_all('a') # here i extracted all the anchor tags of my website
total_links=len(many_link) # len function is use to calculate length of your array
print("total links in my website :",total_links)
print()
for i in many_link[:6]: # here i use slicing to fetch only first 6 links from rest of them.
    print(i)

second_link=many_link[1] #here i fetch second link which place on 1 index number in many_links.
print(second_link)
print()
print("href is :",second_link['href']) #only href link is extracted from ancor tag


# select div tag from second link
nested_div=second_link.find('div')
# As you can see div element extarcted , it also have inner elements
print(nested_div)
print()


    
