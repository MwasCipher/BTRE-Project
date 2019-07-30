from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.
from contacts.models import Contact
from django.core.mail import send_mail


def contact(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']

        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(listing_id=listing_id, user_id=user_id,)

            if has_contacted:
                messages.error(request, 'You Already Submitted a Request for This Listing')
                return redirect('/listings/'+listing_id)

        contact = Contact(listing=listing, listing_id=listing_id, name=name, email=email,
                          phone=phone, message=message, user_id=user_id)

        contact.save()

        send_mail(
            'property Listing Enquiry',
            'There Has Been An Enquiry For ' + listing + 'Sign into Admin Panel For More',
            'mwangiwawerucollins@gmail.com',
            [realtor_email, 'collinsmwangiwaweru@gmail.com'],
            fail_silently=False

        )

        messages.success(request, 'Successfully Submitted Request')
        return redirect('/listings/'+listing_id)
