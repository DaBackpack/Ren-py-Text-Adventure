label news4:
  python:
  
    key = "news4"
    
    subj = "Electric Sheep Inc. Opens New Branch"
    
    tx = "newsletter@electrosheep.ca"
    
    rx = username[:5] + "713@electrosheep.ca"
  
    text = """    Electric Sheep Incorporated opened a new
office today in Edmonton.  This marks the fourth 
major expansion of the controversial corporation 
this year as their stock continues to soar.
  
    Those interested in working at the branch 
can apply at electricsheep.ca/jobs (AIs need 
not apply)."""
  
    email = Email(key, subj, tx, rx, text)
    emaillist[key] = email