import pandas as pd
import datetime
from slugify import slugify
import os
import pdfkit
from pyquery import PyQuery

now = datetime.datetime.now()

df = pd.DataFrame([
        {'package': 'PEPTize', 'student': 'Yashvant Singh', 'level': 'Level 1'}
        # {'package': 'PlaceMe Mechanical', 'student': 'Rajeev Kumar', 'level': 'Level 2'},
        # {'package': 'N2N Python', 'student': 'Gaurav Singh', 'level': 'Level 2'},
        # {'package': 'PEPTize', 'student': 'Rakesh Sharma', 'level': 'Level 3'},
    ])
print(df)


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

                student_name = df.student.item()
                student_level = df.level.item()
                student_package = df.package.item()
                student_certdate = now.strftime("%Y-%m-%d %H:%M")
                
                html = html.replace("{{student}}",student_name)
                html = html.replace("{{level}}",student_level)
                html = html.replace("{{package}}",student_package)
                html = html.replace("{{certdate}}",student_certdate)

                html_file = open(html_file_path,"w")
                html_file.write(html)
                html_file.close()
                #make sure the file name is valid

                valid_file_name = file_name.replace(" ","").replace(":","")

                #Note:if you are using Windows,pls make sure Spooler service is enabled
                pdfkit.from_file(html_file_path, valid_file_name+'.pdf')


                #For retivieng the value to previous in the html 
                #read from html file
                html_file = open(html_file_path)
                html = html_file.read()
                html_file.close()


                html = html.replace(student_name,"{{student}}")
                html = html.replace(student_level,"{{level}}")
                html = html.replace(student_package,"{{package}}")
                html = html.replace(student_certdate,"{{certdate}}")


                html_file = open(html_file_path,"w")
                html_file.write(html)
                html_file.close()

input("test:")
