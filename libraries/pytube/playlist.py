from pytube import Playlist

playlist= Playlist('https://www.youtube.com/watch?v=QM9PqfE86j8&list=PL_EueQXDyk8n1l3Enp3x3OuQolzkg22AW')

for vid in playlist.videos:
    print(vid.title)
