
#stages
rounds = {"1-1", "1-2", "1-3", "1-4",
            "2-1", "2-2", "2-3", "2-4", "2-5", "2-6", "2-7",
            "3-1", "3-2", "3-3", "3-4", "3-5", "3-6", "3-7",
            "4-1", "4-2", "4-3", "4-4", "4-5", "4-6", "4-7",
            "5-1", "5-2", "5-3", "5-4", "5-5", "5-6", "5-7",
            "6-1", "6-2", "6-3", "6-4", "6-5", "6-6", "6-7",
            "7-1", "7-2", "7-3", "7-4", "7-5", "7-6", "7-7"}
     
carousel_round = {"2-4", "3-4", "4-4", "5-4", "6-4", "7-4"}

carousel_round_first = {"1-1"}

pve_round = {"1-2", "1-3", "1-4", "2-7", "3-7", "4-7", "5-7", "6-7", "7-7"}

component_anvil_round = {"4-7", "5-7", "6-7", "7-7"}

pvp_round = {"2-2", "2-3", "2-5", "2-6",
            "3-1", "3-3", "3-5", "3-6",
            "4-1", "4-3", "4-5", "4-6",
            "5-1", "5-2", "5-3", "5-5", "5-6",
            "6-1", "6-2", "6-3", "6-5", "6-6",
            "7-1", "7-2", "7-3", "7-5", "7-6"}

augment_pvp_round = {"2-1", "3-2", "4-2"}

#items
items = {"GuinsoosRageblade", "InfinityEdge", "SunfireCape", "Bloodthirster", "GiantSlayer", "GargoyleStoneplate", "JeweledGauntlet", 
"ProtectorsVow", "ArchangelsStaff", "Morellonomicon", "HandOfJustice", "TitansResolve", "SpearofShojin", "WarmogsArmor", 
"ThiefsGloves", "BlueBuff", "ZekesHerald", "LastWhisper", "ZzRotPortal", "EdgeofNight", "IonicSpark", 
"DragonsClaw", "RunaansHurricane", "HextechGunblade", "StatikkShiv", "Redemption", "BrambleVest", "ChaliceofPower", 
"RabadonsDeathcap", "Quicksilver", "Zephyr", "ShroudofStillness", "GuardBreaker", "HeartEmblem", "LocketoftheIronSolari", 
"Deathblade", "RapidFirecannon", "OxForceEmblem", "RenegadeEmblem", "AnimaSquadEmblem", "ADMINEmblem", "GuildEmblem", 
"DuelistEmblem", "MascotEmblem", "EvokerEmblem", "GoldmancersStaff", "MogulsMail", "DravensAxe", "GamblersBlade", 
"NeedlesslyBigGem", "AnimaVisage", "MysticEmblem", "DeathsDefiance", "EternalWinter", "InfinityForce", "LaserCorpsEmblem", 
"RascalsGloves", "TacticiansCrown", "GoldCollector", "BruiserEmblem", "ObsidianCleaver", "Manazane", "Demonslayer", 
"DiamondHands", "RanduinsSanctum", "WarriorEmblem", "Rocket-PropelledFist", "FistofFairness", "ZhonyasParadox", "TempestEmblem", 
"Urf-AngelsStaff", "ZenithEdge", "CannoneerEmblem", "DeterminedInvestor", "BlessedBloodthirster", "ScalescornEmblem", "TitansVow", 
"ZekesHarmony", "GuinsoosReckoning", "GlamorousGauntlet", "WarmogsPride", "RabadonsAscendedDeathcap", "BrinkofDawn", "DarkflightEmblem", 
"AssassinEmblem", "SpearofHirana", "BulwarksOath", "HextechLifeblade", "JadeEmblem", "BlueBlessing", 
"DvarapalaStoneplate", "CovalentSpark", "ChaliceofCharity", "ZzRotsInvitation", "RunaansTempest", "DragonsWill", "EternalWhisper", 
"SunlightCape", "CrownOfChampions", "RosethornVest", "LuminousDeathblade", "BansheesSilence", "StatikksFavor", "Quickestsilver", 
"Absolution", "Mistral", "RapidLightcannon", "ShroudofReverence", "LocketofTargonPrime", "DarkflightEssence"}

items_list = ["GuinsoosRageblade", "InfinityEdge", "SunfireCape", "Bloodthirster", "GiantSlayer", "GargoyleStoneplate", "JeweledGauntlet", 
"ProtectorsVow", "ArchangelsStaff", "Morellonomicon", "HandOfJustice", "TitansResolve", "SpearofShojin", "WarmogsArmor", 
"ThiefsGloves", "BlueBuff", "ZekesHerald", "LastWhisper", "ZzRotPortal", "EdgeofNight", "IonicSpark", 
"DragonsClaw", "RunaansHurricane", "HextechGunblade", "StatikkShiv", "Redemption", "BrambleVest", "ChaliceofPower", 
"RabadonsDeathcap", "Quicksilver", "Zephyr", "ShroudofStillness", "GuardBreaker", "HeartEmblem", "LocketoftheIronSolari", 
"Deathblade", "RapidFirecannon", "OxForceEmblem", "RenegadeEmblem", "AnimaSquadEmblem", "ADMINEmblem", "GuildEmblem", 
"DuelistEmblem", "MascotEmblem", "EvokerEmblem", "GoldmancersStaff", "MogulsMail", "DravensAxe", "GamblersBlade", 
"NeedlesslyBigGem", "AnimaVisage", "MysticEmblem", "DeathsDefiance", "EternalWinter", "InfinityForce", "LaserCorpsEmblem", 
"RascalsGloves", "TacticiansCrown", "GoldCollector", "BruiserEmblem", "ObsidianCleaver", "Manazane", "Demonslayer", 
"DiamondHands", "RanduinsSanctum", "WarriorEmblem", "Rocket-PropelledFist", "FistofFairness", "ZhonyasParadox", "TempestEmblem", 
"Urf-AngelsStaff", "ZenithEdge", "CannoneerEmblem", "DeterminedInvestor", "BlessedBloodthirster", "ScalescornEmblem", "TitansVow", 
"ZekesHarmony", "GuinsoosReckoning", "GlamorousGauntlet", "WarmogsPride", "RabadonsAscendedDeathcap", "BrinkofDawn", "DarkflightEmblem", 
"AssassinEmblem", "SpearofHirana", "BulwarksOath", "HextechLifeblade", "JadeEmblem", "BlueBlessing", 
"DvarapalaStoneplate", "CovalentSpark", "ChaliceofCharity", "ZzRotsInvitation", "RunaansTempest", "DragonsWill", "EternalWhisper", 
"SunlightCape", "CrownOfChampions", "RosethornVest", "LuminousDeathblade", "BansheesSilence", "StatikksFavor", "Quickestsilver", 
"Absolution", "Mistral", "RapidLightcannon", "ShroudofReverence", "LocketofTargonPrime", "DarkflightEssence"]

