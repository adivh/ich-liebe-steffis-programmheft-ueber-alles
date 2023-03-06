import requests
import time

def save_to_out(url, name):

    sleep_time = 1

    r = requests.post("https://vhs.link", params={'url': url, 'keyword': '', 'secure': '5'})

    while r.status_code != 200:
        print("Sending POST to https://vhs.link returned with status code {}. Retrying in {} seconds.".format(r.status_code, sleep_time))
        time.sleep(sleep_time)
        sleep_time = sleep_time * 2
        r = requests.post("https://vhs.link", params={'url': url, 'keyword': '', 'secure': '5'})

    qr_link = r.text[-252:-226]
    if qr_link[:-9] != 'https://vhs.link/' or qr_link[-3:] != '.qr':
        print("{} caused a problem: {}\n\n{}".format(url, qr_link, r.text))
        exit()

    print("{} ({}) ({})".format(qr_link, url, r.status_code))

    i = requests.get(qr_link)

    while i.status_code != 200:
        print("Sending GET to {} returned with status code {}. Retrying in {} seconds.".format(qr_link, r.status_code, sleep_time))
        time.sleep(sleep_time)
        sleep_time = sleep_time * 2
        i = requests.get(qr_link)

    file_name = "out/{}.png".format(name)
    with open(file_name, "wb") as f:
        f.write(i.content)
        print("{} saved in out/".format(file_name))


if __name__ == "__main__":
    print("ran file_loader directly")