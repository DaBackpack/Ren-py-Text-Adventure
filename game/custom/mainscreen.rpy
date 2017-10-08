label mainscreen:
    $expected = ["look", "l", "help", "?", "mail.app", "chat.app"]
    $pickup = []
    $room = "Home"
    $desc = """{cps=150}<PLACEHOLDER: This is the main screen> Login: MOTD, graphics, etc. here{/cps}
    
Available programs: <{color=#87ceeb}mail.app{/color}>, <{color=#87ceeb}chat.app{/color}>"""
    
    $say()
    
    while True:
        $echo()
        
        if cmd not in expected:
            $input_error()
        
        elif cmd == "look" or cmd == "l":
            if len(args) == 0:
                $flush_input()
                nvl clear
                jump mainscreen
            else:
                $has_args()
                
        elif cmd == "help" or cmd == "?":
            $help()
        
        elif cmd == "mail.app":
            if len(args) == 0:
                $flush_input()
                $desc = "Starting mail.app{cps=2}... ... ...{/cps} {cps=130}Ready!{/cps}\n" \
                        "Press {b}ENTER{/b} to continue to mail."
                $say()
                nvl clear
                jump mail
            else:
                $has_args()
        
        elif cmd == "chat.app":
            if len(args) == 0:
                $flush_input()
                $desc = "Starting chat.app{cps=2}... ... ...{/cps} {cps=130}Ready!{/cps}\n" \
                        "Press {b}ENTER{/b} to continue to chat."
                $say()
                nvl clear
                jump chat
            else:
                $has_args()
            
    return