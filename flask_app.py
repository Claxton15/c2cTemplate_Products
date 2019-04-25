from flask import Flask, request, render_template, redirect
import requests
import random
app = Flask(__name__)



@app.route('/', methods=['GET'])
def main():
    r=requests.get("https://www.googleapis.com/youtube/v3/search?part=snippet&maxresult=25&q=overwatch%20easter%20eggs&key=AIzaSyDYCJ1jsTCVm7h2jiDaind5B51uybE382U")
    name=r.json()
    app.logger.info(name)
    print(name)
    videoId=random.choice(name["items"])["id"]["videoId"]
    return render_template("index.html", json=name, videoId=videoId, title=name["items"][0]["snippet"]["title"] )

@app.route('/BTS', methods=['GET'])
def BTS():
    BTSsearch = random.choice(["upcoming%20games","new%20games"])
    return search(BTSsearch)

@app.route('/easteregg', methods=['GET'])
def easteregg():
    eggSearch= random.choice(["fallout%20easter%20eggs","fallout%20secrets"])
    return search(eggSearch)

@app.route('/tutorials', methods=['GET'])
def tutorials():
    tutorSearch= random.choice(["garrys%20mod%20tutorial","garrys%20mod%20tips%20and%20tricks","garrys&20mod%20how%20to%play"])
    return search(tutorSearch)

@app.route('/letsPlay', methods=['GET'])
def letsPlay():
    gameplay= random.choice(["skyrim%20lets%20play","skyrim%20gameplay"])
    return search(gameplay)

@app.route('/skits', methods=['GET'])
def skits():
    skitSearch= random.choice(["minecraft%20skit","minecraft%20machinima"])
    return search(skitSearch)

@app.route('/proGaming', methods=['GET'])
def proGaming():
    proSearch= random.choice(["csgo%20pro%20gaming","csgo%20eleague","csgo%20tournament"])
    return search(proSearch)

def search(query):
    r=requests.get("https://www.googleapis.com/youtube/v3/search?part=snippet&maxresult=25&q=" + query + "&key=AIzaSyDYCJ1jsTCVm7h2jiDaind5B51uybE382U")
    json=r.json()
    videoId=random.choice(json["items"])["id"]["videoId"]
    return redirect("http://www.youtube.com/watch?v=" + videoId, code=302)


if __name__ == '__main__':
    app.run()