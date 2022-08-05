import os

def save_file(file, filename, path):
    fname = os.path.join(path, 'upload', filename)
    with open(fname, 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)

    return fname