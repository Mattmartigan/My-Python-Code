import sys
class Intro:
    def __init__(self):
       
        print("Welcome to BORING ADVENTURE GAME!!!\n")
        if input("Press ANY key to start. Type 'skip' to skip the boring intro. ").upper() != "SKIP":
            input("\nCONGRATULATIONS! You found the 'ANY' key! :DDDDDDD")
            input("\n\n\n\n\nYou are person who happens to go by the name of 'Hum'.")
            input("\nYou are 'Hum Drum' from Dullsville and you are a very easily entertained person.\n")
            input("\nHello Hum Drum.\n")
            input("\nYou like to go on long uneventful walks through the city.\n")
            input("\nWhile on you're daily dull walk, you come upon Boring Manner like you always do. \nInstead of passing it by you are hit with sudden flash of something.  \nCould it be... 'CURIOSITY!?'")
            input("\nYou think to yourself, \"I've never been curious about anything in my entire life!\"")
            input("\nYou are very dull after all.")
            input("\nYou immediately dismiss the fealing and walk on by as if nothing ever happened \nand go about your day, dull as ever!")
            input("\nThe next day you take the same walk by the same Boring Manner \nand you get the same flash of curiosity.")
            input("\nInstead of walking on by you stop this time and debate with yourself whether or not you should go take a closer look.")
            input("\nWhat is it about that manner?  How could it possibly be more entertaining than your daily walk which you love?")
            input("\nWhat if there were 'art' being displayed on the walls!?")
            input("\nThat would be a little too much excitment for you.")
            input("\nYou find yourself walking towards the gate regardless, excitment building with each step.")
            input("\nYou are in front of the gate now, hands with sweaty palms raising, heart pounding in your chest.")
            input("\nYou push on the gate and...")
            input("\nIt's locked.")
            input("\nYou see a small sign on the gate which reads 'Manner closed to the public on weekends.'")
            input("\nRelieved, you decide to give up on your silly flight of fancy and continue \non the remainder of your walk and avoid any heart-attacks today from too much excitment.")
            input("\nAll the remainder of your walk you can't stop thinking about Boring Manner. What could be in it?")
            input("\nThat night you lie awake in bed thinking about it, and the next night too.")
            input("\n'Why am i so curious all of a sudden!?' You think to yourself.")
            input("\nI'de better not let anyone in Dullsville catch on to my curiosity, \nI'de be run out of town for sure!'")
            input("\nThe next day you find yourself in front of the same gate, sweaty palms, \nheart pounding as much as the first time.  The gate, which has a big 'B' on it, \nlooks like an iron gate that has been painted a slightly \nless dull shade of off-white than literally every other house in Dullsville,\nwhich only makes you more excited!")
            input("\nYou raise your hands slowly and begin to push on the gate...")
            input("\n'This is it!' You think. 'I'm doing it!'")      
            input("\nYou can feel the gate starting to give way!")
            input("\nAs you push you feel a tingling going down your spine, \na rush of excitment surging through your veins like you were an astronaut on his first spacewalk!")
            input("\nYou take one step forward and nearly collapse because your knees are so weak!")
            input("\nYou take another step along the plain gray path that leads to the manner")
            input("\nYou take another step...")
            input("\nAnd another step...")
            input("\nAnd ANOTHER step!")
            input("\nYou're confidence is building now!")
            input("\nYou take several more steps towards the big wooden doors that actually have WINDOWS in them!")
            input("\nYou find yourelf laughing out loud as you skip along the pathway!")
            input("\nYou are absolutely giddy with excitement!")
            input("\nYou leap up the front steps onto the front porch and jam your finder into the doorbell and wait eagerly!")
            input("\nA middle aged well dressed woman opens the door and greets you with an excited smile.")
            input("\nAre you here to see the manner!? She asks eagerly.")
            input("\nYes! You reply with zeal.")
            input("\nCome on in!  The lady says, stepping aside.")
            input("\nYou hop though the front door...\nPress any key>>\n\n\n\n\n\n\n\n")

        else:
            None
class Player:
    def __init__(self):
        #endgame is conditioned on both these variables being true
        
        self.west=False
        self.east=False
     
