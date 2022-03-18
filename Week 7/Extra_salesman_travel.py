# https://www.codewars.com/kata/56af1a20509ce5b9b000001e
# Level 6 kyu

# Directions:
# The function travel will take two parameters r (addresses' list of all clients' as a string) and zipcode and returns a string in the following format:
# zipcode:street and town,street and town,.../house number,house number,...
# The street numbers must be in the same order as the streets where they belong.
# If a given zipcode doesn't exist in the list of clients' addresses return "zipcode:/"
# Examples
# r = "123 Main Street St. Louisville OH 43071,432 Main Long Road St. Louisville OH 43071,786 High Street Pollocksville NY 56432"
# travel(r, "OH 43071") --> "OH 43071:Main Street St. Louisville,Main Long Road St. Louisville/123,432"
# travel(r, "NY 56432") --> "NY 56432:High Street Pollocksville/786"
# travel(r, "NY 5643") --> "NY 5643:/"
# Note for Elixir:
# In Elixir the empty addresses' input is an empty list, not an empty string.


# Function
def travel(r, zipcode):
    print(zipcode)
    # If zipcode given is not enough letters/numbers, is empty, or is not in provided addresses, it is invalid.
    if len(zipcode) < 8 or zipcode == '' or zipcode not in r:
        return f'{zipcode}:/'
    # Create list of addresses seperated by their commas.
    address_list: list = r.split(',')
    # Create empty list for storing addresses that are associated with zipcode.
    zip_code_list: list = []
    # Loop through each address...
    for address in address_list:
        # Store zip_code.
        zip_code = address[-8:]
        # If that zip_code matches the zipcode provided...
        if zip_code == zipcode:
            # Then add it to the zip_code_list.
            zip_code_list.append(address[:-9])
    # Create empty lists for storing address data.
    street_number_list: list = []
    street_address_list: list = []
    
    # Loop through the zip_code_list to build answer string.
    for address in zip_code_list:
        # Store address numbers
        number: int = address.split(' ')[0]
        street_number_list.append(number)
        # Store street names.
        street_address: str = address.replace(number, '')[1:]
        street_address_list.append(street_address)
    # Turn address data lists into strings.
    street_numbers: str = ','.join(street_number_list)
    street_addresses: str = ','.join(street_address_list)
        
    return f'{zipcode}:{street_addresses}/{street_numbers}'
    

# Test Cases
ad = ("123 Main Street St. Louisville OH 43071,432 Main Long Road St. Louisville OH 43071,786 High Street Pollocksville NY 56432,"
  "54 Holy Grail Street Niagara Town ZP 32908,3200 Main Rd. Bern AE 56210,1 Gordon St. Atlanta RE 13000,"
  "10 Pussy Cat Rd. Chicago EX 34342,10 Gordon St. Atlanta RE 13000,58 Gordon Road Atlanta RE 13000,"
  "22 Tokyo Av. Tedmondville SW 43098,674 Paris bd. Abbeville AA 45521,10 Surta Alley Goodtown GG 30654,"
  "45 Holy Grail Al. Niagara Town ZP 32908,320 Main Al. Bern AE 56210,14 Gordon Park Atlanta RE 13000,"
  "100 Pussy Cat Rd. Chicago EX 34342,2 Gordon St. Atlanta RE 13000,5 Gordon Road Atlanta RE 13000,"
  "2200 Tokyo Av. Tedmondville SW 43098,67 Paris St. Abbeville AA 45521,11 Surta Avenue Goodtown GG 30654,"
  "45 Holy Grail Al. Niagara Town ZP 32918,320 Main Al. Bern AE 56215,14 Gordon Park Atlanta RE 13200,"
  "100 Pussy Cat Rd. Chicago EX 34345,2 Gordon St. Atlanta RE 13222,5 Gordon Road Atlanta RE 13001,"
  "2200 Tokyo Av. Tedmondville SW 43198,67 Paris St. Abbeville AA 45522,11 Surta Avenue Goodville GG 30655,"
  "2222 Tokyo Av. Tedmondville SW 43198,670 Paris St. Abbeville AA 45522,114 Surta Avenue Goodville GG 30655,"
  "2 Holy Grail Street Niagara Town ZP 32908,3 Main Rd. Bern AE 56210,77 Gordon St. Atlanta RE 13000")


code = ("OH 43071,NY 56432,ZP 32908,AE 56210,RE 13000,EX 34342,SW 43098,AA 45521,GG 30654,ZP 32908,AE 56215,RE 13200,EX 34345,"
     "RE 13222,RE 13001,SW 43198,AA 45522,GG 30655,XX 32321,YY 45098")

def testing(actual, expected):
    test.assert_equals(actual, expected)

test.describe("travel")
test.it("Basic tests")
testing(travel(ad, "AA 45522"), "AA 45522:Paris St. Abbeville,Paris St. Abbeville/67,670")
testing(travel(ad, "EX 34342"), "EX 34342:Pussy Cat Rd. Chicago,Pussy Cat Rd. Chicago/10,100")
testing(travel(ad, "EX 34345"), "EX 34345:Pussy Cat Rd. Chicago/100")
testing(travel(ad, "AA 45521"), "AA 45521:Paris bd. Abbeville,Paris St. Abbeville/674,67")
testing(travel(ad, "AE 56215"), "AE 56215:Main Al. Bern/320")



