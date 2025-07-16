from django.shortcuts import render,redirect
import razorpay
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from razorpay.errors import SignatureVerificationError
from adddestinations.adddestimodel import destinationCatalogClass
from django.core.mail import send_mail
from datetime import datetime

# Create your views here.

razorpay_client = razorpay.Client(auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))

def razorpay_views(request):
    
    razor_id=settings.RAZOR_KEY_ID
    razor_key=settings.RAZOR_KEY_SECRET
    print(request.session.get("tamount"))
    vtel=request.session.get("telno")
    vbookingid=request.session.get("bookingids")
    uemailid=request.session.get("useremail")
    username=request.session.get("username")
    razorpay_order = razorpay_client.order.create({"amount":int(request.session.get("tamount"))*100,"currency":"INR","payment_capture":"0"}) 
    print(razorpay_order)
    context = {
        'amount':razorpay_order["amount"],
        'orderid':razorpay_order["id"],
        'rid':settings.RAZOR_KEY_ID,
        'ctel':vtel,
        'cbid':vbookingid,
        'cemail':uemailid,
        'cname':username,
    }
    return render(request,'payment.html',context)

@csrf_exempt
def paymenthandler(request):
    if request.method=="POST":
            payment_id = request.POST.get('razorpay_payment_id', '')
            razorpay_order_id = request.POST.get('razorpay_order_id', '')
            signature = request.POST.get('razorpay_signature', '')
            print(payment_id)
            print(razorpay_order_id)
            print(signature)
            params_dict = {
                'razorpay_order_id': razorpay_order_id,
                'razorpay_payment_id': payment_id,
                'razorpay_signature': signature
            }
            
            try: 
                razorpay_client.utility.verify_payment_signature(params_dict)
                # amt=12300
                razorpay_client.payment.capture(payment_id, int(request.session.get("tamount")*100))
                payment_details = razorpay_client.payment.fetch(payment_id)
                print(payment_details)
                destinationCatalogClass.savepaymentdetails(request.session.get("bookingids"),payment_details['order_id'],payment_details['id'],payment_details['entity'],payment_details['amount']/100,payment_details['currency'],'Sucess',payment_details['method'],payment_details['description'],request.session.get('useremail'),request.session.get('telno'),payment_details['acquirer_data']['upi_transaction_id'])
                send_mail(
                subject=f'Booking Confirmed – Your Tour to {request.session.get('vdesname')} is All Set!',
                 message=(
                    f"Hello {request.session.get('username')},\n\n"
                    f"We're excited to confirm your booking for an unforgettable tour to {request.session.get('vdesname')}!"
                    "Thank you for choosing Explore India. Your order has been successfully received and is now being processed. \n\n "
                    "Booking Details:\n"
                    f"Booking ID: {request.session.get("bookingids")} \n"
                    f"Destination: { request.session.get('vdesname') }\n"
                    f"Package Duration: {request.session.get('moredays')} days\n"

                    f"Total Price: ₹{payment_details['amount']/100}\n"

                    f"Payment Status: Sucess \n"

                    f"Booking Date: {datetime.now().strftime("%Y-%m-%d")}\n\n"
                    "What’s Next?\n"
                    "Sit back and relax while we finalize your travel itinerary. We'll keep you updated with all the necessary details and will share the full itinerary, contact information, and travel tips before your journey begins.\n\n"

                    "Thank you for exploring India with us!\n"
                    f"We wish you a safe and joyful journey to {request.session.get('vdesname')}.\n\n"

                    "Warm regards,\n"
                    "Team Explore India"
                ),
                from_email=('Explore India'),  # Display name and email
                recipient_list=[request.session.get('useremail')],
                fail_silently=False,
            )

                return redirect('home')
                
            except SignatureVerificationError as e:
                print(e)
                return render(request,'home.html')


