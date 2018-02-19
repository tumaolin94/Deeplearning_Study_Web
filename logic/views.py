from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.conf import settings
import sys
sys.path.append('D:/pythonspace/machinelearningWeb/logic/assignment1')
import test1

# from ./ssignment1 import test1
# sys.path.append("..")
# import assignment1.test1
def hello(request):
    static_path = settings.BASE_DIR
    static_path2 = settings.STATICFILES_DIRS[0];
    host = request.get_host()
    path = request.get_full_path()
    print(request.get_host())
    print(request.get_full_path())
    print(static_path2)
    # test1.start()
    try:
        test1.load_data(static_path,static_path2)
    except Exception as inst:
        print(type(inst))  # the exception instance
        print(inst.args)  # arguments stored in .args
        print(inst)
    context = {}
    context['test'] = test1.test()
    context['src'] = "/static/0.png"
    return render(request, 'ass1.html', context)