radiant_items_dict = {
    "ArchangelsStaff" : "Urf-AngelsStaff",
    "Bloodthirster" : "BlessedBloodthirster",
    "BlueBuff" : "BlueBlessing",
    "BrambleVest" : "RosethornVest",
    "ChaliceofPower" : "ChaliceofCharity",
    "Deathblade" : "LuminousDeathblade",
    "DragonsClaw" : "DragonsWill",
    "ProtectorsVow" : "BulwarksOath",
    "GargoyleStoneplate" : "DvarapalaStoneplate",
    "Giantslayer" : "DemonSlayer",
    "EdgeofNight" : "BrinkofDawn",
    "GuinsoosRageblade" : "GuinsoosReckoning",
    "HandOfJustice" : "FistofFairness",
    "HextechGunblade" : "HextechLifeblade",
    "InfinityEdge" : "ZenithEdge",
    "IonicSpark" : "CovalentSpark",
    "JeweledGauntlet" : "GlamorousGauntlet",
    "LastWhisper" : "EternalWhisper",
    "LocketoftheIronSolari" : "LocketofTargonPrime",
    "Quicksilver" : "Quickestsilver",
    "RabadonsDeathcap" : "RabadonsAscendedDeathcap",
    "RapidFirecannon" : "RapidLightcannon",
    "Redemption" : "Absolution",
    "RunaansHurricane" : "RunaansTempest",
    "ShroudofStillness" : "ShroudofReverance",
    "SpearofShojin" : "SpearofHirana",
    "StatikkShiv" : "StatikkFavor",
    "SunfireCape" : "SunlightCape",
    "ThiefsGloves" : "RascalsGloves",
    "TitansResolve" : "TitansVow",
    "BansheesClaw" : "BansheesSilence",
    "WarmogsArmor" : "WarmogsPride",
    "ZekesHerald" : "ZekesHarmony",
    "Zephyr" : "Mistral",
    "ZzRotPortal" : "ZzRotsInvitation"
}

radiant_items = {"Absolution", "BansheesSilence", "BlessedBloodthirster", "BlueBlessing", "BrinkofDawn", "BulwarksOath",
                "ChaliceofCharity", "CovalentSpark", "DemonSlayer", "DragonsWill", "DvarapalaStoneplate", "EternalWhisper",
                "FistofFairness", "GlamorousGauntlet", "GuinsoosReckoning", "HextechLifeblade", "LocketofTargonPrime",
                "LuminousDeathblade", "Mistral", "Quickestsilver", "RabadonsAscendedDeathcap", "RapidLightcannon", "RascalsGloves",
                "RosethornVest", "RunaansTempest", "ShroudofReverance", "SpearofHirana", "StatikkFavor", "SunlightCape", "TitansVow",
                "Urf-AngelsStaff", "WarmogsPride", "ZekesHarmony", "ZenithEdge", "ZzRotsInvitation"
}

ornn_items = {"AnimaVisage", "DeathsDefiance", "EternalWinter", "GoldCollector", "InfinityForce", "Manazane", 
            "ObsidianCleaver", "RanduinsSanctum", "Rocket-PropelledFist", "ZhonyasParadox"
}

item_parts = {"NeedlesslyLargeRod", "TearoftheGoddess", "SparringGloves", "Spatula", "GiantsBelt", "NegatronCloak", "ChainVest", "BFSword", "RecurveBow"}

item_parts_list = ["NeedlesslyLargeRod", "TearoftheGoddess", "SparringGloves", "Spatula", "GiantsBelt", "NegatronCloak", "ChainVest", "BFSword", "RecurveBow"]

dict_full_items_craftable = {"ArchangelsStaff": ("NeedlesslyLargeRod", "TearoftheGoddess"),
              "RenegadeEmblem": ("SparringGloves", "Spatula"),
              "GuardBreaker": ("GiantsBelt", "SparringGloves"),
              "Bloodthirster": ("BFSword", "NegatronCloak"),
              "BlueBuff": ("TearoftheGoddess", "TearoftheGoddess"),
              "BrambleVest": ("ChainVest", "ChainVest"),
              "OxForceEmblem": ("Spatula", "ChainVest"),
              "ChaliceofPower": ("NegatronCloak", "TearoftheGoddess"),
              "Deathblade": ("BFSword", "BFSword"),
              "DragonsClaw": ("NegatronCloak", "NegatronCloak"),
              "AnimaSquadEmblem": ("Spatula", "NeedlesslyLargeRod"),
              "EdgeofNight": ("BFSword", "ChainVest"),
              "ProtectorsVow": ("ChainVest", "TearoftheGoddess"),
              "GargoyleStoneplate": ("ChainVest", "NegatronCloak"),
              "GiantSlayer": ("BFSword", "RecurveBow"),
              "MascotEmblem": ("Spatula", "GiantsBelt"),
              "GuinsoosRageblade": ("NeedlesslyLargeRod", "RecurveBow"),
              "HandofJustice": ("SparringGloves", "TearoftheGoddess"),
              "HextechGunblade": ("BFSword", "NeedlesslyLargeRod"),
              "InfinityEdge": ("BFSword", "SparringGloves"),
              "IonicSpark": ("NeedlesslyLargeRod", "NegatronCloak"),
              "JeweledGauntlet": ("NeedlesslyLargeRod", "SparringGloves"),
              "LastWhisper": ("RecurveBow", "SparringGloves"),
              "LocketoftheIronSolari": ("ChainVest", "NeedlesslyLargeRod"),
              "HeartEmblem": ("Spatula", "TearOfTheGodess"),
              "ADMINEmblem": ("Spatula", "NegatronCloak"),
              "Morellonomicon": ("GiantsBelt", "NeedlesslyLargeRod"),
              "Quicksilver": ("NegatronCloak", "SparringGloves"),
              "RabadonsDeathcap": ("NeedlesslyLargeRod", "NeedlesslyLargeRod"),
              "DuelistEmblem": ("Spatula", "RecurveBow"),
              "RapidFirecannon": ("RecurveBow", "RecurveBow"),
              "Redemption": ("GiantsBelt", "TearoftheGoddess"),
              "RunaansHurricane": ("NegatronCloak", "RecurveBow"),
              "LaserCorpsEmblem": ("Spatula", "BFSword"),
              "ShroudofStillness": ("ChainVest", "SparringGloves"),
              "SpearofShojin": ("BFSword", "TearoftheGoddess"),
              "StatikkShiv": ("RecurveBow", "TearoftheGoddess"),
              "SunfireCape": ("ChainVest", "GiantsBelt"),
              "TacticiansCrown": ("Spatula", "Spatula"),
              "ThiefsGloves": ("SparringGloves", "SparringGloves"),
              "TitansResolve": ("ChainVest", "RecurveBow"),
              "WarmogsArmor": ("GiantsBelt", "GiantsBelt"),
              "ZekesHerald": ("BFSword", "GiantsBelt"),
              "Zephyr": ("GiantsBelt", "NegatronCloak"),
              "ZzRotPortal": ("GiantsBelt", "RecurveBow")}

