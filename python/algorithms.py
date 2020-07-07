
def len(iterable):
    return sum(1 for x in iterable)

def count(iterable, element):
    return sum(1 for x in iterable if x == element)

def count_if(iterable, predicate):
    return sum(1 for x in iterable if predicate(x))
