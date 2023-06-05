# using this way because it is officially supported. See https://pip.pypa.io/en/stable/user_guide/#using-pip-from-your-program

import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    
# beautiful soup 4 to work with htmls
install("beautifulsoup4")

# beautiful soup 4 to generate with http responses
install("requests")