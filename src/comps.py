import generalData
import coordinates

# final comp [champ_name, champ_slot, champ_items, champ_stars]

# Astral comp
champs_with_items = ["Lux", "Sylas", "Varus", "Skarner"]
best_lux_items = ["JeweledGauntlet", "SpearofShojin", "ArchangelsStaff"]
lux_items_equipped = [False, False, False]
best_sylas_items = ["SunfireCape", "GargoyleStoneplate"]
sylas_items_equipped = [False, False]
best_varus_items = ["MageEmblem", "StatikkShiv", "GuinsoosRageblade"]
varus_items_equipped = [False, False, False]
best_skarner_items = ["ProtectorsVow"]
skarner_items_equipped = [False]
item_lists = [best_lux_items, best_sylas_items, best_varus_items, best_skarner_items]
equipped_items_boolean_lists = [lux_items_equipped, sylas_items_equipped, varus_items_equipped, skarner_items_equipped]

# lvl 8 with Aurelion Sol
final_lux_comp_with_aurelion = ["Skarner", 3, best_skarner_items, 3, "Sylas", 5, best_sylas_items, 2,
                    "Vladimir", 20, "None", 3, "Nidalee", 21, "None", 3,
                    "Varus", 25, best_varus_items, 3, "AurelionSol", 26, "None", 2,
                    "Lux", 27, best_lux_items, 3]

# lvl 8 without Aurelion Sol
core_lux_comp_without_aurelion = ["Skarner", 3, best_skarner_items, 3, "Sylas", 5, best_sylas_items, 2,
                    "Vladimir", 20, "None", 3, "Nidalee", 21, "None", 3,
                    "Varus", 25, best_varus_items, 3, "Lux", 27, best_lux_items, 3]

fill_pairs = [("Twitch", 26, "None", 2, "Jayce", 24, "None", 2), ("Lilia", 13, "None", 2, "Zoe", 26, "None", 2)]

