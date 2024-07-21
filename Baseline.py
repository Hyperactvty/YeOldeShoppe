import datetime
import keyboard
import sys
import math
import random

"""
THOUGHT PROCESS
===============
Either 1500's or 1800's shopkeeper. People bring things to you to either buy, sell, or for things to look out for. 

Horror game, maybe..?

Buy stock at end of day. Takes a few days for some items to arrive. Some items take longer if it comes from distant area.

"Weird things come through those doors..."

Can launder currency through items. Can send money to an undiscloded storehouse.

You can overthrow the monarchy if you so please. Effects:
    - No tax on items
    - Depending on how long the monarchy has been gone, militants or criminals may come in more often. May warrant more hired help to mitigate effect.

"""

class Settings:
  # class Mode:
  #   Morse2Alpha = 0
  #   Alpha2Morse = 1

  def __init__(self):
    return
    # self.inputBuffer = _ib # This is the delay between a long press or a short press
    # self.charBuffer = _cb # This is the delay before the character is converted
    # self.programMode = _pm # The program's mode
    # self.selfTimeout = _sto # Time before the program auto stops

class Item:
  class Origin: 
    Local: 0
    # Make a list of random names, like "Hrgaburt"

  class Rarity:
    Rubbish = {"type": "Rubbish", "col": "gray", "taxRate": 0}
    Common = {"type": "Common", "col": "white", "taxRate": 5}
    Rare = {"type": "Rare", "col": "blue", "taxRate": 10}
    Epic = {"type": "Epic", "col": "purple", "taxRate": 20}
    Legendary = {"type": "Legendary", "col": "orange", "taxRate": 50}
    Exotic = {"type": "Exotic", "col": "red", "taxRate": 0, "desc": "You shouldn't have this..."} # red or black may be fitting
    Cursed = {"type": "Cursed", "col": "dark_red", "taxRate": 0, "desc": "You shouldn't have this..."}

  def __init__(self, _n: str, _d: str, _r: Rarity, _p: int, _o: Origin):
    self.name = _n
    self.description = _d
    self.rarity = _r
    self.price = _p
    self.origin = _o

class Storehouse:
  stock = {}
  def getStock():
    return Storehouse.stock

  def getBank(): # Money you don't want found. Dirty money can be laundered.
    return

class Input:
  def __init__(self, _is=0, _ie=0):
    self.inputStart = _is
    self.inputEnd = _ie
  
class Mechanics:
  class General:
    class Weather:
      Clear: 0
      Cloudy: 1
      Rain: 2
      Windy: 3
      EclipseLunar: 100
      EclipseSolar: 101
      EndOfTimes: 666
    
    """
    Having a good affinity determines how much tax you **may** have to pay
    """
    class Affinity:
      Hunted: -5
      Hated: -4
      Hostile: -3
      Corrupt: -2
      Disliked: -1
      Neutral: 0
      Liked: 1
      Favorable: 2
      Loved: 3
      Respected: 4
      Adored: 5

    data={
      "date": datetime.datetime(1500, 5, 1, 8, 0, 0),
      "weather": 0, #Weather.Clear,
      "taxCollectionDate": 7, # 7 days (maybe)
      "propertyTaxDate": -31, # -31 for "end of month" 
      # "factions": {
      #   "Monarchy":Affinity.Neutral,
      #   "Thieves":Affinity.Neutral,
      #   "Merchant":Affinity.Neutral
      # }
    }
    def currencyConverter(_amt: int):
      gold=math.floor(_amt/10000); _amt-=gold*10000
      silver=math.floor(_amt/100); _amt-=silver*100
      copper=_amt
      return {"g": gold, "s": silver, "c": copper}
    
    def __init__(self) -> None:
      data={
        "date": datetime.datetime(1500, 5, 1, 8, 0, 0),
        "weather": Mechanics.General.Weather.Clear,
        "taxCollectionDate": 7, # 7 days (maybe)
        "propertyTaxDate": -31, # -31 for "end of month" 
        # "factions": {
        #   "Monarchy":Affinity.Neutral,
        #   "Thieves":Affinity.Neutral,
        #   "Merchant":Affinity.Neutral
        # }
      }

  class User:
    def buy():
      return
    def sell():
      return
    def haggle():
      return

    def stockOrder():
      return
    def callGuards():
      # If a sketchy looking fella arrives, toss 'em out!
      return
      
    def __init__(self, _is=0, _ie=0):
      self.inputStart = _is
      self.inputEnd = _ie
  
