from idlelib.debugger_r import codetable

first = 'Vineesh'
last = 'Chauhan'
msg = first + '[ '+last+ '] is a coder'
print(msg)
msg = f'{first} [{last}] is a coder'
print(msg)

print(len(msg))

print(msg.upper())
# function are general purpose like len() function above.
# functions specific to one class are called methods.
print(msg.find('i'))


print('coder' in msg)