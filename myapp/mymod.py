from models import MyModel

def foo(x):

    try:
        MyModel.objects.get(pk=x)
    except MyModel.DoesNotExist:
        return 'raised'
    return 'not raised'