# LOGIN: first day login prompt
label login_first:
    
    scene bg black
    play music "music/bg0.mp3" fadein 3.8 loop
    
label login_first_again:

    $expected = ["LOOK", "L", "HELP", "?", "NEW"]
    $pickup = []
    $room = "New User"
    $desc = """{cps=0}{font=font/AnonymousPro.ttf}{color=#ffd700}
        ███████╗██╗     ███████╗ ██████╗████████╗██████╗ ██╗ ██████╗        
        ██╔════╝██║     ██╔════╝██╔════╝╚══██╔══╝██╔══██╗██║██╔════╝        
        █████╗  ██║     █████╗  ██║        ██║   ██████╔╝██║██║             
        ██╔══╝  ██║     ██╔══╝  ██║        ██║   ██╔══██╗██║██║             
        ███████╗███████╗███████╗╚██████╗   ██║   ██║  ██║██║╚██████╗        
        ╚══════╝╚══════╝╚══════╝ ╚═════╝   ╚═╝   ╚═╝  ╚═╝╚═╝ ╚═════╝        
                                                                    
        ███████╗██╗  ██╗███████╗███████╗██████╗     ██╗███╗   ██╗ ██████╗   
        ██╔════╝██║  ██║██╔════╝██╔════╝██╔══██╗    ██║████╗  ██║██╔════╝   
        ███████╗███████║█████╗  █████╗  ██████╔╝    ██║██╔██╗ ██║██║        
        ╚════██║██╔══██║██╔══╝  ██╔══╝  ██╔═══╝     ██║██║╚██╗██║██║        
        ███████║██║  ██║███████╗███████╗██║         ██║██║ ╚████║╚██████╗██╗
        ╚══════╝╚═╝  ╚═╝╚══════╝╚══════╝╚═╝         ╚═╝╚═╝  ╚═══╝ ╚═════╝╚═╝                  
{/color}{/font}{/cps}
Welcome, new user!  

Please type {b}new{/b} to set up your account.  You can type {b}help{/b} or {b}?{/b} at any time to see the list of currently available commands.  If you become lost on any screen, type {b}look{/b} or {b}l{/b} (lowercase L) to recall the original prompt."""
    
    $say()
    
    while True:
        $echo()
        
        if cmd.upper() not in expected:
            python:
                eastered = False
                for word in easters:
                    if cmd == word or args == word or word in args:
                        easter(word)
                        eastered = True
                
                if not eastered:
                    input_error()
            
        elif cmd.upper() == "LOOK" or cmd.upper() == "L":
            if len(args) == 0:
                $flush_input()
                nvl clear
                jump login_first_again
            else:
                $has_args()
        
        elif cmd.upper() == "HELP" or cmd == "?":
            $help()
            
        elif cmd.upper() == "NEW":
            if len(args) == 0:
                $flush_input()
                nvl clear
                jump login_new
            else:
                $has_args()
    return
    
