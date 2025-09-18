from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required(login_url='/login')
def home_page(req):
    return render(req, 'index.html')


def device_list_page(req):
    pass


def device_details_page(req):
    pass


def commands_page(req):
    pass


def admin_page(req):
    pass


def login_page(req):
    context = {
        "page_title" : "Login Page",
    }
    return render(req,"login.html",context=context)

def register_page(req):
    pass

