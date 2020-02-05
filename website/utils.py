import hashlib
import string
import random
from datetime import datetime

class Utils():

    def shaHash256(data):
        return hashlib.sha224(bytes(data)).hexdigest()
    
    def urlGen(sourceName, database):
        urlTemp = sourceName.split(" ")
        tmp = ""
        for word in urlTemp:
            tmp = tmp + word + "-"
        tmp2 = tmp + str(datetime.now())
        counter = 0
        while 1:
            exists = database.query.filter(database.url == tmp2).scalar()
            if exists is not None:
                tmp2 = tmp + str(datetime.now())
            else:
                return tmp
            counter += 1
            if counter > 10:
                return None