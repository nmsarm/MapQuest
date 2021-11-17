import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
key = "mNYWrQQHE28GXaWeFNWnG7r6yXABk5iW"
# data = {'distance': 'Kilometers', 'fuel': 'Liters'}


def fetchData(start, des, distance, fuel):
    # print(type(start))
    # print(type(des))
    # print(type(distance))
    # print(type(fuel))
    url = main_api + \
        urllib.parse.urlencode({"key": key, "from": start, "to": des})
    # print("URL: " + (url))
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

        if distance == "Miles":
            # data['distance'] = distance
            output += "\nMiles: " + \
                str("{:.2f}".format((json_data["route"]["distance"])))
        else:
            output += "\nKilometers: " + \
                str("{:.2f}".format((json_data["route"]["distance"])*1.61))

        if fuel == 'Gallons':
            # data['fuel'] = fuel
            output += "\nFuel Used (Gal): " + \
                str("{:.2f}".format(json_data["route"]["fuelUsed"]))
            output += "\n=============================================\n"
        else:
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
        output += "For Status Code: " + str(json_status) + "; Refer to:\n"
        output += "https://developer.mapquest.com/documentation/directions-api/status-codes\n"
        output += "************************************************************************\n"
    return output
