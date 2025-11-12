def favorite_songs(playlist):

    sorted_playlist = sorted(playlist, key=lambda song: song["plays"], reverse=True)

    top_two_titles = [song["title"] for song in sorted_playlist[:2]]

    return top_two_titles

print(favorite_songs([{"title": "Sync or Swim", "plays": 3}, {"title": "Byte Me", "plays": 1}, {"title": "Earbud Blues", "plays": 2} ]))
print(favorite_songs([{"title": "Skip Track", "plays": 98}, {"title": "99 Downloads", "plays": 99}, {"title": "Clickwheel Love", "plays": 100} ]))
print(favorite_songs([{"title": "Song A", "plays": 42}, {"title": "Song B", "plays": 99}, {"title": "Song C", "plays": 75} ]))
