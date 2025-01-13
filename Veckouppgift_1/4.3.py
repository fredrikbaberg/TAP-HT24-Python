# 3a Skriv ett program som talar om dagens datum.
import datetime

print("Idag är det {}".format(datetime.date.today()))


# 3b (svårare) Ändra programmet så att det kan tala om vilket datum det är om 7 dagar.
today = datetime.date.today()
in_seven_days = datetime.datetime.now() + datetime.timedelta(days=7)
print("Om 7 dagar är det {}".format(in_seven_days.date()))