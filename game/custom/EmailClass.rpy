init -1 python: 

  class Email:

    ##
    ## Constructor
    ##
    
    # Initialize the Email:
    #     id:   String - unique identifier, used in $emaillist
    #     text: String - pre-formatted for terminal output
    # No validation is done on inputs.
    def __init__(self, id, subj, tx, rx, text):
      self.__id = id
      self.__read = False
      self.subj = subj
      self.tx = tx
      self.rx = rx
      self.__text = text
      

    ##
    ##  Accessors
    ##
    
    # getId() -> String
    def getId(self):
      return self.__id

    # getRead() -> Bool
    def getRead(self):
      return self.__read
      
    # getReadColor() -> Char
    def getReadColor(self):
    
      global highlight1
      global highlight2
      
      if self.__read:
        return highlight1
      else:
        return highlight2
    
    # getSubj() -> String
    def getSubj(self):
      return self.subj

    # getText() -> String
    def __getText(self):
      return self.__text


    ## 
    ##  Mutators
    ## 
    
    # setRead(): sets read flag
    def __setRead(self):
      self.__read = True

    ##
    ##  Methods
    ## 
    
    # read() -> String
    # The programmatic way to interact with an email in the game
    def read(self):
      outputString = ""
      
      # TODO: Time increment?
      self.__setRead()
      
      # Format output string          |15                                     |40
      outputString = "\n{cps=100}{color=#" + highlight1 + "}"
      outputString += "===== [[ Email: " + self.getId() + "] ==========================\n\n"
      outputString += "  {b}From{/b}: " + self.tx + "\n"
      outputString += "  {b}To{/b}: " + self.rx + "\n"
      outputString += "  {b}Subject{/b}: {i}" + self.subj + "{/i}\n\n"
      outputString += self.__text + "\n\n"
#       outputString += "{color=#" + highlight1 + "}"
      outputString += "===== [[ message ends ] ========================={/color}{/cps}{nw}"
      
      return outputString
      

      