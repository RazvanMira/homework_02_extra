sound_level = float(input("Introduce the decibel level of the sound.\n"))
if sound_level < 40:
    print("The sound level is lower than a quiet room.")
elif sound_level == 40:
    print("The sound level is that of a quiet room.")
elif sound_level > 40 and sound_level < 70:
    print("The sound level is between that of a quiet room and an alarm clock.")
elif sound_level == 70:
    print("The sound level is that of an alarm clock.")
elif sound_level > 70 and sound_level < 103:
    print("The sound level is between that of an alarm clock and a gas lawnmower.")
elif sound_level == 103:
    print("The sound level is that of a gas lawnmower.")
elif sound_level > 103 and sound_level < 130:
    print("The sound level is between that of a gas lawnmower and a jackhammer.")
elif sound_level == 130:
    print("The sound level is that of a jackhammer.")
elif sound_level > 130:
    print("The sound level is above that of a jackhammer.")