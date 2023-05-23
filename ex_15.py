import sys



try:
    path = sys.argv[1]
    print(path)
except IndexError as e:
    print(f"Take path to folder as param. {e}")