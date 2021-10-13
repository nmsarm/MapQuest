# from original code
import urllib.parse
import requests
# gui and styling module
from tkinter import *
from tkinter import ttk, filedialog, messagebox, _tkinter
from tkinter.scrolledtext import *

# from original code
main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "mNYWrQQHE28GXaWeFNWnG7r6yXABk5iW"

# creating window
root = Tk()
root.title('Map Quest Mod (Group 3 - 4ITH)')
# initializing style -> button and label style
style = ttk.Style(root)
style.configure('all.TButton', font=('Raleway', 12),
                foreground='#4A6FA5', background='#4A6FA5')
style.configure('all.TLabel', font=('Raleway', 12),
                background='#333', foreground='#fff', padding=2)
# screen size
screenWidth = root.winfo_screenwidth()
screenHeight = root.winfo_screenheight()
# The standard resolution used today is 1024x768.
appWidth = 900
appHeight = 750
# sets window in the middle of the screen
root.geometry(
    f'{appWidth}x{appHeight}+{int(screenWidth/2-appWidth/2)}+{int(screenHeight/2-appHeight/2)}')
# frames as rows of the window
frame1 = Frame(root)
frame1.pack(padx=10, pady=10)
frame2 = Frame(root)
frame2.pack(padx=10, pady=10)
frame3 = Frame(root)
frame3.pack(padx=10, pady=10)
frame4 = Frame(root)
frame4.pack(padx=10, pady=10)
framelast = Frame(root)
framelast.pack(padx=10, pady=10)

# function for reset button


def clearFields():
    startText.delete("1.0", "end")
    desText.delete("1.0", "end")
    displayOutput.configure(state='normal')
    displayOutput.delete(1.0, END)
    displayOutput.configure(state='disabled')

# function for closing the program


def closeProgram():
    if messagebox.askokcancel("Closing Program", "Click OK to close the program."):
        root.destroy()

# function for submit button


def sumite():
    # gets starting loc and destination from text boxes and strips white spaces
    start = (startText.get("1.0", "end")).strip()
    des = (desText.get("1.0", "end")).strip()
    # uses mapquest api to get the data - from original code - modified to fit code structure
    url = main_api + \
        urllib.parse.urlencode({"key": key, "from": start, "to": des})
    print("URL: " + (url))
    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]
    # output stores the string to be displayed in the text area
    output = "URL: " + (url)
    if json_status == 0:  # meaning the request was successful
        output += "\n\nAPI Status: " + \
            str(json_status) + " = A successful route call.\n"
        output += "=============================================\n"
        output += "Directions from " + (start) + " to " + (des)
        output += "\nTrip Duration: " + (json_data["route"]["formattedTime"])
        output += "\nKilometers: " + \
            str("{:.2f}".format((json_data["route"]["distance"])*1.61))
        output += "\nFuel Used (Ltr): " + \
            str("{:.2f}".format((json_data["route"]["fuelUsed"])*3.78))
        output += "\n=============================================\n"
        for each in json_data["route"]["legs"][0]["maneuvers"]:
            output += (each["narrative"]) + " (" + \
                str("{:.2f}".format((each["distance"])*1.61) + " km)")
            output += "\n\n"
    elif json_status == 402:  # meaning the input(s) was/were invalid
        output += "**********************************************\n"
        output += "Status Code: " + \
            str(json_status) + "; Invalid user inputs for one or both locations.\n"
        output += "**********************************************\n"
    elif json_status == 611:  # meaning there is/are missing inputs
        output += "**********************************************\n"
        output += "Status Code: " + \
            str(json_status) + "; Missing an entry for one or both locations.\n"
        output += "**********************************************\n"
    else:  # to handle other errors
        output += "************************************************************************\n"
        output += "For Staus Code: " + str(json_status) + "; Refer to:\n"
        output += "https://developer.mapquest.com/documentation/directions-api/status-codes\n"
        output += "************************************************************************\n"
    # displaying the output text to the text area
    displayOutput.configure(state='normal')
    displayOutput.delete(1.0, END)
    displayOutput.insert(END, output)
    displayOutput.configure(state='disabled')


# creating and embedding the header title
titleLabel = ttk.Label(frame1, text='MapQuest - Group 3', font=('Raleway', 20))
titleLabel.pack(padx=5, side=LEFT)
# creating and embedding the start location label and text box
startLabel = ttk.Label(frame2, text='Starting Location: ')
startLabel.pack(padx=5, side=LEFT)
startText = Text(frame2, height=1, width=100, font=('Raleway', 12))
startText.pack(padx=5, side=LEFT)
# creating and embedding the destination location label and text box
desLabel = ttk.Label(frame3, text='Destination: ')
desLabel.pack(padx=5, side=LEFT)
desText = Text(frame3, height=1, width=100, font=('Raleway', 12))
desText.pack(padx=5, side=LEFT)
# creating and embedding the submit and reset buttons
btnSubmit = ttk.Button(
    frame4, text='Submit', command=sumite, width=50, style='all.TButton')
btnSubmit.pack(padx=5, pady=5, side=LEFT)
btnReset = ttk.Button(
    frame4, text='Reset', command=clearFields, width=50, style='all.TButton')
btnReset.pack(padx=5, pady=5, side=LEFT)
# creating and embedding the display text area
displayOutput = ScrolledText(
    framelast, height=30, width=100, font=('Raleway', 12))
displayOutput.configure(state='disabled')
displayOutput.pack(padx=5, pady=10, side=LEFT)
# close handler of the application
root.protocol("WM_DELETE_WINDOW", closeProgram)
# render the window
root.mainloop()
