import os
import time
import sys

directory = ""  # OBS Recording path
match_directory = ""  # Where we want to store recorded matches
current_match = 0


def check_and_copy_obs_video(argument=""):
    for path in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, path)):
            new_directory = f"{match_directory}\\match_{current_match}"
            os.mkdir(new_directory)
            os.rename(os.path.join(directory, path), os.path.join(new_directory, path))


def get_current_league_match():
    pass


if __name__ == '__main__':
    time.sleep(5)  # Give OBS time to save the file
    check_and_copy_obs_video(sys.argv[1])

