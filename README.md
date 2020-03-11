# BatchTranslatorWithPY
A batch translator using python , which can translate a column string to other columns in excel

To use this tool, you need to have a Microsoft Azure account (https://portal.azure.com/)

Language support:

This script only identified English, Chinese(zh-CN), Russian, Thai, Korean, Japanese.
You can modify the script to add more languages as long as Microsoft supports them(modify LanguagePostfix.py).

Steps to use this script:

1. Prepare your secret token for Azure translation service.
2. Prepare your translation texts in an excel file. 
   The column which needs to be translated marked as RED (FFFF0000)
   The columns you want to translate should be named as the RED title + "_" + LanguagePostfix
   See sample.xlsx for reference.
3. Run the script, input the azure token and the excel file, it will go to Azure, translate them, output to the excel file and save.

Future Plan of this script:
Add google translate support


Dependency:

Python version:
Python3

pip3 install openpyxl
pip3 install requests


