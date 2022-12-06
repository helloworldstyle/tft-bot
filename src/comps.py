import generalData
import coordinates

#TODO: champ as an object with attributes in general (not as one specific unit on the field or bench)

#TODO: comp as an object
class Comp:
    def __init__(self, name):
        self.name = name


how_many_unique_wanted_champs_on_board = 0 # initalisation global variable

# final comp [champ_name, champ_slot, champ_items, champ_stars]


# Ashe ReRoll Comp
ashe_comp_strategy = "Slowroll6"

ashe_champs_with_items = ["Ashe", "Renekton", "Sejuani"]
best_ashe_items = ["LastWhisper", "RunaansHurricane", "GuinsoosRageblade"]
ashe_items_equipped = [False, False, False]
best_renekton_items = ["Bloodthirster", "WarmogsArmor", "Redemption"]
renekton_items_equipped = [False, False, False]
best_sejuani_items = ["Morellonomicon"]
sejuani_items_equipped = [False]
item_lists_ashe = [best_ashe_items, best_renekton_items, best_sejuani_items]
equipped_items_boolean_lists_ashe = [ashe_items_equipped, renekton_items_equipped, sejuani_items_equipped]

final_ashe_comp = ["Gangplank", 0, "None", 3, "Renekton", 1, best_renekton_items, 3, "Sejuani", 2, best_sejuani_items, 2, "Malphite", 3, "None", 3,
                        "Vi", 5, "None", 3, "LeeSin", 6, "None", 3,
                        "Ashe", 21, best_ashe_items, 3, "Vayne", 27, "None", 2]

ashe_comp_champs_on_board = {
                            "Gangplank": False,
                            "Renekton": False,
                            "Sejuani": False,
                            "Malphite": False,
                            "Vi": False,
                            "LeeSin": False,
                            "Ashe": False,
                            "Vayne": False
}
ashe_comp_champs_max_star_reached = {
                            "Gangplank": False,
                            "Renekton": False,
                            "Sejuani": False,
                            "Malphite": False,
                            "Vi": False,
                            "LeeSin": False,
                            "Ashe": False,
                            "Vayne": False
}
ashe_comp_stars = {
                            "Gangplank": 3,
                            "Renekton": 3,
                            "Sejuani": 2,
                            "Malphite": 3,
                            "Vi": 3,
                            "LeeSin": 3,
                            "Ashe": 3,
                            "Vayne": 2
}
ashe_comp_placement_on_board = {
                            "Gangplank": 0,
                            "Renekton": 1,
                            "Sejuani": 2,
                            "Malphite": 3,
                            "Vi": 5,
                            "LeeSin": 6,
                            "Ashe": 21,
                            "Vayne": 27
}

ashe_comp_champs = {"Gangplank", "Renekton", "Sejuani", "Malphite", "Vi", "LeeSin", "Ashe", "Vayne"}
ashe_comp_champs_list = ["Gangplank", "Renekton", "Sejuani", "Malphite", "Vi", "LeeSin", "Ashe", "Vayne"]
# different solution
ashe_comp_star_coords = [coordinates.skarner_star_coords, coordinates.sylas_star_coords, coordinates.vladimir_star_coords, coordinates.nidalee_star_coords, coordinates.varus_star_coords, coordinates.lux_star_coords, coordinates.lux_star_coords, coordinates.lux_star_coords]
ashe_comp_placement_on_board_list = [0, 1, 2, 3, 5, 6, 21, 27]

ashe_augments_ranked = ["Absolution", "AceHeart", "AdaptiveDefensives", "A.D.M.I.NHeart", "AegisHeart", "AFK", "AimAssist", 
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
"UrfsGrabBagII", "VerdantVeil", "Windfall", "Windfall+", "Windfall++", "WiseSpending", "WoodlandCharm", "ChanneledFerromancy"]

# Renekton and Yasuo ReRoll Comp
yasuo_comp_strategy = "Slowroll6"
yasuo_champs_with_items = ["Renekton", "Yasuo", "Sejuani"]
best_renekton_items = ["RapidFirecannon", "GuinsoosRageblade", "GiantSlayer"]
renekton_items_equipped = [False, False, False]
best_yasuo_items = ["JeweledGauntlet", "HandOfJustice", "ArchangelsStaff"]
yasuo_items_equipped = [False, False, False]
best_sejuani_items = ["Morellonomicon"]
sejuani_items_equipped = [False]
item_lists_yasuo = [best_renekton_items, best_yasuo_items, best_sejuani_items]
equipped_items_boolean_lists_yasuo = [renekton_items_equipped, yasuo_items_equipped, sejuani_items_equipped]

final_yasuo_comp = ["Blitzcrank", 0, "None", 3, "LeeSin", 2, "None", 3, "Sejuani", 3, best_sejuani_items, 2, "Malphite", 5, "None", 2,
                        "Renekton", 7, best_renekton_items, 3, "Yasuo", 8, best_yasuo_items, 3, "Gangplank", 10, "None", 3,
                        "Soraka", 21, "None", 2]

