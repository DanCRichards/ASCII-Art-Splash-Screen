import random
import os
i = random.randrange(10)
i = 1 #Putting to one at the moment, as there is only 1 art file on the page
website="https://raw.githubusercontent.com/DanCRichards/ASCII-Art-Splash-Screen/master/art/"+ str(i) + ".txt"
os.system("curl " +  website)
