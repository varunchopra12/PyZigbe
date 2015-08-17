from  scapy.all import *

mymac=”aa:bb:cc:dd:ee:ff” #Any random Mac Address

apmac=”ab:cd:ef:ff:aa:bb” #Mac Address of the Router whose SSID is Hidden

pkt=RadioTap()/Dot11(type=0,subtype=5,addr1=mymac,addr2=apmac,addr3=apmac)/Dot11ProbeResp()/Dot11Elt(ID=0,info=”Cloacked”)/Dot11Elt(ID=1,info=”\x02\x04\x0b\x16”)/  #Forging a packet which cloacks our orignal SSID
sendp(pkt,iface=”mon0”,count=3,inter=.3) #Flood the packets in wireless stream #count = no of packets  


