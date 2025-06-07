# Created as a part of BAIL on 02/09

"""
? What are API's?
Application Programming Interface

- API is a set of commands, functions, protocols, and objects that programmers can use to create software or interact with an external system.
- The focus on this section is to interact with the external system. Creation of software will be discussed in a future Instructional.
- Your program or code needs to function accordingly to a set of rules created by the external system in order to get an appropriate response.

Imagine the websites as a sort of 'restaurant'. The data that powers the websites could be the 'kitchen'. You can't go straight to the 'kitchen' and start making your own food or messing around.
There is a 'menu' (like an interface between you and the 'kitchen'). It is a list of items that you can interact with and 'order' to properly interact with the 'kitchen' based on their set of rules.
This is similiar to how an API works, where there is a set of data or programs that you or your programs might need access to. However, in order to access it -
your code needs to abide by a certain set of rules in order to access that data or program.

? API Endpoint
- Important aspect of API's
- Imagine this as a location of where that external service or data is stored
- Usually in the form of a url (like api.coinbase.com, this is the location where coinbase data can be found)

Imagine this as a street address for the restaurant that you wish to visit. It's usually available with a simple google search, or searching through dev docs.

? API Request
- You must also make a specific request from the API endpoint
- Based on the type of request made, some authentication might be required

Imagine this request as a sort of bank where you wish to withdraw some money. The 'money' in this case can be the data that you wish to 'withdraw'.
Approaching the 'teller' at the bank and asking to 'withdraw' would be akin to making an API call or a simple GET request, where you wish to GET some info from the source of data.
There is some information where there is no authentication required to GET the info, such as asking the 'teller' the 'opening hours'...
But 'withdrawing' your 'money' would require authentication.

? Output
- The output of these API endpoints is usually in JSON format.
- JSON files are simple to transfer over the internet and can be recreated to a readable/easily viewable format once received in your program
"""

# Example of a simple API call below.
# This will result in a response code from the list below

"""
? Response Codes General Format -- More details available at : https://httpstatuses.io/
1XX - Informational
2XX - Success
3XX - Redirection
4XX - Client Error
5XX - Server Error
"""

import requests

# The below makes one API call to the URL and places it into a variable
response = requests.get(url="http://api.open-notify.org/iss-now.json")

# If there is an error in the url, or a server issue, or any other response that does not result in a successful API call, the method below will raise an exception. It's a catch all.
response.raise_for_status()

# The below will return the json formatted response and place it into a variable for processing
data = response.json()

# The below pulls in specific information requested from the JSON (Latitude and Longitude)
latitude = data["iss_position"]["latitude"]
longitude = data["iss_position"]["longitude"]
iss_position = (longitude, latitude)

print(iss_position)
