import os
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse
import time

class Complex(object):
    def __init__(self, real, imag=None):
        self.real = real
        self.imag = 0

    def __str__(self):
        return "({0}+{1}j)".format(self.real, self.imag)

start = time.time()
primeNumbers = []
output = ""

for i in xrange(2, 300000):
    divisible = False
    inum = Complex(i)

    for number in primeNumbers:
        if inum.real % number.real == 0:
            divisible = True
            break

    if divisible == False:
        primeNumbers.append(inum)
        output += str(inum)


print 'time: %f' % (time.time() - start)
print len(primeNumbers), len(output)

from . import database
from .models import PageView

# Create your views here.

def index(request):
    hostname = os.getenv('HOSTNAME', 'unknown')
    PageView.objects.create(hostname=hostname)

    return render(request, 'welcome/index.html', {
        'hostname': hostname,
        'database': database.info(),
        'count': PageView.objects.count()
    })

def health(request):
    return HttpResponse(PageView.objects.count())
