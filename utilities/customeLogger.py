import logging

class logGen:
    @staticmethod
    def loggen():
        logging.basicConfig(filename="C://Users/comp/PycharmProjects/Pytest_POM_HybridFramework_15April/Logs/automation.log",
                            format='%(asctime)s: %(message)s: %(levelname)s',
                            datefmt='%m/%d/%Y %I: %M: %S %p'
                            )
        logger=logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger