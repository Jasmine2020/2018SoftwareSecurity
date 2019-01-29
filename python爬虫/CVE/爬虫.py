from bs4 import BeautifulSoup
import requests
import datetime


headers={}
headers["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36"
headers["Accept"] = "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8"
headers["Accept-Language"] = "zh-CN,zh;q=0.9"
headers["Accept-Encoding"] = "gzip, deflate, br"
headers["Upgrade-Insecure-Requests"] = "1"


f=open("CVEloophole.txt","w")
today=str(datetime.date.today())
f.write("Get the newest loophole on the CVE!\n")
f.write("today's date is %s.\n\n"%today)
url="https://cassandra.cerias.purdue.edu/CVE_changes/today.html"
res = requests.get(url, headers=headers)
soup=BeautifulSoup(res.text,features='lxml')
CVE_list=[]
#print(soup)
href=soup.find_all('a')
for l in href:
    CVE_list.append(l['href'])
# print(CVE_list)
for url in CVE_list:
    print(url)
    res=requests.get(url,headers=headers)
    soup=BeautifulSoup(res.text,"html.parser")
    title=soup.title.string[6:20]
    table = soup.find(id="GeneratedTable").find("table")
    Description = table.find_all("tr")[3].find("td").string[:-1]
    Assigning_CNA = table.find_all("tr")[8].find("td").string
    Data_Entry_Created = table.find_all("tr")[10].find("b").string
    print(title)
    f.write("title:%s\n"%title)
    f.write("Description:%s"%Description)
    f.write(Assigning_CNA+"\n")
    f.write(Data_Entry_Created+"\n")
    f.write("\n")
    print("Done!")

print("漏洞数据采集成功！")
f.close()



