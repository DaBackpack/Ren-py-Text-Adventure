label mail:
    $update_avails()
    $expected = ["LOOK", "L", "HELP", "?", "SHOW", "READ", "EXIT"]
    $pickup = []
    $room = "Email"
    $update_roomlabel()
    $desc = ""
    $desc += make_header("mail.app")
    $desc += """{cps=0}|                                                                        |
| Type <show emails> to see the list of available emails, <read> followed|
| by the message number you wish to open, or <exit> to quit.  New emails |
| are shown in {color=#""" + highlight2 + """}this color{/color} and previously read emails are shown in {color=#""" + highlight1 + """}this   {/color}|
| {color=#""" + highlight1 + """}color{/color}.                                                                 |
|                                                                        |
| Example: {b}> read news0{/b}                                                 |
|________________________________________________________________________|

{/cps}     You have ({color=#""" + errorcolor + """}[numEmails]{/color}) unread emails."""
    
    $say()
    
    while True:
        $echo()
        
        if cmd.upper() not in expected:
            python:
                eastered = False
                for word in easters:
                    if cmd == word or args == word or word in args:
                        easter(word)
                        flush_input()
                        eastered = True
                
                if not eastered:
                    input_error()
        
        elif cmd.upper() == "LOOK" or cmd.upper() == "L":
            if len(args) == 0:
                $flush_input()
                nvl clear
                jump mail
            else:
                $has_args()
                
        elif cmd.upper() == "HELP" or cmd == "?":
            $help()
            
        elif cmd.upper() == "EXIT":
            if len(args) == 0:
                $flush_input()
                
                term "Closing mail.app{cps=6}... ... {/cps}{nw}"
                play sound "music/beep2.ogg"
                extend "{cps=130}Done.{/cps} \nPress {b}ENTER{/b} to return to main screen."
                
                nvl clear
                jump mainscreen
            else:
                $has_args()
                
        elif cmd.upper() == "SHOW":
            
            if len(args) == 1 and args[0].upper() == "EMAILS":
                $flush_input()
                if len(emaillist) > 0:
                    python:
                        s = ""
                        for id in emaillist.keys():
                            s += "  [[{color=#" + emaillist[id].getReadColor() + "}" + id + "{/color}]: "
                            s += "'" + emaillist[id].getSubj() + "'\n"
                else:
                    $s = "{cps=150}You have no emails.{/cps}"
                    
                $desc = s
                $say()
            
            else:
                $flush_input()
                $desc = "{color=#f00}Error{/color}: please type {b}show emails{/b} to view your email list."
                $say()
        
        elif cmd.upper() == "READ":
            
            if len(args) == 1:
                $key = args[0]
                $flush_input()
                if key in emaillist.keys():
                    
                    term "Downloading email [key]{cps=6}... ... ... {/cps}{nw}"
                    play sound "music/beep.ogg"
                    extend "{cps=130}Done.{/cps} \nPress {b}ENTER{/b} to continue to mail."

                    $flush_input()
                    nvl clear
                    
                    $desc = emaillist[key].read()
                    $update_avails()
                    $say()
                    
                    $desc = "     You have ({color=#" + errorcolor + "}[numEmails]{/color}) unread emails."
                    $say()
                    
                else:  
                    $flush_input()
                    $desc = "Please enter a valid email message."
                    $say()
                
            else:
                $flush_input()
                $desc = "Command 'read' takes exactly one argument."
                $say()
            
    return