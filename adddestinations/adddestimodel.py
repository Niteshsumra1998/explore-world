from django.db import connection

class destinationCatalogClass():
    def adddestionationRecord(destinationname,destinationdesc,destinationprice,destinationimage):
        with connection.cursor() as addrecord:
            addrecord.execute("select @msg='';")
            addrecord.execute("call adddestinations(%s,%s,%s,%s,@msg);",[destinationname,destinationdesc,destinationprice,destinationimage])
            addrecord.execute("select @msg;")
            resultMsg=addrecord.fetchone()[0]
        return resultMsg
    def getalldestinations():
        with connection.cursor() as getdestinations:
            getdestinations.execute("call getalldestinations;")
            destinationdetails=getdestinations.fetchall()
        return destinationdetails
    
    def getalldestname():
        with connection.cursor() as getdestnm:
            getdestnm.execute("call getalldestinationanme;")
            destidname=getdestnm.fetchall()
        return destidname
    
    def additernary(destid,destfeature):
        with connection.cursor() as additrecord:
            additrecord.execute("select @msg='';")
            additrecord.execute("call adddestinationiternay(%s,%s,@msg);",[destid,destfeature])
            additrecord.execute("select @msg;")
            resultMsg=additrecord.fetchone()[0]
        return resultMsg
    def getdestfeature(destid):
        with connection.cursor() as getdestf:
            getdestf.execute("call getalldestinationiternary(%s);",[destid])
            destfeature=getdestf.fetchall()
        return destfeature 
    
    def adddestinationpackages(destid,travelmethod,staytype,packageprice):
        with connection.cursor() as additrecord:
            additrecord.execute("select @msg='';")
            additrecord.execute("call addpackinterary(%s,%s,%s,%s,@msg);",[destid,travelmethod,staytype,packageprice])
            additrecord.execute("select @msg;")
            resultMsg=additrecord.fetchone()[0]
        return resultMsg
    def getalldestpackbyid(destid):
        with connection.cursor() as getdestpack:
            getdestpack.execute("call getpackdetailsbyid(%s);",[destid])
            destpackbyid=getdestpack.fetchall()
        return destpackbyid
    
    def savebookingdetails(userid,contactno,address,nooftravellers,destinationid,ipackageid,JourneyStartDate,JourneyEndDate,TotalAmount):
        with connection.cursor() as addbookingdet:
            addbookingdet.execute("select @bookingid='';")
            addbookingdet.execute("call addbookingdetails(%s,%s,%s,%s,%s,%s,%s,%s,%s,@bookingid);",[userid,contactno,address,nooftravellers,destinationid,ipackageid,JourneyStartDate,JourneyEndDate,TotalAmount])
            addbookingdet.execute("select @bookingid;")
            resultbookingid=addbookingdet.fetchone()[0]
        return resultbookingid
    
    def savetravellerdetails(bookingid,travellername,travellerage):
        with connection.cursor() as addtravellers:
            addtravellers.execute("select @msg='';")
            addtravellers.execute("call addtravellerdetails(%s,%s,%s,@msg);",[bookingid,travellername,travellerage])
            addtravellers.execute("select @msg;")
            resultMsg=addtravellers.fetchone()[0]
        return resultMsg
    
    def savepaymentdetails(p_bookingid , p_ordered ,p_paymentid , p_entity, p_amount, p_currency, p_paymentstatus ,p_paymentmethod  , p_orderdescription , p_useremail ,p_usercontact ,p_method_trax_id):
        with connection.cursor() as savepayment:
            savepayment.execute("call addpaymentdetails(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);",[p_bookingid , p_ordered ,p_paymentid , p_entity, p_amount, p_currency, p_paymentstatus ,p_paymentmethod  , p_orderdescription , p_useremail ,p_usercontact ,p_method_trax_id ])

    def getdestinationbysearch(searchq):
        with connection.cursor() as getsearch:
            getsearch.execute("call getalldestinationsearch(%s);",[searchq])
            getdestinations=getsearch.fetchall()
        return getdestinations
        