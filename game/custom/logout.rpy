label force_logout:
    
    $expected = ["LOOK", "L", "HELP", "?", "LOGOUT"]
    $pickup = []
    $room = "Logout"
    $update_roomlabel()
    $desc = """{cps=150}
    Your work day is now over.  Please log out of your session with the {b}logout{/b} command.{/cps}"""
    
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
                jump force_logout
            else:
                $has_args()
                
        elif cmd.upper() == "HELP" or cmd == "?":
            $help()
        
        elif cmd.upper() == "LOGOUT":
            if len(args) == 0:
                $flush_input()
                $desc = """Your screenings for today have been registered with the system and will be corroborated with external interviews with the candidates.  You will be rewarded for each screening you classified correctly, and your employee status will be updated upon your next login.  Goodbye."""
                $say()
                $flush_input()
                
                $displayname = "logged out"
                nvl clear
#                 jump next_day   # DEMO BUILD
                jump demo_end
            else:
                $has_args()
            
    return
    
label next_day:

    $new_day()
    
    jump login
    

label demo_end:

  $desc = """\n\n\n\n\n\n\n\n           This concludes the game demo.  Thanks for playing!"""
  $say()
  
  return
                
                