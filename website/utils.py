from datetime import datetime

class Utils():
    def __init__(self):
        print("url gen")
    def shaHash256(data):
        return hashlib.sha224(bytes(data)).hexdigest()
    
    def urlGen(sourceName, database):
        urlTemp = sourceName.split(" ")
        tmp = ""
        counter = 0 
        for word in urlTemp:
            tmp = tmp + word + "-"
            if counter > 4:
                break
        time = ((str(datetime.now()).replace("-", "").replace(" ", "-")).replace(":", ""))
        tmp2 = tmp + time[0:time.find(".")]
        counter = 0
        while 1:
            exists = database.query.filter(database.url == tmp2).scalar()
            if exists is not None:
                time = ((str(datetime.now()).replace("-", "").replace(" ", "-")).replace(":", ""))
                tmp2 = tmp + time[0:time.find(".")]
            else:
                return tmp2
            counter += 1
            if counter > 10:
                return None