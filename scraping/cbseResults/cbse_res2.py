import urllib, subprocess
import time
import multiprocessing
import sqlite3
import lxml.html

conn = sqlite3.connect("info.db")
c = conn.cursor()
c.execute('''CREATE TABLE Student (StudentName text,  FatherName text, RollNo integer)''')

#count = 0
def rollfind(startr,endr):
    for roll in range(startr,endr+1):
        cmd = "curl 'http://resultsarchives.nic.in/cbseresults/cbseresults2015/class12/cbse122015_all_rev.asp' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8' --compressed -H 'Accept-Language: en-US,en;q=0.5' -H 'Connection: keep-alive' -H 'Content-Type: application/x-www-form-urlencoded' -H 'Host: resultsarchives.nic.in' -H 'Referer: http://resultsarchives.nic.in/cbseresults/cbseresults2015/class12/cbse122015_all_rev.htm' -H 'Upgrade-Insecure-Requests: 1' -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:59.0) Gecko/20100101 Firefox/59.0' --data 'regno={}&B1=Submit'".format(roll)
        handle = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, close_fds=True, shell=True)
        res = handle.stdout.read()
        root = lxml.html.fromstring(res)
        roll = root.xpath('//table')[4].findall('tr')[0].findall('td')[1].findall('font')[0].text.strip()
        name = root.xpath('//table')[4].findall('tr')[1].findall('td')[1].findall('font')[0].findall('b')[0].text.strip()
        fname = root.xpath('//table')[4].findall('tr')[3].findall('td')[1].findall('font')[0].text.strip()
        ''' query = "SELECT EXISTS(SELECT 1 FROM Student where StudentName='{}' and FatherName='{}' and RollNo={});".format(name,fname,roll)
        c.execute(query)
        if len(c.fetchall())==0:
            query = "INSERT INTO Student VALUES ('{}','{}',{})".format(name,fname,roll)
            c.execute(query)
            conn.commit()
            print("Details of {} Committed".format(roll))
        else:
            print("Already in DB !!!") '''
        query = "INSERT INTO Student VALUES ('{}','{}',{})".format(name,fname,roll)
        c.execute(query)
        conn.commit()
        print("Credentials of {} Added !!".format(roll))


''' def kill_pool():
    print("Quitting all Processes !!")
    pool.terminate() '''

start = time.time()
rlist = [x for x in range(9100001,9200001,200)]

pool = multiprocessing.Pool(500)
for r in range(0,len(rlist)+1):
    try:
        pool.apply_async(rollfind,args=(rlist[r],rlist[r+1]))
    except:
        pass

pool.close()
pool.join()

conn.close()
print(time.time()-start)
