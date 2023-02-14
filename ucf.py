import requests
from requests.exceptions import ConnectionError
from bs4 import BeautifulSoup
import time
import sys

def end():
    print("----------------------------------------")
    print("Kindly check your downloads directory")
    print("All coupons are saved in coupons.txt")

def logo():
    print("__/\\\\\\\\\\\\\\\\\\\\\\\\\\____________         ")
    print(" _\////////////\\\_____________         ")
    print("  ___________/\\\/______________       ")
    print("   _________/\\\/________________      ")
    print("    _______/\\\/__________________     ")
    print("     _____/\\\/____________________    ")
    print("      ___/\\\/_______UDEMY_COUPON___   ")
    print("       __/\\\\\\\\\\\\\\\\\\\\\\\\\\\\\___FETCHER__  ")
    print("        _\///////////////__V1.0________ ")
    print("----------------------------------------")
    print("\tAuthor : SUS ")
    print("This tool is made for educational purpose!\n\tAny misuse of this tool \n     is not Author's responsiblity")
    print("----------------------------------------")

def nice_print(coupon_list, title_list):
    for (title, coupon) in zip(title_list, coupon_list):
        file.write(title + '\n' + coupon + '\n\n')

def get_coupons(go_links):
    coupons = []
    titles = []
    for coupon_link in go_links:
        res = requests.get(coupon_link)
        soup = BeautifulSoup(res.text, 'html.parser')
        coupon = soup.find('div', attrs={'class': 'ui segment'}).a['href']
        title = soup.find('h1', attrs={'class': 'ui grey header'}).getText()
        coupons.append(coupon)
        titles.append(title)
    return nice_print(coupons, titles)

def get_go_links(list_url):
    go_link = []
    for link in list_url:
        res = requests.get(link)
        soup = BeautifulSoup(res.text, 'html.parser')
        link_class = soup.find('div', attrs={'class': 'ui center aligned basic segment'}).a['href']
        go_link.append(link_class)
    return get_coupons(go_link)

def get_links(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    link_class = soup.select('.card-header')
    hn = []
    for idx, item in enumerate(link_class):
        href = link_class[idx].get('href')
        hn.append(href)
    return get_go_links(hn)

def process():
    try:
        logo()
        print('>> Enter 1 for 15 coupons or 2 for 30 coupons: ')
        try:
            if len(sys.argv) > 1:
                num = int(sys.argv[1])
            else:
                num = 1
            if num == 1:
                try:
                    get_links('https://www.discudemy.com/all')
                    end()
                except ConnectionError:
                    print('[!] Please check your network connection!')
            elif num == 2:
                try:
                    get_links('https://www.discudemy.com/all')
                    get_links('https://www.discudemy.com/all/2')
                    end()
                except ConnectionError:
                    print('[!] Please check your network connection!')
            else:
                print('[!] please enter a valid number')
        except ValueError:
            print('[!] Please enter a valid number!')
    except KeyboardInterrupt:
        print('[!] CTRL + C detected\n[!] Quitting...')

def main():
    t1 = time.time()
    process()
   
