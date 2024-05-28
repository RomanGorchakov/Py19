import pathlib
import collections
from datetime import datetime

def tree(directory):
    print(f'+ {directory}')
    for path in sorted(directory.rglob('*')):
        depth = len(path.relative_to(directory).parts)
        spacer = ' ' * depth
        print(f'{spacer}+ {path.name}')

def unique_path(directory, name_pattern):
    counter = 0
    while True:
        counter += 1
        path = directory/name_pattern.format(counter)
        if not path.exists():
            return path

if __name__ == '__main__':
    path = pathlib.Path.cwd()
    tree = tree(pathlib.Path.cwd())

    with open(path, mode='r') as fid:
        headers = [line.strip() for line in fid if line.startswith('#')]
    print('\n'.join(headers))

    if not destination.exists():
        source.replace(destination)
    with destination.open(mode='xb') as fid:
        fid.write(source.read_bytes())

    print(collections.Counter(p.suffix for p in pathlib.Path.cwd().iterdir()))
    time, file_path = max((f.stat().st_mtime, f) for f in directory.iterdir())
    print(datetime.fromtimestamp(time), file_path)
    max((f.stat().st_mtime, f) for f in directory.iterdir()).read_text()
    path0 = unique_path(pathlib.Path.cwd(), 'test{:03d}.txt')
    print(path0)