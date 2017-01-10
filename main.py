import time
import requests
from pushbullet import Pushbullet
pb = Pushbullet("API CODE FROM PUSHBULLET")




response = requests.get("WEBSITE GOES HERE")
while response.status_code != 200:
    print ("sleeping:")
    print ("sleeping:")
    time.sleep(5.0)
    response = requests.get("WEBSITE GOES HERE")
print ("done!")
push = pb.push_note("Website is up", "Website is up")
exit()
