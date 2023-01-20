import argparse
import os

import gkeepapi
from decouple import config


def run_task(title='Title', text="Text"):
    print("" * os.get_terminal_size().columns)
    mail = config("MAIL")
    print("", mail)
    print("", title if title != "" else "No title")
    print("" * os.get_terminal_size().columns)
    print(text)
    print("" * os.get_terminal_size().columns)
    try:
        keep = gkeepapi.Keep()
        success = keep.login(mail, config("PASS"))

        note = keep.createNote(title=title, text=text)
        note.pinned = True
        note.color = gkeepapi.node.ColorValue.Red
        keep.sync()
        print(" Note synced ")
    except Exception as e:
        print(e)
        print(" Error in note creation ")


if __name__ == "__main__":
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
        # output error, and return with an error code
        print(str(err))
    else:
        # Execute function
        run_task(title=title, text=text)
