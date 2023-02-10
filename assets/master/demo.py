import os
from bs4 import BeautifulSoup
from time import sleep
def UI_designers(tag):
    if tag.endswith(".html"):
        return tag+"/"

    return "{% static '"+tag+"' %}"
def for_html(tag):
    return tag[::-1][5:][::-1]+'/'
def filter_(sri):
    with open(sri,'r') as file:
        soup=BeautifulSoup(file,'html.parser')

    for j in soup.find_all(['img','script','iframe','audio','embed','input','source','track','video'],recursive=True):
        try:
            temp=j['src']
            i=temp.lower()
            if i.endswith('.css') or i.endswith('.js') or i.endswith('.gif'):
                j['src']=UI_designers(temp)
            elif i.endswith('.png') or i.endswith('.jpg') or i.endswith('.jpeg') or i.endswith('.ico'):
                j['src']=UI_designers(temp)
            elif i.endswith('.svg') or i.endswith('.mp3') or i.endswith('.pdf') or i.endswith('.exe'):
                j['src']=UI_designers(temp)
            elif i.endswith('.docx') or i.endswith('.ttf') or i.endswith('.woff'):
                j['src']=UI_designers(temp)
        except:
            pass
    for j in soup.find_all(['a','link','area','base'],recursive=True):
        try:
            temp=j['href']
            i=temp.lower()
            if i.endswith('.html'):
                j['href']=for_html(temp)
            elif i.endswith('.css') or i.endswith('.js') or i.endswith('.gif'):
                j['href']=UI_designers(temp)
            elif i.endswith('.png') or i.endswith('.jpg') or i.endswith('.jpeg') or i.endswith('.ico'):
                j['href']=UI_designers(temp)
            elif i.endswith('.svg') or i.endswith('.mp3') or i.endswith('.pdf') or i.endswith('.exe'):
                j['href']=UI_designers(temp)
            elif i.endswith('.docx') or i.endswith('.ttf') or i.endswith('.woff'):
                j['href']=UI_designers(temp)
        except:
            pass
    with open('H:\\sri_projects\\cec\\'+''+sri,'w') as file2:
        file2.write('{% load static %}')
        file2.write('\n')
        file2.write(str(soup))
for i in os.listdir('H:\\sri_projects\\practise'):
    if i.endswith('.html'):
        filter_(i)

      
    