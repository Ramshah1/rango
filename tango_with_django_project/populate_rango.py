import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE','tango_with_django_project.settings')

import django
django.setup()

from rango.models import Category, Page

def populate():
    c_cat = add_cat('C++', likes=23, views=12)

    add_page(cat=c_cat,
             title= "C Programming tutorial",
             url="http://www.cprogramming.com/tutorial/c-tutorial.html")

    add_page(cat=c_cat,
        title="Tutorial Point for C",
        url="http://www.tutorialspoint.com/cprogramming/")

    add_page(cat=c_cat,
        title="Program-Z for C++",
        url="http://www.programiz.com/c-programming")

    java_cat  = add_cat("Java", likes= 56,views= 98)

    add_page(cat=java_cat,
        title="Official Java Documentation",
        url="https://docs.oracle.com/javase/tutorial/")

    add_page(cat=java_cat,
        title="Java Point Tutorial",
        url="http://www.javatpoint.com/java-tutorial")

    add_page(cat=java_cat,
        title="Java Course",
        url="https://www.udemy.com/java-tutorial/")


    cc_cat = add_cat("C Sharp", likes= 128, views= 32)

    add_page(cat=cc_cat,
        title="MSDN",
        url="https://msdn.microsoft.com/en-us/library/aa288436(v=vs.71).aspx/")

    add_page(cat=cc_cat,
        title=".Net Tutorial",
        url="http://csharp.net-tutorials.com/")

    add_page(cat=cc_cat,
        title="Free C sharp tutorials",
        url="http://www.homeandlearn.co.uk/csharp/csharp.html")

    for c in Category.objects.all():
        for p in Page.objects.all():
            print "- {0} - {1}".format(str(c), str(p))

def add_page(cat, title, url, views=0):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url=url
    p.views=views
    p.save()
    return p

def add_cat(name, likes=0, views=0):
    c= Category.objects.get_or_create(name=name, likes= likes, views=views)[0]
    return c

if __name__ == '__main__':
    print "Starting Rango population script..."
    populate()