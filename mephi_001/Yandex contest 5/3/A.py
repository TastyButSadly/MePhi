n = int(input())
song_count = {}

for _ in range(n):
    k = int(input())
    songs = input().split()
    for song in songs:
        if song in song_count:
            song_count[song] += 1
        else:
            song_count[song] = 1

common_songs = [song for song, count in song_count.items() if count == n]
common_songs.sort()

print(len(common_songs))
print(" ".join(common_songs))
