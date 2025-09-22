from django.conf import settings
# HttpRequest.path

def custom_context(request):
    menu_items  = settings.URL_PAGES or []
    path        = request.path
    
    if (path == '/index'):
        path = "/" 

    title  = "Device Control"
    for i in menu_items:
        if (i['href'] ==  path and path != '/'):
            title = i['name']

    req_headers = dict(request.headers)
    global_context = {
        'globals' : { 
            "menu_items"    : menu_items,
            'req_headers'   : req_headers,
        },
        'req_path' : path,
        'page_title' : title
    }
    return global_context