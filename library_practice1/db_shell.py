
# exec(open(r'G:\Learnings\practice_django\library_practice1\library_practice1\db_shell.py').read())

from app1.models import Book

obj = Book(name='test1', price=455, qty=15)
obj.save()