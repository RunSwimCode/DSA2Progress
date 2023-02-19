import csv
import math
import datetime
import math
totalDistance = 0
class ChainingHashTable:
    def __init__(self, initial_capacity=10):
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])
    def insert(self, key, value):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]
        for kv in bucket_list:
            # print (key_value)
            if kv[0] == key:
                kv[1] = value
                return True
        key_value = [key, value]
        bucket_list.append(key_value)
        return True
    def search(self, pID):
        bucket = hash(pID) % len(self.table)
        bucket_list = self.table[bucket]
        for kv in bucket_list:
            if kv[0] == pID:
                return kv[1]  # value
        return None
    def remove(self, key):
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]
        for kv in bucket_list:
            # print (key_value)
            if kv[0] == key:
                bucket_list.remove(kv)
packageHash = ChainingHashTable(10)

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
truck1 = Truck()
truck2 = Truck()
truck3 = Truck()

def loadPackageData():
    import csv
    with open("packages.csv", "r") as f:
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
            package = Package(pID, pAddress, pCity, pState, pZip, pDeadline, pMass, pSpecialNotes)
            packageHash.insert(package.pID, package)
            num_packages += 1
            packages.append(package)
        return packages
loadPackageData()

def loadDistanceData():
    distanceData = []
    with open('distanceTable.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            distanceData.append(row)
            #print(row)

    return distanceData

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
def loadTrucks(packageHash, truck1, truck2, truck3):
     for pID in range(1, 41):
         package = packageHash.search(pID)
         if package.pID in [1, 2, 4, 5, 7, 13, 14, 15, 16, 19, 20, 21, 29, 30, 33, 34, 35]:
             truck1.add_delivery(package.pAddress, 0)
         elif package.pID in [3, 10, 11, 12, 17, 18, 21, 22, 23, 24, 27, 36, 37, 38, 39, 40]:
             truck2.add_delivery(package.pAddress, 0)
         else:
             truck3.add_delivery(package.pAddress, 0)
loadTrucks(packageHash, truck1, truck2, truck3)
def deliverPackages(truck1_deliverys, truck2_deliverys, truck3_deliverys):
    truck1distance = 0
    truck2distance = 0
    truck3distance = 0
    for delivery in truck1_deliverys:
        index = truck1_deliverys.index(delivery)
        firstaddress = delivery[0]
        if index < len(truck1_deliverys) - 1:   
            secondaddress = truck1_deliverys[index + 1]
            secondaddress = secondaddress[0]
        else:
            secondaddress = truck1_deliverys[index]
            secondaddress = secondaddress[0]
        distanceBetweenPackages = distanceBetween(firstaddress, secondaddress)
        truck1distance += distanceBetweenPackages
    for delivery in truck2_deliverys:
        index = truck2_deliverys.index(delivery)
        firstaddress = delivery[0]
        if index < len(truck2_deliverys) - 1:   
            secondaddress = truck2_deliverys[index + 1]
            secondaddress = secondaddress[0]
        else:
            secondaddress = truck2_deliverys[index]
            secondaddress = secondaddress[0]
        distanceBetweenPackages = distanceBetween(firstaddress, secondaddress)
        truck2distance += distanceBetweenPackages
    for delivery in truck3_deliverys:
        index = truck3_deliverys.index(delivery)
        firstaddress = delivery[0]
        if index < len(truck3_deliverys) - 1:   
            secondaddress = truck3_deliverys[index + 1]
            secondaddress = secondaddress[0]
        else:
            secondaddress = truck3_deliverys[index]
            secondaddress = secondaddress[0]
        distanceBetweenPackages = distanceBetween(firstaddress, secondaddress)
        truck3distance += distanceBetweenPackages
    print(f'The three trucks traveled a total distance of {round(truck1distance + truck2distance + truck3distance)} miles. Truck 1 traveled {round(truck1distance)} miles, truck 2 traveled {round(truck2distance)} miles, and truck 3 traveled {round(truck3distance)} miles.')
    return [truck1distance, truck2distance, truck3distance]
deliverPackages(truck1.deliveries, truck2.deliveries, truck3.deliveries)