#champions
champions = {"Ashe", "Blitzcrank", "Galio", "Gangplank", "Kayle", "Lulu", "Lux", "Nasus", "Poppy",
            "Renekton", "Sylas", "Talon", "Wukong", "Annie", "Camille", "Draven", "Ezreal", "Fiora",
            "Jinx", "LeeSin", "Malphite", "Rell", "Sivir", "Vi", "Yasuo", "Yummi", "Alistar", "ChoGath",
            "Jax", "KaiSa", "LeBlanc", "Nilah", "Rammus", "Riven", "Senna", "Sona", "Vayne", "VelKoz",
            "Zoe", "AurelionSol", "BelVeth", "Ekko", "MissFortune", "Samira", "Sejuani", "Sett", "Soraka",
            "Taliyah", "Viego", "Zac", "Zed", "Aphelios", "Fiddlesticks", "Janna", "Leona", "Mordekaiser",
            "Nunu", "Syndra", "Urgot"}

champions_one_cost = {"Ashe", "Blitzcrank", "Galio", "Gangplank", "Kayle", "Lulu", "Lux", "Nasus", "Poppy",
            "Renekton", "Sylas", "Talon", "Wukong"}

champions_two_cost = {"Annie", "Camille", "Draven", "Ezreal", "Fiora", "Jinx", "LeeSin", "Malphite", "Rell",
            "Sivir", "Vi", "Yasuo", "Yummi"}

champions_three_cost = {"Alistar", "ChoGath","Jax", "KaiSa", "LeBlanc", "Nilah", "Rammus", "Riven", "Senna",
            "Sona", "Vayne", "VelKoz", "Zoe"}

champions_four_cost = {"AurelionSol", "BelVeth", "Ekko", "MissFortune", "Samira", "Sejuani", "Sett", "Soraka",
            "Taliyah", "Viego", "Zac", "Zed"}

champions_five_cost = {"Aphelios", "Fiddlesticks", "Janna", "Leona", "Mordekaiser",
            "Nunu", "Syndra", "Urgot"}

champions_list = ["Ashe", "Blitzcrank", "Galio", "Gangplank", "Kayle", "Lulu", "Lux", "Nasus", "Poppy",
                "Renekton", "Sylas", "Talon", "Wukong", "Annie", "Camille", "Draven", "Ezreal", "Fiora",
                "Jinx", "LeeSin", "Malphite", "Rell", "Sivir", "Vi", "Yasuo", "Yummi", "Alistar", "ChoGath",
                "Jax", "KaiSa", "LeBlanc", "Nilah", "Rammus", "Riven", "Senna", "Sona", "Vayne", "VelKoz",
                "Zoe", "AurelionSol", "BelVeth", "Ekko", "MissFortune", "Samira", "Sejuani", "Sett", "Soraka",
                "Taliyah", "Viego", "Zac", "Zed", "Aphelios", "Fiddlesticks", "Janna", "Leona", "Mordekaiser",
                "Nunu", "Syndra", "Urgot"]

champions_failed = {}

champion_data = {}

champion_origins = {"Underground", "Threat", "Supers", "Star Guardian", "Ox Force", "Mecha: Prime", "Laser Corps",
                "Gadgeteen", "Corrupted", "Civilian", "Anima Squad", "A.D.M.I.N"}

champion_classes = {"Sureshot", "Spellslinger", "Renegade", "Recon", "Prankster", "Mascot", "Heart", "Hacker",
                "Forecaster", "Deulist", "Defender", "Brawler", "Arsenal", "Aegis", "Ace"}

