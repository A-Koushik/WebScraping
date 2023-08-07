import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd

desired_width=320
pd.set_option('display.width', desired_width)
pd.set_option('display.max_columns',10)


url="https://www.flipkart.com/search?p%5B%5D=facets.brand%255B%255D%3DSamsung&sid=tyy%2F4io&sort=recency_desc&ctx=eyJjYXJkQ29udGV4dCI6eyJhdHRyaWJ1dGVzIjp7InRpdGxlIjp7Im11bHRpVmFsdWVkQXR0cmlidXRlIjp7ImtleSI6InRpdGxlIiwiaW5mZXJlbmNlVHlwZSI6IlRJVExFIiwidmFsdWVzIjpbIkxhdGVzdCBTYW1zdW5nIG1vYmlsZXMgIl0sInZhbHVlVHlwZSI6Ik1VTFRJX1ZBTFVFRCJ9fX19fQ%3D%3D&wid=1.productCard.PMU_V2_1"
response = requests.get(url)
html = BeautifulSoup(response.content, 'html.parser')

processors=[]
for i in html.find_all("li",class_="rgWa7D") :
    if "processor" in i.text.lower() :
        processors.append(i.text)

camera=[]
for i in html.find_all("li",class_="rgWa7D") :
    if "camera" in i.text.lower() :
        camera.append(i.text)


with open("DS_CSV.csv", "w", newline='',encoding='utf-8') as file:
    file_attr = ["Product_Names", "Product_Price","Processor","Camera"]                      # Declaration of Attributes in csv file
    file_writer = csv.DictWriter(file, fieldnames=file_attr)            # Creating a dictionary to store key and values where keys are attributes and values are values lol
    file_writer.writeheader()                                           # This will write the Attributes
    for product,price,processor,cam in zip(html.find_all("div", class_="_4rR01T"),html.find_all("div", class_="_30jeq3 _1_WHN1"),processors,camera):              # find_all is used to find the all attributes conents
        file_writer.writerow({"Product_Names": product.text,"Product_Price": price.text,"Processor" : processor,"Camera" : cam})           # write row will write the values in product.text into csv file



df = pd.read_csv("C:/Users/koush/Documents/Python_Projects/DS_CSV.csv")
print(df.head(10))

