def crck():
    print('\033[01m-\033[00m'*92)
    print('\033[31m                        {+} ---   | Welcome To Manual Hash Cracking for md5!! |   --- {+}\033[00m')
    print('\033[01m-\033[00m'*92)
    print('''\033[33m                                  .___.\033[00m
    \033[33m          /)               ,-^     ^-. \033[00m
    \033[33m         //               /           \.\033[00m
    \033[33m.-------| |--------------/  __     __  \-------------------.__\033[00m
    \033[33m|WMWMWMW| |>>>>>>>>>>>>> | />>\   />>\ |>>>>>>>>>>>>>>>>>>>>>>:>\033[00m
    \033[31m`-------| |--------------| \_@/   \_@/ |\033[00m
    \033[33m         \.\              \    /|\    /\033[00m\033[31m--->> Select |1| Option:\033[00m
    \033[33m          \)               \   \_/   /\033[00m  [\033[93m01\033[00m]\033[32m Auto Manual Cracking Level-1 (short pre-defined lst)\033[00m
    \033[33m                            |       |\033[00m   [\033[93m02\033[00m]\033[32m Auto Manual Cracking Level-2 (Long lst = more tym!)\033[00m
                                |\033[31m+H+H+H+\033[00m|   [\033[93m03\033[00m]\033[32m Advance Manual Cracking! (with thread control)\033[00m   
    \033[33m                            \       / \033[00m''')
    option5 = input('\033[33m                                 ^-----^ => Enter Here: \033[00m')
    def cracker():
        print('\033[01m-\033[00m'*92)
        print('\033[31m                        {+} ---   | Welcome To Auto Manual Cracking Level-1  |   --- {+}\033[00m')
        import hashlib  # for encoding digesting the hashes
        import time
        flag = 0 # check_point 1
        hash = str(input('\033[33m{+} Enter the hash to decrypt:\n==>\033[00m'))
        wordlst = ('short_pass.txt') # short
        try:
            start_time = time.time()
            print('\033[35m{+} Opening the Pre-defined_Wordlst..................//\033[00m')
            time.sleep(0.5)
            pass_file = open(wordlst, 'r') # reading the file
            time.sleep(0.5)
            print('\033[35m{+} Analysing the  Pre-defined_Wordlst........................//\033[00m')

        except:
            print('\033[31m{-} No Pre-defined File founded!\033[00m')
            exit()


        for word in pass_file:
            encode = word.encode('utf-8')  # encoding the words in normal word list
            digest = hashlib.md5(encode.strip()).hexdigest() # digesting the hash (md5)
            print('\033[31m{+} Decoded txt is [\033[00m'+str(encode)+'\033[31m]\033[00m')

            time.sleep(0.01)
            print('\033[33m{+} After Converting the Decoded txt, Encoded Hash is [\033[00m' +str(digest)+'\033[33m]\033[00m')
            time.sleep(0.01)
            print('\033[93m{-} Hash [\033[00m'+str(hash)+'\033[93m] Not cracked!\033[00m\n')
            if (digest == hash):
                end_time = time.time()
                total_time = end_time-start_time
                print('{+} Craked Time:')
                print(float(total_time))
                print('\033[33m{+} Hash [\033[00m'+str(hash)+'\033[33m]cracked!\033[00m\n')
                print('\033[33m{+} Pwd Founded!! ;)\033[00m')
                time.sleep(0.8)
                print('\033[33m{+} Cracked PWD is [\033[00m'+str(word)+'\033[33m]\033[00m')
                flag = 1 # check_point 2
                break
        if (flag ==  0):
            print('\033[31m{-} Failed to Crack [\033[00m'+str(hash)+'\033[31m] :((\033[00m')
            time.sleep(0.001)
            print('\033[31m{-} Exiting.........\033[00m')



    def cracker2():
         print('\033[01m-\033[00m'*92)
         print('\033[31m                        {+} ---   | Welcome To Auto Manual Cracking Level-2  |   --- {+}\033[00m')
         import hashlib  # for encoding digesting the hashes
         import time
         flag = 0 # check_point 1
         hash = str(input('\033[33m{+} Enter the hash to decrypt:\n==>\033[00m'))
         wordlst = ('large_pass.txt') # short
         try:
             start_time = time.time()
             print('\033[31mNote: This Cracking Might take more than previous 1\033[00m')
             print('\033[35m{+} Opening the Pre-defined_Long_Wordlst..................//\033[00m')
             time.sleep(0.3)
             pass_file = open(wordlst, 'r') # reading the file
             time.sleep(0.5)
             print('\033[35m{+} Analysing the  Pre-defined_Wordlst........................//\033[00m')
         except:
             print('\033[31m{-} No Pre-defined File founded!\033[00m')
             exit()

         for word in pass_file:
             encode = word.encode('utf-8')  # encoding the words in normal word list
             digest = hashlib.md5(encode.strip()).hexdigest() # digesting the hash (md5)
             print('\033[31m{+} Decoded txt is [\033[00m'+str(encode)+'\033[31m]\033[00m')

             time.sleep(0.04)
             print('\033[33m{+} After Converting the Decoded txt, Encoded Hash is [\033[00m' +str(digest)+'\033[33m]\033[00m')
             time.sleep(0.05)
             print('\033[93m{-} Hash [\033[00m'+str(hash)+'\033[93m] Not cracked!\033[00m\n')
             if (digest == hash):
                 end_time = time.time()
                 total_time = end_time-start_time
                 print('{+} Craked Time:')
                 print(float(total_time))
                 print('\033[33m{+} Hash [\033[00m'+str(hash)+'\033[33m]cracked!\033[00m\n')
                 print('\033[33m{+} Pwd Founded!! ;)\033[00m')
                 time.sleep(0.9)
                 print('\033[33m{+} Cracked PWD is [\033[00m'+str(word)+'\033[33m]\033[00m')
                 flag = 1 # check_point 2
                 break

         if (flag ==  0):
             print('\033[31m{-} Failed to Crack [\033[00m'+str(hash)+'\033[31m] :((\033[00m')
             time.sleep(0.001)
             print('\033[31m{-} Exiting.........\033[00m')

    def manual():
         print('\033[01m-\033[00m'*92)
         print('\033[31m                        {+} ---   | Welcome To Advance Manual Cracking!  |   --- {+}\033[00m')
         import hashlib  # for encoding digesting the hashes
         import time
         flag = 0 # check_point 1
         hash = str(input('\033[33m{+} Enter the hash to decrypt:\n==>\033[00m'))
         wordlst = input('Enter the lst: ') # short
         take = float(input('Enter the thread Speed (recomm 0.001): '))
         try:
             start_time = time.time()
             print('\033[31mNote: This is manual Cracking thus, depends on your Custom lst!\033[00m')
             print('\033[35m{+} Opening the Pre-defined_Long_Wordlst..................//\033[00m')
             time.sleep(take)
             pass_file = open(wordlst, 'r') # reading the file
             time.sleep(take)
             print('\033[35m{+} Analysing the  Pre-defined_Wordlst........................//\033[00m')

         except:
              print('\033[31m{-} No Pre-defined File founded!\033[00m')
              exit()

         for word in pass_file:
             encode = word.encode('utf-8')  # encoding the words in normal word list
             digest = hashlib.md5(encode.strip()).hexdigest() # digesting the hash (md5)
             print('\033[31m{+} Decoded txt is [\033[00m'+str(encode)+'\033[31m]\033[00m')

             time.sleep(take)
             print('\033[33m{+} After Converting the Decoded txt, Encoded Hash is [\033[00m' +str(digest)+'\033[33m]\033[00m')
             time.sleep(take)
             print('\033[93m{-} Hash [\033[00m'+str(hash)+'\033[93m] Not cracked!\033[00m\n')
             if (digest == hash):
                 end_time = time.time()
                 total_time = end_time-start_time
                 print('{+} Craked Time:')
                 print(float(total_time))
                 print('\033[33m{+} Hash [\033[00m'+str(hash)+'\033[33m]cracked!\033[00m\n')
                 print('\033[33m{+} Pwd Founded!! ;)\033[00m')
                 time.sleep(0.9)
                 print('\033[33m{+} Cracked PWD is [\033[00m'+str(word)+'\033[33m]\033[00m')
                 flag = 1 # check_point 2
                 break


         if (flag ==  0):
             print('\033[31m{-} Failed to Crack [\033[00m'+str(hash)+'\033[31m] :((\033[00m')
             time.sleep(0.001)
             print('\033[31m{-} Exiting.........\033[00m')


    if (option5 == '1'):

        cracker()

    elif(option5 =='2'):

        cracker2()

    elif (option5 == '3'):

        manual()


    else:
         exit()


crck()