# (origin, first class, second class)
champion_origins_and_classes_dict = {
    "Ashe": ("Lasercorps", "Recon", ""),
    "Blitzcrank": ("A.D.M.I.N", "Brawler", ""),
    "Galio": ("Civilian", "Mascot", ""),
    "Gangplank": ("Supers", "Duelist", ""),
    "Kayle": ("Underground", "Duelist", ""),
    "Lulu": ("Gadgeteens", "Heart", ""),
    "Lux": ("Star Guardian", "Spellslinger", ""),
    "Nasus": ("Anima Squad", "Mascot", ""),
    "Poppy": ("Gadgeteens", "Defender", ""),
    "Renekton": ("Lasercorps", "Brawler", ""),
    "Sylas": ("Anima Squad", "Renegade", ""),
    "Talon": ("Ox Force", "Renegade", ""),
    "Wukong": ("Mecha Prime", "Defender", ""),
    "Annie" : ("Spellslinger", "Gadgeteens", "Ox Force"),
    "Camille": ("A.D.M.I.N", "Renegade", ""), 
    "Draven": ("Mecha Prime", "Ace", ""),
    "Ezreal": ("Underground", "Recon", ""),
    "Fiora": ("Duelist", "Ox Force", ""),
    "Jinx": ("Anima Squad", "Prankster", ""),
    "LeeSin": ("Supers", "Brawler", "Heart"),
    "Malphite": ("Supers", "Mascot", ""),
    "Rell": ("Star Guardian", "Defender", ""),
    "Sivir": ("Civilian", "Sureshot", ""),
    "Vi": ("Underground", "Aegis", "Brawler"),
    "Yasuo": ("Lasercorps", "Duelist", ""),
    "Yummi": ("Star Guardian", "Heart", ""),
    "Alistar": ("Ox Force", "Aegis", "Mascot"), 
    "ChoGath": ("Threat", "", ""),
    "Jax": ("Mecha Prime", "Brawler", ""),
    "KaiSa": ("Star Guardian", "Recon", ""),
    "LeBlanc": ("A.D.M.I.N", "Hacker", "Spellslinger"),
    "Nilah": ("Star Guardian", "Duelist", ""),
    "Rammus": ("Threat", "", ""),
    "Riven": ("Anima Squad", "Brawler", "Defender"),
    "Senna": ("Lasercorps", "Sureshot", ""),
    "Sona": ("Underground", "Heart", "Spellslinger"),
    "Vayne": ("Anima Squad", "Recon", "Duelist"),
    "VelKoz": ("Threat", "", ""),
    "Zoe": ("Gadgeteens", "Hacker", "Prankster"),
    "AurelionSol": ("Threat", "", ""),
    "BelVeth": ("Threat", "", ""),
    "Ekko": ("Star Guardian", "Prankster", "Aegis"),
    "MissFortune": ("Anima Squad", "Ace", ""),
    "Samira": ("Underground", "Sureshot", "Ace"),
    "Sejuani": ("Lasercorps", "Brawler", ""),
    "Sett": ("Mecha Prime", "Defender", ""),
    "Soraka": ("A.D.M.I.N", "Heart", ""),
    "Taliyah": ("Star Guardian", "Spellslinger", ""),
    "Viego": ("Ox Force", "Renegade", ""),
    "Zac": ("Threat", "", ""),
    "Zed": ("Lasercorps", "Duelist", "Hacker"),
    "Aphelios": ("Ox Force", "Arsenal", "Sureshot"),
    "Fiddlesticks": (("Corrupted", "Threat"), "", ""),
    "Janna": ("Civilian", "Forecaster", ""),
    "Leona": ("Mecha Prime", "Aegis", "Renegade"),
    "Mordekaiser": ("Lasercorps", "Ace", ""),
    "Nunu": ("Gadgeteens", "Mascots", ""),
    "Syndra": ("Star Guardian", "Heart", ""),
    "Urgot": ("Threat", "", "")
}

