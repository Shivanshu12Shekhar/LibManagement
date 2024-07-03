#Library management system
import pickle
import datetime
def bukmen() : # book file menu options
    print('Book File Menu')
    print('''

    1. => Add a book
    2. => Discard a book
    3. => Go to main menu''')

def memmen() : # member menu options
    print('Member File Menu')
    print('''
    1. => Add a new member
    2. => Remove a member
    3. => Correction
    4. => Go to main menu''')

def repmen() : #report menu options
    print('Report Menu')
    print('''
    1. => Book list
    2. => Member list
    3. => Issued books
    4. => Go to main menu''')

def pin() : # security pin
    pin = '0'
    while pin != '4949' :
        pin = str(input('Enter pin: '))
        if pin != '4949' :
            print('Incorrect pin try again')
        else :# correct pin is '4949'
            print('Welcome')

def bckbuk() : # back to book menu
    l = str(input('Do you want to go back to Book file menu(y/n): '))
    if l.lower() == 'y' :
        bukmen()
    else :
        exit()

def bckmem() : #back to member menu
    l = str(input('Do you want to go back to Member file menu(y/n): '))
    if l.lower() == 'y' :
        memmen()
    else :
        exit()
def bckrep() : # back to report menu
    l = str(input('Do you want to go back to Report menu(y/n): '))
    if l.lower() == 'y' :
        repmen()
    else :
        exit()
def library_management() :
    print('Library Management System')
    print('welcome user')
    print('''
    1. => Book file menu
    2. => Member file menu
    3. => Issue book
    4. => Return book
    5. => Report
    6. => Quit
    ''')
    choice_main = int(input('Enter your Choice: ')) # choice for main menu

    if choice_main == 1 : # Book file menu starts
        bukmen()
        book_file = int(input('Enter your choice: ')) # choice for book file menu

        while book_file in [1,2,3] : # for other options it will come out of program

            
            if book_file == 1 : # adding book in book menu
                pin()
                y_addbuk = 'y'
                while y_addbuk.lower() == 'y' :
                    b_id = str(input('1.Enter Book id: '))
                    b_name = str(input('2.Enter Book name: '))
                    b_aut = str(input('3.Enter Author name: '))
                    b_tot = int(input('4.Enter Total number of copies: '))
                    b_iss = int(input('5.Enter number of copies issued: '))
                    b_av = int(input('Enter number of copies available'))
                    b_details = [b_id,b_name,b_aut,b_tot,b_iss,b_av]
                    print(b_details)
                    
                    b = open('book.dat','ab')
                    b_add = pickle.dump(b_details,b) # adding book particulars in book.dat
                    b.close()
                    print('Added successfully')
                    y_addbuk = str(input('Do you want to add another book?(y/n): '))
                bckbuk()
                book_file = int(input('Enter your choice: '))


                
            elif book_file == 2 : #removing a book in book menu
                pin()
                y_rembuk = 'y'
                while y_rembuk.lower() == 'y' :
                    disc = str(input('Enter Book id of book which have to be discarded : '))
                    b_disc = []
                    try :
                        bo = open('book.dat','rb')
                        try :
                            while True :
                                b_show = pickle.load(bo)
                                b_disc.append(b_show) # adding list of all books in a single list
                        except EOFError :
                            pass
                        bo.close()
                    except FileNotFoundError :
                        print('File not found')
