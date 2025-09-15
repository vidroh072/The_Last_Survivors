import random
from scavange_buildings import select_buidling,get_all_buildings

def show_squads(data):
    squads_data = data["squads"]
    print("Squads")
    for squad in squads_data:
        print("","_"*50)
        print("|"," "*20,squad," "*18," |")
        for each in squads_data[squad]:

            if each =="members":
                list_mem = []
                weapon_list = squads_data[squad]["weapons"]
                for member in squads_data[squad]["members"]:
                    if len(member)<6:
                        l = 6 - len(member)
                        member =member+" "*l
                    list_mem.append(member)
                    ind = list_mem.index(member)
        print(f"|  -   {list_mem[0]} : {weapon_list[0]}",end="   |")
        print(f"  -   {list_mem[1]} : {weapon_list[1]}","   |")
        print(f"|  -   {list_mem[2]} : {weapon_list[2]}",end="   |")
        print(f"  -   {list_mem[3]} : {weapon_list[3]}","   |")
        print("","`"*50)

def send_squad(data):
    while True:
        print("\n")
        print("="*36)
        available = False
        for squad in data["squads"]:
            if data["squads"][squad]["status"]=="available":
                print(f"{squad[6]}. {squad}")
                available = True
        if not available:
            print("No squads available!")
            return
        

        print("0 Exit")
        print("="*36)
        choice = input(" ---> ")
        squad = f"squad_{choice}"
        if choice =="0":
            break

        if choice=="1" or choice =="2" and data["squads"][squad]["status"]=="available":

            building,building_data= select_buidling()
            time_out = random.randint(3,6)
            data["squads"][squad]["status"] ="scavanging"
            data["squads"][squad]["location"] =building
            data["squads"][squad]["time_out"] = time_out
            print(f"  {squad}  -- Scavanging At -- >  {building}")
            return [time_out,building,building_data]
    


def Squad_came(data):
    for squad in data["squads"]:
        if data["squads"][squad]["status"]=="available":
            continue
        if data["squads"][squad]["time_out"]>0:
            print("-"*53)
            data["squads"][squad]["time_out"]-=1
            time = data["squads"][squad]["time_out"]
            print(f"  {squad}  ⌛  Hours {time} Remaining ")

        if data["squads"][squad]["time_out"]==0:
            print("."*53)
            print(f"  -{squad} Returned !!")
            location = data["squads"][squad]["location"]
            buildings = get_all_buildings()
            if location in buildings:
                build_data = buildings[location]

                loot_types = ["food", "water", "ammo", "meds", "grains"]
                loot_gained = {}
                for item in loot_types:
                    if item in build_data:
                        qty = random.randint(1, build_data[item])
                        data["resources"][item] += qty
                    else:
                        qty = 0
                    loot_gained[item] = qty
                
                food = loot_gained["food"]
                water = loot_gained["water"]
                ammo = loot_gained["ammo"]
                meds = loot_gained["meds"]
                grains = loot_gained["grains"]

                if "weapons" in build_data:
                    weapons_list = []
                    qty_list=[]
                    for  weapon in build_data["weapons"]:
                        qty = random.randint(1,2)
                        weapons_list.append(weapon)
                        qty_list.append(qty)
                        if weapon in data["resources"]["weapons"]:
                            data["resources"]["weapons"][weapon]+=qty
                        else:
                            data["resources"]["weapons"][weapon]=qty
                else:
                    weapons_list=[]
                    qty_list=[]
                print("","_"*52)
                print(f"|  🍴 Food : +{food}  | 💧 Water : +{water}  |  🌾 Grains: +{grains}   |")
                print(f"|  💉 Meds : +{meds}  | 🧨 Ammo  : +{ammo}  |"," "*16,"|")
                print(f"|   Weapons:"," "*39,"|")
                for weapon ,qty in zip(weapons_list,qty_list):
                    if len(weapon)<7:

                        weapon = weapon+" "*(7-len(weapon))
                    print("|"," "*10,weapon," :",qty," "*26,"|")
                print("","`"*52)
                data["squads"][squad]["status"]="available"
                data["squads"][squad]["location"]="base"
            else:
                print("Squad Already At Base!!")

def Add_sqd(data):
    squads_list = []
    count = 0
    squds = data["squads"]
    for sqd in squds:
        if len(squds[sqd]["members"])<=4:
            squads_list.append(sqd)
        if len(squds[sqd]["members"])==4:
            print(f"  ℹ️   {sqd} MaX Reached !!")
            count +=1
    if count==2:
        return

    print("="*15,"Showing Survivors","="*15)
    surviors_list = []
    ind = 1
    for survior in data["survivors"]:
        if survior["role"]=="idle":
            surviors_list.append(survior)
            print(f" | {ind}.   {survior['name']}   |   {survior['role']} |")
            ind+=1
    choice = input("  0 Exit | Choose Sur ---------->  ")
    if choice =="0":
        pass
    if int(choice) <=ind:
        sur_name = surviors_list[int(choice)-1]["name"]
        print(f" |  Survivor - {sur_name} ")
        print(" - Choose For Sqd 1 Or Sqd 2 [1,2]")
        inner_choice = input("  --------->  ")
        print(squads_list)
        if inner_choice=="1" or inner_choice=="2":
            sq = squads_list[int(inner_choice)-1]

            if len(data["squads"][sq]["members"])<4:
                data["squads"][sq]["members"].append(sur_name)
                data["squads"][sq]["weapons"].append("knife")

                for dic in data["survivors"]:
                    print(dic["name"])
                    if dic["name"]==sur_name:
                        dic["role"]=sq
                        
                print("\n  ✅   Succesfully Add TO SQUADS ")

            else:
                print("Squad Full !!")
        else:
            print(" ❌  Invalid Choice !!")
def Manage_sqd(data):
    while True:
        print("="*15,"Squads Manage","="*15)
        print("1. Create Sqd")
        print("2. Show No Of Sqd And Mem")
        print("3. Assign gun to each")
        print("0. Exit")
        choice = input("---------> ")
        if choice =="1":
            Add_sqd(data)
        elif choice =="2":
            show_squads(data)
        elif choice =="3":
            pass
        elif choice =="0":
            break
        else:
            print(" ❌  Invalid Choice !!")