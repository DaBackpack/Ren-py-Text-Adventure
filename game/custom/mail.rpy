label mail:
    $expected = ["look", "l", "help", "?", "show", "email", "exit"]
    $pickup = []
    $room = "Email"
    $desc = """{cps=150}<PLACEHOLDER: This is the email app screen> Fancy ASCII email graphics{/cps}

Type {b}show emails{/b} to see the list of available emails, {b}email{/b} followed by the message number you wish to open, or "exit" to quit.

Example: {b}> email e_boss0{/b}"""
    
    $say()
    
    while True:
        $echo()
        
        if cmd not in expected:
            python:
                eastered = False
                for word in easters:
                    if cmd == word or args == word or word in args:
                        easter(word)
                        eastered = True
                
                if not eastered:
                    input_error()
        
        elif cmd == "look" or cmd == "l":
            if len(args) == 0:
                $flush_input()
                nvl clear
                jump mail
            else:
                $has_args()
                
        elif cmd == "help" or cmd == "?":
            $help()
            
        elif cmd == "exit":
            if len(args) == 0:
                $flush_input()
                $desc = "Closing mail.app{cps=2}... ... ... Done.{/cps} \n" \
                        "Press {b}ENTER{/b} to return to main screen."
                $say()
                
                nvl clear
                jump mainscreen
            else:
                $has_args()
                
        elif cmd == "show":
            
            if len(args) == 1 and args[0] == "emails":
                $s = "{cps=150}{color=#faebd7}" + "    * " + "\n    * ".join(emaillist) + "{/color}{/cps}"
                $desc = s
                $say()
            
            else:
                $desc = "{color=#f00}Error{/color}: please type {b}show emails{/b} to view your email list."
                $say()
        
        elif cmd == "email":
            if len(args) == 1:
                if args[0] in emaillist:
                    
                    $desc = "Downloading email [args[0]]{cps=2}... ... ...{/cps} Done.\n" \
                            "Press {b}ENTER{/b} to open email."
                    $say()
                    
                    nvl clear
                    jump expression args[0]
                    
                else:  
                    $flush_input()
                    $desc = "Please enter a valid email message."
                    $say()
                
            else:
                $flush_input()
                $desc = "Command 'email' takes exactly one argument."
                $say()
            
    return