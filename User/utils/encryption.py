import binascii
from pyDes import des, CBC, PAD_PKCS5


class Encryption:
    def des_encrypt(s):
        """
        DES 加密
        :param s: 原始字符串
        :return: 加密后字符串，16进制
        """
        secret_key = '19951113'
        iv = secret_key
        k = des(secret_key, CBC, iv, pad=None, padmode=PAD_PKCS5)
        en = k.encrypt(s, padmode=PAD_PKCS5)
        de = binascii.b2a_hex(en)
        data = de.decode('UTF-8')
        return data

    def des_descrypt(s):
        """
        DES 解密
        :param s: 加密后的字符串，16进制
        :return:  解密后的字符串
        """
        string=s.encode('UTF-8')
        secret_key = '19951113'
        iv = secret_key
        k = des(secret_key, CBC, iv, pad=None, padmode=PAD_PKCS5)
        de = k.decrypt(binascii.a2b_hex(string), padmode=PAD_PKCS5)
        data = de.decode('UTF-8')
        return data





if __name__ == "__main__":
    a = 'root'
    b=Encryption.des_encrypt(a)
    c=Encryption.des_descrypt(b)
    print(b)
    print(c)

