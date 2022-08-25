#!/usr/bin/python3

import sys
import tkinter
import pyperclip


QUERY_TEMPLATE = "https://letmegooglethat.com/?q={QUERY}"
VERSION = "0.1"

def show_help() -> None:
    """Shows CLI program help message
    """

    print(f"""Usage: {sys.argv[0]}: [OPTIONS] | <query>

[-h | --help]               Shows this message
[-g | --gui]                Make this program use GUI version
[-v | --version]            Shows the version
<query>                     Your query to copy to your clipboard
""")



def gui_main() -> None:
    """GUI version of the program
    """

    root = tkinter.Tk()
    root.geometry("400x100")
    root.configure(background="white")
    root.resizable(width=False, height=False)

    label = tkinter.Label(root, text="Enter your query")
    label.pack()

    query_box = tkinter.Text(root, height=2, width=70)
    query_box.pack()

    copy_query_button = tkinter.Button(
        root,
        text="Copy query to clipboard",
        command=pyperclip.copy(query_box.get("1.0", "end-1c"))
    )
    copy_query_button.pack()

    root.mainloop()


if len(sys.argv) == 1:
    show_help()
    sys.exit(0)

if len(sys.argv) == 2:
    match sys.argv[1]:
        case "-h" | "--help":
            show_help()
            sys.exit(0)
        case "-g" | "--gui":
            gui_main()
            sys.exit(0)
        case "-v" | "--version":
            print(f"LetMeGoogleThat.PY v{VERSION}\n")
            sys.exit(0)
        case _:
            pass


# sys.argv[0] is script name so I don't take it
query_search = '+'.join(sys.argv[1:])
url = QUERY_TEMPLATE.format(QUERY=query_search)

pyperclip.copy(url)

