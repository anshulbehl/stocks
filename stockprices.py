import requests
from operator import itemgetter
from BeautifulSoup import BeautifulSoup as bs




arr = ['MARUTI.BO','HDFCBANK.BO','ZEEMEDIA.BO','INFY.BO','ACC.BO']
low=high=current=opened=ask=bid=0
data={}
print "\t\t\t\t\t\t\t\t\tAccumulating Data for all shares".upper()+"\n\n"
#print "\t\tCurrent Value\tTodays Low\tTodays High\tOpened at\tAsking Price\tBidding Price"
print('%-25s%-25s%-25s%-25s%-25s%-25s%-25s'%('','\033[1m'+'Current Value','Todays Low','Todays High','Opened at','Asking Price','Bidding Price'))
for stock in arr:
	arr ={}
	r = requests.get("https://in.finance.yahoo.com/q?s="+stock+"&ql=0")
	soup = bs(r.content)
	#for span in soup.findAll('span'):
	#    print  span.text
	ids = stock.lower()
	spans = soup.findAll('span')
	for span in spans:
		if span.has_key('id'):
			if span['id'] == "yfs_l84_"+ids:
				current = span.text
				arr['current'] = current
				#print "\tCurrent value of "+stock+" is "+span.text
			if span['id'] == "yfs_g53_"+ids:
				#print "\tTodays low of "+stock+" is "+span.text
				low = span.text
				arr['low']=low
			if span['id'] == "yfs_h53_"+ids:
				#print "\tTodays high of "+stock+" is "+span.text
				high = span.text
				arr['high']=high
			if span['id'] == "yfs_b00_"+ids:
				bid = span.text
				arr['bid']=bid
			if span['id'] == "yfs_a00_"+ids:
				ask = span.text
				arr['ask']=ask
	rows=soup.findAll('tr')
	for row in rows:
		ths = row.findAll('th')
		for th in ths:
			if th.text == "Open:":
				arr['open'] = th.nextSibling.text
	data[ids]=arr
	#print "\t\t"+str(current)+"\t"+str(low)+"\t"+str(high)+"\t"+str(opened)+"\t"+str(ask)+"\t"+str(bid)
print "\033[0m\n"
for key in data:
	#print key,data[key]['current'],data[key]['low'],data[key]['high']
	#print("{0:10} {0:10} {0:10}".format(key,data[key]['current'],data[key]['low']))
	print('%-25s%-25s%-25s%-25s%-25s%-25s%-25s'%(key.upper(),data[key]['current'],data[key]['low'],data[key]['high'],data[key]['open'],data[key]['ask'],data[key]['bid'])) 

print "This is a different change"
