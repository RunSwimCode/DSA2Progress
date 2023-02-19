# Amy Couture WGU ID: 786932

import csv
import math
import datetime


totalDistance = 0
# Here is Section A and the sample set of steps:
# A) Package data steps:
# 1-Create HashTable data structure (See C950 - Webinar-1 - Let’s Go Hashing webinar)
# 2-Create Package and Truck objects and have packageCSV and distanceCSV and addressCSV files ready
# 3-Create loadPackageData(HashTable) to
# - read packages from packageCSV file (see C950 - Webinar-2 - Getting Greedy, who moved my data  webinar)
# - update Package object
# - insert Package object into HashTable with the key=PackageID and Item=Package



#A1

# Here is the basic data structure for a chaining hash table from video #1
class ChainingHashTable:
    # Constructor with "optional initial capacity parameter"
    # so, you can decide how big the capacity will be to start with
    # This will assign buckets with an empty list
    def __init__(self, initial_capacity=10):
        # initialize the hash table with empty bucket list entries.
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])

    # This method inserts a new item into the hash table (does both insert and update) from Video 1
    def insert(self, key, value):
        # get the bucket list where this item will go.
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # update key if it is already in the bucket
        for kv in bucket_list:
            # print (key_value)
            if kv[0] == key:
                kv[1] = value
                return True

        # if not, insert the item to the end of the bucket list.
        key_value = [key, value]
        bucket_list.append(key_value)
        return True

    # Searches for an item with matching key in the hash table.
    # Returns the item if found, or None if not found.
    def search(self, pID):
        # get the bucket list where this key would be.
        bucket = hash(pID) % len(self.table)
        bucket_list = self.table[bucket]
        # print(bucket_list)

        # to search for the key value in the bucket list
        for kv in bucket_list:
            if kv[0] == pID:
                return kv[1]  # value
        return None

    # Removes an item with matching key from the hash table.
    def remove(self, key):
        # get the bucket list where this item will be removed from.
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # remove the item from the bucket list if it is present.
        for kv in bucket_list:
            # print (key_value)
            if kv[0] == key:
                bucket_list.remove(kv)

    # Hash table instance


packageHash = ChainingHashTable(10)

# A2: Create Package and Truck objects and have packageCSV and distanceCSV and addressCSV files ready
class Package:
    def __init__(self, pID, pAddress, pCity, pState, pZip, pDeadline, pMass, pSpecialNotes):
        self.pID = pID
        self.pAddress = pAddress
        self.pCity = pCity
        self.pState = pState
        self.pZip = pZip
        self.pDeadline = pDeadline
        self.pMass = pMass
        self.pSpecialNotes = pSpecialNotes

    # I need this to be able to return the strings
    def __str__(self):
        return (
            f'ID: {self.pID}, Address: {self.pAddress}, City: \
    {self.pCity}, '
            f'State: {self.pState}, Zip: {self.pZip}, Deadline: \
    {self.pDeadline}, '
            f'Mass: {self.pMass}, Special Notes: {self.pSpecialNotes}'
        )


class Truck:
    def __init__(self):
        self.deliveries = []
        self.delivery_time = None
        self.miles_driven = 0

    def add_delivery(self, address, distance):
        self.deliveries.append([address, distance])
        self.miles_driven += distance
        self.delivery_time = datetime.datetime.now()
        global totalDistance
        totalDistance += distance


# This creates an instance of the Truck class, "Truck 1"
truck1 = Truck()

# This creates an instance of the Truck class, "Truck 2"
truck2 = Truck()

# This creates an instance of the Truck class, "Truck 2"
truck3 = Truck()

# A3
# Create loadPackageData(HashTable) to
# - read packages from packageCSV file (see C950 - Webinar-2 - Getting Greedy, who moved my data  webinar)
# - update Package object
# - insert Package object into HashTable with the key=PackageID and Item=Package
def loadPackageData():
    import csv
    with open("packages.csv", "r") as f:
        # read the  csv file
        reader = csv.reader(f)
        next(reader)
        packageData = csv.reader(f, delimiter=',')
        next(packageData)
        num_packages = 0
        packages = []
        for package in reader:
            pID = int(package[0])
            pAddress = package[1]
            pCity = package[2]
            pState = package[3]
            pZip = package[4]
            pDeadline = package[5]
            pMass = package[6]
            pSpecialNotes = package[7]

            # Now I have a package object called "package" with the 8 parameters from the csv file
            package = Package(pID, pAddress, pCity, pState, pZip, pDeadline, pMass, pSpecialNotes)

            # insert packages into the hash table. Remember, the hash table is called "packageHash"
            packageHash.insert(package.pID, package)
            num_packages += 1

            # Also add the packages to a list
            packages.append(package)


