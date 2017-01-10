import time
import requests
from pushbullet import Pushbullet
pb = Pushbullet("o.LxrFcxRbkCHh8AKdEkZPjF3DgYxu1Pvk")




response = requests.get("http://192.168.178.45/test.php")
while response.status_code != 200:
    print ("sleeping:")
    print ("sleeping:")
    time.sleep(5.0)
    response = requests.get("http://192.168.178.45/test.php")
print ("done!")
push = pb.push_note("AOS <3", "AOS <3")
exit()
