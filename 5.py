import os
import re
import threading


def get_all_files(dir_path):
    dirs = [dir_path]
    while dirs:
        dir_path = dirs.pop()
        for filename in os.listdir(dir_path):
            path = os.path.join(dir_path, filename)
            if os.path.isdir(path):
                dirs.append(path)
            else:
                yield path


def task1():
    # в папке test найти все файлы filenames вывести колличество

    filename_to_count = "filename"
    start_dir = os.path.join(os.path.dirname(__file__), "test")

    counter = 0
    for filepath in get_all_files(start_dir):
        filename = os.path.basename(filepath)
        if filename.startswith(filename_to_count):
            counter += 1

    print(counter)
    return counter


def task2():
    # в папке test найти все email адреса записанные в файлы
    start_dir = os.path.join(os.path.dirname(__file__), "test")

    def get_mails(filepaths_list, mails):
        email_regex = re.compile(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+")
        for filepath in filepaths_list:
            with open(filepath) as f:
                d = f.read()
                finded_mails = re.findall(email_regex, d)
                if finded_mails:
                    mails.extend(finded_mails)

    files = list(get_all_files(start_dir))
    threads = []
    len_files = len(files)
    step = 30
    mails = []
    for r in range(0, len_files, step):
        thread = threading.Thread(target=get_mails, args=(files[r:r+step], mails, ))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    print(mails)
    return mails


def main():
    task1()
    task2()
    # дополнительно: придумать над механизм оптимизации 2-й задачи (используя threading)


if __name__ == '__main__':
    main()
