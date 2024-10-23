import os,sys,platform,time
Lija = platform.architecture()[0]
if Lija == '64bit':import LMNxDEX_FILE
elif Lija == '32bit':
    os.system("clear")
    os.system('xdg-open https://t.me/TEAM_LMNx9')
    time.sleep(3)
    sys.exit("\n</> Your Device Is Not Supported For Run This Tool..!")
else:
    os.system("clear")
    sys.exit("\n</> Something Went Wrong..! Try Again")
    
