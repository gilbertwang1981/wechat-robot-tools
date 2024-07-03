import pymysql
import RobotConfig


def getDatabaseConnection4Vendor():
    mysqlConn4Robot = pymysql.connect(host=RobotConfig.robotConfig['robot']['db']['host'],
                                      port=RobotConfig.robotConfig['robot']['db']['port'],
                                      user=RobotConfig.robotConfig['robot']['db']['user'],
                                      password=RobotConfig.robotConfig['robot']['db']['pass'],
                                      database=RobotConfig.robotConfig['robot']['db']['dbName'])

    return mysqlConn4Robot


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