yasuo_comp_champs_on_board = {
                            "Blitzcrank": False,
                            "LeeSin": False,
                            "Sejuani": False,
                            "Malphite": False,
                            "Renekton": False,
                            "Yasuo": False,
                            "Gangplank": False,
                            "Soraka": False
}
yasuo_comp_champs_max_star_reached = {
                            "Blitzcrank": False,
                            "LeeSin": False,
                            "Sejuani": False,
                            "Malphite": False,
                            "Renekton": False,
                            "Yasuo": False,
                            "Gangplank": False,
                            "Soraka": False
}
yasuo_comp_stars = {
                            "Blitzcrank": 3,
                            "LeeSin": 3,
                            "Sejuani": 2,
                            "Malphite": 2,
                            "Renekton": 3,
                            "Yasuo": 3,
                            "Gangplank": 3,
                            "Soraka": 2
}
yasuo_comp_placement_on_board = {
                            "Blitzcrank": 0,
                            "LeeSin": 2,
                            "Sejuani": 3,
                            "Malphite": 5,
                            "Renekton": 7,
                            "Yasuo": 8,
                            "Gangplank": 10,
                            "Soraka": 21
}

yasuo_comp_champs = {"Blitzcrank", "LeeSin", "Sejuani", "Malphite", "Renekton", "Yasuo", "Gangplank", "Soraka"}
yasuo_comp_champs_list = ["Blitzcrank", "LeeSin", "Sejuani", "Malphite", "Renekton", "Yasuo", "Gangplank", "Soraka"]
# different solution
yasuo_comp_star_coords = [coordinates.skarner_star_coords, coordinates.sylas_star_coords, coordinates.vladimir_star_coords, coordinates.nidalee_star_coords, coordinates.varus_star_coords, coordinates.lux_star_coords, coordinates.lux_star_coords, coordinates.lux_star_coords]
yasuo_comp_placement_on_board_list = [0, 2, 3, 5, 7, 8, 10, 21]

yasuo_augments_ranked = ["Absolution", "AceHeart", "AdaptiveDefensives", "A.D.M.I.NHeart", "AegisHeart", "AFK", "AimAssist", 
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
"UrfsGrabBagII", "VerdantVeil", "Windfall", "Windfall+", "Windfall++", "WiseSpending", "WoodlandCharm", "ChanneledFerromancy"]

# Kayle Reroll comp
kayle_champs_with_items = ["Kayle", "Riven"]
best_kayle_items = ["GuinsoosRageblade", "GiantSlayer", "HandOfJustice"]
kayle_items_equipped = [False, False, False]
best_riven_items = ["SunfireCape", "BrambleVest", "DragonsClaw"]
riven_items_equipped = [False, False, False]
item_lists_kayle = [best_kayle_items, best_riven_items]
equipped_items_boolean_lists_kayle = [kayle_items_equipped, riven_items_equipped]

kayle_comp_champs_on_board = {
                            "LeeSin": False,
                            "Vi": False,
                            "Sejuani": False,
                            "Malphite": False,
                            "Riven": False,
                            "Gangplank": False,
                            "Kayle": False,
                            "Sona": False
}
kayle_comp_champs_max_star_reached = {
                            "LeeSin": False,
                            "Vi": False,
                            "Sejuani": False,
                            "Malphite": False,
                            "Riven": False,
                            "Gangplank": False,
                            "Kayle": False,
                            "Sona": False
}
kayle_comp_stars = {
                            "LeeSin": 3,
                            "Vi": 2,
                            "Sejuani": 2,
                            "Malphite": 3,
                            "Riven": 2,
                            "Gangplank": 3,
                            "Kayle": 3,
                            "Sona": 2
}
kayle_comp_placement_on_board = {
                            "LeeSin": 0,
                            "Vi": 1,
                            "Sejuani": 3,
                            "Malphite": 5,
                            "Riven": 8,
                            "Gangplank": 10,
                            "Kayle": 21,
                            "Sona": 22
}

kayle_comp_champs = {"LeeSin", "Vi", "Sejuani", "Malphite", "Riven", "Gangplank", "Kayle", "Sona"}
kayle_comp_champs_list = ["LeeSin", "Vi", "Sejuani", "Malphite", "Riven", "Gangplank", "Kayle", "Sona"]

kayle_comp_placement_on_board_list = [0, 1, 3, 5, 8, 10, 21, 22]

kayle_augments_ranked = ["Absolution", "AceHeart", "AdaptiveDefensives", "A.D.M.I.NHeart", "AegisHeart", "AFK", "AimAssist", 
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
"UrfsGrabBagII", "VerdantVeil", "Windfall", "Windfall+", "Windfall++", "WiseSpending", "WoodlandCharm", "ChanneledFerromancy"]

# Gangplank Duelist Supers Reroll comp
gangplank_champs_with_items = ["Gangplank", "LeeSin"]
best_gangplank_items = ["Bloodthirster", "JeweledGauntlet", "BlueBuff"]
gangplank_items_equipped = [False, False, False]
best_leesin_items = ["ZzRotPortal", "GargoyleStoneplate", "SunfireCape"]
leesin_items_equipped = [False, False, False]
item_lists_gangplank = [best_gangplank_items, best_leesin_items]
equipped_items_boolean_lists_gangplank = [gangplank_items_equipped, leesin_items_equipped]

