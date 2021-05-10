import configparser

config=configparser.RawConfigParser()
config.read(".\\Configuration\\config.ini")

class ReadConfig:
    @staticmethod
    def getApplicationURL():
        url=config.get('common info','baseURL')
        return url

    @staticmethod
    def getApplicationusername():
        username = config.get('common info', 'username')
        return username

    @staticmethod
    def getApplicationpassword():
        password = config.get('common info', 'password')
        return password

