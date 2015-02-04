# Image-Getter
A program to fetch data serially from accounts in a database, the data in this case being photos. 

Here, we have used our college exam result page(here:: exam.msrit.edu) to fetch images of students based on their unique identification code. This is done by appending the post parameters(obtained by assessing the page headers in the network tab in the javascript console in Google Chrome) to the page url and then passing the request. Then using the BeautifulSoup library we obtain the student images using the respective img tag and the image is finally downloaded on the computer using urllib.The program can be used here to download the set of student images from a set of  particular identification codes(here USN) and store them in a folder.

Fin. 
