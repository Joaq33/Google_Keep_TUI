# Google Keep: Notes from Terminal  
Quickly create notes without leaving your terminal  

## Requirements
Python modules required:
- gkeepapi
- python-decouple
- keyring
- requests

## Quickstart
1. Create a `.env` file with your primary account:
   ```env
   MAIN_MAIL='YOUR_GMAIL@gmail.com'
   ```
2. Set up your Google Keep master token in the system keyring:
   ```python
   import keyring
   keyring.set_password("google-keep-token", "main_email", "YOUR_MASTER_TOKEN")
   ```
   *Note: You can obtain a master token using `gkeepapi` utilities or by following their documentation.*

## Tips
- Create an alias for quick access using `uv`:
  `alias k='uv run $WORKSPACE/src/main.py'`
  where `WORKSPACE` is the absolute path to the repository.
  Now you can create notes using: `k "note content"`

## Usage

```  
positional arguments:  
  text                  The text to parse.  
  
optional arguments:  
  -h || --help          Show help message and exit  
  -tt || --title        Title of the new note  
```

### TODO
- Improve installation (pipx, make or other)
- Parallelize sync
- Use Rich library for better UI
- Add more note customization options (colors, labels)