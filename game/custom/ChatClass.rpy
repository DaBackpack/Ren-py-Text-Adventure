init -1 python:

  ## PRECONDITION: each chat must have at least three questions
  ## NOTE: we're going to need to grab getQuestions() and concatenate it
  ##       to $expected in order to validate user inputs... Christ.
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
      self.__color = "#" + color
      self.__questions = questions
      self.__asked = []
      self.__answers = answers
      self.__followupQ = followupQ
      self.__followupA = followupA
      self.__qList = []
      self.__currentQ = ""
    
    
    ##
    ##  ACCESSORS
    ##
    
    # getID() -> String
    def getId(self):
      return self.__id
    
    # isHuman() -> Bool
    def isHuman(self):
      return self.__isHuman
    
    # getQuestions() -> list of Strings
    # list comprised of: follow-up, if any, plus available questions
    # return list max size 3 (for screen density)
    def getQuestions(self):     
      return qList
    
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
      chatlist.remove(id)                       # can't re-engage this target
      self.__qList = self__questions.keys()[:3] # get first three questions
    
    # reportTarget(Bool)
    # ends the chat
    def reportTarget(self, report):
      # TODO: IMPLEMENT
    
    # asked(question) -> Bool
    def asked(self, question):
      return question in asked
      
    # queueQuestion(): adds one new question to qList, if available
    def __queueQuestion(self):
      for question in self.__questions.key():
        if not asked(question):
          self.__qList.append(question)
          return 
          
    # ask(question)
    def ask(self, question):
    
      # Get question
      q = question
      
      # Flush input
      flush_input()
    
      # Validate question
      if q not in qList:
        # If invalid, error out and return
        # TODO: IMPLEMENT

      else:      
        # Add question to asked
        self.__addAsked(q)
      
        # If question is not follow-up from last, remove follow-up and add 
        # another question if available (top-up to qList size 3)
        if q != self.__currentQ:
          self.__qList.remove(self.__currentQ)
          self.__queueQuestion()
      
        # Remove question from qList, set it to currentQ
        self.__qList.remove(q)
        self.__currentQ = q
      
        # Add another question if available (top-up to qList size 3)
        self.__queueQuestion()
      
        # Print player question text to terminal
      
        # Print target answer to terminal
      
        # If not follow-up, add follow-up to beginning of qList
    
    
    
    
    
    
