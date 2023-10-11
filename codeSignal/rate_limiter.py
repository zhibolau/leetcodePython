# timestamps = [1600040547954, 1600040547957, 1600040547958], 
# ipAddresses = ["127.105.232.211", "127.105.232.211", "127.105.232.211"], 
# limit = 1 
# timeWindow = 3 #miliseconds

def solution(timestamps, ipAddresses, limit, timeWindow):
    if not timestamps or not ipAddresses or not limit or not timeWindow:
        return []
    res=[]
    d= {}
    for index,ip in enumerate(ipAddresses):
        if ip not in d:
            d[ip]=(1,timestamps[index])
            res.append(1)
            print(ip)
            print(d[ip])
        else:
            #ip already in d
            ip_in_time=d[ip][1]
            if timestamps[index]-ip_in_time <= timeWindow:
                ip_appear_now=d[ip][0]
                if ip_appear_now + 1 <=limit:
                    d[ip] = (d[ip][0]+1,ip_in_time)
                    print(ip)
                    print(d[ip])
                    res.append(1)
                else:
                    res.append(0)
                    print(ip)
                    print(d[ip])
            else: 
                #timewindow passed
                d[ip]=(d[ip][0]-1,timestamps[index])
                res.append(1)
                print(ip)
                print(d[ip])
    return res
            
            
                
                    
    

print(solution([1600000000000, 1600000000001, 1600000000003, 1600000000004, 1600000000005, 1600000000006, 1600000000007, 1600000000009, 1600000000010, 1600000000011, 1600000000013, 1600000000016, 1600000000017, 1600000000018, 1600000000019, 1600000000020, 1600000000021, 1600000000022, 1600000000024, 1600000000025],
["1.2.2.1", 
 "1.6.2.7", 
 "1.6.2.7", 
 "1.2.2.1", 
 "1.6.2.7", 
 "1.6.2.7", 
 "1.2.2.1", 
 "1.2.2.1", 
 "1.2.2.1"]
,3,8))


#[1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1]   mine
#[1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1]  yes