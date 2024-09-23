# How the different Calibers should be named on the Webpage, 
# "%Caliber%" Shot will be generated automatically if a Caliber has ammo with more then one projectile (e.g. Buckshot).
# Removed the following calibers
# 40x36 (underbarrel)
# 30x29 (underbarrel)
# 127x108 (HMG)
# 20x1 (Toy Gun)
caliber_map = {
    "Caliber556x45NATO": "5.56x45mm",
    "Caliber12g": "12/70",
    "Caliber762x54R": "7.62x54mm R",
    "Caliber762x39": "7.62x39mm",
    "Caliber9x19PARA": "9x19mm",
    "Caliber545x39": "5.45x39mm",
    "Caliber762x25TT": "7.62x25mm TT",
    "Caliber9x18PM": "9x18mm PM",
    "Caliber9x39": "9x39mm",
    "Caliber762x51": "7.62x51mm",
    "Caliber366TKM": ".366 TKM",
    "Caliber9x21": "9x21mm",
    "Caliber20g": "20/70",
    "Caliber46x30": "4.6x30mm",
    "Caliber127x55": "12.7x55mm",
    "Caliber57x28": "5.7x28mm",
    "Caliber1143x23ACP": ".45 ACP",
    "Caliber23x75": "23x75mm",
    "Caliber762x35": ".300",
    "Caliber86x70": ".338 Lapua Magnum",
    "Caliber9x33R": ".357 Magnum",
    "Caliber26x75": "26x75mm",
    "Caliber68x51": "6.8x51mm"
}

available_data_types = ["PenetrationPower", "DurabilityBurnModificator", "Damage", "Weight", "ArmorDamage", "ProjectileCount",
                        "InitialSpeed", "BallisticCoeficient", "RicochetChance", "FragmentationChance", "BulletMassGram",
                        "HeavyBleedingDelta", "LightBleedingDelta", "MalfFeedChance", "MalfMisfireChance", "HeatFactor",
                        "AmmoAccr", "AmmoHear", "AmmoRec", "Name", "Caliber"]