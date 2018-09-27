from platform import uname as name
from getpass import getuser as user
from datetime import datetime as time
#}
def login(stat):

    file = open('log.txt','a')
    file.write('-> '+stat+' from '+name()[1]+' host '+user()+' user'+' on '+name()[0]+name()[2]+name()[4]+' os at '+str(time.now())+'\n')
    file.close()
