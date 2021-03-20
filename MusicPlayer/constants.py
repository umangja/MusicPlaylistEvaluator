from users.models import TIMELIMIT

TIME_LIMIT = int(TIMELIMIT.objects.all()[0].timeLimit)




INFORMATION_ABOVE_SONG_LIST = []

INFORMATION_ABOVE_SONG_LIST_ITEM1 = "Please Rate how much random you find playlist not how much you liked it."
INFORMATION_ABOVE_SONG_LIST.append(INFORMATION_ABOVE_SONG_LIST_ITEM1)


INFORMATION_ABOVE_SONG_LIST_ITEM2 = "Only first " + str(TIME_LIMIT) + " seconds of songs will be played."
INFORMATION_ABOVE_SONG_LIST.append(INFORMATION_ABOVE_SONG_LIST_ITEM2)

INFORMATION_ABOVE_SONG_LIST_ITEM3 = "Songs onces played can not be paused."
INFORMATION_ABOVE_SONG_LIST.append(INFORMATION_ABOVE_SONG_LIST_ITEM3)

#Can add more items



#Keep this as LAST ITEM
INFORMATION_ABOVE_SONG_LIST_ITEM_LAST = "Please Rate between 1 to 5 with "
INFORMATION_ABOVE_SONG_LIST.append(INFORMATION_ABOVE_SONG_LIST_ITEM_LAST)



RATINGS_MEANING = []

# RATING1_MEANING = "1 being something like S1 S1 S2 S2 S3 S3 S4 S4 (because it doesn't look random to human)"
RATING1_MEANING = "Not Random"

RATINGS_MEANING.append(RATING1_MEANING)

RATING2_MEANING = "Very Little Randomness"
RATINGS_MEANING.append(RATING2_MEANING)

RATING3_MEANING = "Somewhat Random"
RATINGS_MEANING.append(RATING3_MEANING)

RATING4_MEANING = "Almost Random"
RATINGS_MEANING.append(RATING4_MEANING)

RATING5_MEANING = "Random"
RATINGS_MEANING.append(RATING5_MEANING)




APP_DESCRIPTION = "WebApp to evaluate Music Playlist Pseudo-Random Shuffling Algorithms. Main Aim for our project is to form random Shuffling Algorithms that appears random to human."
DEVELOPERS   = "This App is developed by ,<a href=\"https://umangja.github.io\">Umang Jain</a> And Anuraj Singh, Computer Science Students of IIT (BHU) Varansi as a needed tool for their BTP project under Dr. Anil Kumar Singh sir And Miss Naina Mam"

