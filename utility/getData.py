import json
import re

path_items = "SPT_Data/Server/database/templates/items.json"
path_language = "SPT_Data/Server/database/locales/global/en.json"
path_rm = "user/mods/SPT-Realism/src/ballistics/ammo.js"
# Toy, Flare
blacklist_caliber = ["Caliber20x1mm", 'Caliber26x75']
blacklist_ammo_keyword = [keyword.lower() for keyword in ["!!!DO_NOT_USE!!!", "Airsoft", "Ammo", "Shrapnel"]]
caliber_show_name = {"Caliber1143x23ACP": ".45 ACP",
                     "Caliber127x108": "12.7x108mm",
                     "Caliber127x33": ".50 AE",
                     "Caliber127x55": "12.7x55mm",
                     "Caliber12g": "12/70",
                     "Caliber20g": "20/70",
                     "Caliber23x75": "23x75mm",
                     "Caliber366TKM": ".366 TKM",
                     "Caliber40x46": "4.40x46mm",
                     "Caliber46x30": "4.6x30mm",
                     "Caliber545x39": "5.45x39mm",
                     "Caliber556x45NATO": "5.56x45mm",
                     "Caliber57x28": "5.7x28mm",
                     "Caliber68x51": "6.8x51mm",
                     "Caliber762x25TT": "7.62x25mm",
                     "Caliber762x35": ".300",
                     "Caliber762x39": "7.62x39mm",
                     "Caliber762x51": "7.62x51mm",
                     "Caliber762x54R": "7.62x54mm R",
                     "Caliber86x70": ".338 Lapua Magnum",
                     "Caliber9x18PM": "9x18mm",
                     "Caliber9x19PARA": "9x19mm",
                     "Caliber9x21": "9x21mm",
                     "Caliber9x33R": ".357 Magnum",
                     "Caliber9x39": "9x39mm"}


data = {}
try:
    with open(path_items, encoding="UTF-8", mode="r") as file:
        data["item"] = json.load(file)
    with open(path_language, encoding="UTF-8", mode="r") as file:
        data["lang"] = json.load(file)
except OSError:
    print("The files could not be read")
    exit()


new_data = []
for i, item in enumerate(filter(lambda x: (data["item"][x].get("_props", {}).get("ammoType", "") in ("bullet", "buckshot"))
                                and (data["item"][x].get("_props", {}).get("Caliber", "") not in blacklist_caliber)
                                and ((data["lang"].get(f'{x} Name', "Ammo").lower()[:3] == "23x") or not any(keyword in data["lang"].get(f'{x} Name', "Ammo").lower() for keyword in blacklist_ammo_keyword)),
                                data["item"])):
    cal = caliber_show_name.get(data["item"][item]["_props"]["Caliber"], f"NO CALIBER_SHOW_NAME FOR {data["item"][item]["_props"]["Caliber"]}")
    typ = data["item"][item]["_props"]["ammoType"]
    name = data["lang"][f'{item} Name'].removeprefix(cal).strip()
    penetrationPower = data["item"][item]["_props"]["PenetrationPower"]
    armorDamage = data["item"][item]["_props"]["ArmorDamage"]
    count = data["item"][item]["_props"]["ProjectileCount"]
    damage = data["item"][item]["_props"]["Damage"]
    initialSpeed = data["item"][item]["_props"]["InitialSpeed"]
    ballisticCoefficient = data["item"][item]["_props"]["BallisticCoeficient"]
    ricochetChance = data["item"][item]["_props"]["RicochetChance"]
    fragmentationChance = data["item"][item]["_props"]["FragmentationChance"]
    bulletMassGram = data["item"][item]["_props"]["BulletMassGram"]
    heavyBleedingDelta = data["item"][item]["_props"]["HeavyBleedingDelta"]
    lightBleedingDelta = data["item"][item]["_props"]["LightBleedingDelta"]
    ammoAccr = data["item"][item]["_props"]["ammoAccr"]
    ammoHear = data["item"][item]["_props"]["ammoHear"]
    ammoRec = data["item"][item]["_props"]["ammoRec"]
    malfMisfireChance = data["item"][item]["_props"]["MalfMisfireChance"]
    misfireChance = data["item"][item]["_props"]["MisfireChance"]
    malfFeedChance = data["item"][item]["_props"]["MalfFeedChance"]
    durabilityBurnModificator = data["item"][item]["_props"]["DurabilityBurnModificator"]
    heatFactor = data["item"][item]["_props"]["HeatFactor"]
    new_data.append({"id": item,
                     "caliber": cal if typ != "buckshot" else f'{cal} shot',
                     "name": name,
                     "PenetrationPower": penetrationPower,
                     "ArmorDamage": armorDamage,
                     "ProjectileCount": count,
                     "Damage": damage,
                     "InitialSpeed": initialSpeed,
                     "BallisticCoeficient": ballisticCoefficient,
                     "RicochetChance": ricochetChance,
                     "FragmentationChance": fragmentationChance,
                     "BulletMassGram": bulletMassGram,
                     "HeavyBleedingDelta": heavyBleedingDelta,
                     "LightBleedingDelta": lightBleedingDelta,
                     "ammoAccr": ammoAccr,
                     "ammoHear": ammoHear,
                     "ammoRec": ammoRec,
                     "MalfMisfireChance": malfMisfireChance,
                     "MisfireChance": misfireChance,
                     "MalfFeedChance": malfFeedChance,
                     "DurabilityBurnModificator": durabilityBurnModificator,
                     "HeatFactor": heatFactor
                     })
    # Create a single pellet variant of the buckshot round
    if typ == "buckshot":
        new_data.append({"id": new_data[-1]["id"],
                         "caliber": f'{cal} single',
                         "name": name,
                         "PenetrationPower": penetrationPower,
                         "ArmorDamage": armorDamage,
                         "ProjectileCount": count,
                         "Damage": damage / count,
                         "InitialSpeed": initialSpeed,
                         "BallisticCoeficient": ballisticCoefficient,
                         "RicochetChance": ricochetChance,
                         "FragmentationChance": fragmentationChance,
                         "BulletMassGram": bulletMassGram,
                         "HeavyBleedingDelta": heavyBleedingDelta,
                         "LightBleedingDelta": lightBleedingDelta,
                         "ammoAccr": ammoAccr,
                         "ammoHear": ammoHear,
                         "ammoRec": ammoRec,
                         "MalfMisfireChance": malfMisfireChance,
                         "MisfireChance": misfireChance,
                         "MalfFeedChance": malfFeedChance,
                         "DurabilityBurnModificator": durabilityBurnModificator,
                         "HeatFactor": heatFactor
                         })
