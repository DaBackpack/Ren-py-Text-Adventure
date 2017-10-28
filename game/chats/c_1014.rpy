label sheep_1014:
  python:
    questions = {
      "START" : "I'm ready to begin the training session.",
      "QUESTIONS" : "What are the pre-approved questions?",
      "DISCERN" : "How can I use these questions to help me discern between humans and AI?",
      "REPORT" : "What do I do once I think I've figured out whether the candidate is AI or human?",
      "REWARD" : "What happens if I report a candidate correctly or incorrectly?",
      "END" : "I think I've learned everything I need to get started."
    }

    answers = {
      "START": "Welcome, " + username + ".  I am 1014, the AI tutorial bot.  Welcome to the training program.  You will be determining whether candidates are humans or AIs by asking them questions and evaluating their responses.  You can ask any of the daily pre-approved questions to each candidate.",
      "QUESTIONS": """Today's questions are:
    {b}MATH{/b}: Ask the candidate a math question
    {b}REALJOKE{/b}: Tell the candidate a hilarious joke
    {b}FAKEJOKE{/b}: Tell the candidate a joke with an incorrect punchline
    {b}MEMORY{/b}: Ask the candidate about their earliest memory
    {b}EMPATHY{/b}: Ask the candidate a question which tests their empathy.""",
      "DISCERN" : "Look for indicators in the answers you receive that the candidate is AI or human.  For example, AIs with less customization will commonly be more precise when answering mathematical questions than humans.",
      "REPORT" : "You can register a decision at any time after the first answer you receive from a candidate by typing 'REPORT HUMAN' or 'REPORT AI'.",
      "REWARD" : "You will receive gold stars for every candidate you screen correctly.  It is an {i}incentive{/i}.  These stars will be awarded the next working day after the candidate has undergone external assessment based on your screening.",
      "END" : "The tutorial is now complete.  I am going to take a snack break.  I have bits and bytes today.  I will queue up a test candidate for you to screen."
    }

    followupQ = { 
      "DISCERN1" : "Is there anything else that can help me decide?",
      "REPORT1" : "What if I'm not sure if they're human or AI?" 
    }

    followupA = { 
      "DISCERN1" : "One more important indicator is that AIs will often fail to display empathy, unlike humans.  For example, how are you today, " + username + "?  ...Just kidding.  I do not care.",
      "REPORT1" : "You can ask the candidate more questions until you have determined your answer.  If you have used all five questions, you must report them as one or the other based on the answers you have received." 
    }

    target = Chat("sheep_1014", 0, crimson, questions, answers, followupQ, followupA)
    target.start()

label lolaStart:

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
                jump lolaStart
            else:
                $has_args()
                
        elif cmd.upper() == "HELP" or cmd == "?":
            $help()
            
        elif cmd.upper() == "END":
            $q = cmd
            $flush_input()
            
            $target.ask(q)
            
            $expected = []
            $desc = "Press {b}ENTER{/b} to end the tutorial and return to chat.app."
            $say()
            
            $chatlist.append("sheep_1015")
            nvl clear
            jump chat
            
        else:
            if len(args) == 0:
                # Correct input
                $q = cmd
                $flush_input()
                
                # Question and answer
                $target.ask(q)
                
                # Updated $expected with current command options
                $expected = ["LOOK", "L", "HELP", "?"]
                $expected += target.getQuestions()
                
                $desc = "Your chat options are:"
                $desc += target.questionsOutput()
                $say()
                                
            else:
                $desc = "Please enter only the tag of the conversation option you wish to pursue."
                $say()
                    
    return