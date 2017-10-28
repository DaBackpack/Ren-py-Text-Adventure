label c_demo0:
    $expected = ["look", "l", "help", "?", "1"]
    $pickup = []
    $room = "Chat: c_demo0"
    $update_roomlabel()
    $desc = """You are now chatting with '{color=#ff1493}c_demo0{/color}'.  In these chats, you will be given a list of options for what you can say, prefixed by a number.  Enter the number of the conversation option you wish to pursue.
    
    <{color=#fffaf0}1{/color}> You see a young child crying in the street.  What do you do?"""
    
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
                jump c_demo0
            else:
                $has_args()
                
        elif cmd == "help" or cmd == "?":
            $help()
            
        elif cmd == "1":
            if len(args) == 0:
                # Correct input
                $desc = "{color=#fffaf0}{b}[username]{/b}: You see a young child crying in the street.  What do you do?"
                $say()
                jump c_demo0_1
                
            else:
                $desc = "Please enter only the number of the conversation option you wish to pursue."
                $say()
                    
    return
    
label c_demo0_1:
    $expected = ["look", "l", "help", "?", "1", "2", "3", "report"]
    $pickup = []
    $room = "Chat: c_demo0"
    $desc = """{color=#ff1493}{b}c_demo0{/b}: I would go over and help them, or see what's wrong.{/color}
        
    <{color=#fffaf0}1{/color}> That's very kind of you.  Would you worry the child would be afraid of you?
    <{color=#fffaf0}2{/color}> I'm sure the child would appreciate your assistance.
    <{color=#fffaf0}3{/color}> Could you solve for x in the following equation: 
        -3x + 10 = 5x - (-12)"""
    
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
                jump c_demo0_1
            else:
                $has_args()
                
        elif cmd == "help" or cmd == "?":
            $help()
            
        elif cmd == "1":
            if len(args) == 0:
                # Correct input
                $flush_input()
                $desc = "Choice 1"
                $say()
                
#                 jump c_demo0_1
                
            else:
                $desc = "Please enter only the number of the conversation option you wish to pursue."
                $say()
        
        elif cmd == "2":
            if len(args) == 0:
                # Correct input
                $flush_input()
                $desc = "Choice 2"
                $say()
                
#                 jump c_demo0_1
                
            else:
                $desc = "Please enter only the number of the conversation option you wish to pursue."
                $say()
                
        elif cmd == "3":
            if len(args) == 0:
                $flush_input()
                $desc = "Choice 3"
                $say()
                
#                 jump c_demo0_1
                
            else:
                $desc = "Please enter only the number of the conversation option you wish to pursue."
                $say()                    
    return