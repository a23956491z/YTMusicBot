from ytmusicapi import YTMusic

import inspect

ytmusic = YTMusic('../config/headers_auth.json')

class YTMusicWrapper:
    def __init__(self):
        pass
# search_results = ytmusic.search("百鬼祭 / 常闇トワ(cover)")
# print(len(search_results))
# print(search_results[0].keys())

# first_result_video_id = search_results[0]['videoId']

# radio_list_id = 'RDAMVM' + first_result_video_id
# print(radio_list_id)

# # playlist = ytmusic.search(radio_list_id, filter="playlists")
# # print(playlist)

# url = "https://www.youtube.com/watch?v={id}?list={prefix}{id}".format(id=first_result_video_id, prefix='RDAMVM')
# print(url)

plst = ytmusic.get_watch_playlist(first_result_video_id)['tracks']

# # playlist_test_id = 'RDAMPL'+'PLcirGkCPmbmFeQ1sm4wFciF03D_EroIfr'
# # plst = ytmusic.get_playlist(playlist_test_id)
# # plst = plst['tracks']
# for i in plst:
#     print(i['title'])
# # # print(inspect.getmembers(YTMusic, predicate=inspect.isfunction))

