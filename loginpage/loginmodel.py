from django.db import connection

class logindetails():
    @staticmethod
    def adduserrec(uemail,upass):
        with connection.cursor() as addusercursor:
            addusercursor.execute("set @msg= '' ;")
            addusercursor.execute("call validatelogin(%s,%s,@msg)",[uemail,upass])
            addusercursor.execute("select @msg")
            result=addusercursor.cursor.fetchone()[0]
        return result