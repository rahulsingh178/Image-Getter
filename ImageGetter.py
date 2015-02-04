from bs4 import BeautifulSoup
import urllib

string1="/components/com_examresult/assets/images/MSRITbanner.jpg"

string2="/components/com_examresult/assets/images/OBElogo.png"

for n in range(1,200):

    if len(str(n))==1:
        v="00"+str(n)

    if len(str(n))==2:
        v="0"+str(n)

    if len(str(n))==3:
        v=str(n)
        
    usn_value="1MS14IM"+v
    
    post_parameters={
        "usn":usn_value,
        "option":"com_examresult",
        "task":"getResult"
        }

    post_argument=urllib.urlencode(post_parameters)

    url="http://exam.msrit.edu/index.php"

    fp=urllib.urlopen(url,post_argument)

    soup=BeautifulSoup(fp)

    s1=soup.findAll("img")
    
    for x in s1:

        if x["src"]!=string1 and x["src"]!=string2:
        
            print x["src"]
            realurl="http://exam.msrit.edu" + x["src"]
            urllib.urlretrieve(realurl,"D:/Python Stuff/photos/"+usn_value+".jpg")
              
                                                          
