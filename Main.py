import Items
import Player

foodItems = []
coffee = Items.FoodItem("Hot Coffee",Items.FoodItem.STATE_LIQUID, Items.FoodItem.TEMP_HOT)
foodItems.append(coffee)

water = Items.FoodItem("Cold Water",Items.FoodItem.STATE_LIQUID, Items.FoodItem.TEMP_COLD)
foodItems.append(water)

veg = Items.FoodItem("Steamed Vegetables",Items.FoodItem.STATE_SOLID, Items.FoodItem.TEMP_HOT)
foodItems.append(veg)

ice_cream = Items.FoodItem("Ice Cream",Items.FoodItem.STATE_SOLID, Items.FoodItem.TEMP_COLD)
foodItems.append(ice_cream)

defenseItems = []

hat = Items.DefenseItem("Chef's Hat",Items.DefenseItem.TYPE_CLOTH,Items.DefenseItem.SIZE_SMALL)
defenseItems.append(hat)

apron = Items.DefenseItem("Apron",Items.DefenseItem.TYPE_CLOTH,Items.DefenseItem.SIZE_LARGE)
defenseItems.append(apron)

bowl = Items.DefenseItem("Chef's Hat",Items.DefenseItem.TYPE_METAL,Items.DefenseItem.SIZE_SMALL)
defenseItems.append(bowl)

sheet = Items.DefenseItem("Chef's Hat",Items.DefenseItem.TYPE_METAL,Items.DefenseItem.SIZE_LARGE)
defenseItems.append(sheet)

playerName = input("What is your name? ")
player1 = Player.Chef(playerName, Player.Chef.TYPE_HUMAN)
player2 = Player.Chef("Robo-Cook", Player.Chef.TYPE_ROBOT)

for i in range(0,2):
  print("\nDING DING! Round {}".format(i))
  player1Food = player1.selectItem(foodItems)
  player1Defense = player1.selectItem(defenseItems)
  player2Food = player2.selectItem(foodItems)
  player2Defense = player2.selectItem(defenseItems)
  player1DefenseBonus = player2Defense.calculateBonus(player2Food)
  player2DefenseBonus = player1Defense.calculateBonus(player1Food)
  player1Score = 100 - player2DefenseBonus
  player2Score = 100 - player1DefenseBonus
  player1.addScore(player1Score)
  player2.addScore(player2Score)
  print("")
  print("{} scored {} by throwing {} against {}'s {}".format(playerName, player1Score, player1Food.name, player2.name, player2Defense.name))
  print("{} scored {} by throwing {} against {}'s {}".format(player2.name, player2Score, player2Food.name, player1.name, player1Defense.name))
  print("Current Scores: {} has {}, {} has {}".format( player1.name, player1Score, player2.name, player2Score))

print("")
print("{} = {}".format(player1.name, player1Score))
print("{} = {}".format(player2.name, player2Score))
