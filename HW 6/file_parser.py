import sys
from pathlib import Path

PNG = []
MP3 = []
MP4 = []
MOV = []
DOCX = []
TXT = []
PDF = []
XLSX = []
OTHER = []
ARCHIVES = []

REGISTER_EXTENSIONS = {
    'PNG': PNG, 'MP3': MP3, 'MP4': MP4,
    'MOV': MOV, 'DOCX': DOCX, 'TXT': TXT,
    'PDF': PDF, 'XLSX': XLSX, 'ZIP': ARCHIVES,
}

FOLDERS = []
EXTENSIONS = set()
UNKNOWN = set()


def get_extension(filename: str):
    return Path(filename).suffix[1:].upper()


def scan(folder: Path):
    for item in folder.iterdir():
        if item.is_dir():
            if item.name not in ('archives', 'video', 'audio', 'documents', 'images', 'OTHER'):
                FOLDERS.append(item)
                scan(item)
            continue
        ext = get_extension(item.name)
        fullname = folder / item.name
        if not ext:
            OTHER.append(fullname)
        else:
            try:
                container = REGISTER_EXTENSIONS[ext]
                EXTENSIONS.add(ext)
                container.append(fullname)
            except KeyError:
                UNKNOWN.add(ext)
                OTHER.append(fullname)


if __name__ == '__main__':
    try:
        folder_for_scan = sys.argv[1]
        print(f'Start in folder {folder_for_scan}')
        scan(Path(folder_for_scan))
        print(f'Images png: {PNG}')
        print(f'Audio mp3: {MP3}')
        print(f'Video mp3: {MP4}')
        print(f'Video mov: {MOV}')
        print(f'Document docx: {DOCX}')
        print(f'Document txt: {TXT}')
        print(f'Document pdf: {PDF}')
        print(f'Document xlsx: {XLSX}')
        print(f'Archives: {ARCHIVES}')
        print(f'Types of files in folder: {EXTENSIONS}')
        print(f'Unknown files of types: {UNKNOWN}')
        print(FOLDERS[::-1])
    except IndexError:
        print('Any arguments?')