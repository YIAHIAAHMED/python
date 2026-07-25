# function is a first class object 
def double_decker():
    print('starting the double')

    def inner_fun():
        print('inside the inner')
        return 3000
    return inner_fun
    
# print(double_decker())
# print(double_decker()())

def do_something(work):
    print('work started')
    #print(work)
    work() # jodi function patai tahole erokom
    print('work ended')

# do_something(2)
# do_something('ami busy')

# function o dite pari
def coding():
    print('coding in')

# do_something(coding)

def sleeping():
    print('sleeeing and ')

do_something(sleeping)