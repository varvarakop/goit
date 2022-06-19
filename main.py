from pathlib import Path
import shutil
import sys
import file_parser as parser
from normalize import normalize


def handle_media(filename: Path, target_folder: Path):
    target_folder.mkdir(exist_ok=True, parents=True)
    filename.replace(target_folder / (normalize(filename.stem) + filename.suffix))


def handle_documents(filename: Path, target_folder: Path):
    target_folder.mkdir(exist_ok=True, parents=True)
    filename.replace(target_folder / (normalize(filename.stem) + filename.suffix))


def handle_other(filename: Path, target_folder: Path):
    target_folder.mkdir(exist_ok=True, parents=True)
    filename.replace(target_folder / (normalize(filename.stem) + filename.suffix))


def handle_archive(filename: Path, target_folder: Path):
    target_folder.mkdir(exist_ok=True, parents=True)
    folder_for_file = target_folder / \
                      normalize(filename.name.replace(filename.suffix, ''))
    folder_for_file.mkdir(exist_ok=True, parents=True)
    try:
        shutil.unpack_archive(str(filename.resolve()),
                              str(folder_for_file.resolve()))
    except shutil.ReadError:
        print(f'Not an archive {filename}!')
        folder_for_file.rmdir()
        return None
    filename.unlink()


def handle_folder(folder: Path):
    try:
        folder.rmdir()
    except OSError:
        print(f'Can not delete the folder {folder}')


def main(folder: Path):
    parser.scan(folder)
    for file in parser.PNG:
        handle_media(file, folder / 'images' / 'PNG')
    for file in parser.MP3:
        handle_media(file, folder / 'audio' / 'MP3')
    for file in parser.MP4:
        handle_media(file, folder / 'video' / 'MP4')
    for file in parser.MOV:
        handle_media(file, folder / 'video' / 'MOV')
    for file in parser.DOCX:
        handle_documents(file, folder / 'documents' / 'DOCX')
    for file in parser.TXT:
        handle_documents(file, folder / 'documents' / 'TXT')
    for file in parser.PDF:
        handle_documents(file, folder / 'documents' / 'PDF')
    for file in parser.XLSX:
        handle_documents(file, folder / 'documents' / 'XLSX')
    for file in parser.OTHER:
        handle_other(file, folder / 'Others')
    for file in parser.ARCHIVES:
        handle_archive(file, folder / 'archives')
    for folder in parser.FOLDERS[::-1]:
        handle_folder(folder)

    print('\n\tWell DONE!\n')


if __name__ == '__main__':
    try:
        if sys.argv[1]:
            folder_scanning = Path(sys.argv[1])
            print(f'Start in folder {folder_scanning.resolve()}')
            main(folder_scanning.resolve())
    except IndexError:
        print('\nEnter Folder for scan!\n')