champion_cost_dict = {
    "Ashe": 1,
    "Blitzcrank": 1,
    "Galio": 1,
    "Gangplank": 1,
    "Kayle": 1,
    "Lulu": 1,
    "Lux": 1,
    "Nasus": 1,
    "Poppy": 1,
    "Renekton": 1,
    "Sylas": 1,
    "Talon": 1,
    "Wukong": 1,
    "Annie" : 2,
    "Camille": 2, 
    "Draven": 2,
    "Ezreal": 2,
    "Fiora": 2,
    "Jinx": 2,
    "LeeSin": 2,
    "Malphite": 2,
    "Rell": 2,
    "Sivir": 2,
    "Vi": 2,
    "Yasuo": 2,
    "Yummi": 2,
    "Alistar": 3, 
    "ChoGath": 3,
    "Jax": 3,
    "KaiSa": 3,
    "LeBlanc": 3,
    "Nilah": 3,
    "Rammus": 3,
    "Riven": 3,
    "Senna": 3,
    "Sona": 3,
    "Vayne": 3,
    "VelKoz": 3,
    "Zoe": 3,
    "AurelionSol": 4,
    "BelVeth": 4,
    "Ekko": 4,
    "MissFortune": 4,
    "Samira": 4,
    "Sejuani": 4,
    "Sett": 4,
    "Soraka": 4,
    "Taliyah": 4,
    "Viego": 4,
    "Zac": 4,
    "Zed": 4,
    "Aphelios": 5,
    "Fiddlesticks": 5,
    "Janna": 5,
    "Leona": 5,
    "Mordekaiser": 5,
    "Nunu": 5,
    "Syndra": 5,
    "Urgot": 5
}
print(champion_cost_dict["Senna"])
#augments
#TODO: some augment names might be flawed
augments = {"Absolution", "AceHeart", "AdaptiveDefensives", "A.D.M.I.NHeart", "AegisHeart", "AFK", "AimAssist", 
"AnimaSquadHeart", "Armored-dillo", "AxiomArcI", "BandofThievesI", "BattlemageI", "Behemoth", "BigFriendI", 
"Bigger,BetterBuckler", "BlueBatteryI", "BoxingLessons", "BrawlerHeart", "BuiltDifferentI", "BurningSpirit", "CelestialBlessingI", 
"ChannelledFerromancy", "CivilianHeart", "CombatTrainingI", "Consistency", "CorpsFocus", "CorpsFormation", "CosmicBarrier", 
"CulltheMeek", "CyberneticImplantsI", "CyberneticShellI", "CyberneticUplinkI", "Cyclone", "DefenderHeart", "DeliveryTips", 
"DisintegratorI", "DivineAscent", "DoubleBubble", "DoubleTroubleI", "DuelistHeart", "DynamicDefenses", "Edgelord", 
"ElectrochargeI", "EndlessPizza", "EnergyVoid", "Evasion", "EveryoneGoesBOOM", "ExilesI", "FeatherweightsI", 
"FirstAidKitI", "FlamingRicochet", "Flurry", "FosterGrowth", "FrontlineFencing", "Frostburn", "FrozenTundra", 
"FutureSightI", "GadgeteenHeart", "GetExcited", "GetPaid", "Gifted", "GrowthSpurt", "GuardianSpirit", 
"HackerHeart", "HeartHeart", "HextechRetribution", "HoldtheLine", "IlluminatingSingularity", "IntotheNight", "Invigorate", 
"ItemGrabBagI", "JubilantVeil", "JusticePunch", "Kingslayer", "KnifesEdgeI", "LaserCorpsHeart", "LaserFocus", 
"LategameSpecialist", "LeagueofDraven", "LucentBarrier", "LudensEchoI", "MakeshiftArmorI", "MascotHeart", "Mecha:PRIMEHeart", 
"MirrorImage", "Multi-Shot", "OxForceHeart", "OX-ianRage", "PandorasBench", "PandorasItems", "PetriciteChains", 
"PowerGrid", "PranksterHeart", "PredatoryPrecision", "Preparationl", "RaidersSpoils", "Recombobulator", "ReconHeart", 
"Re-Energize", "ReflectorShield", "ReignofAnger", "RelentlessAssault", "RenegadeHeart", "Reverberation", "RighteousRange", 
"RisingSpellForce", "RocketGrab", "RockSolid", "RuthlessBlades", "SafetyFirst", "SecondWindI", "SiphoningWinds", 
"SleepyTime", "Smash", "SoulEater", "SpellslingerHeart", "SpikedShell", "SpiritoftheExile", "SpreadShot", 
"StacksonStacks", "StandUnitedI", "Star-Crossed", "StarGuardianHeart", "SteadfastPresence", "SupersHeart", "SureshotHeart", 
"ThrilloftheHuntI", "TinyTitans", "TriForceI", "TriumphantReturn", "Undercurrent", "UndergroundHeart", "UnrelentingForce", 
"VitalityoftheOx", "Zoomies", "AceCrest", "A.D.M.I.NCrest", "AegisCrest", "AncientArchivesI", "AnimaSquadCrest", "Ascension", "AxiomArcII", 
"BackforBlood", "BattlemageII", "BetheStone", "BetterTogether", "BigFriendII", "BrawlerCrest", "BuiltDifferentII", 
"BunnyMercenary", "CalculatedLoss", "CelestialBlessingII", "Chronobreak", "CivilianCrest", "ClearMind", "ClutteredMind", 
"CombatTrainingII", "ComponentGrabBag", "ComponentGrabBag+", "ContemptfortheWeak", "CyberneticImplantsII", "CyberneticShellII", "CyberneticUplinkII", 
"Daredevil", "DefenderCrest", "DisintegratorII", "DoubleTroubleII", "DuelistCrest", "ElasticSlingshot", "ElectrochargeII", 
"ExilesII", "ExtinctionEvent", "FeatherweightsII", "GadgetExpert", "GlacialPrison", "HackerCrest", "HeartCrest", 
"Heartstopper", "Hustler", "Infuse", "JeweledLotus", "KnifesEdgeII", "LaserCorpsCrest", "LastStand", 
"LudensEchoII", "MakeItRain", "MakeshiftArmorII", "MascotCrest", "Mecha:PRIMECrest", "MetabolicAccelerator", "OxForceCrest", 
"PartnersinCrime", "PhonyFrontline", "PortableForge", "PranksterCrest", "PreparationII", "PunchProtocol", "ReconCrest", 
"RegenerativeShields", "RenegadeCrest", "Resonance", "RichGetRicher", "RichGetRicher+", "SalvageBin", "ScopedWeaponsI", 
"SecondWindII", "ShadowJutsu", "Shatter", "SpellslingerCrest", "StandUnitedII", "StarGuardianCrest", "Stoneweaver", 
"StyleandFlair", "SunfireBoard", "Supersize", "SureshotCrest", "ThreesCompany", "ThrilloftheHuntII", "TradeSector", 
"TradeSector+", "TriForceII", "TrueTwos", "UndergroundCrest", "Upgrade:Berserk", "VelocityImpact", "Voidmother",
"AbsoluteCorruption", "AceCrown", "A.D.M.I.NCrown", "AegisCrown", "AncientArchivesII", "AnimaSquadCrown", "ArmorPiercingRounds", 
"BandofThieves", "BattlemageIII", "BinaryAirdrop", "BrawlerCrown", "BuiltDifferentIII", "CelestialBlessingIII", "CivilianCrown", 
"CombatTrainingIII", "ContagiousLaughter", "CruelPact", "CursedCrown", "CyberneticImplantsIII", "CyberneticShellIII", "CyberneticUplinkIII", 
"DefenderCrown", "DisintegratorIII", "DoubleTroubleIII", "DuelistCrown", "EclipsePrime", "ElectrochargeIII", "EmpoweredReserves", 
"ExaggeratedReporting", "ExilesIII", "FeatherweightsIII", "FutureSightII", "GadgeteenSoul", "GoldenTicket", "HackerCrown", 
"HeartCrown", "HighEndShopping", "HighRoller", "ItemGrabBagII", "KnifesEdgeIII", "LaserCorpsCrown", "LevelUp", 
"LivingForge", "LockedandLoaded", "LuckyGloves", "LudensEchoIII", "MakeshiftArmorIII", "MarchofProgress", "MascotCrown", 
"Mecha:PRIMECrown", "NewRecruit", "NotSoHeavyMetal", "Obliterate", "OxForceCrown", "perfected-solar-flare", "PowerOverwhelming", 
"PranksterCrown", "PreparationIII", "RadiantRelics", "RapidReporting", "ReconCrown", "RenegadeCrown", "RisingTide", 
"ScopedWeaponsII", "Shiny", "SpellslingerCrown", "StandUnitedIII", "StarGuardianCrown", "SupersSoul", "SureshotCrown", 
"TheGoldenEgg", "TheySeeMeRolling", "ThinkFast", "TraumaticMemories", "TriForceIII", "UndergroundCrown", "UndergroundSoul", 
"UrfsGrabBagII", "VerdantVeil", "Windfall", "Windfall+", "Windfall++", "WiseSpending", "WoodlandCharm", "ChanneledFerromancy"}

