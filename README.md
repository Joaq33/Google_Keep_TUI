# Google Keep: Notes from Terminal  
Quickly create notes without leaving your terminal  

## Requirements
`An auxiliar gmail account is required to create the notes and share them to the main account`\
Python modules required:
- gkeepapi
- python-decouple
- requests

## Quickstart
create `.env` file with your configured values:
````
AUX_MAIL='YOUR_AUXILIAR_GMAIL@gmail.com'  
AUX_MAIL_PASS='YOUR_AUXILIAR_GMAIL_PASSWORD'  
MAIN_MAIL='YOUR_GMAIL@gmail.com'
````

## Tips  
- create an alias for quick access like this:\  
``alias k='. $WORKSPACE/venv/bin/activate && python $WORKSPACE/src/main.py'``\  
where WORKSPACE environment variable is your absolute path. \  
Now you can create notes just using ``k note content``  

````  
positional arguments:  
  text                  The text to parse.  
  
optional arguments:  
  -h || --help          Show help message and exit  
  -tt || --title        Title of the new note  
````

### TODO
- improve installation (pipx, make or other)
- paralellize sync
- use Rich library for better ui
- improve authentication