def scan_folders() :
    #scan folders for music

    #import
    import os

    #bool for pathloop and initial path0
    pathloop = True
    global path0
    path0 = ""

    #pathloop
    while pathloop == True :
        #find path
        print("\nWich folder do you want to open?")
        if path0 == "" :
            path0 = path0 + input()
            print(path0)
        else :
            path0 = path0 + "\\" + input()
            print(path0)

        #scan path0
        obj0 = os.scandir(path0)

        #list for all songs
        global songs
        songs = []

        #print files from path0
        print("\nSound files in '% s':" % path0)
        for entry in obj0 :
            if entry.is_dir() or entry.is_file() and not (".flac" in entry.name or ".mp3" in entry.name or ".wav" in entry.name):
                print(entry.name)


            elif entry.is_file() and (".flac" in entry.name or ".mp3" in entry.name or ".wav" in entry.name):
                pathloop = False
                print(entry.name)

                #add songs to list
                songs.append(entry.name)
def play_music() :
    #play selected file

    #imports
    import vlc
    import time

    #user chooses song
    print("\nWhat song number do you want to play?")
    wich_song = int(input())
    wich_song = wich_song - 1
    song = (path0 + "\\" + songs[wich_song])

    #print playing(song)
    print(f"\nPlaying:\t{songs[wich_song]}\n (Stop the program to stop the song)")

    #play song
    player = vlc.MediaPlayer(song)
    player.play()
    time.sleep(1)
    duration = player.get_length()
    time.sleep(duration/1000)  # duration is in milliseconds

scan_folders()
play_music()
