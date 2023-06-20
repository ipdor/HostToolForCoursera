import requests
import re

hosts=["www.coursera.org","www-cloudfront-alias.coursera.org", "d3c33hcgiwev3.cloudfront.net", "d3njjcbhbojbot.cloudfront.net"]
hostsFile="C:\Windows\System32\drivers\etc\hosts"


def deleteOldRecords():
    file=""
    with open(hostsFile,"r") as f:
        file = f.readlines()
    newfile=[]
    for x in file:
        if x.strip()=="":
            continue
        notContain=1
        for i in range(len(hosts)):
            if  x.find(hosts[i])>=0:
                notContain*=-1
                break
        if notContain==1:
            newfile.append(x+"\n")
            print(x)
    with open(hostsFile,"w") as f:
        f.writelines(newfile)

def getAddresses():
    headers = {
        'Host': 'ping.eu',
        'User-Agent': 'Mozilla/5.0',
        'Content-Type': 'application/json',
        'Origin': 'https://ping.eu',
        'Referer':'https://ping.eu/nslookup/'
    }
    data={
        "host":"",
        "go":"Go"
    }
    res=[]
    for i in range(len(hosts)):
        data["host"] = hosts[i]
        print(data)
        response  = requests.post(url="https://ping.eu/action.php?atype=3",data=data).text

        pattern = r'\.innerHTML \+\= \"(.*) has address <span class=t2>(.*)</span>'
        matches = re.findall(pattern, response)
        result = ['  '.join(match[::-1]) for match in matches]
        if  result==[]:
            continue
        result.append("\n")
        print(result)
        res+=(result)
    
    with open(hostsFile,"a") as f:
        for x in res:
            f.writelines(x+"\n")

if __name__ == "__main__":
    deleteOldRecords()
    getAddresses()
