import sys
import requests


#  your own Telegram User ID
USERID = 1323422423

#  create your own Bot with @Botfather and paste API token
APITOKEN = "312323231:AAE6zTu5A5okjSXfu6MMLb19HIGPq6GUv9k"

requests.get("https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}".format(APITOKEN,
                                                                                    USERID,
                                                                                    str(sys.stdin.read())))

