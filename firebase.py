import imp
import pyrebase
import config


# lk = database.child("LED_STATUS").get()

# database.update({"LED_STATUS": 0})

con = config.config()
fireBase = pyrebase.initialize_app(con)
database = fireBase.database()


def light_off():
  database.update({"LED_STATUS": 0})

def light_on():
  database.update({"LED_STATUS": 1})









