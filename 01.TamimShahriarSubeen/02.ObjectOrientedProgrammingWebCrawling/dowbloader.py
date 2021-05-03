import requests
import sys
imgUrl = sys.argv[1]
fileName=sys.argv[2]
r = requests.get(imgUrl)

with open(fileName, "wb") as f:
    f.write(r.content)



# open terminal and type "python        downloader.py              https://wallpapercave.com/wp/wp6154835.jpg             pybook1.jpg"