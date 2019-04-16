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

@app.route('/easteregg', methods=['GET'])
def easteregg():
    r=requests.get("https://www.googleapis.com/youtube/v3/search?part=snippet&maxresult=25&q=overwatch%20easter%20eggs&key=AIzaSyDYCJ1jsTCVm7h2jiDaind5B51uybE382U")
    json=r.json()
    videoId=random.choice(json["items"])["id"]["videoId"]
    return redirect("http://www.youtube.com/watch?v=" + videoId, code=302)




if __name__ == '__main__':
    app.run()