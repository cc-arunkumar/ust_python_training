class Book:

    book_id : int
    book_id (string, unique)
title (string)
authors (list of string)
isbn (string, unique)
tags (list of string)
total_copies (int)
available_copies (int)
Methods:
to_dict()
update(**kwargs)
is_available()
increase_copies(n)
decrease_copies(n)