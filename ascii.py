import random
import os
i = random.randrange(8) + 1 
website="https://raw.githubusercontent.com/DanCRichards/ASCII-Art-Splash-Screen/master/art/"+ str(i) + ".txt"
os.system("curl " +  website)
