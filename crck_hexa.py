#!/usr/bin/python3
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pyperclip
from time import sleep
import sys
# Beta firefox --headless not working
#from selenium.webdriver.chrome.options import Options
# firefox_options=options
usage = '''Usage:
     Optional arguments:          
      -h 0 0 --help   Show the Help Message & Exit!
\33[31m--------------------------------------------------------------\33[00m'''

usage1 = '''Usage:
     {Automations}:
      * python3 crck_hexa.py -a -Hash_type Your_hash [-a Automation Hash] 
     {Hash_type}:
      * python3 crck_hexa.py -t -a -Your_hash [-t hash_type, -a Automations] 
     {Manual Cracking}:
      * python3 crck_hexa.py -m -0 -0 [-m manual_hashes_cracking, -0 none] 
           
     Optional arguments:          
      -h 0 0 --help   Show the Help Message & Exit!
            
     Hash_type:
      -m    --md5 
      -s1   --sha1 
      -s2   --sha256 
      -s3   --sha384 
      -s5   --sha512 
\33[31m--------------------------------------------------------------\33[00m'''

def banner():
    print('''\033[31m_________          \033[00m\033[35m       __         .__         \033[00m                  
\033[31m\_   ___ \_______   ____ |  | __ \033[00m\033[35m    |  |__   ____ ___  ________   \033[00m
\033[31m/    \  \/\_  __ \_/ ___\|  |/ / \033[00m\033[35m    |  |  \_/ __ \.\  \/  /\__  \  \033[00m
\033[31m\     \____|  | \/\  \___|    <  \033[00m\033[35m    |   Y  \  ___/ >    <  / __ \_\033[00m
 \033[31m\______  /|__|    \___  >__|_ \_\033[00m\033[35m____|___|  /\___  >__/\_ \(____  /\033[00m
\033[31m        \/             \/     \/__\033[00m\033[35m___/    \/     \/      \/     \/\033[00m''')
    
    sleep(0.5)
    print("                 _________-----_____")
    print("       _____------           __      ----_")
    print("___----             ___------              \.")
    print("   ----________        ----                 \.")
    print("               -----__    |             _____)")
    print("\033[31m                    __-                /  _   \.        {+}---- \033[33mCrck_Hexa\033[00m \033[31m----{+}\033[00m")
    print("\033[31m\033[31m        _______-----    ___--          \  @  /\.             {+}-- \033[33mv1.0\033[00m\033[31m --{+}\033[00m")
    print("\033[31m  ------_______      ---____            \__/  /   {+}-->\033[33m Coded By Predator0x300\033[00m\033[31m <--{+} \033[00m   ")
    print("\033[35m               -----__    \ --    _          /\.\033[00m")
    print("\033[35m                      --__--__     \_____/   \_/\.\033[00m")
    print("                              ----|   /          |")
    print("                                  |  |___________|")
    print("\033[33m                                  |  | ((_(_)| )_)   \033[00m")
    print("\033[33m                                  |  \_((_(_)|/(_)\033[00m")
    print("                                  \             (")
    print("                                   \_____________)")
    print('\33[31m--------------------------------------------------------------\33[00m')


banner()