# Now call the function to actually load the packages from the csv file into the hash table
loadPackageData()

# print out the packages in the hash table
# for i in range(len(packageHash.table)):
   #print("Package: {}".format(packageHash.search(i)))


# -------------------------------------------------------------------------------------------------------
# So far to this point, this is working. I have a hash table that prints to the console w/ correct info

# Section B: Now, I need to upload the distances information by creating a 2D list w/addresses and distances
# B) Distance data steps:
# B.1) Upload Distances:
# 4-Create distanceData List
# 5-Define loadDistanceData(distanceData) to read distanceCSV file
# - read distances from distanceCSV file; row by row
# - append row to distanceData (two-dimensional list. See C950 WGUPS Distance Table Metrics)
# B.2) Upload Addresses:
# 6-Create addressData List
# 7-Define loadAddressData(addressData) to read addressCSV file
# - read only addresses from addressCSV file
# - append address to addressData.


# Get the address data from the csv file
# def loadAddressData():
#     result = []
#     with open('allAddresses.csv', 'r') as file:
#         reader = csv.reader(file)
#         for row in reader:
#             result.append(row)
#
#     return result
#
#
# addressData = loadAddressData()

# This function is meant to create a loadDistanceData list
# B1 -- upload distances
def loadDistanceData():
    distanceData = []
    with open('distanceTable.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            distanceData.append(row)
            #print(row)

    return distanceData

# B.2 Upload Addresses:  6-   Create addressData List  and def load Address data
# This function hopefully creates an addressData List
def loadAddressData():
    addressData = []
    with open('allAddresses.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            addressData.append(row[0])
            #print(row)

    return addressData


addressData = loadAddressData()
distanceData = loadDistanceData()

#print(addressData[4])
#print(distanceData[7][2])

# --------------------------------------------------------------------------------------------------------------------
# C) Algorithm to Load Packages:
# C.1) Function to return the distance between two addresses:
# 8-Define distanceBetween(address1, address2)
# 9-Return distanceData[addressData.index(address1)][addressData.index(address2)]
#    i.e. distances between addresses can be accessed via distanceData[i][j];


def addressFind(address):
    try:
        return addressData.index(address)
    except ValueError:
        return None


def distanceBetween(address1, address2):
    try:
     return float(distanceData[addressFind(address1)][addressFind(address2)])
    except:
     return float(distanceData[addressFind(address2)][addressFind(address1)])


distanceCheck = distanceBetween('1488 4800 S','300 State St')
print("The distance between these two addresses is" , distanceCheck)


def loadTrucks(packageHash, truck1, truck2, truck3):
    # I need to iterate over the 40 packages in packageHash and put some in each truck
    for pID in range(1, 40):
        package = packageHash.search(pID)

        # sort the packages manually here, according to the special notes
        if package.pID in [1, 2, 4, 5, 7, 13, 14, 15, 16, 19, 20, 21, 29, 30, 33, 34, 35]:
            truck1.add_delivery(package.pAddress, 0)
        elif package.pID in [3, 10, 11, 12, 17, 18, 21, 22, 23, 24, 27, 36, 37, 38, 39, 40]:
            truck2.add_delivery(package.pAddress, 0)
        else:
            truck3.add_delivery(package.pAddress, 0)

loadTrucks(packageHash, truck1, truck2, truck3)
print("Truck 1 is loaded with packages for these addresses", truck1.deliveries)
print("Truck 2 is loaded with packages for these addresses", truck2.deliveries)
print("Truck 3 is loaded with packages for these addresses", truck3.deliveries)



#  This next part is not working yet. It cannot find any of the addresses . . .
def deliver_packages(truck, packageHash):
    global totalDistance
    for delivery in truck.deliveries:
        address = delivery[0]
        distance = delivery[1]
        package = packageHash.search(address)
        if package:
            print(f"Delivering package {package.pID} to {address}")
            totalDistance += distance
        else:
            print(f"Could not find package for address {address}")
    print(f"Total distance driven by {truck.__class__.__name__}: {truck.miles_driven}")

deliver_packages(truck1, packageHash)