augments1 = {"Absolution", "AceHeart", "AdaptiveDefensives", "A.D.M.I.NHeart", "AegisHeart", "AFK", "AimAssist", 
"AnimaSquadHeart", "Armored-dillo", "AxiomArcI", "BandofThievesI", "BattlemageI", "Behemoth", "BigFriendI", 
"Bigger,BetterBuckler", "BlueBatteryI", "BoxingLessons", "BrawlerHeart", "BuiltDifferentI", "BurningSpirit", "CelestialBlessingI", 
"ChannelledFerromancy", "CivilianHeart", "CombatTrainingI", "Consistency", "CorpsFocus", "CorpsFormation", "CosmicBarrier", 
"CulltheMeek", "CyberneticImplantsI", "CyberneticShellI", "CyberneticUplinkI", "Cyclone", "DefenderHeart", "DeliveryTips", 
"DisintegratorI", "DivineAscent", "DoubleBubble", "DoubleTroubleI", "DuelistHeart", "DynamicDefenses", "Edgelord", 
"ElectrochargeI", "EndlessPizza", "EnergyVoid", "Evasion", "EveryoneGoesBOOM", "ExilesI", "FeatherweightsI", 
"FirstAidKitI", "FlamingRicochet", "Flurry", "FosterGrowth", "FrontlineFencing", "Frostburn", "FrozenTundra", 
"FutureSightI", "GadgeteenHeart", "GetExcited", "GetPaid", "Gifted", "GrowthSpurt", "GuardianSpirit", 
"HackerHeart", "HeartHeart", "HextechRetribution", "HoldtheLine", "IlluminatingSingularity", "IntotheNight", "Invigorate", 
"ItemGrabBagI", "JubilantVeil", "JusticePunch", "Kingslayer", "KnifesEdgeI", "LaserCorpsHeart", "LaserFocus", 
"LategameSpecialist", "LeagueofDraven", "LucentBarrier", "LudensEchoI", "MakeshiftArmorI", "MascotHeart", "Mecha:PRIMEHeart", 
"MirrorImage", "Multi-Shot", "OxForceHeart", "OX-ianRage", "PandorasBench", "PandorasItems", "PetriciteChains", 
"PowerGrid", "PranksterHeart", "PredatoryPrecision", "Preparationl", "RaidersSpoils", "Recombobulator", "ReconHeart", 
"Re-Energize", "ReflectorShield", "ReignofAnger", "RelentlessAssault", "RenegadeHeart", "Reverberation", "RighteousRange", 
"RisingSpellForce", "RocketGrab", "RockSolid", "RuthlessBlades", "SafetyFirst", "SecondWindI", "SiphoningWinds", 
"SleepyTime", "Smash", "SoulEater", "SpellslingerHeart", "SpikedShell", "SpiritoftheExile", "SpreadShot", 
"StacksonStacks", "StandUnitedI", "Star-Crossed", "StarGuardianHeart", "SteadfastPresence", "SupersHeart", "SureshotHeart", 
"ThrilloftheHuntI", "TinyTitans", "TriForceI", "TriumphantReturn", "Undercurrent", "UndergroundHeart", "UnrelentingForce", 
"VitalityoftheOx", "Zoomies", "ChanneledFerromancy"}

augments2 = {"AceCrest", "A.D.M.I.NCrest", "AegisCrest", "AncientArchivesI", "AnimaSquadCrest", "Ascension", "AxiomArcII", 
"BackforBlood", "BattlemageII", "BetheStone", "BetterTogether", "BigFriendII", "BrawlerCrest", "BuiltDifferentII", 
"BunnyMercenary", "CalculatedLoss", "CelestialBlessingII", "Chronobreak", "CivilianCrest", "ClearMind", "ClutteredMind", 
"CombatTrainingII", "ComponentGrabBag", "ComponentGrabBag+", "ContemptfortheWeak", "CyberneticImplantsII", "CyberneticShellII", "CyberneticUplinkII", 
"Daredevil", "DefenderCrest", "DisintegratorII", "DoubleTroubleII", "DuelistCrest", "ElasticSlingshot", "ElectrochargeII", 
"ExilesII", "ExtinctionEvent", "FeatherweightsII", "GadgetExpert", "GlacialPrison", "HackerCrest", "HeartCrest", 
"Heartstopper", "Hustler", "Infuse", "JeweledLotus", "KnifesEdgeII", "LaserCorpsCrest", "LastStand", 
"LudensEchoII", "MakeItRain", "MakeshiftArmorII", "MascotCrest", "Mecha:PRIMECrest", "MetabolicAccelerator", "OxForceCrest", 
"PartnersinCrime", "PhonyFrontline", "PortableForge", "PranksterCrest", "PreparationII", "PunchProtocol", "ReconCrest", 
"RegenerativeShields", "RenegadeCrest", "Resonance", "RichGetRicher", "RichGetRicher+", "SalvageBin", "ScopedWeaponsI", 
"SecondWindII", "ShadowJutsu", "Shatter", "SpellslingerCrest", "StandUnitedII", "StarGuardianCrest", "Stoneweaver", 
"StyleandFlair", "SunfireBoard", "Supersize", "SureshotCrest", "ThreesCompany", "ThrilloftheHuntII", "TradeSector", 
"TradeSector+", "TriForceII", "TrueTwos", "UndergroundCrest", "Upgrade:Berserk", "VelocityImpact", "Voidmother"}

augments3 = {"AbsoluteCorruption", "AceCrown", "A.D.M.I.NCrown", "AegisCrown", "AncientArchivesII", "AnimaSquadCrown", "ArmorPiercingRounds", 
"BandofThieves", "BattlemageIII", "BinaryAirdrop", "BrawlerCrown", "BuiltDifferentIII", "CelestialBlessingIII", "CivilianCrown", 
"CombatTrainingIII", "ContagiousLaughter", "CruelPact", "CursedCrown", "CyberneticImplantsIII", "CyberneticShellIII", "CyberneticUplinkIII", 
"DefenderCrown", "DisintegratorIII", "DoubleTroubleIII", "DuelistCrown", "EclipsePrime", "ElectrochargeIII", "EmpoweredReserves", 
"ExaggeratedReporting", "ExilesIII", "FeatherweightsIII", "FutureSightII", "GadgeteenSoul", "GoldenTicket", "HackerCrown", 
"HeartCrown", "HighEndShopping", "HighRoller", "ItemGrabBagII", "KnifesEdgeIII", "LaserCorpsCrown", "LevelUp", 
"LivingForge", "LockedandLoaded", "LuckyGloves", "LudensEchoIII", "MakeshiftArmorIII", "MarchofProgress", "MascotCrown", 
"Mecha:PRIMECrown", "NewRecruit", "NotSoHeavyMetal", "Obliterate", "OxForceCrown", "perfected-solar-flare", "PowerOverwhelming", 
"PranksterCrown", "PreparationIII", "RadiantRelics", "RapidReporting", "ReconCrown", "RenegadeCrown", "RisingTide", 
"ScopedWeaponsII", "Shiny", "SpellslingerCrown", "StandUnitedIII", "StarGuardianCrown", "SupersSoul", "SureshotCrown", 
"TheGoldenEgg", "TheySeeMeRolling", "ThinkFast", "TraumaticMemories", "TriForceIII", "UndergroundCrown", "UndergroundSoul", 
"UrfsGrabBagII", "VerdantVeil", "Windfall", "Windfall+", "Windfall++", "WiseSpending", "WoodlandCharm"}

