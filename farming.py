def show_farming_production(data):
    print("","="*15," Farming Production ","="*15)
    if not "production" in data:
        print("No Production Set!!")
        return
    if "farming" in data["production"]:
        farming = data["production"]["farming"]
        vegetables = farming["food"]["vegetables"]
        vegetables_prd = farming["field"]*2
        grains = farming["food"]["grains"]
        grains_prd = farming["field"]*2
        print(f"|  !      Fields : {farming['field']}"," "*31,"|")
        print(f"|  🥔🫑    Production    : Vegetables : { vegetables_prd} Per Day"," "*3,"|")
        print(f"|  🌾🫛                  : Grains     : { grains_prd} Per Day"," "*3,"|")
        print("|"," "*50,"|")
        print(f"|  🥒🥕   Storage       : Vegetables : {vegetables}"," "*11,"|")
        print(f"|                       : Grains     : {grains}"," "*11,"|")
        print("","="*52)


def build_field(data):
    if data["resources"].get("wood",0)<5 or data["resources"].get("grains",0)<1:
        print("Out of Resources!!!")
        print()
        return
    data["resources"]["wood"]-=5
    data["resources"]["grains"]-=1
    if not "production" in data:
        farming = {"field":0,
                   "food":{
                    "vegetables":0,"grains":0},
                    }
        data["production"]={"farming":farming}
    data["production"]["farming"]["field"]+=1
    print(" ✅  Field Succesfully Build")

def build_farms(data):
    print("="*15," Build Farms ","="*15)
    while True:
        print("1. Build Field  [Crops]")
        print("2. Animal Husbandry  [milk] ---coming")
        print("3. Greenhouses  [Protected from weather]")
        print("0. Exit")
        choice = input("---------> ")

        if choice =="1":
            while True:
                print("  - Require  5 Wood | [1 Bag Of grain ]")
                print("1. Build")
                print("0. Exit")
                inner_choice = input("---------> ")
                if inner_choice =="1":
                    build_field(data)
                elif inner_choice =="0":
                    break
                else:
                    print("Invalid Choice !!")

        elif choice =="2":
            pass
        elif choice =="3":
            pass
        elif choice =="0":
            break
        else:
            print("Invalid Choice !!")

def Manage_farm(data):
    print("\n")
    print("="*15," Farming ","="*15)
    while True:
        print("1. Show Production")
        print("2. Start Cook Food")
        print("3. Build Farm")
        print("0. Exit")
        
        choice = input("---------> ")
        if choice =="1":
            show_farming_production(data)
        elif choice =="2":
            initialise_cook_house(data)
        elif choice =="3":
            build_farms(data)
        elif choice =="0":
            break
        else:
            print("Invalid Choice !!")

def initialise_cook_house(data):
    if "cook" not in data["adapted_buildings"]:
        print(" - No Cook House Set Yet!!!")
        return
    if "field" not in data["production"]["farming"]:
        print(" - No Farming FIelds!!!")
        return
    print("","_"*20)
    print("1. Start Cooking")
    print("2. Stop Cooking")
    print("","_"*20)
    choice = input("---------> ")
    if choice =="1":
        data["adapted_buildings"]["cook"]["state"] = "True"
        print("   - Production Set : True")
    elif choice =="2":
        data["adapted_buildings"]["cook"]["state"] = "False"
        print("   - Production Set : False")
    else:
        print(" Invalid Input!!!")
    