gangplank_comp_champs_on_board = {
                            "LeeSin": False,
                            "Vi": False,
                            "Sejuani": False,
                            "Malphite": False,
                            "Riven": False,
                            "Gangplank": False,
                            "Kayle": False,
                            "Sona": False
}
gangplank_comp_champs_max_star_reached = {
                            "LeeSin": False,
                            "Vi": False,
                            "Sejuani": False,
                            "Malphite": False,
                            "Riven": False,
                            "Gangplank": False,
                            "Kayle": False,
                            "Sona": False
}
gangplank_comp_stars = {
                            "LeeSin": 3,
                            "Vi": 2,
                            "Sejuani": 2,
                            "Malphite": 3,
                            "Riven": 2,
                            "Gangplank": 3,
                            "Kayle": 3,
                            "Sona": 2
}
gangplank_comp_placement_on_board = {
                            "LeeSin": 0,
                            "Vi": 1,
                            "Sejuani": 3,
                            "Malphite": 5,
                            "Riven": 8,
                            "Gangplank": 10,
                            "Kayle": 21,
                            "Sona": 22
}

gangplank_comp_champs = {"LeeSin", "Vi", "Sejuani", "Malphite", "Riven", "Gangplank", "Kayle", "Sona"}
gangplank_comp_champs_list = ["LeeSin", "Vi", "Sejuani", "Malphite", "Riven", "Gangplank", "Kayle", "Sona"]

gangplank_comp_placement_on_board_list = [0, 1, 3, 5, 8, 10, 21, 22]

gangplank_augments_ranked = ["Absolution", "AceHeart", "AdaptiveDefensives", "A.D.M.I.NHeart", "AegisHeart", "AFK", "AimAssist", 
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
"UrfsGrabBagII", "VerdantVeil", "Windfall", "Windfall+", "Windfall++", "WiseSpending", "WoodlandCharm", "ChanneledFerromancy"]


# empty data structure
champs_with_items = []
item_lists = []
equipped_items_boolean_lists = []
comp_champs_on_board = {}
comp_champs_max_star_reached = {}
comp_stars = {}
comp_placement_on_board = {}
comp_champs = {}
comp_champs_list = []
augments_ranked = []
comp_placement_on_board_list = []


# dictionaries
champs_with_items_dict = {
    "Ashe": ashe_champs_with_items,
    "Kayle": kayle_champs_with_items,
    "Gangplank": gangplank_champs_with_items
}
item_lists_dict = {
    "Ashe": item_lists_ashe,
    "Kayle": item_lists_kayle,
    "Gangplank": item_lists_gangplank
}
equipped_items_boolean_lists_dict = {
    "Ashe": equipped_items_boolean_lists_ashe,
    "Kayle": equipped_items_boolean_lists_kayle,
    "Gangplank": equipped_items_boolean_lists_gangplank
}
comp_champs_on_board_dict = {
    "Ashe": ashe_comp_champs_on_board,
    "Kayle": kayle_comp_champs_on_board,
    "Gangplank": gangplank_comp_champs_on_board
}
comp_champs_max_star_reached_dict = {
    "Ashe": ashe_comp_champs_max_star_reached,
    "Kayle": kayle_comp_champs_max_star_reached,
    "Gangplank": gangplank_comp_champs_max_star_reached
}
comp_stars_dict = {
    "Ashe": ashe_comp_stars,
    "Kayle": kayle_comp_stars,
    "Gangplank": gangplank_comp_stars
}
comp_placement_on_board_dict = {
    "Ashe": ashe_comp_placement_on_board,
    "Kayle": kayle_comp_placement_on_board,
    "Gangplank": gangplank_comp_placement_on_board
}
comp_champs_dict = {
    "Ashe": ashe_comp_champs,
    "Kayle": kayle_comp_champs,
    "Gangplank": gangplank_comp_champs
}
comp_champs_list_dict = {
    "Ashe": ashe_comp_champs_list,
    "Kayle": kayle_comp_champs_list,
    "Gangplank": gangplank_comp_champs_list
}
comp_placement_on_board_list_dict = {
    "Ashe": ashe_comp_placement_on_board_list,
    "Kayle": kayle_comp_placement_on_board_list,
    "Gangplank": gangplank_comp_placement_on_board_list
}
augments_ranked_dict = {
    "Ashe": ashe_augments_ranked,
    "Kayle": kayle_augments_ranked,
    "Gangplank": gangplank_augments_ranked
}


# comps overview
#final_comps_list = [final_renekton_comp, final_kayle_comp]




def get_missing_augments(augments_ranked) -> list:
    missing_augments = []
    for augment in generalData.augments:
        if(not augments_ranked.__contains__(augment)):
            missing_augments.append(augment)
    if(len(missing_augments) == 0):
        print("all augments found")
    return missing_augments