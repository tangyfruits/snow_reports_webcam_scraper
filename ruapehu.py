import urllib2
import time
import schedule


def build_url(webcam):
    url = "https://webcams.mtruapehu.com/" + webcam.lower().replace(" ", "") +"/latest.jpg?" + str(time.time())
    print url
    return url

	
def save_img():
	whakapapa = ["Happy Valley","Te Heuheu Valley","Waterfall","The Pinnacles","Far West T Bar"] #["Happy Valley","Te Heuheu Valley","Waterfall","The Pinnacles","Far West T Bar","West Ridge Far West"]
	turoa = ["Alpine Meadows","Blyth Flat","Nga Waiheke","Giant Cafe","Highnoon Top"]

	for w in whakapapa:
		print w
		url = build_url(w)
		f = urllib2.urlopen(url)
		data = f.read()
		with open("whakapapa/" + w + "/" + url.split('?')[-1] + ".jpg", "wb") as imgfile:
			imgfile.write(data)
                time.sleep(0.1)
	for t in turoa:
		print t
		url = build_url(t)
		f = urllib2.urlopen(url)
		data = f.read()
		with open("turoa/" + t + "/" + url.split('?')[-1] + ".jpg", "wb") as imgfile:
			imgfile.write(data)
                time.sleep(0.1)

	print "done"

schedule.every(15).minutes.do(save_img)


while 1:
    schedule.run_pending()
    time.sleep(1)
