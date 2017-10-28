init -1 python:

  ## PRECONDITION: each chat must have at least three questions
  ## NOTE: we're going to need to grab getQuestions() and concatenate it
  ##       to $expected in order to validate user inputs... Christ.
  ##
  ## NOTE: a question has key 'entry', corresponding to the user input
  ##       a follow-up question to that question has key 'entry<X>'
  ##       e.g. 'entry' = 'JOKE', follow-ups are 'entry2, entry3'
  class Chat:

    ## Members:
    # id: unique identifier for the chat; used in $chatlist
    # isHuman: False if AI, True if human
    # color: hexcode value to display target text
    # questions: DICT { 'entry' : 'Question text' } - for displaying
    # asked:     LIST containing 'entry's of questions already asked
    # answers:   DICT { 'entry' : 'Answer test' }   - target response
    # followupQ: DICT { 'entry' : 'Followup text' } - for displaying
    # followupA: DICT { 'entry' : 'Followup text' } - target response
    # qList: LIST containing three options for the player:
    #           first element is a follow-up, if relevant
    #           other elements are available questions
    #           if qList empty, force the report
    # currentQ:  used for state storage (e.g. knowing when to wipe followup)
    
    # Note: 'entry' is the inputcode that the user enters to reference a question
    #  since all answers and follow-ups derive from the question that is asked,
    #  we can use this as the associated key for everything having to do with it

    ## 
    ##  Constructor - no validation of inputs
    ##                YOLO
    def __init__(self, id, isHuman, color, questions, answers, followupQ, followupA):
      self.__id = id
      self.__isHuman = isHuman
      self.__color = color
      self.__questions = questions
      self.__asked = []
      self.__answers = answers
      self.__followupQ = followupQ
      self.__followupA = followupA
      self.__qList = []
      self.__currentQ = "NONE"
    
    
    ##
    ##  ACCESSORS
    ##
    
    # getID() -> String
    def getId(self):
      return self.__id
    
    # isHuman() -> Bool
    def isHuman(self):
      return self.__isHuman
      
    # color() -> String (color ID)
    def color(self):
      return self.__color
    
    # getQuestions() -> list of Strings
    # list comprised of: follow-up, if any, plus available questions
    # return list max size 3 (for screen density)
    def getQuestions(self):     
      return self.__qList
    
    # getAnswer(question) -> String
    def getAnswer(self, question):
      return self.__answers[question]
  
    # getFollowupQ(question) -> String
    # Text of follow-up question, used for printing to terminal
    def getFollowupQ(self, question):
      return self.__followupQ[question]
    
    # getFollowupA(question) -> String
    def getFollowupA(self, question):
      return self.__followupA[question]
    
    # isQuestion(key) -> Bool
    def isQuestion(self, key):
      return key in self.__questions
    
    # isFollowup(key) -> Bool
    def isFollowup(self, key):
      return key in self.__followupQ
      
    
    ##
    ##  MUTATORS
    ##

    # addAsked(question): adds question to asked list
    def __addAsked(self, question):
      self.__asked.append(question)


    ## 
    ##  METHODS
    ##

    # start()
    # Sets chat to engaged state, initializes qList
    def start(self):
      # Special class of chat - only add START key
      if "START" in self.__questions.keys():
        self.__qList.append("START")
      else:
        self.__qList = self.__questions.keys()[:3] # get first three questions
    
    # reportAsHuman(Bool)
    # report is True for reporting human, False for reporting AI
    def reportAsHuman(self, report):
      global right
      global wrong
      
      if report == self.isHuman():
        right += 1
      else:
        wrong += 1
      
      return
      
    # questionFormat()
    def questionsOutput(self):
      outputString = "\n"
      for q in self.__qList:
        if q.isalpha():
          lineString = "  * {color=" + highlight1 + "}" + q + "{/color}: " + self.__questions[q] + "\n"
        else:
          lineString = "  * {color=" + highlight1 + "}" + q + "{/color}: " + self.__followupQ[q] + "\n"
        outputString += lineString
      
      if self.__currentQ != "NONE" and "START" not in self.__questions.keys():
        outputString += "  * {color=" + highlight1 + "}REPORT{/color} <AI/HUMAN>"
      
      return outputString
      
    # userFormat(outputText) -> String (formatted for terminal output)
    def userFormat(self, text):
      outputString = "{cps=0}{color=#" + usercolor + "}{b}" + username + "{/b}{/color}{/cps}: " + text + "{nw}"
      
      return outputString
      
    # typingMessage() -> String (formatted for terminal output)
    # Interlude between user question being asked and target reply
    def typingMessage(self):
      outputString = "{cps=0}{color=#" + self.__color + "}{b}" + self.__id + "{/b}{/color}{/cps} is typing{cps=2}...{/cps}{nw}"
      
      return outputString
      
    # targetFormat(outputText) -> String (formatted for terminal output)
    def targetFormat(self, text):
      
      # Prepend target username in user color
      outputString = "{cps=0}{color=#" + self.__color + "}{b}" + self.__id + "{/b}{/color}{/cps}: " + text + "{nw}"
            
      return outputString
    
    # asked(question) -> Bool
    def asked(self, question):
      return question in self.__asked
      
    # queueQuestion(): adds one new question to qList, if available
    def __queueQuestion(self):
      if len(self.__qList) < 3:
        questions = self.__questions.keys()
        for question in questions:
          if not self.asked(question) and question not in self.__qList:            
            self.__qList.append(question)
            return 
          
    # ask(question)
    def ask(self, question):
    
      global desc
    
      # Get question
      q = question.upper()
    
      # Validate question
      if q not in self.__qList:
        # If invalid, error out and return
        return
      
      # Question key is valid
      else:      
      
        # Question is asked, removed from qList
        self.__qList.remove(q) 
      
        # Remove all previous follow-up questions on key, set currentQ
        lastQ = self.__currentQ
        self.__currentQ = q
        isFollow = False
        
        # Add current question to asked, set it as currentQ
        self.__addAsked(q)
        
        
        if lastQ == "NONE" and q == "START":
          self.__qList.append("QUESTIONS")
        else:
          self.__queueQuestion()
          
        if q == "QUESTIONS" and "START" in self.__questions.keys():
          self.__queueQuestion()
          self.__queueQuestion()
        
        if lastQ != "NONE":
        
          # If previous question was a follow-up, get the main key
          if lastQ[-1:].isnumeric():
            isFollow = True
            lastQ = lastQ[:-1]
        
          # Remove all questions that are key<#>
          for key in self.__qList:
            if key[:-1] == lastQ:
              self.__qList.remove(key)
              self.__queueQuestion()
               
        # If it has follow-up questions, add it to the qList
        for f in self.__followupQ.keys():
          if q == f[:-1]:
            self.__qList.insert(0, f)
            if len(self.__qList) > 3:
              self.__qList.pop()
        
        if q[-1:].isnumeric():
          # OUTPUT: Print player follow-up question text to terminal
          desc = self.userFormat(self.__followupQ[q])
          renpy.music.play("music/tx.ogg", channel="sound")
          say()
          
          # TODO: Some kind of wait, or target is typing interlude?
          desc = self.typingMessage()
          say()
      
          # OUTPUT: Print target answer to terminal
          desc = self.targetFormat(self.__followupA[q])
          renpy.music.play("music/rx.ogg", channel="sound")
          say()
          
          
        else:
          # OUTPUT: Print player question text to terminal
          desc = self.userFormat(self.__questions[q])
          renpy.music.play("music/tx.ogg", channel="sound")
          say()
                  
          # TODO: Some kind of wait, or target is typing interlude?
          desc = self.typingMessage()
          say()
      
          # OUTPUT: Print target answer to terminal
          desc = self.targetFormat(self.__answers[q])
          renpy.music.play("music/rx.ogg", channel="sound")
          say()
          
    
    
    
    
