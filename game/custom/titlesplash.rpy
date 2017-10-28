label titlesplash:

  python:
    
    hide_val = True
    
    size = 15
    linesFromTop = 15
    frames = 10

    colors = [
      "000000", # Black
      "000000", # Black
      "000000", # Black
      "000000", # Black
      "000000", # Black
      "000000", # Black
      "000000", # Black
      "000000", # Black
      "000000", # Black
      "000000", # Black
      "000000", # Black
      "000000", # Black
      "000000", # Black
      "2f4f4f", # SlateGrey
      "696969", # DimGrey
#       "708090", # SlateGrey
      "808080", # Grey
      "a9a9a9", # DarkGrey
      "d3d3d3", # LightGrey
      "f8f8ff", # GhostWhite
      "faf0e6", # Linen
#       "ffdead", # NavajoWhite
      "fffff0", # Ivory
      "ffffff", # White
    ]
    
  
    splash = [                                                                              
      "\"8a                                             88                            ",
      "  \"8a           ,d                              \"\"                            ",
      "    \"8a         88                                                            ",
      "      \"8a     MM88MMM  88       88  8b,dPPYba,  88  8b,dPPYba,    ,adPPYb,d8  ",
      "      a8\"       88     88       88  88P'   \"Y8  88  88P'   `\"8a  a8\"    `Y88  ",
      "    a8\"         88     88       88  88          88  88       88  8b       88  ",
      "  a8\"           88,    \"8a,   ,a88  88          88  88       88  \"8a,   ,d88  ",
      "a8\"             \"Y888   `\"YbbdP'Y8  88          88  88       88   `\"YbbdP\"Y8  ",
      "                                                                  aa,    ,88  ",
      "                                                                   \"Y8bbdP\"   "
    ]

    # Play title splash music
    renpy.music.play("music/title.ogg", channel="sound")

    # Run as many times as there are characters
    for color in colors:
      
      # Clear output
      nvl_clear()
      desc = "{cps=0}{size=" + str(size) + "}{color=" + color + "}"
      
      # Header spacer
      for each in range(linesFromTop):
        desc += "\n"
      
      # Iterate for each line in the splash
      for line in splash:
      
        # Add the thing
        desc += line + "\n"
      
      # String closer and output
      desc += "{/color}{/size}{/cps}{nw}"
      say()
    
    # Make it stick
    desc = "{cps=1}   {/cps}{nw}"
    say()
    
    colors.reverse()
  
    # Fade it out now
    for color in colors:
  
      # Clear output
      nvl_clear()
      desc = "{cps=0}{size=" + str(size) + "}{color=" + color + "}"
    
      # Header spacer
      for each in range(linesFromTop):
        desc += "\n"
    
      # Iterate for each line in the splash
      for line in splash:
    
        # Add the thing
        desc += line + "\n"
    
      # String closer and output
      desc += "{/color}{/size}{/cps}{nw}"
      say()
  
  # Jump to next
  nvl clear
  
  jump login_first
      