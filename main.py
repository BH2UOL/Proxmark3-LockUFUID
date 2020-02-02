# -*- coding: utf-8 -*-
# @Time : 2020/2/2
# @Author : Angel
# @File : main.py

import subprocess, os

os.system("clear")
pm3 = subprocess.Popen("/usr/local/bin/proxmark3 /dev/cu.usbmodemiceman1", shell=True, stdout=subprocess.PIPE,stdin=subprocess.PIPE,stderr=subprocess.PIPE)
pm3.stdin.write('hf 14a raw -p -a -b 7 40 \n')
pm3.stdin.write('hf 14a raw -p -a 43 \n')
pm3.stdin.write('hf 14a raw -p -a e0 00 39 f7 \n')
pm3.stdin.write('hf 14a raw -p -a e1 00 e1 ee \n')
pm3.stdin.write('hf 14a raw -p -a 85 00 00 00 00 00 00 00 00 00 00 00 00 00 00 08 18 47 \n')
out = pm3.communicate()[0]
