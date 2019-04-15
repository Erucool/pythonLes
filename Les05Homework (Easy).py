# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os
import sys
import shutil

print(sys.argv)


def make_a_lot_of_dir():
    if not sys.argv[1]:
        print('Вы забыли передать первый параметр add_dirs')
        return
    for x in range(0, 9):
        dir_path = os.path.join(os.getcwd(), 'dir_{}'.format(1 + x))
        try:
            os.mkdir(dir_path)
            print('Директория {} создана!'.format(dir_path))
        except FileExistsError:
            print('Такая директория {} уже существует!'.format(dir_path))


def delete_generated_dirs():
    for x in range(0, 9):
        dir_path = os.path.join(os.getcwd(), 'dir_{}'.format(1 + x))
        try:
            os.rmdir(dir_path)
            print('Директория {} удалена!'.format(dir_path))
        except FileNotFoundError:
            print('Такой директории {} здесь не было!'.format(dir_path))




    if not sys.argv[1]:
        print('Вы забыли передать первый параметр add_dirs')
    if sys.argv[1] == 'add_dirs':
        make_a_lot_of_dir()
    elif sys.argv[1] == 'delete_dirs':
        delete_generated_dirs()
# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.
    elif sys.argv[1] == 'show_dirs':
        print(os.listdir(os.getcwd()))
# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
    elif sys.argv[1] == 'copy_file':
        current_file = os.path.join(os.getcwd(), sys.argv[0])
        new_file = os.path.join(os.getcwd(), sys.argv[0] + 'new')
        shutil.copyfile(current_file, new_file)
        print('Файл {} создан!'.format(sys.argv[0] + 'new'))
    else:
        pass