# LOGIN: login new user
label login_new:
    $flush_input()
    $expected = ["LOOK", "L", "HELP", "?", "CREATE"]
    $pickup = []
    $room = "Create User"
    $desc = """{cps=0}{font=font/AnonymousPro.ttf}{color=#ffd700}
        ███████╗██╗     ███████╗ ██████╗████████╗██████╗ ██╗ ██████╗        
        ██╔════╝██║     ██╔════╝██╔════╝╚══██╔══╝██╔══██╗██║██╔════╝        
        █████╗  ██║     █████╗  ██║        ██║   ██████╔╝██║██║             
        ██╔══╝  ██║     ██╔══╝  ██║        ██║   ██╔══██╗██║██║             
        ███████╗███████╗███████╗╚██████╗   ██║   ██║  ██║██║╚██████╗        
        ╚══════╝╚══════╝╚══════╝ ╚═════╝   ╚═╝   ╚═╝  ╚═╝╚═╝ ╚═════╝        
                                                                    
        ███████╗██╗  ██╗███████╗███████╗██████╗     ██╗███╗   ██╗ ██████╗   
        ██╔════╝██║  ██║██╔════╝██╔════╝██╔══██╗    ██║████╗  ██║██╔════╝   
        ███████╗███████║█████╗  █████╗  ██████╔╝    ██║██╔██╗ ██║██║        
        ╚════██║██╔══██║██╔══╝  ██╔══╝  ██╔═══╝     ██║██║╚██╗██║██║        
        ███████║██║  ██║███████╗███████╗██║         ██║██║ ╚████║╚██████╗██╗
        ╚══════╝╚═╝  ╚═╝╚══════╝╚══════╝╚═╝         ╚═╝╚═╝  ╚═══╝ ╚═════╝╚═╝   
{/color}{/font}{/cps}
We're {cps=50}thrilled to have you join our company!{/cps}  Let's create your account.  Please type {b}create{/b} followed by your desired username (at least five characters long) to create your login.  If you become lost on any screen, type {b}look{/b} or {b}l{/b} (lowercase L) to see the original prompt.
    
Example: {b}> create shelby{/b}"""

    $say()
    
    while True:
        $echo()
        $add_time() # TODO: REMOVE, testing
        
        if cmd.upper() not in expected:
            python:
                eastered = False
                for word in easters:
                    if cmd == word or args == word or word in args:
                        easter(word)
                        eastered = True
                
                if not eastered:
                    input_error()
            
        elif cmd.upper() == "LOOK" or cmd.upper() == "L":
            if len(args) == 0:
                $flush_input()
                nvl clear
                jump login_new
            else:
                $has_args()
                
        elif cmd.upper() == "HELP" or cmd == "?":
            $help()
        
        elif cmd.upper() == "CREATE":

            if len(args) == 1:
                if len(args[0]) < 5:
                    $flush_input()
                    $desc = "Your username must be at least five characters long."
                    $say()
                
                else: 
                    $set_username(args[0])
                    $flush_input()
                    
                    $desc = """Your username has been set to {u}[username]{/u}.  {b}Please remember this username{/b} as you will use it to log in each day along with your bio-authentication.\n\nPress {b}<ENTER>{/b} to continue when you are ready."""
                    $say()
                    
                    $chatlist.append("sheep_1014")
                    call news4
                    $update_avails()

                    nvl clear                
                    jump login

            else:
                $flush_input()
                $desc = "{color=#f00}Error{/color}: Please enter a valid username."
                $say()

        else:
            $input_error()
    
    return
    
