import random, os, requests

def Generate_Code():
    code = ''
    for i in range(6):
        code += str(random.randint(0,9))
    return code

def valid_url():
    valid = False

    while valid == False:
        url = 'https://nhentai.net/g/'+Generate_Code()+'/'
        r = requests.get(url)
        if r.status_code != 404:
            valid = True
    return url

print('choose A, B or C depending on which browser you want to open in')
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
