from django.db import connection


class userrecord():
    @staticmethod
    def adduserrecord(username,email,password):
        with connection.cursor() as adduser:
            adduser.execute("set @msg='';")
            adduser.execute("call addloginrecords(%s,%s,%s, @msg);",[username,email,password])
            adduser.execute("SELECT @msg ;")
            resultmessage=adduser.fetchone()[0]
        return resultmessage