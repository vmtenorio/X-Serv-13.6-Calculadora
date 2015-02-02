#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Script de comprobación de entrega de ejercicio

Para ejecutarlo, desde la shell:
 $ python check.py login_github

"""

import os
import random
import sys

ejercicio = 'X-Serv-13.6-Calculadora'

files = ['calculadora.py',
         'check.py',
         'README.md',
         '.gitignore',
         '.git']

if len(sys.argv) != 2:
    print
    sys.exit("Usage: $ python check.py login_github")

repo_git = "http://github.com/" + sys.argv[1] + "/" + ejercicio


aleatorio = str(int(random.random() * 1000000))

error = 0

print
print "Clonando el repositorio " + repo_git + "\n"
os.system('git clone ' + repo_git + ' /tmp/' + aleatorio + ' > /dev/null 2>&1')
try:
    student_file_list = os.listdir('/tmp/' + aleatorio)
except OSError:
    error = 1
    print "Error: No se ha podido acceder al repositorio " + repo_git + "."
    print
    sys.exit()

if len(student_file_list) != len(files):
    error = 1
    print "Error: número de ficheros en el repositorio incorrecto"

for filename in files:
    if filename not in student_file_list:
        error = 1
        print "\tError: " + filename + " no encontrado en el repositorio."

if not error:
    print "Parece que la entrega se ha realizado bien."
print
