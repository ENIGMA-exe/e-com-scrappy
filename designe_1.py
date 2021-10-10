from colorama import init,Fore,Back
from subprocess import call
init(convert=True)

class bcolors:
    CYAN = '\033[96m'
    PURPLE = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    ENDC = '\033[0m'

    def disable(self):
        self.CYAN = ''
        self.PURPLE = ''
        self.BLUE = ''
        self.GREEN = ''
        self.RED = ''
        self.BOLD = ''
        self.YELLOW = ''
        self.ENDC = ''

def logo():
    print(" ")
    print(bcolors.GREEN +"            O               O"+ bcolors.ENDC)
    print(bcolors.GREEN +"             \             /"+ bcolors.ENDC)
    print(bcolors.GREEN +"              \___________/"+ bcolors.ENDC)
    print(bcolors.GREEN +"              //----------\ "+ bcolors.ENDC)
    print(bcolors.GREEN +"             //||          \ "+ bcolors.ENDC)
    print(bcolors.GREEN +"       O_.__// ||___  ___   \_________________"+ bcolors.ENDC)
    print(bcolors.GREEN +"            \  ||---\||_// Nzen  Automation   |"+ bcolors.ENDC)
    print(bcolors.GREEN +"             \ ||___/||___ ___________________|"+ bcolors.ENDC)
    print(bcolors.GREEN +"              \__________//"+ bcolors.ENDC)
    print(bcolors.GREEN +"              /           \ "+ bcolors.ENDC)
    print(bcolors.GREEN +"             /             \ "+ bcolors.ENDC)
    print(bcolors.GREEN +"            O               O"+ bcolors.ENDC)
    print(" ")

def options():
    print(" BEnzen script scraps the details of your data from following sites:-")
    print(" ")
    print(bcolors.YELLOW + bcolors.BOLD+"  [1]Amazon.in                     [2]Flipkart"+ bcolors.ENDC)
    print(bcolors.YELLOW + bcolors.BOLD+"  [3]Snapdeal                      [4]Alibaba."+ bcolors.ENDC)
    print(bcolors.YELLOW + bcolors.BOLD+"  [5]Ebay India.                   [6]Jabong."+ bcolors.ENDC)
    print(bcolors.YELLOW + bcolors.BOLD+"  [7]Shopclues."+ bcolors.ENDC)

def syp():
    print(bcolors.BLUE+bcolors.BOLD+"           ______________________________"+ bcolors.ENDC)
    print(bcolors.BLUE+bcolors.BOLD+"          |                              |"+ bcolors.ENDC)
    print(bcolors.BLUE+bcolors.BOLD+"          |       WRITE YOUR PRODUCT     |"+ bcolors.ENDC)
    print(bcolors.BLUE+bcolors.BOLD+"          |______________________________|"+ bcolors.ENDC)
    print("  ")



logo()
options()
syp()

# product = input()

class callPy(object):

    def __init__(self, path_1='amazon_scrp.py', path_2='flipkart_scrp.py', path_3='ebay_scrp.py'):
        self.path_1 = path_1
        self.path_2 = path_2
        self.path_3 = path_3 

    # def __init__(self,path_2 = 'flipkart_scrp.py'):
    #     self.path_2 = path_2

    # def __init__(self,path_3 = 'ebay_scrp.py'):
    #     self.path_3 = path_3    

    def call_python_file(self):
        call(["python","{}".format(self.path_1)])
        call(["python","{}".format(self.path_2)])
        call(["python","{}".format(self.path_3)])


if __name__ == "__main__":
    c = callPy()
    c.call_python_file()