# LOGIN: regular login prompt
label login:
    $expected = ["LOOK", "L", "HELP", "?", "LOGIN"]
    $pickup = []
    $room = "Login"
    $desc = """{cps=0}{font=font/AnonymousPro.ttf}{color=#ffd700}
        ███████╗██╗     ███████╗ ██████╗████████╗██████╗ ██╗ ██████╗        
        ██╔════╝██║     ██╔════╝██╔════╝╚══██╔══╝██╔══██╗██║██╔════╝        
        █████╗  ██║     █████╗  ██║        ██║   ██████╔╝██║██║             
        ██╔══╝  ██║     ██╔══╝  ██║        ██║   ██╔══██╗██║██║             
        ███████╗███████╗███████╗╚██████╗   ██║   ██║  ██║██║╚██████╗        
        ╚══════╝╚══════╝╚══════╝ ╚═════╝   ╚═╝   ╚═╝  ╚═╝╚═╝ ╚═════╝        
                                                                    
        ███████╗██╗  ██╗███████╗███████╗██████╗     ██╗███╗   ██╗ ██████╗   
        ██╔════╝██║  ██║██╔════╝██╔════╝██╔══██╗    ██║████╗  ██║██╔════╝   
        ███████╗███████║█████╗  █████╗  ██████╔╝    ██║██╔██╗ ██║██║        
        ╚════██║██╔══██║██╔══╝  ██╔══╝  ██╔═══╝     ██║██║╚██╗██║██║        
        ███████║██║  ██║███████╗███████╗██║         ██║██║ ╚████║╚██████╗██╗
        ╚══════╝╚═╝  ╚═╝╚══════╝╚══════╝╚═╝         ╚═╝╚═╝  ╚═══╝ ╚═════╝╚═╝   
{/color}{/font}{/cps}
Please type {b}login <username>{/b} to log in, or {b}help{/b} for a list of available commands.  If you become lost on any screen, type {b}look{/b} or {b}l{/b} (lowercase L) to see the original prompt again."""
    
    $say()
    
    while True:
        $echo()
        
        if cmd.upper() not in expected:
            python:
                eastered = False
                for word in easters:
                    if cmd == word or args == word or word in args:
                        easter(word)
                        eastered = True
                
                if not eastered:
                    input_error()
        
        elif cmd.upper() == "LOOK" or cmd.upper() == "L":
            if len(args) == 0:
                $flush_input()
                nvl clear
                jump login
            else:
                $has_args()
                
        elif cmd.upper() == "HELP" or cmd == "?":
            $help()
        
        elif cmd.upper() == "LOGIN":
            if len(args) == 1:
                if args[0] == username:
                    $desc = "Press and hold {b}<ENTER>{/b} for one second for bioauthentication..."
                    $say()
                    
                    play sound "music/scan.ogg"
                    
                    $desc = "{cps=3}...{/cps} {nw}"
                    $say()
            
                    $desc = "{color=#87ceeb}Login successful{/color}!  Welcome, " + username + ".  Press {b}<ENTER>{/b} to proceed."
                    $say()
                    $flush_input()
                    nvl clear
                    jump captcha
                                    
                else:
                    $s = " ".join(args)
                    $flush_input()
                    $desc = "{color=#f00}Error{/color}: Incorrect login '" + s + "'!  Please try again."
                    $say()
            elif len(args) == 0:
                $flush_input()
                $desc = "{color=#f00}Error{/color}: You must supply a username after {b}login{/b}."
                $say()
            else:
                $flush_input()
                $desc = "{color=#f00}Error{/color}: Please type {b}login <username>{/b} to log in.  Your username is only one word."
                $say()
            
    return

# CAPTCHA
label captcha:
    $expected = []
    $pickup = []
    $room = "CAPTCHA"
    $desc = """{cps=0}{font=font/AnonymousPro.ttf}{color=#ffd700}
                                                                              
             --    ./                 `:/+-`                  :dmmmmh+.       
       my   -MN-   yy                yMMmdMM+    h/     `d.   oMM::+yNM:      
       sM-  ymNd  .m/                MM.  +Mm   `No     -M:   .MN    sM.      
        dm`:M+:m. dm  myys+.         +MNs-dN-   .MmddhhhNM-   /MM--+yMN`      
        :Mo/d  +m.Mo dh   sN-      `yNs:+dMh`   .Mo``  .yM-   `NMNmmho`       
         omm.  .NMN` yN:  oM-      +Md    oMh   :M-     oN    -MM`            
          yh`   /y:   /ydhs-       :MMs/:/mM+   -d`     -s    .MM`            
                                    -odddds:                   /+        
{/color}{/font}{/cps}
Please enter the case-sensitive CAPTCHA above to prove that you are human.  Do not include any spaces."""
    
    $say()
    
    while True:
        $echo()
        
        if cmd == "Wo8HP":
            $flush_input()
            $desc = "Your network authentication has been approved.  Press {b}<ENTER>{/b} to proceed."        
            $say()
            $flush_input()
            
            nvl clear
            jump mainscreen
        
        else:
            $flush_input()
            $desc = "Your response has been flagged for Human Resources review.  Press {b}<ENTER>{/b} to proceed."
            $say()

            $flush_input()
            nvl clear
            jump mainscreen
            
    return