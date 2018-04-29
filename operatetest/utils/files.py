import os

__all__ = ["path_join","make_dirs"]


def path_join(*args):
    return os.path.join(*args)


def make_dirs(path):
    os.makedirs(path,exist_ok=True)





if __name__ == '__main__':
    print(path_join(r"D:\dev\workspace\aototest","drivers"))