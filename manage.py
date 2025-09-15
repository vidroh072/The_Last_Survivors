def buildings_available():
    return {"shelter":{"🪵   wood  ":5,"🧱  bricks":2,"capacity":2}, # capacity = Rest
          "clinic":{"🪵   wood  ":4,"🧱  bricks":4,"capacity":1}, # capacity = pationet
          "storage":{"🪵   wood  ":10,"🧱  brick":10,"capacity":10}, #capacity = store
          "cook":{"🪵   wood  ":8,"🧱  brick":10,"capacity":2}}    #capacity = cook space
def adaptions(data,adapt_type):
    buildings = buildings_available()
    if adapt_type in buildings:
        bld_data = buildings[adapt_type]
        print(f" - {adapt_type}  Req  : ")
        req = []
        for res in bld_data:
            capacity = buildings[adapt_type]["capacity"]
            print(f"      :  {res}   |  {buildings[adapt_type][res]}")

            qty = buildings[adapt_type][res]
            req.append([res,qty])
        print("  ","_"*20)
        print("  |  1. Adapt"," "*8,"|")
        print("  |  0. Skip "," "*8,"|")
        print("  ","`"*20)

        choice = input(" -------->  ")
        if choice =="1":
            #check res
            # req = [[wood,0],[brick,10]]
            wood , brick = data["resources"]["wood"],data["resources"]["brick"]
            if wood < req[0][1] or brick < req[1][1]:
                print("  ℹ️   Low Resources Check Resourcess !!")
                return
            wood,brick = req[0][1],req[1][1]
            if adapt_type not in data["adapted_buildings"]:
                data["adapted_buildings"][adapt_type] = {"capacity":0}
                
            data["adapted_buildings"][adapt_type]["capacity"]+=capacity
            data["resources"]["wood"] -=wood
            data["resources"]["brick"]-=brick
            if adapt_type =="cook":
                data["adapted_buildings"]["cook"]["state"] = "True"
                

            print(f" - Nearby Building Adapted As {adapt_type}  |  Capacity 🏚️  {capacity}")
        else:
            print(" ❌  Invalid Input Returning!!")
            return


        
def Adapt_build(data):
    while True:
        print("="*15,"Adaptions Manage","="*15)
        print("1. Adapt Shelter")
        print("2. Adapt Clinic")
        print("3. Adapt Storage")
        print("4. Adapt Cook")
        print("0. Exit")
        choice = input(" -------->  ")

        if choice =="1":
            adaptions(data,"shelter")    
        elif choice =="2":
            adaptions(data,"clinic")    
        elif choice =="3":
            adaptions(data,"storage")    
        elif choice =="4":
            adaptions(data,"cook")    
        elif choice =="0":
            break
        else:
            print(" ❌  Invalid Choice !!")