lux_comp_champs_on_board = {
                            "Skarner": False,
                            "Sylas": False,
                            "Vladimir": False,
                            "Nidalee": False,
                            "Varus": False,
                            "Lux": False
}
lux_comp_champs_max_star_reached = {
                            "Skarner": False,
                            "Sylas": False,
                            "Vladimir": False,
                            "Nidalee": False,
                            "Varus": False,
                            "Lux": False
}
lux_comp_stars = {
                            "Skarner": 3,
                            "Sylas": 2,
                            "Vladimir": 3,
                            "Nidalee": 3,
                            "Varus": 3,
                            "Lux": 3
}
how_many_unique_wanted_champs_on_board = 0 # initalisation global variable
lux_comp_champs = {"Skarner", "Sylas", "Vladimir", "Nidalee", "Varus", "Lux"}
lux_comp_champs_list = ["Skarner", "Sylas", "Vladimir", "Nidalee", "Varus", "Lux"]
lux_comp_star_coords = [coordinates.skarner_star_coords, coordinates.sylas_star_coords, coordinates.vladimir_star_coords, coordinates.nidalee_star_coords, coordinates.varus_star_coords, coordinates.lux_star_coords]
lux_comp_placement_on_board_list = [3, 5, 20, 21, 25, 27]
lux_comp_placement_on_board = {
                            "Skarner": 3,
                            "Sylas": 5,
                            "Vladimir": 20,
                            "Nidalee": 21,
                            "Varus": 25,
                            "Lux": 27
}
lux_comp_cost_dict = {
                        "Skarner": 1,
                        "Sylas": 3,
                        "Vladimir": 1,
                        "Nidalee": 1,
                        "Varus": 3,
                        "Lux": 2
}
lux_augments_ranked = ["PortableForge", "CelestialBlessingII", "MageCrown", "UrfsGrabBagI", "ThrilloftheHuntII", "MageCrest", "JeweledLotus", 
"BetterTogether", "ComponentGrabBag", "GuildCrest", "GuildCrown", "BlueBatteryI", "CyberneticUplinkII", "SecondWindII", 
"Ascension", "CelestialBlessingI", "MageHeart", "BandofThievesI", "LudensEchoI", "ThrilloftheHuntI", "StandUnitedII", 
"CelestialBlessingIII", "BlueBatteryII", "ItemGrabBagI", "PreparationII", "SecondWindI", "EvokerCrown", "CyberneticUplinkIII", 
"EssenceTheft", "LudensEchoII", "BigFriendII", "Oasis", "LagoonCrest", "AxiomArcII", "TinyTitans", 
"BaseCamp", "AncientArchivesI", "ProtectorsoftheCosmos", "ScalescornCrown", "CyberneticUplinkI", "LagoonCrown", "EvokerCrest", 
"Weakspot", "PresstheAttack", "MysticHeart", "TheGoldenEgg", "PreparationI", "BeastsDen", "PersonalTraining", 
"LootMaster", "CyberneticShellII", "LevelUp", "LivingForgeHallucinate", "ExilesII", "WoodlandCharm", "MirageCrest", 
"EvokerHeart", "CyberneticShellI", "CalculatedLoss", "RichGetRicher", "BuiltDifferentI", "Scorch", "ExilesI", 
"SwiftshotCrest", "TriForceI", "ShimmerscaleHeart", "TriForceIII", "BruiserHeart", "DoubleTroubleII", "GoldenTicket", 
"DevastatingCharge", "GuardianCrown", "RichGetRicher+", "Windfall++", "BandofThievesII", "HeroicPresence", "CruelPact", 
"SalvageBin", "DragonmancerConference", "MirageHeart", "BigFriendI", "SwiftshotCrown", "BruiserCrest", "Tantrum", 
"CyberneticShellIII", "BestFriendsI", "ElectrochargeIII", "ThinkFast", "AncientArchivesII", "GuardianCrest", "ScopedWeaponsI", 
"TitanicStrength", "TrueTwos", "ScopedWeaponsII", "BattlemageII", "CyberneticImplantsI", "HighRoller", "Windfall", 
"JadeSoul", "Hero-In-Training", "MirageCrown", "CombatTraining", "CavalierUnity", "DarkflightCrown", "ItemGrabBagII", 
"ShimmerscaleCrest", "PandorasItems", "ClutteredMind", "TradeSector", "ElectrochargeII", "GearUpgrades", "AxiomArcI", 
"SunfireBoard", "StandUnitedIII", "LagoonHeart", "StandUnitedI", "MarchofProgress", "BuiltDifferentIII", "CyberneticImplantsII", 
"HighTide", "ElectrochargeI", "NewRecruit", "DoubleTroubleIII", "GadgetExpert", "CyberneticImplantsIII", "BuiltDifferentII", 
"ShimmerscaleSoul", "CursedCrown", "FirstAidKitI", "PandorasBench", "BinaryAirdrop", "LategameSpecialist", "FirstAidKitII", 
"DragonmancerCrown", "LastStand", "RadiantRelics", "GuildHeart", "LudensEchoIII", "TradeSector+", "PreparationIII", 
"BestFriendsII", "TriForceII", "UrfsGrabBagII", "CavalierCrown", "JadeCrest", "Terrify", "WiseSpending", 
"AFK", "DragonmancerCrest", "ClearMind", "CavalierCrest", "Consistency", "MetabolicAccelerator", "AgeofDragons", 
"ScalescornCrest", "DragonImperialist", "HighEndShopping", "SwiftshotHeart", "LuckyGloves", "ScalescornHeart", "KnifesEdgeII", 
"FeatherweightsI", "BruiserCrown", "FeatherweightsII", "MysticSoul", "WarriorHeart", "ThreesCompany", "AssassinCrown", 
"FeatherweightsIII", "PaytoWin", "CavalierHeart", "JadeHeart", "GuardianHeart", "Windfall+", "TempestCrown", 
"FutureSightII", "ShapeshifterHeart", "BattlemageI", "BestFriendsIII", "Penitence", "TempestHeart", "EyeoftheStorm", 
"VerdantVeil", "DarkflightCrest", "Hustler", "ShapeshifterSoul", "WarriorCrown", "EternalProtection", "FutureSightI", 
"BirthdayPresent", "DragonSoul", "KnifesEdgeIII", "WarriorCrest", "TempestCrest", "HotShot", "Tiamat", 
"WhispersHeart", "ExilesIII", "Ricochet", "DoubleTroubleI", "RagewingHeart", "BattlemageIII", "Recombobulator", 
"Cutthroat", "CannoneerHeart", "CannoneerCrest", "RagewingSoul", "DarkflightHeart", "AssassinHeart", "CannoneerCrown", 
"SoulSiphon", "Knife's Edge I", "AFK", "LivingForge", "Part-TimeAssassin", "PreparationI", "PreparationIII", "Dragonmancer Conference",
"Loot Master", "Personal Training", "Preparation II", "The Golden Egg"]

