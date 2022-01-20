import os
import time
import random

os.system("clear")

print(" #     #                           #####                                                   ###### ")
print(" ##   ##  ######   ####     ##    #     #  ######  #    #    ##        ######  #    #      #     #  #   #  #####  #    #   ####   #    # ")
print(" # # # #  #       #    #   #  #   #        #       ##   #   #  #       #       ##  ##      #     #   # #     #    #    #  #    #  ##   # ")
print(" #  #  #  #####   #       #    #   #####   #####   # #  #  #    #      #####   # ## #      ######     #      #    ######  #    #  # #  # ")
print(" #     #  #       #  ###  ######        #  #       #  # #  ######      #       #    #      #          #      #    #    #  #    #  #  # # ")
print(" #     #  #       #    #  #    #  #     #  #       #   ##  #    #      #       #    #      #          #      #    #    #  #    #  #   ## ")
print(" #     #  ######   ####   #    #   #####   ######  #    #  #    #      ######  #    #      #          #      #    #    #   ####   #    # ")

time.sleep(2)

print("\n\nPalpite para o próximo jogo ...\n")

print("Dezenas sorteadas: {}".format(random.randint(1,60)), end=' ')
time.sleep(1)
print(" - {}".format(random.randint(1,60)), end=' ')
time.sleep(1)
print(" - {}".format(random.randint(1,60)), end=' ')
time.sleep(1)
print(" - {}".format(random.randint(1,60)), end=' ')
time.sleep(1)
print(" - {}".format(random.randint(1,60)), end=' ')
time.sleep(1)
print(" - {}".format(random.randint(1,60)), end=' ')
print("\n\nBoa Sorte!\n")
