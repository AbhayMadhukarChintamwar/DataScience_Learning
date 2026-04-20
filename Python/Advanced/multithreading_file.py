
from threading import Thread
from time import sleep,time

def download(file_name):
    print('Downloading file... ', file_name)
    sleep(0.5)
    print('Download complete: ')



if __name__ == '__main__':

    files = ['video.mp4', 'music.mp3', 'document.pdf']
    start = time()
    for f in files:
        download(f)
    end = time()
    print(f'Total time taken: {end - start:.2f} seconds')

    threads = []
    for f in files:
        t = Thread(target=download, args=(f,))
        threads.append(t)

        start = time()


    for t in threads:
        t.start()

    for t in threads:
        t.join()

    end = time()
    print(f'Total time taken with threads: {end - start:.2f} seconds')

    print('Bye')