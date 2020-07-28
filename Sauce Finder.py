import random, os, requests
from bs4 import BeautifulSoup

def Generate_Code(): #function generates a random 6 digit number
    code = ''
    for i in range(6):
        code += str(random.randint(0,9))
    return code

def valid_url(): #function checks whether a doujin exists with the generates code
    valid = False

    while valid == False:
        url = 'https://nhentai.net/g/'+Generate_Code()+'/'
        r = requests.get(url)
        if r.status_code != 404:
            valid = True
    return url

generate = True

while generate == True: #get the tags from the page and ask user if they want to read a doujin with these tags
    data = requests.get(valid_url())
    soup = BeautifulSoup(data.text, 'html.parser')

    tags = soup.find_all('span', class_='name')
    tag = [i.text for i in tags]

    print('Tags : ', end = '')
    for i in tag:
        print(i+', ', end = '')
    print('\n\nType [y] if you want to read or [n] to generate another one (y/n)')
    response = input().lower()
    if response in ['y','n'] and response == 'y':
        generate = False
    elif response not in ['y','n']:
        while response not in ['y','n']:
            print('That is not an option please choose again')
            response = input().lower()
    else:
        os.system('cls')
        generate = True

print('\nchoose A, B or C depending on which browser you want to open in') #if they say yes open the url in the browser of their choice in private browsing mode
print('(A) Microsoft Edge\n(B) Google Chrome\n(C) FireFox')
browser = input().lower()
if browser not in ['a','b','c']:
    while browser not in ['a','b','c']:
        print('That is not an option please choose again')
        browser = input().lower()

if browser == 'a':
    os.system('start shell:AppsFolder\Microsoft.MicrosoftEdge_8wekyb3d8bbwe!MicrosoftEdge -private '+valid_url())
elif browser == 'b':
    os.system('start chrome --incognito '+'"'+valid_url()+'"')
else:
    os.system('start firefox.exe -private -url '+valid_url())
