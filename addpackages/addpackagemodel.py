from django.db import connection

class packageCatalogClass():
    def addpackageRecord(packagename,packagedesc,packageprice,packageimage):
        with connection.cursor() as addrecord:
            addrecord.execute("select @msg='';")
            addrecord.execute("call addpackage(%s,%s,%s,%s,@msg);",[packagename,packagedesc,packageprice,packageimage])
            addrecord.execute("select @msg;")
            resultMsg=addrecord.fetchone()[0]
        return resultMsg
    def getallpackages():
        with connection.cursor() as getpackages:
            getpackages.execute("call getallpackages;")
            packagesdetails=getpackages.fetchall()
        return packagesdetails
    