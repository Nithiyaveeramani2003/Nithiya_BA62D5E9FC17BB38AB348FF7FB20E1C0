# Define the base class player
class player:
  def play(self):
      print("The player is the playing cricket.")
# Define the drived class Batsman
class Batsman(player):
  def play(self):
      print("The batsman is batting.")
# Define the derived class Bowler
class Bowler(player):
  def play(self):
      print("The bowler is bowling.")
# crate object of batman and Bowler classes
batsman = Batsman()
bowler = Bowler()
# call the play() method for each object
batsman.play()
bowler.play()