# New Data is the base Data. We take the RM Data and apply it onto the newData.
new_data.sort(key=lambda x: x["caliber"])

# Read the RM Data
rm_data = []
find_id = re.compile(r'(?<=== ")[a-fA-F0-9]+(?=")')
find_data = re.compile(r'(?<=\._props\.)([a-zA-Z]+) = (-?[0-9]+\.?[0-9]*)')
try:
    with (open(path_rm, mode="r", encoding="UTF-8")) as file:
        # Read till the loadAmmoStats function
        for line in file:
            if line.count("loadAmmoStats"):
                break
        current_item = {}
        current_id = -1
        for line in file:
            line = line.strip()
            if line.count("Ammo Stats Loaded"):
                break
            if (not line.count("serverItem")):
                continue
            # Read until server._id is found this will be the id to replace
            if line.count("serverItem._id"):
                if current_id != -1:
                    rm_data.append(current_item)
                current_item = {}
                current_id = find_id.findall(line)[0]
                current_item["id"] = current_id
            elif line.count("serverItem._props"):
                line_data = find_data.findall(line)
                if not len(line_data):
                    continue
                current_item[line_data[0][0]] = float(line_data[0][1])
except OSError:
    print("The RM-File could not be read")
    exit()

# Only take the rm data for the preselected items
data_ids = [item["id"] for item in new_data]
rm_data = list(filter(lambda x: x["id"] in data_ids, rm_data))
for item in rm_data:
    # Find the orig item
    index = [i for i, x in enumerate(new_data) if x["id"] == item["id"]][0]
    # Loop through the rm item and apply keys which are also present in the orig item
    for key, value in item.items():
        if key not in new_data[index].keys():
            continue
        new_data[index][key] = value

# Final transform to make the data useable for the website
web_data = {"info": {}, "item": {}}

for item in new_data:
    item_obj = {
        "id": item["id"],
        "name": item["name"],
        "PenetrationPower": item["PenetrationPower"],
        "ArmorDamage": item["ArmorDamage"],
        "ProjectileCount": item["ProjectileCount"],
        "Damage": item["Damage"],
        "InitialSpeed": item["InitialSpeed"],
        "BallisticCoeficient": item["BallisticCoeficient"],
        "RicochetChance": item["RicochetChance"],
        "FragmentationChance": item["FragmentationChance"],
        "BulletMassGram": item["BulletMassGram"],
        "HeavyBleedingDelta": item["HeavyBleedingDelta"],
        "LightBleedingDelta": item["LightBleedingDelta"],
        "ammoAccr": item["ammoAccr"],
        "ammoHear": item["ammoHear"],
        "ammoRec": item["ammoRec"],
        "MalfMisfireChance": item["MalfMisfireChance"],
        "MisfireChance": item["MisfireChance"],
        "MalfFeedChance": item["MalfFeedChance"],
        "DurabilityBurnModificator": item["DurabilityBurnModificator"],
        "HeatFactor": item["HeatFactor"]
    }

    for key, value in list(item_obj.items())[2:]:
        if key in web_data["info"]:
            web_data["info"][key].append(value)
        else:
            web_data["info"][key] = [value]

    if item["caliber"] in web_data["item"]:
        web_data["item"][item["caliber"]].append(item_obj)
    else:
        web_data["item"][item["caliber"]] = [item_obj]

for key, value in web_data["info"].items():
    web_data["info"][key] = [min(value), max(value)]

with open("data.js", mode="w", encoding="UTF-8") as file:
    file.write("const data = ")
    json.dump(web_data, file, indent=3)
    file.write(";")
