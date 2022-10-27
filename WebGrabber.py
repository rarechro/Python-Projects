'''
Version 1.0

By Payton J.

'''
import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup  
#imports needed to run the below code without error...hopefully


page_Url = "https://www.indeed.com/jobs?q=python&remotejob=032b3046-06a3-4876-8dfd-474eb5e7ed11&advn=5163623796312029&vjk=6ab92fafedca93a3" 
uClient = uReq(page_Url)
#getting the url and requesting

page_Soup = soup(uClient.read(), "html.parser")
f = open("Python_Job_Output", "w")
f.write(page_Soup.prettify())
f.close()
uClient.close()
#getting the data into html, exporting the data to a .txt document then closing the request

f = open("Python_Job_Output", "r")
file_contents = f.read()
#printing the data


jobs = page_Soup.find_All('div', class_="jobsearch-SerpJobCard unifiedRow row result clickcard")
for job in jobs:
    job_Elements = jobs.find_All('div', class_="jobsearch-SerpJobCard unifiedRow row result clickcard")
    print(job_Titles)



jobs = page_Soup.find_All('h2', class_="title")

print(jobs)