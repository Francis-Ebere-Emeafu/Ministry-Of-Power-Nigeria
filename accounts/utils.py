from accounts.models import Account
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib import messages



@login_required
def profile_home(request):
    if is_staff(request.user):
        print("The user is a STAFF")
        return redirect('home')
    elif is_erd_staff(request.user):
        print("The user is a ERD STAFF")
        messages.success(request, "ERD STAFF Login Successful")
        return redirect('senior_staff_profile')
    elif is_dsd_staff(request.user):
        print("The user is a MANAGER")
        messages.success(request, "ERD STAFF Login Successful")
        return redirect('manager_profile')
    elif is_isd_staff(request.user):
        print("The user is a MANAGER")
        messages.success(request, "ISD STAFF Login Successful")
        return redirect('manager_profile')
    elif is_rrd_staff(request.user):
        print("The user is a MANAGER")
        messages.success(request, "RRD STAFF Login Successful")
        return redirect('manager_profile')
    elif is_tsd_staff(request.user):
        print("The user is a MANAGER")
        messages.success(request, "TSD STAFF Login Successful")
        return redirect('manager_profile')
    elif request.user.has_perm('user.is_superuser'):
        print("The user is a SUPERUSER STAFF")
        # logout(request)
        return redirect('profile')


def is_staff(user):
    if Account.objects.filter(user=user):
        account = Account.objects.get(user=user)
        # confirm that the user is a staff
        # if account.user_type == 0:
        if account.user_type == Account.STAFF:
            return True
        return False


def is_emiu_staff(user):
    if Account.objects.filter(user=user):
        account = Account.objects.get(user=user)
        # confirm that the user is a staff
        if account.user_type == Account.EMIU:
            return True
        return False


def is_erd_staff(user):
    if Account.objects.filter(user=user):
        account = Account.objects.get(user=user)
        # confirm that the user is a staff
        if account.user_type == Account.ERD:
            return True
        return False


def is_dsd_staff(user):
    if Account.objects.filter(user=user):
        account = Account.objects.get(user=user)
        # confirm that the user is a staff
        if account.user_type == Account.DSD:
            return True
        return False


def is_isd_staff(user):
    if Account.objects.filter(user=user):
        account = Account.objects.get(user=user)
        # confirm that the user is a staff
        if account.user_type == Account.ISD:
            return True
        return False


def is_rrd_staff(user):
    if Account.objects.filter(user=user):
        account = Account.objects.get(user=user)
        # confirm that the user is a staff
        if account.user_type == Account.RRD:
            return True
        return False


def is_tsd_staff(user):
    if Account.objects.filter(user=user):
        account = Account.objects.get(user=user)
        # confirm that the user is a staff
        if account.user_type == Account.TSD:
            return True
        return False


def is_management_staff(user):
    if Account.objects.filter(user=user):
        account = Account.objects.get(user=user)
        # confirm that the user is a staff
        if account.user_type == Account.MANAGEMENT:
            return True
        return False
