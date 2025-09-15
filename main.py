from save_load import save_game , load_game,show_resources
from game_state import initial_game_state,production_inc,change_time,give_time,daily_consumptions,food_productions
from squads import show_squads,send_squad,Squad_came,Manage_sqd
from farming import Manage_farm
from manage import Adapt_build
from shelter import show_shelter
gamedata = load_game()
if not gamedata:
    gamedata = initial_game_state()

def main():
    while True:
        print("\n-------- The Last Survivors --------")
        give_time(gamedata)
        print("="*36)
        print("1. Show Squads")
        print("2. Show shelter")
        print("3. Send Squad")
        print("4. Show Resources")
        print("5. End Day")
        print("6. Manage")
        print("0. Exit")
        choice = input("---------> ")
        if choice =="1":
            show_squads(gamedata)
        elif choice =="2":
            show_shelter(gamedata)
        elif choice =="3":
            send_squad(gamedata)
        elif choice =="4":
            show_resources(gamedata)
        elif choice =="5":
            production_inc(gamedata)
            #daily_consumptions(gamedata)
            food_productions(gamedata)
        elif choice =="6":
            while True:
                print("1. Farming")
                print("2. Adapt Building")
                print("3. Manage Shelter")
                print("0. Exit")
                inner_choice = input("---------> ")
                if inner_choice =="1":
                    Manage_farm(gamedata)
                elif inner_choice =="2":
                    Adapt_build(gamedata)
                elif inner_choice =="3":
                    #Manage_survivors(gamedata)
                    pass
                elif inner_choice =="0":
                    break
                else:
                    print(" ❌  Invalid Choice !!")
        else:
            print(" ❌  Invalid Choice !!")
        Squad_came(gamedata)
        change_time(gamedata)
        save_game(gamedata)
main()