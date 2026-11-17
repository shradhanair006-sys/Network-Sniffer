from scapy.all import sniff,IP,TCP,UDP,ICMP
def packet_callback(packet):
    print("\n==========PACKET CAPTURED=======")
    if IP in packet:
       print("SOurce IP:",packet[IP].src)
       print("Destination IP:",packet[IP].dst)
       if TCP in packet:
          print("Protocol:TCP")
       elif UDP in packet:
          print("Protocol:UDP")
       elif ICMP in packet:
          print("Protocol:ICMP")
       else:
          print("Protocol:Other")
    print("Packet Details:",packet.summary())
print("Starting Network Sniffer...")
print("Press CTRL+C to stop.")
sniff(prn=packet_callback,count=20,store=False)
