import os
import pdfkit
import os
from pyquery import PyQuery

for root,dirs,files in os.walk("."):
        for filespath in files:
            #process all html files
            if os.path.splitext(filespath)[1]==".html":
                html_file_path = os.path.join(root,filespath)

                #read from html file
                html_file = open(html_file_path)
                html = html_file.read()
                html_file.close()

                #using PyQuery to parse HTML and get content for the name of the file
                pq = PyQuery(html)
                tag = pq('title')
                file_name = tag.text()
                #make sure the file name is valid
                valid_file_name = file_name.replace(" ","").replace(":","")

                #Note:if you are using Windows,pls make sure Spooler service is enabled
                pdfkit.from_file(html_file_path, valid_file_name+'.pdf')

input("test:")
