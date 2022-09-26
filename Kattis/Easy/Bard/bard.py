nb_villager = input()
nb_evenings = int(input())
bard_appeared = False

def parse_input(nb_evenings):
    evenings = list()
    for evening in range(nb_evenings):
        evening = input()
        evenings.append(evening)
    for i in range(len(evenings)):
        evenings[i] = str(evenings[i]).split(" ")
        for x in range(len(evenings[i])):
            evenings[i][x] = int(evenings[i][x])
    evenings_parsed = list()
    for evening in evenings:
        villagers_present = list()
        for i in range(len(evening)):
            if i == 0:
                nb_present = evening[i]
            else:
                villagers_present.append(evening[i])
        evenings_parsed.append((nb_present, villagers_present))
    return evenings_parsed

evenings_parsed = parse_input(nb_evenings)
nb_of_song = 0
villagers_and_known_songs = dict()

for i in range(nb_evenings):
    villagers_on_night = evenings_parsed[i][1]
    if 1 in villagers_on_night:
        nb_of_song += 1
        for villager in villagers_on_night:
            if villager not in villagers_and_known_songs.keys():
                villagers_and_known_songs[villager] = list()
                villagers_and_known_songs[villager].append(nb_of_song)
            else: 
                villagers_and_known_songs[villager].append(nb_of_song)
        bard_appeared = True
    elif bard_appeared:
        shared_knowledge = list()
        for villager in villagers_and_known_songs:
            for song in villagers_and_known_songs.get(villager):
                if song not in shared_knowledge:
                    shared_knowledge.append(song)
        for villager in villagers_on_night:
            if villager not in villagers_and_known_songs.keys():
                villagers_and_known_songs[villager] = list()
                for song in shared_knowledge:
                    villagers_and_known_songs[villager].append(song)
            else: 
                for song in shared_knowledge:
                    if song not in villagers_and_known_songs.get(villager):
                        villagers_and_known_songs[villager].append(nb_of_song)
                        
villagers = list()
for villager in villagers_and_known_songs:
    if len(villagers_and_known_songs.get(villager)) == nb_of_song:
        villagers.append(villager)

villagers.sort()        
for villager in villagers:
    print(villager)