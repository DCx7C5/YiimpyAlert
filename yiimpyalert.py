import sys
import requests
import subprocess


#  your own Telegram User ID
USERID = 1323422423

#  create your own Bot with @Botfather and paste API token
APITOKEN = "312323231:AAE6zTu5A5okjSXfu6MMLb19HIGPq6GUv9k"

requests.get("https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}".format(APITOKEN,
                                                                                    USERID,
                                                                                    str(sys.stdin.read())))
#  UNCOMMENT the following line if you like it nostalgic - and add your mail address
#subprocess.call(["echo", "%s", "|", "mail", "-s", "'<COIN> alert!'", "<YOUR MAIL ADDRESS>"])
