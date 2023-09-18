import requests
import time
import threading


def timer(func):
    def inner(*args, **kwargs):
        start_time = time.time()  # get's the time
        func(*args, **kwargs)
        end_time = time.time()
        print(end_time - start_time)

    return inner


def URL_downloader(URL: str):
    x = requests.get(URL)
    print(x)
    return x


@timer
def main():
    URLs = [
        "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e2/Matzov-unit-insignia-2020.png/330px-Matzov-unit-insignia-2020.png",
        "https://ssl.gstatic.com/ui/v1/icons/mail/rfr/logo_gmail_lockup_default_1x_rtl.png",
        "https://github.githubassets.com/images/modules/open_graph/github-mark.png",
        "https://www.google.co.il/images/branding/googlelogo/2x/googlelogo_color_160x56dp.png",
    ]
    t1 = threading.Thread(target=URL_downloader, args=(URLs[0],))
    t2 = threading.Thread(target=URL_downloader, args=(URLs[1],))
    t4 = threading.Thread(target=URL_downloader, args=(URLs[2],))
    t3 = threading.Thread(target=URL_downloader, args=(URLs[3],))

    t1.start()
    t2.start()
    t3.start()
    t4.start()

    t1.join()
    t2.join()
    t3.join()
    t4.join()


if __name__ == "__main__":
    main()
