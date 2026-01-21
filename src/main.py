import argparse
import os

import gkeepapi
import keyring
from decouple import config


def run_task(title='Title', text="Text"):
    try:
        columns = os.get_terminal_size().columns
    except OSError:
        columns = 80  # Default fallback width

    print("" * columns)
    email = config("MAIN_MAIL")
    print("", email)
    print("", title if title != "" else "No title")
    print("" * columns)
    print(text)
    print("" * columns)
    try:
        keep = gkeepapi.Keep()
        authenticate(email, keep)
        note = keep.createNote(title=title, text=text)
        note.pinned = True
        # note.color = gkeepapi.node.ColorValue.Red
        keep.sync()
        print(" Note synced ")
    except Exception as e:
        print(e)
        print(" Error in note creation ")


def authenticate(email, keep):
    # Prioritize keyring for security
    master_token = keyring.get_password("google-keep-token", "main_email")

    keep.authenticate(email, master_token)
    # if login_response:
    #     print(' Login successful ')
    # else:
    #     print(login_response)
    #     raise Exception("Authentication failed")


def argument_parser() -> tuple[str, str]:
    # Command line arguments options
    try:
        parser = argparse.ArgumentParser(description='Add new note to Google Keep.')
        parser.add_argument('text',
                            action='store',
                            nargs='+',
                            type=str, help='The text to parse.')
        parser.add_argument('-tt', '--title',
                            required=False,
                            type=str,
                            default="",
                            dest="title",
                            nargs='+',
                            metavar="<note title>",
                            help="Title of the new note")
        args = parser.parse_args()
        text = title = ""
        try:
            text = " ".join(args.text)
        except:
            pass
        try:
            title = " ".join(args.title)
        except:
            pass

    except Exception as err:
        # output error, and exit
        print(str(err))
        exit()
    return text, title


def main():
    import sys
    if len(sys.argv) == 1 and os.environ.get('PYCHARM_HOSTED'):
        text, title = 'Hello World', 'Test Note'
    else:
        text, title = argument_parser()
    # Execute function
    run_task(title=title, text=text)


if __name__ == "__main__":
    main()
