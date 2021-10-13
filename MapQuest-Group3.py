import urllib.parse
import requests
from tkinter import *
from tkinter import ttk, filedialog, messagebox, _tkinter
from tkinter.scrolledtext import *

main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "mNYWrQQHE28GXaWeFNWnG7r6yXABk5iW"

root = Tk()
root.title('Map Quest Mod (Group 3 - 4ITH)')
# try:
# https://www.flaticon.com/free-icon/document_888034?term=document&page=1&position=2&page=1&position=2&related_id=888034&origin=search
# root.iconbitmap('document.ico')
# except _tkinter.TclError as e:
#     messagebox.showinfo(
#         title='Error', message=f'App Icon not found: {e}', icon='warning')
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
root.geometry(
    f'{appWidth}x{appHeight}+{int(screenWidth/2-appWidth/2)}+{int(screenHeight/2-appHeight/2)}')
frame1 = Frame(root)
frame1.pack(padx=10, pady=10)
frame2 = Frame(root)
frame2.pack(padx=10, pady=10)
frame3 = Frame(root)
frame3.pack(padx=10, pady=10)

framelast = Frame(root)
framelast.pack(padx=10, pady=10)


def closeProgram():
    if messagebox.askokcancel("Closing Program", "Click OK to close the program."):
        root.destroy()


def sumite():
    start = (startText.get("1.0", "end")).strip()
    des = (desText.get("1.0", "end")).strip()
    url = main_api + \
        urllib.parse.urlencode({"key": key, "from": start, "to": des})
    print("URL: " + (url))
    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]
    output = ''

    if json_status == 0:
        output += "API Status: " + \
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
            output += "\n=============================================\n"
    elif json_status == 402:
        output += "**********************************************\n"
        output += "Status Code: " + \
            str(json_status) + "; Invalid user inputs for one or both locations.\n"
        output += "**********************************************\n"
    elif json_status == 611:
        output += "**********************************************\n"
        output += "Status Code: " + \
            str(json_status) + "; Missing an entry for one or both locations.\n"
        output += "**********************************************\n"
    else:
        output += "************************************************************************\n"
        output += "For Staus Code: " + str(json_status) + "; Refer to:\n"
        output += "https://developer.mapquest.com/documentation/directions-api/status-codes\n"
        output += "************************************************************************\n"
    displayedFile.configure(state='normal')
    displayedFile.delete(1.0, END)
    displayedFile.insert(END, output)
    displayedFile.configure(state='disabled')


startLabel = ttk.Label(frame1, text='Starting Location: ')
startLabel.pack(padx=5, side=LEFT)
startText = Text(frame1, height=1, width=100, font=('Raleway', 12))
startText.pack(padx=5, side=LEFT)

desLabel = ttk.Label(frame2, text='Destination: ')
desLabel.pack(padx=5, side=LEFT)
desText = Text(frame2, height=1, width=100, font=('Raleway', 12))
desText.pack(padx=5, side=LEFT)

btnRemoveFile = ttk.Button(
    frame3, text='Submit', command=sumite, width=90, style='all.TButton')
# btnRemoveFile.configure(state='disabled')
btnRemoveFile.pack(padx=5, pady=5, side=LEFT)


displayedFile = ScrolledText(
    framelast, height=30, width=100, font=('Raleway', 12))
displayedFile.configure(state='disabled')
displayedFile.pack(padx=5, pady=10, side=LEFT)

# while True:
#     orig = input("Starting Location: ")
#     if orig == "quit" or orig == "q":
#         break
#     dest = input("Destination: ")
#     if dest == "quit" or dest == "q":
#         break
#     url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest})
#     print("URL: " + (url))
#     json_data = requests.get(url).json()
#     json_status = json_data["info"]["statuscode"]
#     if json_status == 0:
#         print("API Status: " + str(json_status) + " = A successful route call.\n")
#         print("=============================================")
#         print("Directions from " + (orig) + " to " + (dest))
#         print("Trip Duration: " + (json_data["route"]["formattedTime"]))
#         print("Kilometers: " + str("{:.2f}".format((json_data["route"]["distance"])*1.61)))
#         print("Fuel Used (Ltr): " + str("{:.2f}".format((json_data["route"]["fuelUsed"])*3.78)))
#         print("=============================================")
#         for each in json_data["route"]["legs"][0]["maneuvers"]:
#             print((each["narrative"]) + " (" + str("{:.2f}".format((each["distance"])*1.61) + " km)"))
#             print("=============================================\n")
#     elif json_status == 402:
#         print("**********************************************")
#         print("Status Code: " + str(json_status) + "; Invalid user inputs for one or both locations.")
#         print("**********************************************\n")
#     elif json_status == 611:
#         print("**********************************************")
#         print("Status Code: " + str(json_status) + "; Missing an entry for one or both locations.")
#         print("**********************************************\n")
#     else:
#         print("************************************************************************")
#         print("For Staus Code: " + str(json_status) + "; Refer to:")
#         print("https://developer.mapquest.com/documentation/directions-api/status-codes")
#         print("************************************************************************\n")


root.protocol("WM_DELETE_WINDOW", closeProgram)

root.mainloop()