#updating book file
                    flag = 0
                    checklist = []
                    if b_disc == [] :
                        flag = 1 # Checks for empty list
                    else :
                        bo = open('book.dat','wb') # To remove all particulars from file
                        for bd in b_disc :
                            if bd[0] != disc : # matching inputed book id
                                checklist.append(bd[0])
                                pickle.dump(bd,bo)
                            else :
                                checklist.append(bd[0])
                        bo.close()
                        flag = 3 #checks for successful removal
                        if disc not in checklist :
                            flag = 2 # checks for wrong book id
                    if flag == 1 :
                        print('Book list is already empty.')
                        break
                    elif flag == 2 :
                        print('Book with book id',disc,'is not in the list')
                    elif flag == 3 :
                        print('Book with book id',disc,'is removed successfully')
                    y_rembuk = str(input('Do you want to remove another book(y/n)?: '))
                bckbuk()
                book_file=int(input('Enter your choice: '))

                

            elif book_file == 3 : # Go to main menu
                library_management()


        else:
            print('''incorrect option
please input correct option''')



    elif choice_main == 2 : # member file menu starts
        memmen()
        mem_file = int(input('Enter your choice: '))


        while mem_file in [1,2,3,4] : # for other options it will come out of program


            if mem_file == 1: # Adding a member in member menu
                pin()
                y_addmem = 'y'
                while y_addmem.lower() == 'y' :
                    m_name = str(input('Enter Name : '))
                    m_phone = str(input('Enter Phone No. : '))
                    m_add = str(input('Enter Address : '))
                    m_email = str(input('Enter Email : '))
                    m_issue = 'No'
                    m_bookid = ''
                    m_id = '0' # arbitary member id

                    m = open('member.dat','ab+') # for assigning umique member id 
                    mid_list = []
                    try :
                        while True :
                            m_show = pickle.load(m)
                            mid_list.append(m[0])
                    except EOFError :
                        pass
                    import random
                    x = str(random.randint(1,1000))
                    while m_id != x :
                        if mid_list == [] :
                            m_id = x
                        elif x not in mid_list:
                            m_id = x
                        elif x in mid_list :
                            x = str(random.randint(1,1000))
                     # addition of member       
                    m_details = [m_id,m_name,m_phone,m_add,m_email,m_issue,m_bookid]
                    print(m_details)
                    m_add = pickle.dump(m_details,m)
                    m.close()
                    print('Added successfully')
                    y_addmem = str(input('Do you want to add another member(y/n): '))
                bckmem()
                mem_file = int(input('Enter your choice: '))



            elif mem_file == 2 : # Removing a member in member menu
                pin()
                y_remmem = 'y'
                while y_remmem.lower() == 'y' :
                    disc = str(input('Enter member id you want to remove: '))
                    m_disc = []
                    try : 
                        mo = open('member.dat','rb')
                        try :
                            while True :
                                m_show = pickle.load(mo)
                                m_disc.append(m_show)
                        except EOFError:
                            pass
                        mo.close()
                    except FileNotFoundError :
                        print('File not found')
                    # updating member file
                    flag = 0
                    checklist = []
                    if m_disc == []:
                        flag = 1 # checks for empty list
                    else :
                        for valid in m_disc :
                            # checking that if issued a book 
                            if disc == valid[0] and valid[3] == 'Yes' :
                                print('''Can not remove this member.
Before removing return issued books under Return book section in main menu''')
                                library_management()
                                break
                        mo = open('member.dat','wb')
                        for md in m_disc :
                            if md[0] != disc :
                                checklist.append(md[0])
                                pickle.dump(md,mo)
                            else :
                                checklist.append(md[0])
                        mo.close()
                        flag = 3 # show success in removal
                        
                        if disc not in checklist :
                            flag = 2 # checks for wrong member id 
                    
                    if flag == 1 :
                        print('Member list is already empty')
                        break
                    elif flag == 2 :
                        print('Member with member id',disc,'is not in the list')
                    elif flag == 3 :
                        print('Member with member id',disc,'is removed successfully')

                    y_remmem = str(input('Do you want to remove another member(y/n)?: '))
                bckmem()
                mem_file = int(input('Enter your choice: '))
                            
                    
                    

            elif mem_file == 3 : # corretion in member list
                pin()
                y_cormem = 'y'
                while y_cormem.lower() == 'y' :
                    cor = str(input('Enter member id you want to do correction : '))
                    m_cor = []
                    try : 
                        mo = open('member.dat','rb')
                        try :
                            while True :
                                m_show = pickle.load(mo)
                                m_cor.append(m_show)
                        except EOFError:
                            pass
                        mo.close()
                    except FileNotFoundError :
                        print('File not found')
                    # updating member file
                    flag = 0
                    checklist = []
                    if m_cor == []:
                        flag = 1 # checks for empty list
                    else :
                        for valid in m_cor : # matching given id
                            if cor == valid[0] :
                                m_name = str(input('Enter Name : '))
                                m_phone = str(input('Enter Phone No. : '))
                                m_add = str(input('Enter Address : '))
                                m_email = str(input('Enter Email : '))
                                valid[1] = m_name
                                valid[2] = m_phone
                                valid[3] = m_add
                                valid[4] = m_email
                        mo = open('member.dat','wb')
                        for md in m_cor :
                            checklist.append(md[0])
                            pickle.dump(md,mo)
                        mo.close()
                        flag = 3 # show success in removal
                        
                        if cor not in checklist :
                            flag = 2 # checks for wrong member id

                    if flag == 1 :
                        print('Member list is already empty')
                        break
                    elif flag == 2 :
                        print('Member with member id',cor,'is not in the list')
                    elif flag == 3 :
                        print('Correction in particulars of member with member id',cor,'is done successfully')

                    y_cormem = str(input('Do you want to do correction in another member(y/n)?: '))
                bckmem()
                mem_file = int(input('Enter your choice: '))



            elif mem_file == 4 : # Option to main menu
                library_management()

        else : # msg to restart program
            print('''incorrect option
please restart the program''')



    elif choice_main == 3 :#Issue a book
        pin()

        y_moiss = 'y'
        while y_moiss == 'y' :
             
            y5 = 'y'
            mis = str(input('Enter member id : '))#m_id
            while y5 == 'y' : # will validate m_id
                try :
                    mo = open('member.dat','rb')
                    mcheckvalid = []
                    mcheckissue = []
                    try :
                        while True :
                            m_show = pickle.load(mo)
                            mcheckvalid.append(m_show[0])
                            mcheckissue.append(m_show)
                    except EOFError :
                        pass
                    mo.close()
                except FileNotFoundError :
                    print('Member File not found')
                    library_management()
                    break
                if mis not in mcheckvalid : # checks for wrong id
                    print('''Given id doesnot match any existing id. please input correct id
or check member list''')
                    y5 = str(input('Do you want to continue(y/n)?: '))
                    if y5 == 'y' :
                        mis = str(input('Enter member id: '))
                    else :
                        library_management()
                else :
                    for i in mcheckissue :
                        if i[0] == mis and i[5] == 'Yes' : # checks that if issued a book
                            print('Already issued a book.First return that book before issuing another')
                            y5 = str(input('do you want to continue(y/n)?: '))
                            if y5 == 'y' :
                                mis = str(input('Enter member id: '))
                            else :
                                library_management()
                break # returns correct id
            else :
                library_management()
            
            
            y6 = 'y'
            while y6 == 'y' : # will validate b_id
                bis = str(input('Enter book id: ')) #enter book id
                try :
                    bo = open('book.dat','rb')
                    bcheckvalid = []
                    bcheckavail = []
                    try :
                        while True :
                            b_show = pickle.load(bo)
                            bcheckvalid.append(b_show[0])
                            bcheckavail.append(b_show)
                    except EOFError :
                        pass
                    bo.close()
                except FileNotFoundError :
                    print('File not Found')
                    library_management()
                    break
                if bis not in bcheckvalid : # checks for wrong id
                    print('Given id doesnot match any existing id. please input correct id')
                    y6 = str(input('do you want to continue(y/n)?: '))
                    if y6 == 'y' :
                        bis = str(input('Enter book id: '))
                    else :
                        library_management()
                for j in bcheckavail :
                    if j[0] == bis and j[5] <= 10 : # checks for availblity
                        # minimum 10 books will be there for readers and not for issuing
                        print('This book is not available for issuing. Sorry')
                        y6 = str(input('Do you want to continue(y/n)?: '))
                        if y6 == 'y' :
                            bis = str(input('Enter book id: '))
                        else :
                            library_management()
                break # returns correct id
            else :
                library_management()
                
            yeariss = int(input('Enter Year'))
            monthiss = int(input('Enter Month'))
            dateiss = int(input('Enter Date'))
            
            dis = datetime.date(yeariss, monthiss, dateiss)
            issue_details = [mis,bis,dis]
            
            io = open('record.dat','ab')
            print(issue_details)
            i_add = pickle.dump(issue_details,io) # addition of record  
            io.close()
            # modifying member file
            mo = open('member.dat','rb')
            m_change = []
            try :
                while True :
                    mem_show = pickle.load(mo)
                    m_change.append(mem_show)
            except EOFError :
                pass
            mo.close()
            mo = open('member.dat','wb')
            for mid in m_change :
                if mid[0] == mis :
                    mid[5] = 'Yes'
                    mid[6] = bis
                    pickle.dump(mid,mo)
                else :
                    pickle.dump(mid,mo)
            mo.close()
            #modifying book list
            bo = open('book.dat','rb')
            b_change = []
            try :
                while True :
                    buk_show = pickle.load(bo)
                    b_change.append(buk_show)
            except EOFError:
                pass
            bo.close()
            bo = open('book.dat','wb')
            for bid in b_change :
                if bid[0] == bis :
                    bid[4] += 1
                    bid[5] -= 1
                    av = bid[5]
                    pickle.dump(bid,bo)
                else :
                    pickle.dump(bid,bo)
            bo.close()
            
            
            print('Book with id',bis,'is issued in the name of member with id',mis,'.copies available are',av)
            print('NOTE: No charges for first 7 days. After 7 days Rs 25/- per day will be charged.')
            y_moiss = str(input('Do you want to issue more book(y/n)?'))
        library_management()


    elif choice_main == 4 : # return a book
        pin()

        mret = str(input('Enter member id : '))
        bret = str(input('Enter book id : '))
        yearret = int(input('Enter year'))
        monthret = int(input('Enter month'))
        dateret = int(input('Enter date'))
        dret = datetime.date(yearret, monthret, dateret)
        ret_details = [mret,bret]
        # obtaining saved data
        try :
            io = open('record.dat','rb')
            ret_check = []
            rec_check = []
            try :
                while True :
                    rec = pickle.load(io)
                    ret_check.append(rec)
                    ret_match = [rec[0],rec[1]]
                    rec_check.append(ret_match)
            except EOFError :
                pass
            io.close()
        except FileNotFoundError :
            print('File not found')
            library_management()
        # matching of given data with saved records
        if ret_details in rec_check :