class Npc:
  class NPC_TYPE:
    Civilian: 0
    Merchant: 1
    Wizard: 4
    Guard: 10
    Thief: 11
  
  class Status:
    _None: None
    Buying: 0
    Selling: 1
    LookingFor: 2

  npcStats = {
    "name": None,
    "faction": None,
    "type": 0, #NPC_TYPE.Civilian,
    "status": None, # Status.Buying,
    "attribute": None,
  }
  def getAttributes(self):
    return self.npcStats

  def new(self):
    attributeTemplate = {
      "armLeft": [
        "normal","stolen"
      ],
      "armRight": [
        "normal","stolen"
      ],
      "legLeft": [
        "normal","stolen","pegLeg"
      ],
      "legRight": [
        "normal","stolen","pegLeg"
      ]
    }
    att = [_a for _a in attributeTemplate.items()]
    for _bp,_a in att:
      attChance = random.randint(0,5)/5
      print(f"The Att of {_bp}: {_a} | {attChance}")
      attributeTemplate[_bp] = random.choice(_a[1:]) if attChance >= 0.8 else _a[0]
    self.npcStats["attributes"] = attributeTemplate
    print(f"\tNPC CREATED -> {attributeTemplate}")
    return
  
  def __init__(self) -> None:
    npcStats = {
      "name": None,
      "faction": None,
      "type": 0, # Npc.NPC_TYPE.Civilian,
      "status":0, # Npc.Status.Buying,
      "attribute": None,
    }
    

class User:

  def getStats(self):
    return self.stats

  def getCurrency(self):
    return self.stats["currency"]["data"]
  def setCurrency(self, _amt: int):
    self.stats["currency"]["data"] = _amt
    
  def __init__(self, _name="Generic-o"):
    self.name = _name
    self.stats = {
      "currency": {"data": 250, "alt": None},
      "itemsSold": {"data": 0, "alt": "Items Sold"},
      "totalCurrency": {"data": 0, "alt": "Total Acquired Currency"},
      "factions": {
        "Monarchy":None, # Mechanics.General.Affinity.Neutral,
        "Thieves":None, # Mechanics.General.Affinity.Neutral,
        "Merchant":None # Mechanics.General.Affinity.Neutral
      }
    }


