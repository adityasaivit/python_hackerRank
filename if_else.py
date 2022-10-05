#!/bin/python3

import math
import os
import random
import re
import sys


a=int(input())
if ((a>=1)&(a<=100)):
        if(a%2==0):
                if((a>=6)&(a<=20)):
                        print("Weird")
                else:
                        print("Not Weird")
                
        else:
                print("Weird")
