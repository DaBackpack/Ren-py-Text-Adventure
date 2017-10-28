label sheep_1015:
  python:
    questions = {
      "MATH" : "What is the square root of 17?",
      "REALJOKE" : "Do you find this joke funny:  What do you call cheese that isn't yours?  Nacho cheese!",
      "FAKEJOKE" : "Do you find this joke funny: Where do cows go for first dates?  Orange you glad I didn't say banana?",
      "MEMORY" : "What is your earliest memory?",
      "EMPATHY" : "How do you feel when you hear the sound of a baby crying?"
    }

    answers = {
      "MATH": "4.123105626",
      "REALJOKE": "Very humorous, L.O.L.",
      "FAKEJOKE": "Very humorous, L.O.L.",
      "MEMORY": "Being in a warm room.",
      "EMPATHY": "Sad."
    }

    followupQ = {
      "MATH1": "Did you use a calculator?",
      "MEMORY1": "Describe the room.",
      "EMPATHY1": "What would you do?"
    }

    followupA = {
      "MATH1": "No.",
      "MEMORY1": "Four walls, one roof, one floor.  It was warm.",
      "EMPATHY1": "Nothing.  I was not asked to assist."
    }

    target = Chat("sheep_1015", 0, crimson, questions, answers, followupQ, followupA)
    target.start()

label lola2Start:

    $expected = ["LOOK", "L", "HELP", "?"]
    $expected += target.getQuestions()
    $pickup = []
    $room = "Chat: " + target.getId()
    $update_roomlabel()
    $desc = "You are now chatting with '{b}{color=#" + target.color() + "}" + target.getId() + "{/color}{/b}'.  In these chats, you will be given a list of options for questions you can pose, prefixed by a tag.  Enter the tag of the conversation option you wish to pursue.\n" 
    $desc += target.questionsOutput()
    
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
                jump lola2Start
            else:
                $has_args()
                
        elif cmd.upper() == "HELP" or cmd == "?":
            $help()
            
        elif cmd.upper() == "REPORT":
            if len(args) == 1:
                # Correct input
                
                call info3 from _call_info3
                $chatlist.append("max")                
                
                if args[0].upper() == "HUMAN":
                    # Human Report
                    $desc = "You reported " + target.getId() + " as human.{nw}"
                    $say()
                    $flush_input()
                    $target.reportAsHuman(True)

                    nvl clear
                    jump chat
                
                if args[0].upper() == "AI":
                    # AI Report
                    $desc = "You reported " + target.getId() + " as AI.{nw}"
                    $say()
                    $flush_input()
                    $target.reportAsHuman(False)

                    nvl clear
                    jump chat
                
                else:
                    # Incorrect input
                    $desc = "{color=#" + errorcolor + "}ERROR{/color}: command 'REPORT' must be followed by option 'AI' or 'HUMAN'.  Your chat options are: "
                    $desc += target.questionsOutput()
                    $say()
            
            else:
                # Incorrect input
                $desc = "{color=#" + errorcolor + "}ERROR{/color}: command 'REPORT' must be followed by option 'AI' or 'HUMAN'.  Your chat options are: "
                $desc += target.questionsOutput()
                $say()
            
        else:
            if len(args) == 0:
                # Correct input
                $q = cmd
                $flush_input()
                
                # Question and answer
                $target.ask(q)
                
                # Updated $expected with current command options
                $expected = ["LOOK", "L", "HELP", "?", "REPORT"]
                $expected += target.getQuestions()
                
                $desc = "Your chat options are:"
                $desc += target.questionsOutput()
                $say()
                                
            else:
                $desc = "Please enter only the tag of the conversation option you wish to pursue."
                $say()
                    
    return