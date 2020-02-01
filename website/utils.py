import hashlib
import string
import random
from datetime import datetime

class Utils():

    def shaHash256(data):
        return hashlib.sha224(bytes(data)).hexdigest()
    
    #FIXME: urlGen super buggy
    def urlGen(sourceName, database):
        urlTemp = sourceName.split(" ")
        tmp = ""
        counter = 0
        min = 4
        for word in urlTemp:
            tmp = tmp + word + "-"
            if counter >= min:
                tmpMod = tmp + "-" + str(datetime.now())
                exists = database.query.filter(database.url == tmpMod).scalar()
                if exists is None:
                    return tmpMod
                else:
                    counter += 1
            counter += 1
        print(tmp)
        while 1:
            exists = database.query.filter(database.url == tmp).scalar()
            if exists is not None:
                tmp = tmp + "-" + str(datetime.now()) 
            if exists is None:
                return tmp
        return None