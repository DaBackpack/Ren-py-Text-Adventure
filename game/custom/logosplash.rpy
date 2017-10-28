label logosplash:

  python:
    
    hide_val = True
    
    linesFromTop = 7
    textSpeed = 3
    
    colors = [
      "15db15", # Terminal green             
      "00b200",
      "009900",
      "007f00",
      "006600",
      "004c00",
      "003300",
      "001900",
      "000000",
    ]
  
    splashtop = [
      "        $$$$$$$$\ $$$$$$$$\  $$$$$$\  $$\      $$\    ",
      "        \__$$  __|$$  _____|$$  __$$\ $$$\    $$$ |   ",
      "           $$ |   $$ |      $$ /  $$ |$$$$\  $$$$ |   ",
      "           $$ |   $$$$$\    $$$$$$$$ |$$\$$\$$ $$ |   ",
      "           $$ |   $$  __|   $$  __$$ |$$ \$$$  $$ |   ",
      "           $$ |   $$ |      $$ |  $$ |$$ |\$  /$$ |   ",
      "           $$ |   $$$$$$$$\ $$ |  $$ |$$ | \_/ $$ |   ",
      "           \__|   \________|\__|  \__|\__|     \__|   "
    ]

    splashbottom = [                                                                                          
      "                             $$$$$\ $$$$$$$$\ $$$$$$$$\ $$$$$$$$\ ",
      "                             \__$$ |$$  _____|$$  _____|$$  _____|",
      "                                $$ |$$ |      $$ |      $$ |      ",
      "                                $$ |$$$$$\    $$$$$\    $$$$$\    ",
      "                          $$\   $$ |$$  __|   $$  __|   $$  __|   ",
      "                          $$ |  $$ |$$ |      $$ |      $$ |      ",
      "                          \$$$$$$  |$$$$$$$$\ $$ |      $$ |      ",
      "                           \______/ \________|\__|      \__|      "
    ]
    
    # Run as many times as there are characters
    for charNum in range(1, len(splashtop[0]), textSpeed):
    
      # Clear output
      nvl_clear()
      desc = "{cps=0}"
      
      # Header spacer
      for each in range(linesFromTop):
        desc += "\n"
      
      # Iterate for each line in the logo
      for lineNum in range(len(splashtop)):
      
        # Add x chars from the right side in, plus linebreak
        desc += splashtop[lineNum][-charNum:] + "\n"
      
      # String closer and output
      desc += "{/cps}{nw}"
      say()
      
    # Run the bottom
    for charNum in range(1, len(splashbottom[0]), textSpeed):
    
      # Clear output
      nvl_clear()
      desc = "{cps=0}"
      
      # Header spacer
      for each in range(linesFromTop):
        desc += "\n"
      
      # Start with top already built
      for line in splashtop:
        desc += line + "\n"
      
      # Linebreak between bottom part
      desc += "\n"
      
      # Iterate for each line in the bottom part
      for lineNum in range(len(splashbottom)):
      
        desc += splashbottom[lineNum][-charNum:] + "\n"
      
      # String closer and output
      desc += "{/cps}{nw}"
      say()
    
    # PLAY THAT SOUND
    renpy.music.play("music/jeffname.mp3", channel="sound")
    
    # Make it stick
    nvl_clear()
    
    desc = "{cps=0}"
    for each in range(linesFromTop):
      desc += "\n"
    for line in splashtop:
      desc += line + "\n"
    desc += "\n"
    for line in splashbottom:
      desc += line + "\n"
    desc += "\n\n\n                              {/cps}{cps=10}Presents...{/cps}"
    desc += "{cps=1}  {/cps}{nw}"
    
    say()
    
    # Fade it out
    for color in colors:
    
      # Build each iteration of the color-fade text
      nvl_clear()
      desc = "{cps=0}{color=" + color + "}"
      for each in range(linesFromTop):
        desc += "\n"
    
      for line in splashtop: 
        desc += line + "\n"
    
      desc += "\n"
    
      for line in splashbottom:
        desc += line + "\n"
      
      desc += "\n\n\n                              Presents..."
      desc += "{/color}{/cps}{nw}"
      say()
  
  # Jump to next
  nvl clear
  
  jump titlesplash
      