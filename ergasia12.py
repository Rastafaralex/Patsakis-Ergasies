from datetime import datetime

date_entry = input('dwse imerominia etsi:ΗΗ/ΜΜ/ΕΕΕΕ')#mu vazi o user tin hmerominia 
year, month, day = map(int, date_entry.split(','))#apo edo ego tha paro ta year,month,day
date = datetime(day, month, year)

from datetime import date    
today = date.today().isoformat()
print("simera exume",today)
slo=today
import re
simera = re.sub("[^\w]", " ",  slo).split()#kano tin simerini hmerominia se array kai meta tha kano upologismus 
#to simera einai lista me mera,mina,xrono tou shmera 
mera=year #edo eprepe na kano kapies alages giati tin hmera tin eperne gia xrono kai ton xrono gia mera, mhnas htan idios agia kapio logo alla den mas pirazi
minas=month
if minas in (1,3,5,7,8,10,12):
    print ("o minas pu mu dosate exi 31 meres")
else :
    if minas in(4,6,9,11):
        print("o minas pu dosate exi 30 meres")
    else :
        print("o minas pu dosate einai o februarios kai exi 27 h 29 meres analogos")
xronos=day
simeramera=int(simera[2])
simeraminas=int(simera[1])
simeraxronos=int(simera[0])
if simeramera > mera :
    diaforamera= simeramera-mera
else :
    diaforamera= mera - simeramera
if simeraminas > minas:
    diaforaminas= simeraminas - minas
else:
    diaforaminas= minas - simeraminas
if simeraxronos > xronos:
    diaforaxronos= simeraxronos - xronos 
else:
    diaforaxronos= xronos - simeraxronos
#tora tha metatrepso tis diafores se meres ores kai defterolepta
wres1= 24 * diaforamera
defterolepta1=wres1*3600
meres1=diaforaminas*30
wres2=meres1*24
defterolepta2=wres2*3600
meres2=diaforaxronos*365
wres3=meres2*24
defterolepta3=wres3*3600

sinolomeres= diaforamera + meres1 + meres2 
sinolowres= wres1+wres2+wres3
sinolodeftera= defterolepta1+defterolepta2+defterolepta3
print("h diafora metaxi simerinis hmerominias kai aftis pu dosate se meres,wres,defterolepta einai",sinolomeres,sinolowres,sinolodeftera)
