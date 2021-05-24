# FiletoContacts_Converter
Converts filenames of the specific format ```YYYY-MM-DD - Last Name, First Name``` into entries in a csv file for importting into Microsoft Outlook Contacts.

### Usage
Place the executable script ```convert_contacts.exe``` into the directory containing the directories numbered by year (ex. 2011, 2014). Run the executable and input a starting year and ending year to convert across.

A ```generated_contacts.csv``` file will appear in the same direcetory as the script.

Note: The ouputted file will overwrite a file of the same name if it exists.

### Building
Build the script as an executable using pyinstaller and the line:
```
pyinstaller --onefile convert_contacts.py
```