hero_augments1 = {'CorpsFocus', 'LaserFocus', 'RocketGrab', 'DynamicDefenses', 'SafetyFirst', 'JusticePunch', 'GetPaid', 'FlamingRichochet',
'RighteousRange', 'DivineAscent', 'FosterGrowth', 'GrowthSpurt', 'LucentBarrier', 'IlluminatingSingularity', 'SoulEater', 'StacksonStacks',
'SteadfastPresence', 'Bigger,BetterBuckler', 'CulltheMeek', 'ReignofAnger', 'PetriciteChains', 'Kingslayer', 'OX-ianRage', 'Edgelord',
'Re-Energize', 'Cyclone', 'BurningSpirit', 'ReflectorShield', 'HextechRetribution', 'AdaptiveDefensives', 'RuthlessBlades', 'LeagueofDraven',
'RaidersSpoils', 'RisingSpellForce', 'VitalityoftheOx', 'FrontlineFencing', 'EveryoneGoesBOOM', 'GetExcited', 'Invigorate', 'Flurry',
'GuardianSpirit', 'RockSolid', 'ChanneledFerromancy', 'HoldtheLine', 'EndlessPizza', 'DeliveryTips', 'BoxingLessons', 'UnrelentingForce',
'SpiritoftheExile', 'SiphoningWinds', 'Zoomies', 'PredatoryPrecision', 'Behemoth', 'Smash', 'CosmicBarrier', 'EnergyVoid', 'Evasion',
'RelentlessAssault', 'Star-Crossed', 'Multi-Shot', 'MirrorImage', 'AimAssist', 'JubilantVeil', 'Gifted', 'Armored-dillo', 'SpikedShell',
'TriumphantReturn', 'Reverberation', 'CorpsFormation', 'Absolution', 'Undercurrent', 'PowerGrid', 'IntotheNight', 'SpreadShot', 'FrozenTundra',
'Frostburn', 'SleepyTime', 'DoubleBubble'}

hero_augments2 = {'VelocityImpact', 'ExtinctionEvent', 'Voidmother', 'BackforBlood', 'Chronobreak', 'Resonance', 'MakeItRain', 'BunnyMercenary',
'Daredevil', 'StyleandFlair', 'Shatter', 'GlacialPrison', 'RegenerativeShields', 'PunchProtocol', 'Infuse', 'Upgrade:Berserk', 'BetheStone', 'Stoneweaver',
'PartnersinCrime', 'Heartstopper', 'ElasticSlingshot', 'Supersize', 'ContemptfortheWeak', 'ShadowJutsu'}

hero_augments3 = {'LockedandLoaded', 'ArmorPiercingRounds', 'AbsoluteCorruption', 'TraumaticMemories', 'ExaggeratedReporting', 'RapidReporting',
'EclipsePrime', 'perfected-solar-flare', 'Obliterate', 'NotSoHeavyMetal', 'ContagiousLaughter', 'TheySeeMeRolling', 'EmpoweredReserves',
'PowerOverwhelming', 'RisingTide', 'Shiny'}

support_hero_augments = {'CorpsFocus', 'RocketGrab', 'SafetyFirst', 'GetPaid', 'RighteousRange', 'FosterGrowth',
                        'LucentBarrier', 'SoulEater', 'SteadfastPresence', 'CulltheMeek', 'PetriciteChains', 'OX-ianRage',
                        'Re-Energize', 'BurningSpirit', 'HextechRetribution', 'RuthlessBlades', 'RaidersSpoils', 'VitalityoftheOx',
                        'EveryoneGoesBOOM', 'Invigorate', 'GuardianSpirit', 'ChanneledFerromancy', 'EndlessPizza', 'BoxingLessons',
                        'SpiritoftheExile', 'Zoomies', 'Behemoth', 'CosmicBarrier', 'Evasion', 'Star-Crossed', 'MirrorImage',
                        'JubilantVeil', 'Armored-dillo', 'TriumphantReturn', 'CorpsFormation', 'Undercurrent', 'IntotheNight',
                        'FrozenTundra', 'SleepyTime', 'VelocityImpact', 'Voidmother', 'Chronobreak', 'MakeItRain', 'Daredevil',
                        'Shatter', 'RegenerativeShields', 'Infuse', 'BetheStone', 'PartnersinCrime', 'ElasticSlingshot',
                        'ContemptfortheWeak', 'LockedandLoaded', 'AbsoluteCorruption', 'ExaggeratedReporting', 'EclipsePrime',
                        'Obliterate', 'ContagiousLaughter', 'EmpoweredReserves', 'RisingTide'}

carry_hero_augments = {'LaserFocus', 'DynamicDefenses', 'JusticePunch', 'FlamingRichochet', 'DivineAscent', 'GrowthSpurt',
                    'IlluminatingSingularity', 'StacksonStacks', 'Bigger,BetterBuckler', 'ReignofAnger', 'Kingslayer', 'Edgelord',
                    'Cyclone', 'ReflectorShield', 'AdaptiveDefensives', 'LeagueofDraven', 'RisingSpellForce', 'FrontlineFencing',
                    'GetExcited', 'Flurry', 'RockSolid', 'HoldtheLine', 'DeliveryTips', 'UnrelentingForce', 'SiphoningWinds',
                    'PredatoryPrecision', 'Smash', 'EnergyVoid', 'RelentlessAssault', 'Multi-Shot', 'AimAssist', 'Gifted',
                    'SpikedShell', 'Reverberation', 'Absolution', 'PowerGrid', 'SpreadShot', 'Frostburn', 'DoubleBubble',
                    'ExtinctionEvent', 'BackforBlood', 'Resonance', 'BunnyMercenary', 'StyleandFlair', 'GlacialPrison',
                    'PunchProtocol', 'Upgrade:Berserk', 'Stoneweaver', 'Heartstopper', 'Supersize', 'ShadowJutsu', 'ArmorPiercingRounds',
                    'TraumaticMemories', 'RapidReporting', 'perfected-solar-flare', 'NotSoHeavyMetal', 'TheySeeMeRolling',
                    'PowerOverwhelming', 'Shiny'}

