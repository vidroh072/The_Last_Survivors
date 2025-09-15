def show_shelter(data):
    print()
    if "shelter" in data["adapted_buildings"]:
        cap = data["adapted_buildings"]["shelter"]["capacity"]
        print(" "," "*8,"  -| Shelter |-   ")
        print(" ","="*34)
        print(f"  |   Capacity :  🛏️   {cap}  Survivors","|")
        print("  |"," "*30,"|")
        print(" ","="*34)
    if "cook" in data["adapted_buildings"]:
        cap = data["adapted_buildings"]["cook"]["capacity"]

        print("  |"," "*4,"   - Cook House -   "," "*4,"|")
        print(f"  |            :  🍵  🍛  "," "*7,"|")
        print(f"  |   Capacity :  {cap}"," "*14,"|")
        print("  |"," "*30,"|")
        print(" ","="*34)

    if "clinic" in data["adapted_buildings"]:
        cap = data["adapted_buildings"]["clinic"]["capacity"]

        print("  |"," "*4,"   - Clinic Center -   "," ","|")
        print(f"  |            :  💉  💊  "," "*7,"|")
        print(f"  |   Capacity :  {cap}"," "*14,"|")
        print("  |"," "*30,"|")
        print(" ","="*34)

    if "storage" in data["adapted_buildings"]:
        cap = data["adapted_buildings"]["storage"]["capacity"]

        print("  |"," "*4,"   - Storage -   "," "*7,"|")
        print("  |"," "*30,"|")
        print(f"  |            :  🍞       "," "*6,"|") 
        print(f"  |   Capacity :  {cap}"," "*13,"|")

        print("  |"," "*30,"|")
        print(" ","="*34)
    
t = (("===================================",
     "|   Capacity :  🛏️   2  Survivors  |",
     "|                                 |",
     "==================================="),(
     "|         - Cook House -          |",
     "|            :  🍵  🍛            |",
     "|   Capacity :  2                 |",
     "|                                 |",
     "==================================="),
     (
     "|         - Clinic Center -       |",
     "|            :  💉  💊            |",
     "|   Capacity :  1                 |",
     "==================================="),
     (
     "|         - Storage -             |",
     "|                                 |",
     "|            :  🍞                |",
     "|   Capacity :  10                |",
     "|                                 |",
     "===================================")
     )

