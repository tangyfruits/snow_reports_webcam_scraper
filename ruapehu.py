import urllib.request
import time
import schedule
import os


def build_url(webcam):
    url = "https://webcams.mtruapehu.com/" + webcam.lower().replace(" ", "") + "/latest.jpg?" + str(time.time())
    print(url)
    return url


def save_img():
    whakapapa = ["HV From Sky Waka", "Te Heuheu Valley", "Waterfall", "The Pinnacles", "Far West T Bar"]
    turoa = ["Alpine Meadows", "Blyth Flat", "Giant Cafe", "Highnoon Top", "Turoa Midfield"]

    ruapehu = whakapapa + turoa
    for field in ruapehu:
        print(field)
        os.makedirs(field, exist_ok=True)
        url = build_url(field)
        resp = urllib.request.urlretrieve(url, field + "/" + url.split('?')[-1] + ".jpg")


schedule.every(15).minutes.do(save_img)

while 1:
    schedule.run_pending()
    time.sleep(1)
