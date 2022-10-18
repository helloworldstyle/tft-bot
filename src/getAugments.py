import keyboardFunctions
import ocrFunctions
import time
import os
import cv2 as cv

# get augements ranked after pick or win rate for certain comps via tactics.tools

#top left augment coords in mid pixel [649, 348]
coordinates = [649, 331+17, 649+225, 331+17, 649+2*225, 331+17]
file_location = 'C:/Users/tobia/Documents/Tobias/tft_cheater_current_version/src/augmentsRankedAstral.txt'

def moveFromSilverToPrismatic():
    time.sleep(5)
    runsAmount = 3
    iterations = [13, 12, 13]
    lengthTopBottom = 2 * 17 + 14
    lengthLeftRight = 225
    counter = 0
    file_name = os.path.join(os.path.dirname(__file__), file_location)
    with open(file_name, "w") as fw:
        for runs in range(runsAmount):
            if(runs == 1):
                keyboardFunctions.move_things((1308, 313), (1310, 573))
            if(runs == 2):
                keyboardFunctions.move_things((1308, 560), (1311, 800))

            for iter in range(iterations[runs]):
                coord1 = 649
                coord2 = 348 + iter * lengthTopBottom
                for i in range(3):
                    keyboardFunctions.move_mouse_to((coord1 + i * lengthLeftRight, coord2))
                    time.sleep(2)

                    keyboardFunctions.move_mouse_to((coord1 + i * lengthLeftRight, 400 + iter * lengthTopBottom))
                    keyboardFunctions.left_click((coord1 + i * lengthLeftRight, 400 + iter * lengthTopBottom))
                    keyboardFunctions.left_click((coord1 + i * lengthLeftRight, 400 + iter * lengthTopBottom))
                    keyboardFunctions.left_click((coord1 + i * lengthLeftRight, 400 + iter * lengthTopBottom))
                    keyboardFunctions.copy()
                    keyboardFunctions.switch_windows()
                    keyboardFunctions.paste()
                    keyboardFunctions.switch_windows()
                    
                    # # get augment name with ocr
                    # # screenshot = ocrFunctions.screenshot()
                    # # screenshot.save('pictures/screen.png')
                    # # screenshot = cv.imread('pictures/screen.png')
                    # coord00 = 385 + iter * lengthTopBottom
                    # coord01 = 419 + iter * lengthTopBottom
                    # coord10 = 465 + i * lengthLeftRight
                    # coord11 = 790 + i * lengthLeftRight
                    # #screeny = screenshot[coord00:coord01, 0:1920]

                    # coords = ((coord10, coord00), (coord11, coord01))
                    # augment_name = ocrFunctions.get_text_ImageGrab_champ_names(coords, 3)
                    # print(augment_name)

                    # # write augment name in txt file

                    # if(augment_name in augmentsList):
                    #     counter += 1
                    #     fw.write("")
                    #     fw.write(augment_name)
                    #     fw.write("")
                    #     fw.write(", ")
                    #     if(counter % 6 == 0):
                    #         fw.write("\n")

                    # else:
                    #     for l in range(len(augmentsList)):
                    #         if(augment_name.__contains__(augmentsList[l])):
                    #             counter += 1
                    #             fw.write("")
                    #             fw.write(augmentsList[l])
                    #             fw.write("")
                    #             fw.write(", ")
                    #             if(counter % 6 == 0):
                    #                 fw.write("\n")
                    #             break

    


augmentsList = ["PortableForge", "CelestialBlessingII", "MageCrown", "UrfsGrabBagI", "ThrilloftheHuntII", "MageCrest", "JeweledLotus", 
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
"SoulSiphon", "Knife's Edge I", "AFK", "LivingForge", "Part-TimeAssassin", "PreparationI", "PreparationIII", "Dragonmancer Conference", "Loot Master", "Personal Training", "Preparation II", "The Golden Egg"]

moveFromSilverToPrismatic()
