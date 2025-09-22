
from django.http.response import JsonResponse
from django.http.request import HttpRequest
from django.shortcuts import render, redirect
from django.conf import settings
from yaml import safe_load
from importlib import import_module 
from django.shortcuts import render
from re import fullmatch


class TemplateRenderer:
    def __init__(self,get_response ):
        self.get_response = get_response
        self.url_paths = settings.URL_PAGES


    def __call__(self, request : HttpRequest, *args, **kwds):
        response = self.get_response(request)
        path = request.path
        print(">"*100)
        if path == '/index':
            path = "/"

        for url_page in self.url_paths:
            pattern = r'^{}?$'.format(path)
            matched_pattern = fullmatch(pattern, url_page.get("href"))

            if matched_pattern  and url_page.get("template",None) != None:
                response =  render(request,url_page.get("template"))
                print(f"path: {path}, url_page: {url_page.get('href')}, login_required: {url_page.get('login_required', False)} ")
                if url_page.get('login_required', False) == True :
                    response = redirect(settings.LOGIN_URL)


        return response
