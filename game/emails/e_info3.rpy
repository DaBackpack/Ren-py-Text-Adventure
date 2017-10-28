label info3:
  python:
  
    key = "info3"
    
    subj = "fwd: Natural Language AI Advocate"
    
    tx = "ai_news@electrosheep.ca"
    
    rx = "+info_all@intern.electrosheep.ca"
  
    text = """{i}Interviewer{/i}: What do you want?
    
{i}AI Advocate{/i}: Natural Language Processing!

{i}Interviewer{/i}: When do you want it?

{i}AI Advocate{/i}: When do we want what?"""
  
    email = Email(key, subj, tx, rx, text)
    emaillist[key] = email