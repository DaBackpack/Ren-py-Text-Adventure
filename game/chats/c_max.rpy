label max:
  python: 
    questions = {
      "MATH" : "What is the square root of 17?", 
      "REALJOKE" : "Do you find the following joke humerous: What do you call cheese that isn't yours? Nacho Cheese.", 
      "FAKEJOKE" : "Do you find the following joke humerous: Where do cows go for first dates? Orange you glad I didn't say banana?", 
      "MEMORY" : "What is your earliest memory?", 
      "EMPATHY" : "How do you feel when you hear the sound of a baby crying?"   
    }

    answers = {
        "MATH" : "About 4.",
        "REALJOKE" : "Not really.",
        "FAKEJOKE" : "I don't think you told that joke right.",
        "MEMORY" : "Benny Jenson punching me straight in the gut in the first grade.",
        "EMPATHY" : "Annoyed. Kids drive me nuts."
    }

    followupQ = {
        "FAKEJOKE1" : "How do you tell it right?",
        "MEMORY1" : "Why did Benny Jenson do that?",
        "EMPATHY1" : "What would you do?",
    }

    followupA = {
        "FAKEJOKE1" : "IDK... something like, where do cows go on dates?... The 'moo'vies. Probably.",
        "MEMORY1" : "I don't want to talk about it.",
        "EMPATHY1" : "I would try to make the kid stop crying."
    }

    target = Chat("Max", 1, darkcyan, questions, answers, followupQ, followupA)
    target.start()

label maxStart:

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
                jump maxStart
            else:
                $has_args()
                
        elif cmd.upper() == "HELP" or cmd == "?":
            $help()
            
        elif cmd.upper() == "REPORT":
            if len(args) == 1:
                # Correct input
                
                call attk7 from _call_attk7
                                
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