try:
    if (len(sys.argv) ==4):
        automation1 = sys.argv[1]
        hash_type = sys.argv[2]
        type1 = sys.argv[1]
        auto1 = sys.argv[2]
        hash2 = sys.argv[3]

        if (automation1 == '-a' and hash_type == '-s1'):
            hash1 = str(sys.argv[3])
            #firefox_options.add_argument('--headless')
            class Crack():
                def __init__(self,hash1):
                    print('-'*30)
                    print('\033[31m{+} Cracking sha1 ['+hash1+ '] Hash Pls wait!\033[00m')

                    print('-'*30)
                    fireFoxOptions = webdriver.FirefoxOptions()
                    uxr_l = 's://tin'
                    fireFoxOptions.add_argument('-headless')
                    driver43u = 'http'
                    driver= webdriver.Firefox(executable_path ='/root/Desktop/crck_hexa/geckodriver',options=fireFoxOptions)
                    #driver.minimize_window()
                    cuto = 'yurl.com/y9457pkq'
                    url  = (driver43u+uxr_l+cuto)
                    driver.get(url)
                    print('\033[31m{+} Compiling Started! Pls Wait..../\033[00m')
                    sleep(0.1)

                    self.send = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/form/div/input')
                    print('\33[31m{+} Reading the given hash...................//\033[00m')
                    sleep(0.2)
                    self.send.send_keys(hash1)
                    self.submit = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/form/div/span[2]/button')
                    print('\033[33m{+} Encoding the words in pre-defined database...................//\33[00m')
                    sleep(0.2)
                    self.submit.click()
                    try:
                        self.copy = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div[1]/table/tbody/tr/td[3]/span[1]/a')
                        self.copy.click()
                        self.click1 = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div/table/tbody/tr[1]/td[3]/span[1]/a')

                        print('\033[33m{+} Applying decoding formats...................//\33[00m')
                        sleep(0.2)
                        cracked = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div/div/h1/code').text
                        print('\033[33m{+} Recieving the Cracked PWD...................//\33[00m')
                        sleep(0.2)

                        #self.cracked.send_keys(Keys.CONTROL+'a')
                        #self.cracked.send_keys(Keys.CONTROL+'c')
                    except:
                        print('\33[31m{-} Failed to Crack! {' +hash1+ '} :(\33[00m')
                        sleep(0.1)
                        print('\33[31m{-} No Crack Founded!!!:((\33[00m')
                        sleep(0.1)
                        print('\33[31m{-} Exiting......:(((\33[00m')
                        print('-'*30)
                        sleep(0.2)

                        exit()


                    #txt2 = pyperclip.paste()
                    print('\033[32m{+} Cracked hash is [\033[00m'+str(cracked)+'\033[32m]\33[00m')
                    driver.close()
            Crack(str(hash1))
        elif(automation1 == '-a' and hash_type == '-m'):
            hash1 = str(sys.argv[3])
            #firefox_options.add_argument('--headless')
            class Crack():
                def __init__(self,hash1):
                    print('-'*30)
                    print('\033[31m{+} Cracking md5 ['+hash1+ '] Hash Pls wait!\033[00m')

                    print('-'*30)
                    fireFoxOptions = webdriver.FirefoxOptions()
                    uxr_l = 's://tin'
                    fireFoxOptions.add_argument('-headless')
                    driver43u = 'http'
                    driver= webdriver.Firefox(executable_path ='/root/Desktop/crck_hexa/geckodriver',options=fireFoxOptions)
                    #driver.minimize_window()
                    cuto = 'yurl.com/n4vgxxl'
                    url  = (driver43u+uxr_l+cuto)
                    driver.get(url)
                    print('\033[31m{+} Compiling Started! Pls Wait..../\033[00m')
                    sleep(0.1)

                    self.send = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/form/div/input')
                    print('\33[31m{+} Reading the given hash...................//\033[00m')
                    sleep(0.2)
                    self.send.send_keys(hash1)
                    self.submit = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/form/div/span[2]/button')
                    print('\033[33m{+} Encoding the words in pre-defined database...................//\33[00m')
                    sleep(0.2)
                    self.submit.click()
                    try:
                        self.copy = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div[1]/table/tbody/tr/td[3]/span[1]/a')
                        self.copy.click()
                        self.click1 = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div/table/tbody/tr[1]/td[3]/span[1]/a')

                        print('\033[33m{+} Applying decoding formats...................//\33[00m')
                        sleep(0.2)
                        cracked = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div/div/h1/code').text
                        print('\033[33m{+} Recieving the Cracked PWD...................//\33[00m')
                        sleep(0.2)
                        #self.cracked.send_keys(Keys.CONTROL+'a')
                        #self.cracked.send_keys(Keys.CONTROL+'c')
                    except:
                        print('\33[31m{-} Failed to Crack! {' +hash1+ '} :(\33[00m')
                        sleep(0.1)
                        print('\33[31m{-} No Crack Founded!!!:((\33[00m')
                        sleep(0.1)
                        print('\33[31m{-} Exiting......:(((\33[00m')
                        print('-'*30)
                        sleep(0.2)

                        exit()


                    #txt2 = pyperclip.paste()

                    print('\033[32m{+} Cracked hash is [\033[00m'+str(cracked)+'\033[32m]\33[00m')
                    driver.close()
            Crack(str(hash1))
        elif(automation1  == '-a' and hash_type =='-s2' ):
            hash1 = str(sys.argv[3])
            #firefox_options.add_argument('--headless')
            class Crack():
                def __init__(self,hash1):
                    print('-'*30)
                    print('\033[31m{+} Cracking sha256 ['+hash1+ '] Hash Pls wait!\033[00m')

                    print('-'*30)
                    fireFoxOptions = webdriver.FirefoxOptions()

                    uxr_l = 's://tin'
                    fireFoxOptions.add_argument('-headless')
                    driver43u = 'http'
                    driver= webdriver.Firefox(executable_path ='/root/Desktop/crck_hexa/geckodriver',options=fireFoxOptions)
                    #driver.minimize_window()
                    cuto = 'yurl.com/y85svmmc'
                    url  = (driver43u+uxr_l+cuto)
                    driver.get(url)
                    print('\033[31m{+} Compiling Started! Pls Wait..../\033[00m')
                    sleep(0.1)

                    self.send = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/form/div/input')
                    print('\33[31m{+} Reading the given hash...................//\033[00m')
                    sleep(0.2)
                    self.send.send_keys(hash1)
                    self.submit = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/form/div/span[2]/button')
                    print('\033[33m{+} Encoding the words in pre-defined database...................//\33[00m')
                    sleep(0.2)
                    self.submit.click()
                    try:
                        self.copy = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div[1]/table/tbody/tr/td[3]/span[1]/a')
                        self.copy.click()
                        self.click1 = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div/table/tbody/tr[1]/td[3]/span[1]/a')

                        print('\033[33m{+} Applying decoding formats...................//\33[00m')
                        sleep(0.2)
                        cracked = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div/div/h1/code').text
                        print('\033[33m{+} Recieving the Cracked PWD...................//\33[00m')
                        sleep(0.2)
                        #self.cracked.send_keys(Keys.CONTROL+'a')
                        #self.cracked.send_keys(Keys.CONTROL+'c')
                    except:
                        print('\33[31m{-} Failed to Crack! {' +hash1+ '} :(\33[00m')
                        sleep(0.1)
                        print('\33[31m{-} No Crack Founded!!!:((\33[00m')
                        sleep(0.1)
                        print('\33[31m{-} Exiting......:(((\33[00m')
                        print('-'*30)
                        sleep(0.2)

                        exit()


                    #txt2 = pyperclip.paste()

                    print('\033[32m{+} Cracked hash is [\033[00m'+str(cracked)+'\033[32m]\33[00m')
                    driver.close()
            Crack(str(hash1))

        elif(automation1  == '-a' and hash_type =='-s3' ):
            hash1 = str(sys.argv[3])
            #firefox_options.add_argument('--headless')
            class Crack():
                def __init__(self,hash1):
                    print('-'*30)
                    print('\033[31m{+} Cracking sha384 ['+hash1+ '] Hash Pls wait!\033[00m')

                    print('-'*30)
                    fireFoxOptions = webdriver.FirefoxOptions()
                    uxr_l = 's://tin'
                    fireFoxOptions.add_argument('-headless')
                    driver43u = 'http'
                    driver= webdriver.Firefox(executable_path ='/root/Desktop/crck_hexa/geckodriver',options=fireFoxOptions)
                    driver.minimize_window()
                    cuto = 'yurl.com/ydf5jn5g'
                    url  = (driver43u+uxr_l+cuto)
                    driver.get(url)
                    print('\033[31m{+} Compiling Started! Pls Wait..../\033[00m')
                    sleep(0.1)

                    self.send = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/form/div/input')
                    print('\33[31m{+} Reading the given hash...................//\033[00m')
                    sleep(0.2)
                    self.send.send_keys(hash1)
                    self.submit = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/form/div/span[2]/button')
                    print('\033[33m{+} Encoding the words in pre-defined database...................//\33[00m')
                    sleep(0.2)
                    self.submit.click()
                    try:
                        self.copy = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div[1]/table/tbody/tr/td[3]/span[1]/a')
                        self.copy.click()
                        self.click1 = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div/table/tbody/tr[1]/td[3]/span[1]/a')

                        print('\033[33m{+} Applying decoding formats...................//\33[00m')
                        sleep(0.2)
                        cracked = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div/div/h1/code').text
                        print('\033[33m{+} Recieving the Cracked PWD...................//\33[00m')
                        sleep(0.2)
                        #self.cracked.send_keys(Keys.CONTROL+'a')
                        #self.cracked.send_keys(Keys.CONTROL+'c')
                    except:
                        print('\33[31m{-} Failed to Crack! {' +hash1+ '} :(\33[00m')
                        sleep(0.1)
                        print('\33[31m{-} No Crack Founded!!!:((\33[00m')
                        sleep(0.1)
                        print('\33[31m{-} Exiting......:(((\33[00m')
                        print('-'*30)
                        sleep(0.2)

                        exit()


                    #txt2 = pyperclip.paste()

                    print('\033[32m{+} Cracked hash is [\033[00m'+str(cracked)+'\033[32m]\33[00m')
                    driver.close()
            Crack(str(hash1))


        elif(automation1  == '-a' and hash_type =='-s5' ):
            hash1 = str(sys.argv[3])
            #firefox_options.add_argument('--headless')
            class Crack():
                def __init__(self,hash1):
                    print('-'*30)
                    print('\033[31m{+} Cracking sha512 ['+hash1+ '] Hash Pls wait!\033[00m')

                    print('-'*30)
                    fireFoxOptions = webdriver.FirefoxOptions()
                    uxr_l = 's://tin'
                    fireFoxOptions.add_argument('-headless')
                    driver43u = 'http'
                    driver= webdriver.Firefox(executable_path ='/root/Desktop/crck_hexa/geckodriver',options=fireFoxOptions)
                    #driver.minimize_window()
                    cuto = 'yurl.com/y7j4acby'
                    url  = (driver43u+uxr_l+cuto)
                    driver.get(url)
                    print('\033[31m{+} Compiling Started! Pls Wait..../\033[00m')
                    sleep(0.1)

                    self.send = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/form/div/input')
                    print('\33[31m{+} Reading the given hash...................//\033[00m')
                    sleep(0.2)
                    self.send.send_keys(hash1)
                    self.submit = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/form/div/span[2]/button')
                    print('\033[33m{+} Encoding the words in pre-defined database...................//\33[00m')
                    sleep(0.2)
                    self.submit.click()
                    try:
                        self.copy = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div[1]/table/tbody/tr/td[3]/span[1]/a')
                        self.copy.click()
                        self.click1 = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div/table/tbody/tr[1]/td[3]/span[1]/a')

                        print('\033[33m{+} Applying decoding formats...................//\33[00m')
                        sleep(0.2)
                        cracked = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div/div/h1/code').text
                        print('\033[33m{+} Recieving the Cracked PWD...................//\33[00m')
                        sleep(0.2)
                        #self.cracked.send_keys(Keys.CONTROL+'a')
                        #self.cracked.send_keys(Keys.CONTROL+'c')
                    except:
                        print('\33[31m{-} Failed to Crack! {' +hash1+ '} :(\33[00m')
                        sleep(0.1)
                        print('\33[31m{-} No Crack Founded!!!:((\33[00m')
                        sleep(0.1)
                        print('\33[31m{-} Exiting......:(((\33[00m')
                        print('-'*30)
                        sleep(0.2)

                        exit()


                    #txt2 = pyperclip.paste()

                    print('\033[32m{+} Cracked hash is [\033[00m'+str(cracked)+'\033[32m]\33[00m')
                    driver.close()
            Crack(str(hash1))

        elif (type1 == '-t' and auto1 == '-a'):
            class Type():
                def __init__(self, hash2):
                    print('-'*30)
                    print('\033[31m{+} Looking for ['+hash2+ '] Hash Pls wait!\033[00m')
                    print('-'*30)
                    fireFoxOptions = webdriver.FirefoxOptions()
                    fireFoxOptions.add_argument('-headless')
                    uxr_l = 's://tin'
                    driver = webdriver.Firefox(executable_path='/root/Desktop/crck_hexa/geckodriver',options =fireFoxOptions)
                    #driver.minimize_window()
                     #
                    driver43u = 'http'
                    cuto = 'yurl.com/ybrwhyno'
                    driver.get(driver43u+uxr_l+cuto)
                    self.box = driver.find_element_by_xpath('/html/body/div[1]/div/div/article/div/form/div/input')

                    print('\033[34m{+} Initializing the given hash..........//\33[00m')
                    sleep(0.1)
                    self.box.send_keys(hash2)


                    self.analyse = driver.find_element_by_xpath('/html/body/div[1]/div/div/article/div/form/div/button')
                    print('\033[34m{+} Matching the ['+hash2+'] in Database...........//\33[00m')
                    sleep(0.2)
                    self.analyse.click()
                    sleep(0.3)
                    type4 = driver.find_element_by_xpath(str('/html/body/div[1]/div/div/article/div/div[2]/div/div/table/tbody/tr[2]/td[2]')).text
                    print('\033[34m{+} Recieving the elements......//\33[00m')
                    sleep(0.3)
                    bit = driver.find_element_by_xpath(str('/html/body/div[1]/div/div/article/div/div[2]/div/div/table/tbody/tr[3]/td[2]')).text
                    print('\033[93m{+} Checking for the Bit_length..........//\33[00m')
                    sleep(0.2)
                    character = driver.find_element_by_xpath(str('/html/body/div[1]/div/div/article/div/div[2]/div/div/table/tbody/tr[4]/td[2]')).text
                    print('\033[93m{+} Checking for the the Character length..........//\33[00m')
                    sleep(0.3)
                    char = driver.find_element_by_xpath(str('/html/body/div[1]/div/div/article/div/div[2]/div/div/table/tbody/tr[5]/td[2]')).text
                    print('\033[93m{+} Checking for the Character_type\33[00m\n')
                    sleep(0.4)
                    print('\033[33m{+|+} Fetching the Details ;) ...........//\33[00m\n')
                    sleep(0.3)
                    print('\033[32m{+} Fetched Details: \33[00m')
                    sleep(0.01)
                    print('\33[31m{+} Hash: \33[00m'+hash2)
                    sleep(0.1)
                    print('\33[31m{+} Hash type: \33[00m'+type4)
                    sleep(0.1)
                    print('\33[31m{+} Bit length: \33[00m'+bit)
                    sleep(0.1)
                    print('\33[31m{+} Character length: \33[00m'+character)
                    sleep(0.1)
                    print('\33[31m{+} Character type: \33[00m'+char)
                    sleep(0.1)
                    if (type4 == 'unknown'):
                        print('\33[31m{-} Failed to Look-Up for {' +hash2+ '} :(\33[00m')
                        sleep(0.1)
                        print("\33[31m{-} Couldn't identify the given hash!!!:((\33[00m")
                        sleep(0.1)
                        print('\33[31m{-} Exiting......:(((\33[00m')
                        print('-'*30)
                        sleep(0.2)

                        exit()

                    print('\n')
                    print('\033[31m{-} Exiting..... ;)   \33[00m')
                    print('\n')
                    driver.close()

            Type(hash2)

        elif (type1 =='-m' and auto1 =='-0'):
            print('\033[33m{+} Select |1| of the Option:\033[00m')
            print('\33[31m--------------------------------------------------------------\33[00m')
            print('[\033[31m01\033[00m]\033[32m md5\033[00m')
            print('[\033[31m02\033[00m]\033[32m sha1\033[00m')
            print('[\033[31m03\033[00m]\033[32m sha256\033[00m')
            print('[\033[31m04\033[00m]\033[32m sha384\033[00m')
            print('[\033[31m05\033[00m]\033[32m sha512\033[00m')
            enter6 = input('\033[33m==> \033[00m')
            if (enter6 == '1'):

                import md5
                crck()
            elif (enter6 == '2'):
                import sha1
                crck1()
            elif (enter6 == '3'):
                import sha256
                crck2()
            elif(enter6 == '4'):
                import sha384
                crck4()
            elif(enter6 =='5'):
                import sha512
                crck5()


        # help = sys.argv[1]

        elif(automation1 == '-h'):

            print(usage1)
            exit()

        else:
            print(usage)
    sys.exit()
except:
    if (len(sys.argv) !=4):
        print(usage)










