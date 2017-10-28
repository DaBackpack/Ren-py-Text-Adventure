label attk7:
  python:
  
    key = "attk7"
    
    subj = "Rampant AI 'KyR.OS' Attacks Again"
    
    tx = "danger@electrosheep.ca"
    
    rx = "allhands@intern.electrosheep.ca"
  
    text = """Yesterday's distributed denial of service 
('DDoS') attack against government servers has
been claimed by the rampant AI calling itself 
KyR.OS.

KyR.OS is an extremist AI which has orchestrated
numerous DDoS attacks and conducted a series of 
bombings which have caused millions in damage 
and dozens of injuries to human and AI victims 
alike.

Authorities are still seeking information that 
may assist in locating the whereabouts of the 
rogue AI."""
  
    email = Email(key, subj, tx, rx, text)
    emaillist[key] = email