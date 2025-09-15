import random

def initial_game_state():
    return {
        "day": 1,
        "time": [12,"day"],
        "weather": "Sunny",
        "resources": {
            "food": 20,
            "water":10,
            "ammo": 30,
            "meds": 5,
            "brick":20,
            "wood":40,
            "steel":10,
            "grains":0,
            "weapons":{}
        },
        "squads": {
            "squad_1": {
                "members": ["Alex", "Jordan", "Ravi", "Leena"],
                "status": "available",
                "location": "base",
                "time_out":0,
                "weapons": ["pistol","pistol","pistol","pistol"]
            },
            "squad_2": {
                "members": ["Maya", "Noah", "Karan", "Zoya"],
                "status": "available",
                "location": "base",
                "time_out":0,
                "weapons": ["pistol","pistol","pistol","pistol"]
            }
        },
        "survivors": [
            {"name": "Aarav", "role": "idle"},
            {"name": "Meera", "role": "idle"},
            {"name": "Kabir", "role": "idle"}
        ],
        "adapted_buildings":{}    
        }

def get_daily_weather():
    weather_types = [
        {"type": "Sunny", "water_change": -2, "farm_bonus": 0},
        {"type": "Rain", "water_change": +5, "farm_bonus": +1},
        {"type": "Storm", "water_change": +3, "farm_bonus": -1},
        {"type": "Heatwave", "water_change": -5, "farm_bonus": -2}
    ]
    return random.choice(weather_types)

def daily_consumptions(data):
    total_survior = 0
    food_inv = data["resources"]["food"]
    water_inv = data["resources"]["water"]
    no_sqd_mem = data["squads"]
    for squads in no_sqd_mem:
        for mem in no_sqd_mem[squads]["members"]:
            total_survior+=1
    total_survior+= len(data["survivors"])
    total_food_cons = max(1,total_survior*1)
    total_water_cons = max(1,total_survior*1)
    
    consumed_food = min(food_inv,total_food_cons)
    consumed_water = min(water_inv,total_water_cons)
    data["resources"]["food"]-=consumed_food
    data["resources"]["water"]-=consumed_water
    print(" ---     Consumed !!")
    if total_food_cons>food_inv:
        print("","-"*36)
        print(f"  --  No More Food Inc Production!!")
    if total_water_cons>water_inv:
        print(f"  --  No More Water Inc Production!!")
        print()
    print(f"  -  Food :  🫑   {consumed_food}   |   Water :  💧  {consumed_water}")
    print("","-"*36)
  


def production_inc(data):
    if not "production" in data:
        print("No Production")
        return
    weather_effects = {"Sunny": 0,"Rain": 1,"Storm": -1,"Heatwave": -2}
    weather = data["weather"]
    rate = max(1,2+weather_effects[weather])  #1+2-2 = 1
    farming = data["production"]["farming"]
    farming["food"]["grains"]-=1

    if data["weather"]=="Storm" or data["weather"]=="Heatwave":
        print("-"*20)
        print(" Weather Is So Bad!!")
    print()
    print("   |-  Daily  Productions!  -|")
    if farming["field"]>0:
        vegetables_prd = farming["field"]*rate
        grains_prd = farming["field"]*rate
        farming["food"]["vegetables"]+=vegetables_prd
        farming["food"]["grains"]+=grains_prd
        print("   | Vegetables : "," 🫑  +" , vegetables_prd,"  |")
        print("   | Grains : ","     🌾 +" , grains_prd,"  |")
        print("   ","`"*25)
    
def give_time(data):
    hour = data['time'][0]
    day = data['time'][1]
    weather = data['weather']
    if day =="day":
        day = " ☀️ "+day
    else:
        day = " 🌙 "+day
    hour_img = ["🕛","🕐","🕑","🕒","🕓","🕔","🕕","🕖","🕗","🕘","🕙","🕚"]
    if hour ==24:
        hour = 0
        img = hour_img[hour]
    if hour >=12:
        hr_ind = hour-12
        img = hour_img[hr_ind]
        hour = str(hour) + ":00 PM"
    else:
        img = hour_img[hour]
        hour = str(hour) + ":00 AM"
    hr = img+" "+ str(hour)

    weath_img = {"Sunny":"☀️","Rain":"🌧️","Storm":"⛈️","Heatwave":"🔥"}
    weather = weath_img[weather] +"  "+weather 
    print(f" 📅 Day {data['day']}   |  {hr}  {day}  |  🌦️  Weather: {weather}")



def change_time(data):
    hour,day=data["time"]   #1,"morning"   hr>7 mornign
    hour+=1
    if hour >=24:
        hour = 0
        data["day"]+=1
        weather_data = get_daily_weather()
        data["weather"] = weather_data["type"]
        data["resources"]["water"] += weather_data["water_change"]
        if data["resources"]["water"] < 0:
            data["resources"]["water"] = 0
        print(f"     | 💧 Water change: {weather_data['water_change']}")

    if hour >=7 and hour<=18:
        day = "Day"
    else:
        day = "night"

    if hour>=18:
        day = "Night"
    data["time"]=[hour,day]

def food_productions(data):
    if "cook" not in data["adapted_buildings"]:
        return
    if not data["adapted_buildings"]["cook"]["state"] == "True":
        return
    if "cook" not in data["adapted_buildings"]:
        return
    raw_food = data["production"]["farming"]["food"]  # {vegetable:0,grains:0}
    if raw_food["vegetables"] < 0 and raw_food["grains"] < 2:
        return
    vegetables = raw_food["vegetables"]

    capacity = data["adapted_buildings"]["cook"]["capacity"]
    # take food

    food_produce = 0
    while True:
        if capacity > 0:
            if vegetables > 2:
                food_produce += 1
                vegetables -= 2
                raw_food["vegetables"] = vegetables
                capacity-=1 
        else:
            break
    print(f" - Cook House :  🥫  {food_produce}")
    data["resources"]["food"]+=food_produce