Code to Uncover  Hidden ssids:
#!/usr/bin/python                     /python shell on linux 

From scapy.all import *           /import scapy libraby

Import socket                       /import socket library

HiddenSSID=set()          /creating a set named hidden

Def Packethandler(pkt):                  
    If pkt.haslayer(Dot11Beacon) :
         If not pkt.info:
             If pkt.addr3 not in HiddenSSID :			                     

                    HiddenSSID.add(pkt.addr3)
	     Print “Hidden SSID NETWORK FOUND ! BSSID :”,pkt.addr3

      Elif pkt.haslayer(Dot11ProbResp) and (pkt.addr3in HiddenSSID)
		Print “Hidden SSID UNCOVERED !”,pkt.info,pkt.addr3
		Sniff(iface=”mon0”,count=10000,prn=PacketHandler)
