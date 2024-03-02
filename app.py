
import lib


################## HOC #####################
lib.readDestinations()
lib.readPrice()
while lib.running:
    lib.renderMenu() 
    if lib.option == 1 :
        lib.searchDestination()
    if lib.option == 2:
        lib.renderDestinations()
    if lib.option == 3:
        lib.renderPrice()
    if lib.option == 4:
        lib.writedPrice()
    if lib.option == 5:
        lib.renderOrder()
    if lib.option == 6:
        lib.canceOrder()
    if lib.option == 0:
        running = False





    