best_augments_lux_list = ["PortableForge", "CelestialBlessingII", "MageCrown", "UrfsGrabBagI", "ThrilloftheHuntII", "MageCrest", "JeweledLotus", 
"BetterTogether", "ComponentGrabBag", "GuildCrest", "GuildCrown", "BlueBatteryI", "CyberneticUplinkII", "SecondWindII", 
"Ascension", "CelestialBlessingI", "MageHeart", "BandofThievesI", "LudensEchoI", "ThrilloftheHuntI", "StandUnitedII", 
"CelestialBlessingIII", "BlueBatteryII", "ItemGrabBagI", "PreparationII", "SecondWindI", "EvokerCrown", "CyberneticUplinkIII", 
"EssenceTheft", "LudensEchoII", "BigFriendII", "Oasis", "LagoonCrest", "AxiomArcII", "TinyTitans", 
"BaseCamp", "AncientArchivesI", "ProtectorsoftheCosmos", "ScalescornCrown", "CyberneticUplinkI", "LagoonCrown", "EvokerCrest", 
"Weakspot", "PresstheAttack", "MysticHeart", "TheGoldenEgg", "PreparationI", "BeastsDen", "PersonalTraining", 
"LootMaster", "CyberneticShellII", "LevelUp", "LivingForgeHallucinate", "ExilesII", "WoodlandCharm", "MirageCrest", 
"EvokerHeart", "CyberneticShellI", "CalculatedLoss", "RichGetRicher", "BuiltDifferentI", "Scorch", "ExilesI", 
"SwiftshotCrest", "TriForceI", "ShimmerscaleHeart", "TriForceIII", "BruiserHeart", "DoubleTroubleII", "GoldenTicket", 
"DevastatingCharge", "GuardianCrown", "RichGetRicher+", "Windfall++", "BandofThievesII", "HeroicPresence", "CruelPact", 
"SalvageBin", "DragonmancerConference", "MirageHeart", "BigFriendI", "SwiftshotCrown", "BruiserCrest", "Tantrum", 
"CyberneticShellIII", "BestFriendsI", "ElectrochargeIII", "ThinkFast", "AncientArchivesII", "GuardianCrest", "ScopedWeaponsI", 
"TitanicStrength", "TrueTwos", "ScopedWeaponsII", "BattlemageII", "CyberneticImplantsI", "HighRoller", "Windfall", 
"JadeSoul", "Hero-In-Training", "MirageCrown", "CombatTraining", "CavalierUnity", "DarkflightCrown", "ItemGrabBagII", 
"ShimmerscaleCrest", "PandorasItems", "ClutteredMind", "TradeSector", "ElectrochargeII", "GearUpgrades", "AxiomArcI", 
"SunfireBoard", "StandUnitedIII", "LagoonHeart", "StandUnitedI", "MarchofProgress", "BuiltDifferentIII", "CyberneticImplantsII", 
"HighTide", "ElectrochargeI", "NewRecruit", "DoubleTroubleIII", "GadgetExpert", "CyberneticImplantsIII", "BuiltDifferentII", 
"ShimmerscaleSoul", "CursedCrown", "FirstAidKitI", "PandorasBench", "BinaryAirdrop", "LategameSpecialist", "FirstAidKitII", 
"DragonmancerCrown", "LastStand", "RadiantRelics", "GuildHeart", "LudensEchoIII", "TradeSector+", "PreparationIII", 
"BestFriendsII", "TriForceII", "UrfsGrabBagII", "CavalierCrown", "JadeCrest", "Terrify", "WiseSpending", 
"AFK", "DragonmancerCrest", "ClearMind", "CavalierCrest", "Consistency", "MetabolicAccelerator", "AgeofDragons", 
"ScalescornCrest", "DragonImperialist", "HighEndShopping", "SwiftshotHeart", "LuckyGloves", "ScalescornHeart", "KnifesEdgeII", 
"FeatherweightsI", "BruiserCrown", "FeatherweightsII", "MysticSoul", "WarriorHeart", "ThreesCompany", "AssassinCrown", 
"FeatherweightsIII", "PaytoWin", "CavalierHeart", "JadeHeart", "GuardianHeart", "Windfall+", "TempestCrown", 
"FutureSightII", "ShapeshifterHeart", "BattlemageI", "BestFriendsIII", "Penitence", "TempestHeart", "EyeoftheStorm", 
"VerdantVeil", "DarkflightCrest", "Hustler", "ShapeshifterSoul", "WarriorCrown", "EternalProtection", "FutureSightI", 
"BirthdayPresent", "DragonSoul", "KnifesEdgeIII", "WarriorCrest", "TempestCrest", "HotShot", "Tiamat", 
"WhispersHeart", "ExilesIII", "Ricochet", "DoubleTroubleI", "RagewingHeart", "BattlemageIII", "Recombobulator", 
"Cutthroat", "CannoneerHeart", "CannoneerCrest", "RagewingSoul", "DarkflightHeart", "AssassinHeart", "CannoneerCrown", 
"SoulSiphon", "Knife's Edge I", "AFK", "LivingForge", "Part-TimeAssassin", "PreparationI", "PreparationIII", "Dragonmancer Conference",
"Loot Master", "Personal Training", "Preparation II", "The Golden Egg"]

def get_missing_augments(augments_ranked) -> list:
    missing_augments = []
    for augment in generalData.augments:
        if(not augments_ranked.__contains__(augment)):
            missing_augments.append(augment)
    if(len(missing_augments) == 0):
        print("all augments found")
    return missing_augments
