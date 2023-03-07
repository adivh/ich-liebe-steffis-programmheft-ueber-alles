import pandas as pd
import glob as glob

from os.path import exists
import requests
import time

def load_excel_data(file):
    data = pd.read_excel(file)
    # f_list = glob.glob(file)

    # for f in f_list:
    #     d = pd.read_excel(f)
    #     data.append(d)

    return data

def save_to_out(url, name, sleep=1):

    if exists("out/{}.png".format(name)):
        print("out/{}.png already exists".format(name))
        return -1

    sleep_time = sleep
    retry_counter = 0
    
    time.sleep(sleep_time)
    r = requests.post("https://vhs.link", params={'url': url, 'keyword': '', 'secure': '5'})        

    while r.status_code != 200:

        sleep_time = min(sleep_time + 1, sleep + 1)
        retry_counter = retry_counter + 1

        print("Sending POST to https://vhs.link returned with status code {}. Retrying in {} seconds.".format(r.status_code, sleep_time))
        time.sleep(sleep_time)

        r = requests.post("https://vhs.link", params={'url': url, 'keyword': '', 'secure': '5'})

    qr_link = r.text[-252:-226]

    if qr_link[:-9] != 'https://vhs.link/' or qr_link[-3:] != '.qr':

        print("{} caused a problem: {}\n\n{}".format(url, qr_link, r.text))
        exit()

    print("{} ({}) ({})".format(qr_link, url, r.status_code))

    i = requests.get(qr_link)

    while i.status_code != 200:

        sleep_time = min(sleep_time + 1, sleep + 1)

        print("Sending GET to {} returned with status code {}. Retrying in {} seconds.".format(qr_link, r.status_code, sleep_time))
        time.sleep(sleep_time)

        i = requests.get(qr_link)

    file_name = "out/{}.png".format(name)
    with open(file_name, "wb") as f:
        f.write(i.content)
        print("{} saved in out/".format(file_name))

    return retry_counter


if __name__ == "__main__":
    print("ran file_loader directly")