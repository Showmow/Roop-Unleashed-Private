import sys
import os

# Add the root project folder to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '')))

from roop import core

if __name__ == '__main__':
    core.run()
