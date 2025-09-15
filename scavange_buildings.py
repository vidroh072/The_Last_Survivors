# scavenge_buildings.py
import random

def get_all_buildings():
    return {
    "Supermarket": {"food": 12, "water": 4, "ammo": 2, "zombies": 3},
        "Police Station": {"ammo": 10, "water": 2, "weapons": ["assault", "shotgun"], "zombies": 4},
        "Pharmacy": {"food": 3, "water": 2, "meds": 6, "zombies": 2},
        "Restaurant": {"food": 10, "water": 6, "zombies": 3},
        "Gun Store": {"ammo": 8, "water": 1, "weapons": ["shotgun", "pistol"], "zombies": 5},
        "Clinic": {"food": 2, "water": 3, "meds": 7, "zombies": 2},
        "Office": {"food": 2, "water": 1, "ammo": 1, "zombies": 1},
        "Warehouse": {"food": 5, "water": 3, "ammo": 8,"grains":1, "zombies": 2},
        "House 1": {"food": 4, "water": 2, "meds": 1, "zombies": 1},
        "House 2": {"food": 5, "water": 4, "zombies": 2}
}

def random_building():
    building_list = []
    data = get_all_buildings()
    for building in data:
        building_list.append(building)
    ra = random.choice(building_list)
    return ra , data[ra]

def show_scavange_buidling():
    buidling_no = {}
    data = get_all_buildings()
    count = 1
    for buidling in data:
        print(f"  {count}.  {buidling}  ")
        buidling_no[str(count)]=buidling
        count+=1
    return buidling_no , data

def select_buidling():
    building_no , data = show_scavange_buidling()
    print(" Input [1,2...]  0 Exit",end="  ")
    choice = input("---------> ")
    if not choice in building_no:
        print("Not Found !!")
        return
    buidling_name = building_no[choice]
    buiding_data = data[buidling_name]
    return buidling_name , buiding_data

    