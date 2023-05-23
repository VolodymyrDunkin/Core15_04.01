import os
import pathlib


path = pathlib.Path(r'D:\testfolder')

print(path.is_file())

for i in path.iterdir():
    print(i.name)

for i in path.glob('**/*'):
    print(i)
    
path.joinpath('Video')
