# FiletoContacts_Converter
Converts filenames of the specific format ```YYYY-MM-DD - Last Name, First Name``` into entries in a csv file for importting into Microsoft Outlook Contacts.

### Purpose
The purpose of this application is to save the time of manually entering contact info into Microsoft Outlook Contacts by parsing the contacts' names from their respective files. A list of names (First, Middle, Last) will be put in a csv file with the date being added to the notes section.

### Usage
Place the executable script ```convert_contacts.exe``` into the directory containing the directories numbered by year (ex. 2011, 2014). Run the executable and input a starting year and ending year to convert across.

A ```generated_contacts.csv``` file will appear in the same directory as the script.

Note: 
- The ouputted file will overwrite a file of the same name if it exists.
- Filenames not in the form ```YYYY``` or within the inputted range will be ignored.

### Building
Manually build the script as an executable using pyinstaller and the line:
```
pyinstaller --onefile convert_contacts.py
```

---
### Technologies:
#### [pandas](https://pandas.pydata.org/)
#### [pyinstaller](https://www.pyinstaller.org/)
#### [Travis CI](https://www.travis-ci.com/)
