import sys
sys.path.append('./MapGenerator_')
sys.setrecursionlimit(10**6)

from track import Track

if __name__ == '__main__':
    track_obj = Track(16, 9)
    track_obj.print_track()
    track_obj.generate_track_from_seed(
        seed = '0-2-411411222223333444'
    )
    track_obj.print_track()