class System:
    # def getCode(_s: Settings.Mode, _c: str, _reverse: bool=False):
    #   if(_s==Settings.Mode.Alpha2Morse): _c=_c.upper()
      
    #   vals = MorseLexicon.values() if _s == (Settings.Mode.Morse2Alpha if _reverse==False else Settings.Mode.Alpha2Morse) else MorseLexicon.keys()
    #   if not any(_c in q for q in vals): return
    #   res=""
    #   if(_s == (Settings.Mode.Morse2Alpha if _reverse==False else Settings.Mode.Alpha2Morse)):
    #     res = [r for r, q in MorseLexicon.items() if q == _c]
    #     if(res==[]): return
    #     res=res[0]
    #   else:
    #     res = MorseLexicon[_c]
    #   if(res==[]): return
    #   return res#[0]

  @staticmethod
  def main():
    # region Initialization
    settings = Settings()
    gm = Mechanics()
    npc = Npc()
    storehouse = Storehouse()
    user = User()
    # endregion Initialization

    # Testing
    user.setCurrency(user.getCurrency() + 375)
    print(f"tmp stats -> {user.getStats()}")
    print(f"Currency -> {gm.General.currencyConverter(user.getCurrency())}")
    
  #   mode = next(_m for _m in _mode) # sys.argv
  #   MODES = {"morse": Settings.Mode.Morse2Alpha, "alpha": Settings.Mode.Alpha2Morse }
  #   if(next(_m for _m in _mode) in list(MODES.keys())): mode = MODES[mode]
  #   else:
  #     print(f"IMPORTANT:  Mode was not specified. Running program in [MORSE]")
  #     mode=MODES["morse"]
  #   user_input = Input()

  #   input_registered = False
  #   char_registered = False
  #   program_started = True
  #   cBuf = datetime.datetime.now()
  #   elapsed_ticks = (datetime.datetime.now() - cBuf).total_seconds()
  #   timeFromLastInput=0.0
  #   code = ""; codeBuffer=""; codeString = ""
    print("Press ESC to stop")
    while True:
      if(keyboard.is_pressed('escape')): print("\nPROGRAM TERMINATED"); break
      
      # TESTING
      tmpCiv = npc.new()

      event = keyboard.read_event()
      # THIS IS WHERE THE PROGRAM HALTS UNTIL AN INPUT IS PRESSED
      if event.event_type == keyboard.KEY_DOWN:# and event.name != '>':
        # Set here the methods for each key event
        keyShortcuts = {
          "b" : "buy",
          "s": "sell",
          "h": "haggle",
        }
        key = keyShortcuts.get(event.name) if keyShortcuts.get(event.name) != None else event.name
        
      # return { "msg": None, "status": -1 }

  #       # something about char_registered to get around the first tick geing counted
  #       if(program_started==True and mode==Settings.Mode.Morse2Alpha):
  #         if keyboard.is_pressed('space'):
  #           program_started=False
  #           elapsed_ticks = 0
  #           cBuf = datetime.datetime.now()
  #         else: continue
  #       else: elapsed_ticks = (datetime.datetime.now() - cBuf).total_seconds()
        
  #       # ALPHA2MORSE
  #       if(mode==Settings.Mode.Alpha2Morse):
  #         res = MorseProgram.alpha2Morse(codeString)
  #         if(res["msg"]==None or res["status"]==-1): continue # to avoid "ghost" (non-alpha inputs) or "repeat" inputs
  #         _cs = res["msg"]
  #         codeString = _cs if _cs!=None and type(codeString)!=type(None) else codeString
  #         cBuf=datetime.datetime.now()
  #         print(f"\n{codeString}", sep=' ', end='', flush=True)
  #         print() # Temp, maybe
  #         for _c in codeString:
  #           c=MorseProgram.getCode(mode, _c, False)
  #           print(c, sep=' ', end=' ', flush=True)

  #         continue
        
  #       if(elapsed_ticks > settings.charBuffer and char_registered==False):
  #         char_registered=True
  #         cs = MorseProgram.getCode(mode, code)
  #         if(cs==None):  # Have this reset the current "input"
  #           code=""
  #           char_registered = True
  #           elapsed_ticks=0
  #           print("\nInvalid Input")
  #           MorseProgram.codeOutput(settings,codeString,codeBuffer)
  #           continue
  #         if(cs in ["........", "RE-MORSE"]): # Deletes up to last space
  #           code=""
  #           char_registered = True
  #           elapsed_ticks=0
  #           # reMorse = codeString.split(" ")[:-1].join(str(_c) for _c in codeString.split(" ")[:-1])
  #           codeBuffer = reMorse = ""
  #           program_started=True
  #           print(f"\nYou show re-morse...")
  #           MorseProgram.codeOutput(settings,codeString,codeBuffer)
  #           continue
  #         # codeString += cs
  #         codeBuffer += cs
  #         code = ""
  #         print(f"\n{codeString}> {codeBuffer}")
  #         # Runs through the existing code
  #         MorseProgram.codeOutput(settings,codeString,codeBuffer)
  #       # if not console_key_available():
  #       if keyboard.is_pressed('space'):
  #         if input_registered:
  #             input_registered = False
  #             char_registered = False
  #             cBuf = datetime.datetime.now()
  #             elapsed_ticks = (datetime.datetime.now() - cBuf).total_seconds()
  #       else:
  #           if not input_registered:
  #               input_registered = True
  #               elapsed_ticks = (datetime.datetime.now() - cBuf).total_seconds()
  #               cBuf = datetime.datetime.now()
  #               timeFromLastInput=elapsed_ticks
  #               input_registered_as = "-" if elapsed_ticks > settings.inputBuffer else "."
  #               # print(f"Input held for {elapsed_ticks} -> Input registered as {input_registered_as}")
  #               print(input_registered_as, sep=' ', end='', flush=True)
  #               code+=input_registered_as
  #               # For the reset (..?)
  #               # print(f"{elapsed_ticks}")

  #               # reset()

  #           # Space Integration
  #           if(elapsed_ticks-timeFromLastInput > settings.charBuffer*4):
  #             cs = MorseProgram.getCode(mode, "/")
  #             print("/", sep=' ', end=' ', flush=True)
  #             codeString += codeBuffer + cs
  #             codeBuffer=""
  #             program_started=True

  # def codeOutput(mode,codeString,codeBuffer):
  #   for _c in codeString+codeBuffer:
  #     c=MorseProgram.getCode(mode, _c, True)
  #     print(c, sep=' ', end=' ', flush=True)

  # def alpha2Morse(_cs: str):
  #   event = keyboard.read_event()
  #   # THIS IS WHERE THE PROGRAM HALTS UNTIL AN INPUT IS PRESSED
  #   if event.event_type == keyboard.KEY_DOWN:# and event.name != '>':
  #     cStr=_cs
  #     keyShortcuts = {
  #       "space" : " ",
  #       "backspace": "backspace"
  #     }
  #     key = keyShortcuts.get(event.name) if keyShortcuts.get(event.name) != None else (event.name if len(event.name)==1 and event.name.isalnum() else None)
  #     if(key=="backspace"): return { "msg": cStr[:-1], "status": 200 }
  #     if(key==None): return { "msg": cStr, "status": -1 }
  #     cStr += key
  #     return { "msg": cStr, "status": 200 }
  #   return { "msg": None, "status": -1 }


if(__name__ == "__main__"): System.main()