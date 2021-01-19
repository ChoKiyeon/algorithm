genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]


def get_melon_best_album(genre_array, play_array):
    # 구현해보세요!
    pop_songs_plays = list()
    classic_songs_plays = list()

    pop_plays = 0
    classic_plays = 0
    album = []

    for index in range(len(genre_array)):
        if genre_array[index] == "pop":
            pop_plays += play_array[index]
            pop_songs_plays.append([play_array[index], index])
        else:
            classic_plays += play_array[index]
            classic_songs_plays.append([play_array[index], index])

    pop_songs_plays.sort(reverse=True)
    classic_songs_plays.sort(reverse=True)

    if pop_plays > classic_plays:
        for _plays, index in pop_songs_plays:
            album.append(index)
            if len(album) == 2:
                break
        for _plays, index in classic_songs_plays:
            album.append(index)
            if len(album) == 4:
                break
    else:
        for _plays, index in classic_songs_plays:
            album.append(index)
            if len(album) == 2:
                break
        for _plays, index in pop_songs_plays:
            album.append(index)
            if len(album) == 4:
                break
    return album


print(get_melon_best_album(genres, plays))  # 결과로 [4, 1, 3, 0] 가 와야 합니다!