class Room:
    def __init__(self,directions=[]):
        self.directions=("NORTH","EAST","WEST","SOUTH","GO NORTH","GO EAST","GO WEST","GO SOUTH")

    def contents(self):
        #print description of room contents
        None
    def exits(self):
        None
        #print what exits the room has
        #prompt user wich exit to take and load appropriate room
class Entry(Room):
    def __init__(self):
        self.i=None
    def contents(self): #print description of room contents
        print("\nThe entry way is large with the most elegant looking staircases you have ever \n")
        print("seen winding upwards with an iron railing that looks like ivy and steps made of")
        print("\nbeautiful white marble. ")
        print("\nThe floor is made of the same marble and you can see your reflection in it. ")
        print("\nOverhead is the most wonderous looking chandalier you have seen in your life. ")
        print("\nIt's made of milky glass pieces that seems to glow from within.  ")
        print("\nYou gulp loudly in your throat as you gawk at it. You're head is going so \n") 
        print("far back that you start to lean backwards and just barely catch yourself before")
        print("\nyou topple over.")
        print("\nThe lady sees you stumble and asks if you are alright. 'I'm fine', you say.")
        

    def exits(self,direction=None):
        
        if (p.west == True) and (p.east == True): #check if conditions are right for endgame
            print("\n\n\nNow that you have seen everything in Boring manner you feel your heart give out \ndue to too much excitment for one day and you die. \n...\n...\nRIP Hum Drum.")
            sys.exit()
        print("\n\nThere are exits to the East and West.\n") #print what exits the room has
        i=input("\nWhere do you wish to go?") #prompt user wich exit to take and load appropriate room
        if i.upper() in ("GO WEST","WEST"):
            p.west=True
            west.contents()
            west.exits()
            
        elif i.upper() in ("EAST","GO EAST"):
            p.east=True
            east.contents()
            east.exits()
            
        else:
            if i.upper() == "SOUTH": #Game will end if user leaves the manner
                print("\nAfter entering the front door you look around the entry way which is far more \nelegantly decorated than anything you have ever seen...\n\nYou decide it's too much for you and you turn around and flee in terror, never to return.  GAME OVER")
                sys.exit()
            elif i.upper() in r.directions: #if the user types in and exit that doesn't exist
                print("\nThere is no {} exit. You bump into the wall and get a bloody nose, \nwhich is an exciting experience for you!\n".format(i))
                start.exits()
            print("\nYou must enter a direction like 'West' or 'Go west'.\n")
            start.exits()
        
class West_Room(Room):
    def __init__(self):
        self.i=None

    def contents(self):
        print("\nYou walk into the west room. and notice a large elegant dining table. \n\nIt's the longest table you have ever seen in your life. ")
        print("\nYou see about five bronze busts of people you do not know resting on pedastals \n\nalong the wall.")  
        
    def exits(self):
        print("\nThere is an exit to your East.\n")

        i=input("\nWhere do you wish to go?")
        if i.upper() in ("GO EAST","EAST"):
            start.contents()
            start.exits()

        else:
            if i.upper() in r.directions:
                print("\nThere is no {} exit. You bump into the wall and get a bloody nose, \nwhich is an exciting experience for you!\n".format(i))
                west.exits()
            print("\nYou must enter a direction like 'West' or 'Go west'.")
            west.exits()

class East_Room(Room):
    def __init__(self):
        self.i=None

    def contents(self):
        print("\nYou enter a grand library with a stone fireplace and very expensive looking \n\n")
        print("leather chairs around it. You have never seen so many books in all your life.\n\n")
        print("You look up and notice the shelves go all the way up to the second story.\n\n")
        print("As you look up at the towering bookcases you feel dizzy.")
    def exits(self):
        #print what exits the room has
        #prompt user wich exit to take and load appropriate room
        print("\nThere is an exit to the West.\n")
        i=input("\nWhere do you wish to go?")
        if i.upper() in ("GO WEST","WEST"):
            start.contents()
            start.exits()

        else:
            if i.upper() in r.directions:
                print("\nThere is no {} exit. You bump into the wall and get a bloody nose, \nwhich is an exciting experience for you!\n".format(i))
                east.exits()
            print("\nYou must enter a direction like 'West' or 'Go west'.\n")
            east.exits()


intro=Intro()
p=Player()
r=Room()
east=East_Room()
west=West_Room()
start=Entry()
start.contents()
start.exits()                  
                  
