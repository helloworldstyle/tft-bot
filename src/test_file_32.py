import coordinates
import comps
import champions
import time
import functions
start = time.time()
champions.addChamp("Karma", (100, 100), 1, "SparringGlovese", comps.best_ezreal_items, 0, True, False)
functions.sell_first_champ_if_necessary()

end = time.time()
print(end - start)