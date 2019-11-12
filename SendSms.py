from sim800l import SIM800L

sim800l=SIM800L('/dev/serial0')

sms="Hello there"
dest="+917892302212"

print(sim800l.send_sms(dest,sms))