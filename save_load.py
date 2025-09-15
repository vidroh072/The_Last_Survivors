import json
import os
file = "C:/Users/hp/Desktop/Project/The_Last_survivors/data/save_data.json"
def load_game():
    if os.path.exists(file):
        with open(file) as f:
            try:
                data = json.load(f)
                return data
            except:

                return {}
    else:
        return {}
def save_game(data):
    with open(file,"w") as f:
        json.dump(data,f,indent=2)
        #print("Succsfull")

def show_resources(data):
    print("","="*25," 📦  Resources","="*25)         

    resources = data["resources"]
    print("|   - 🍴  Food :" ,resources["food"] ,end="  |  ")
    print("   - 💧  Water:" ,resources["water"],end="  |  ")
    print("   - 💉  Meds :" ,resources["meds"]," |")
    print("|   - 🪵   Wood :" ,resources["wood"] ,end="  |  ")
    print("   - 🧱  Brick:" ,resources["brick"],end="  |  ")
    print("   -     Steel:" ,resources["steel"]," |")
    print("|   - 🧨  Ammo :",resources["ammo"],end="  |  ",)
    print("   - 🌾  Grains:" ,resources["grains"]," "*22," |")
    print("","="*66)
    gun_list = []
    gun_qty=[]
    weapons = data["resources"]["weapons"]
    print(" "*22,"- Weapons  ᡕᠵデ气亠")
    print("","_"*66)
    print("|",end="")
    guns = {"pistol":"̸̱͂ ̸͆̿͞ ̄̿͞ ̿̅͞ ̿̅͞ ",
            "shotgun":"=══==╦︻",
            "assault":"︻┳═一",
            "knife":"▬ι══ﺤ"
            }
    print(f"      Knife      {guns['knife']}   : #" ,end="   |")
    print(f"      Shotgun    {guns['shotgun']}   : {weapons.get('shotgun',0)}","  |")
    print(f"|      Assault    {guns['assault']}  : {weapons.get('assault',0)}",end="   | ")
    print(f"     Pistol    {guns['pistol']}       : {weapons.get('pistol',0)}","  |")
    print("","`"*66)