# (support_augment, carry_augment)
hero_augments_dict = {
                "Senna": ("CorpsFormation", "Absolution"),
                "Camille": ("HextechRetribution", "AdaptiveDefensives"),
                "LeBlanc": ("MirrorImage", "AimAssist"),
                "Rammus": ("Armored-dillo", "SpikedShell"),
                "Alistar": ("Behemoth", "Smash"),
                "Poppy": ("SteadfastPresence", "Bigger,BetterBuckler"),
                "Vi": ("BoxingLessons", "UnrelentingForce"),
                "Annie": ("BurningSpirit", "ReflectorShield"),
                "Rell": ("ChanneledFerromancy", "HoldtheLine"),
                "Ashe": ("CorpsFocus", "LaserFocus"),
                "ChoGath": ("CosmicBarrier", "EnergyVoid"),
                "Renekton": ("CulltheMeek", "ReignofAnger"),
                "Wukong": ("Re-Energize", "Cyclone"),
                "Sivir": ("EndlessPizza", "DeliveryTips"),
                "Kayle": ("RighteousRange", "DivineAscent"),
                "Zoe": ("SleepyTime", "DoubleBubble"),
                "Blitzcrank": ("RocketGrab", "DynamicDefenses"),
                "Talon": ("OX-ianRage", "Edgelord"),
                "Jax": ("Evasion", "RelentlessAssault"),
                "Jinx": ("EveryoneGoesBOOM", "GetExcited"),
                "Gangplank": ("GetPaid", "FlamingRichochet"),
                "LeeSin": ("Invigorate", "Flurry"),
                "Lulu": ("FosterGrowth", "GrowthSpurt"),
                "Fiora": ("VitalityoftheOx", "FrontlineFencing"),
                "VelKoz": ("FrozenTundra", "Frostburn"),
                "Nilah": ("JubilantVeil", "Gifted"),
                "Malphite": ("GuardianSpirit", "RockSolid"),
                "Lux": ("LucentBarrier", "IlluminatingSingularity"),
                "Vayne": ("IntotheNight", "SpreadShot"),
                "Galio": ("SafetyFirst", "JusticePunch"),
                "Sylas": ("PetriciteChains", "Kingslayer"),
                "Draven": ("RuthlessBlades", "LeagueofDraven"),
                "KaiSa": ("Star-Crossed", "Multi-Shot"),
                "Sona": ("Undercurrent", "PowerGrid"),
                "Yummi": ("Zoomies", "PredatoryPrecision"),
                "Ezreal": ("RaidersSpoils", "RisingSpellForce"),
                "Riven": ("TriumphantReturn", "Reverberation"),
                "Yasuo": ("SpiritoftheExile", "SiphoningWinds"),
                "Nasus": ("SoulEater", "StacksonStacks"),
                "BelVeth": ("Voidmother", "BackforBlood"),
                "Taliyah": ("BetheStone", "Stoneweaver"),
                "MissFortune": ("MakeItRain", "BunnyMercenary"),
                "Ekko": ("Chronobreak", "Resonance"),
                "Zed": ("ContemptfortheWeak", "ShadowJutsu"),
                "Samira": ("Daredevil", "StyleandFlair"),
                "Zac": ("ElasticSlingshot", "Supersize"),
                "AurelionSol": ("VelocityImpact", "ExtinctionEvent"),
                "Sejuani": ("Shatter", "GlacialPrison"),
                "Viego": ("PartnersinCrime", "Heartstopper"),
                "Soraka": ("Infuse", "Upgrade:Berserk"),
                "Sett": ("RegenerativeShields", "PunchProtocol"),
                "Fiddlesticks": ("AbsoluteCorruption", "TraumaticMemories"),
                "Aphelios": ("LockedandLoaded", "ArmorPiercingRounds"),
                "Nunu": ("ContagiousLaughter", "TheySeeMeRolling"),
                "Leona": ("EclipsePrime", "perfected-solar-flare"),
                "Syndra": ("EmpoweredReserves", "PowerOverwhelming"),
                "Janna": ("ExaggeratedReporting", "RapidReporting"),
                "Mordekaiser": ("Obliterate", "NotSoHeavyMetal"),
                "Urgot": ("RisingTide", "Shiny")
}

def compare_augments_typo():
    for champion in champions_list:
        augment_pair = hero_augments_dict[champion]
        augment1 = augment_pair[0]
        augment2 = augment_pair[1]
        if(not augment1 in augments):
            print(champion + " and " + augment1)
        if(not augment2 in augments):
            print(champion + " and " + augment2)
#compare_augments_typo()

def create_support_augments_list():
    list = []
    for champion in champions_list:
        augment_pair = hero_augments_dict[champion]
        support_item = augment_pair[0]
        list.append(support_item)
    print(list)
def create_carry_augments_list():
    list = []
    for champion in champions_list:
        augment_pair = hero_augments_dict[champion]
        carry_item = augment_pair[1]
        list.append(carry_item)
    print(list)

def create_hero_augments_list1():
    list = []
    for champion in champions_list:
        if(champion in champions_one_cost or champion in champions_two_cost or champion in champions_three_cost):
            augment_pair = hero_augments_dict[champion]
            support_item = augment_pair[0]
            carry_item = augment_pair[1]
            list.append(support_item)
            list.append(carry_item)
    print(list)

def create_hero_augments_list2():
    list = []
    for champion in champions_list:
        if(champion in champions_four_cost):
            augment_pair = hero_augments_dict[champion]
            support_item = augment_pair[0]
            carry_item = augment_pair[1]
            list.append(support_item)
            list.append(carry_item)
    print(list)

def create_hero_augments_list3():
    list = []
    for champion in champions_list:
        if(champion in champions_five_cost):
            augment_pair = hero_augments_dict[champion]
            support_item = augment_pair[0]
            carry_item = augment_pair[1]
            list.append(support_item)
            list.append(carry_item)
    print(list)

#consumables
consumables = {"LoadedDice", "MagneticRemover", "NeekosHelp", "Reforger", "TargetDummy", "TomeofTraits"}
# lvl_progress
level_progress = [2, 6, 10, 20, 36, 56, 80, 100]
