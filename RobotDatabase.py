import pymysql
import RobotConfig
import random


def getDatabaseConnection4Vendor():
    mysqlConn4Robot = pymysql.connect(host=RobotConfig.robotConfig['robot']['db']['host'],
                                      port=RobotConfig.robotConfig['robot']['db']['port'],
                                      user=RobotConfig.robotConfig['robot']['db']['user'],
                                      password=RobotConfig.robotConfig['robot']['db']['pass'],
                                      database=RobotConfig.robotConfig['robot']['db']['dbName'])

    return mysqlConn4Robot


def getMessage():
    try:
        _connection = getDatabaseConnection4Vendor()
        _cursor = _connection.cursor()

        _cursor.execute("select message from product_vendor_message order by rand() limit 1")

        row = _cursor.fetchone()

        return row[0]
    except Exception as e:
        e.__str__()

        return '你好，可以加个好友吗，我们进一步聊聊?'
    finally:
        if _cursor:
            _cursor.close()

        if _connection:
            _connection.close()


def getMobiles(start, offset):
    try:
        _connection = getDatabaseConnection4Vendor()
        _cursor = _connection.cursor()

        _cursor.execute("select distinct mobile from product_vendor_mobile limit " + str(start) + "," + str(offset))

        rows = _cursor.fetchall()

        _connection.commit()

        mobiles = []
        for row in rows:
            mobiles.append(row[0])

        return mobiles
    except Exception as e:
        print(e.__str__())

        _connection.rollback()

        return []
    finally:
        if _cursor:
            _cursor.close()

        if _connection:
            _connection.close()
