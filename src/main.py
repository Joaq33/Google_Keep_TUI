import argparse
import os

import gkeepapi
from decouple import config


def run_task(title='Title', text="Text"):
    print("" * os.get_terminal_size().columns)
    auxmail = config("AUX_MAIL")
    collaborator = config("MAIN_MAIL", default = "")
    print("", auxmail)
    print("", "Collaborator:", collaborator)
    print("", title if title != "" else "No title")
    print("" * os.get_terminal_size().columns)
    print(text)
    print("" * os.get_terminal_size().columns)
    try:
        keep = gkeepapi.Keep()
        success = keep.login(auxmail, config("AUX_MAIL_PASS"))

        note = keep.createNote(title=title, text=text)
        note.pinned = False
        # note.color = gkeepapi.node.ColorValue.Red
        note.collaborators.add(collaborator)
        keep.sync()
        print(" Note synced ")
    except Exception as e:
        print(e)
        print(" Error in note creation ")


def argument_parser() -> tuple[str,str]:
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
    text, title = argument_parser()

    # Execute function
    run_task(title=title, text=text)


if __name__ == "__main__":
    main()
