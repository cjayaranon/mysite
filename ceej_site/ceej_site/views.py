from django.http import HttpResponse

def check_num(request, nums):
    
    nums = int(nums)
    
    if nums%2:
        value = ("True")
    else:
        value = ("False")
    htmls = "<html><body>{chu}</body></html>".format(chu=value)
    return HttpResponse(htmls)

def display_name(request, name):
    htmls = "".format(disp=name)