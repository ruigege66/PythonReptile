"""
处理JS加密
"""
import time,random

def getSalt():
    """
    salt公式："" + ((new Date).getTime() + parseInt(10 *Matn.rnandom(),10))
    :return:
    """
    salt = int(time.time()*1000) + random.randint(0,10)

    return salt

def getMD5():
    import hashlib
    md5zhi = hashlib.md5()

    md5zhi.update(v.encoding="uft-8")
    sign = md5zhi.hexdigest()

    return sign
if __name__ == "__main__":
    getSalt()
    getMD5()

