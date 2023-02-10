from bs4 import BeautifulSoup
from urllib.request import urlopen
from time import sleep
import os


with open("home.html",'r') as file:
    soup=BeautifulSoup(file,features='html.parser')
def link():
    global soup
    link_tags=soup.find_all('link')
    href=list()
    for tag in link_tags:
        tag=tag.get('href')
        if tag!=None:
            href.append(tag)
    return href
def script():
    global soup
    link_tags=soup.find_all('script')
    src=list()
    for tag in link_tags:
        tag=tag.get('src')
        if tag!=None:
            src.append(tag)
    return src
def a():
    global soup
    link_tags=soup.find_all('a')
    href=list()
    #<link rel="shortcut icon" href="image/favicon_io/android-chrome-512x512.png">
    for tag in link_tags:
        tag=tag.get('href')
        if tag!=None and tag!='#':
            href.append(tag)
    return href
def img():
    global soup
    link_tags=soup.find_all('img')
    src=list()
    #<link rel="shortcut icon" href="image/favicon_io/android-chrome-512x512.png">
    
    for tag in link_tags:
        tag=tag.get('src')
        if tag!=None:
            src.append(tag)
    return src
def li_back():
    global soup
    link_tags=soup.find_all('li')
    src=list()
    back_img=list()
    #<link rel="shortcut icon" href="image/favicon_io/android-chrome-512x512.png">
    for tag in link_tags:
        tag=tag.get('style')
        if tag!=None:
            src.append(tag)
    for i in src:
        sri=i
        temp=i.find('url(')
        sri=sri[temp+4:-2]
        back_img.append(sri)
    return back_img
def div():
    global soup
    link_tags=soup.find_all('div')
    src=list()
    back_img=list()
    #<link rel="shortcut icon" href="image/favicon_io/android-chrome-512x512.png">
    for tag in link_tags:
        tag=tag.get('style')
        if tag!=None:
            temp=tag.find("background: url(")
            if temp!=-1:
                tag=tag[temp+16:]
                tag=tag[:tag.find(')')]
                back_img.append(tag)
    return src
def start(extend,data):
    url="http://www.cityengineeringcollege.ac.in/"+data
    print(url)
    web=urlopen(url)
    mode=''
    print(extend)
    if extend.endswith('.html')or extend.endswith('.css')or extend.endswith('.js'):
        mode='w'
        with open(extend,mode) as file:
                for i in web:
                    try:
                        file.write(i.decode().strip())
                        file.write('\n')
                    except:
                        pass
        return
    elif extend.endswith('.png')or extend.endswith('.jpg') or extend.endswith('.pdf'):
        mode='wb'
        with open(extend,mode) as file:
            for i in web:
                file.write(i)
        return
def main():
    global root,upload,link,script,a,img,li_back,main_urls
    root=[]
    upload=[]
    for i in link():
        root.append(i)
    for i in script():
        root.append(i)
    for i in a():
        root.append(i)
    for i in img():
        root.append(i)
    for i in li_back():
        root.append(i)
    main_urls=[i for i in root if(i.endswith('.html') or i.endswith('.jpg') or i.endswith('.png') or i.endswith('.css') or i.endswith('.js') or i.endswith('.pdf'))]
    root=[]
    for url in main_urls:
        temp=url
        if temp.find('/')!=-1:
            nav=temp.replace('/','\\'[0])
            root.append(nav)
        else:
            root.append(temp)
    for i,j in zip(main_urls,root):
        if i.endswith('.jpg'):
            check(i,j)

def check(king,item):
    temp=item.find('\\'[0])
    if temp!=-1:
        sri=item[::-1]
        temp=sri.find('\\'[0])
        sub1=sri[temp+1:][::-1]
        sub2=sri[:temp][::-1]
        print(sub1,sub2)
        if os.path.isdir(sub1):
            car=sub1+"\\"[0]+sub2
            sri=car.split("\\"[0])
            car="\\"[0:2].join(sri)
            start(sub1+"\\"[0]+sub2,king)
        else:
            os.makedirs(sub1)
            start(sub2,king)
    else:
        start(item,king)
start("COLLEGE%20ADMINISTRATION_files\\image007.jpg","COLLEGE%20ADMINISTRATION_files\\image007.jpg")