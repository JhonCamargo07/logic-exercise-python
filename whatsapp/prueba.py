import pywhatkit

from datetime import datetime
import time


seconds = time.time() + 60

date = datetime.fromtimestamp(seconds)

pywhatkit.sendwhatmsg('+573142577567', 'Hola', date.hour, date.minute)