# modifying book file
            b_change = []
            bidenty = []
            bo = open('book.dat','rb')
            try :
                while True :
                    b_show = pickle.load(bo)
                    b_change.append(b_show)
                    bidenty.append(b_show[0])
            except EOFError :
                pass
            bo.close()

            if bret in bidenty :
                bo = open('book.dat','wb')
                for bchange in b_change :
                    if bchange[0] == bret :
                        bchange[4] -= 1
                        bchange[5] += 1
                        av = bchange[5]
                        pickle.dump(bchange,bo)
                    else :
                        pickle.dump(bchange,bo)
                bo.close()
                print('Book is successfully returned. Available copies are',av)

            else : 
                print('''Book is already discarded.
So no changes will take place in Book list''')
# modifying member file
            m_change = []
            mo = open('member.dat','rb')
            try :
                while True :
                    m_show = pickle.load(mo)
                    m_change.append(m_show)
            except EOFError :
                pass
            mo.close()

            mo = open('member.dat','wb')
            for mchange in m_change :
                if mchange[0] == mret :
                    mchange[5] = 'No'
                    mchange[6] = ''
                    pickle.dump(mchange,mo)
                else :
                    pickle.dump(mchange,mo)
            mo.close()
            print('No book is issued against the member with id',mret,'. Thank you for returning')
            io = open('record.dat','wb')
