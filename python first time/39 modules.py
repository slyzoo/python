#module = a file containing python code. may contain functions, classes, etc.
#used with modular programming, which is to seperate a program into parts


import messages

import messages as msg

from messages import hello, bye, fuckyou


messages.hello()

messages.bye()

messages.fuckyou()


msg.hello()

msg.bye()

msg.fuckyou()


#this names all the modules
help("modules")
