from django.views.generic import ListView
from django.shortcuts import render
from school.models import Student, Teacher
import functools
from django.db import connection, reset_queries
import time


def query_debugger(func):

    @functools.wraps(func)
    def inner_func(*args, **kwargs):
        reset_queries()
        start_queries = len(connection.queries)
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()
        end_queries = len(connection.queries)
        print(f"Function : {func.__name__}")
        print(f"Number of Queries : {end_queries - start_queries}")
        print(f"Finished in : {(end - start):.2f}s")
        return result

    return inner_func


@query_debugger
def students_list_slow(request):
    template = 'school/students_list.html'
    students = Student.objects.all().order_by('group')
    context = {'students': students}

    return render(request, template, context)


@query_debugger
def students_list_fast(request):
    template = 'school/students_list.html'
    students = Student.objects.all().order_by('group').prefetch_related('teachers')
    context = {'students': students}

    return render(request, template, context)