# modifying issued book records
            for ichange in ret_check :
                if [ichange[0],ichange[1]] != ret_details :
                    pickle.dump(ichange,io)
                else :
                    dis = ichange[2]
                    date = dret - dis # difference between day of returning & issuing
            io.close()
            # cahrge calculator
            if date <= datetime.timedelta(days=7) : #change to be done
                print('No charges will be charged')
            else :
                d = date.days
                print('Number of day(s) is/are', d)
                charge = 25*(d-7)
                print('Please pay Rs ', charge)
                
            print('Issued books record is updated successfully')
                    
        else : 
            print('This member have not issued this book try again')

        library_management()

            
        
    elif choice_main == 5 : # Report

        repmen()
        rep = int(input('Enter your choice: '))

        while rep in [1,2,3,4] : # for other options it will come out of program
            if rep == 1 : # book list 
                pin()
                print(['Book id','Book name','Author name','Total copies','Copies issued','Copies available'])
                try :
                    bo = open('book.dat','rb')
                    try :
                        while True :
                            b_show = pickle.load(bo)
                            print(b_show)
                    except EOFError :
                        print('''No more books.
                               ------end-----''')
                        pass

                    bo.close()
                except FileNotFoundError :
                    print('File not found')

                bckrep()
                rep = int(input('Enter your choice: '))

            elif rep == 2 : # member list
                pin()
                print(['Member id','Name','Phone no.','Address','Email','Book issued(Yes/No)','Book id(if issued)'])
                try :
                    mo = open('member.dat','rb')
                    try :
                        while True :
                            m_show = pickle.load(mo)
                            print(m_show)
                    except EOFError :
                        print('''no more members.
                                ------end-----''')
                        pass
                    mo.close()
                except FileNotFoundError :
                    print('File not found')
                bckrep()
                rep = int(input('Enter your choice: '))

            elif rep == 3 : # issued book
                pin()
                print(['Member id','Book id','Date of issue'])
                try :
                    io = open('record.dat','rb')
                    try :
                        while True :
                            rec = pickle.load(io)
                            print(rec)
                    except EOFError :
                        print('''No more records
                                 ------end------''')
                        pass
                    io.close()
                except FileNotFoundError :
                    print('File not found')
                
                bckrep()
                rep = int(input('Enter your choice: '))

            elif rep == 4 : # option to main menu
                 library_management()

        else :# msg to restart program
            print('''incorrect option
please restart the program''')
          
       
    elif choice_main == 6 : # Quit the program
        print('Exiting program')
        exit()

library_management() # recurssive function
