from graph import Graph

class Locations:
        def __init__(self):

                # list of locations found at that key
                self._locations = {
        'A' : ["Cedar", "Pepperwood", "Alder", "Tan Oak", "Maple", "Madrone", 
                "Hemlock", "Chinquapin"],
        'A2' : ["Student Recreation Area"],
        'B' : ["Creekside Lounge", "Laurel", "Junior", "Fern", "Willow"], 
        'B2' : ["Lumberjack Arean", "Kinesiology & Athletics"], 
        'C' : ["Jolly Giant Commons"], 
        'C2' : ["Forbes Gym"], 
        'D' : ["Sunset Hall", "Redwood Hall"], 
        'D2' : ["Sci B", "Sci C", "GRNH", "Sci D", "Dennis K. Walker Greenhouse",
                "BROH", "Brookins House", "Greenhouse" ],
        'E' : ["Cypress Hall"], 
        'E2' : ["Student & Business Services"], 
        'F' : ["FWH", "Feuerwerker House"], 
        'F2' : ["Del Norte", "Shasta", "CCFLR", "College Creek Field", 
                "College Creek Field Locker Rooms"], 
        'G' : ["Nelson Hall West", "Nelson Hall East"], 
        'G2' : ["Child Development Lab", "Harry Griffith Hall"], 
        'H' : ["Founders Hall"], 
        'H2' : ["Community Center", "Trinity", "Mendocino", "College Creek Field"],
        'I' : ["HAH", "BRH", "LAPT", "Little Apartments", "Brero House", "Hagopian House"], 
        'I2' : ["Campus Events Field"], 
        'J' : ["University Center", "The Depot", "Bookstore", "UC Quad"], 
        'J2' : ["Wildlife & Fisheries", "WLDF"], 
        'K' : ["Student Health and Counseling"], 
        'K2' : ["Marine Wildlife Care Center"], 
        'L' : ["Library", "Library Circle"], 
        'L2' : ["Wildlife Game Pens", "Fish Hatchery"],
        'M' : ["Van Matre Hall"], 
        'M2' : ["Natural Resources"], 
        'N' : ["Siemens Hall"], 
        'N2' : ["Facilities Management", "Shipping & Recieving"], 
        'O' : ["Redwood Bowl"], 
        'O2' : ["BOAT", "Boat Facility"], 
        'P' : ["Music A"], 
        'P2' : ["Behavioral & Social Sceinces", "BSS", "Native American Forum", 
                "BUCH","Buck House (CCAT)"],
        'Q' : ["Upper Playing Field"], 
        'Q2' : ["JENH", "TOD", "MCOM", "WWH", "MWH", "BH", "Baiocchi House",
                "Jensen House (Children's Center", "Marketing and Communications",
                "Marry Warren House", "Toddler Center", "Walter Warren House (INRSEP)"],
        'R' : ["Music B", "Art B"], 
        'R2' : ["Forestry"], 
        'S' : ["HH", "BALH", "Balabanis House (MCC)", "Hadley House"], 
        'S2' : ["Trinity Annex"], 
        'T' : ["Recreation & Wellness Center"], 
        'T2' : ["Schatz Energy Research Center"], 
        'U' : ["TH", "Telonicher House"], 
        'V' : ["Art A"], 
        'W' : ["WH", "BHH", "Campus Apartments", "Bret Harte House", 
                "Warren House"], 
        'X' : ["Sculpture Lab", "Ceramics Lab", "WAGH", "Wagner House"], 
        'Y' : ["Gist Hall"], 
        'Z' : ["Sci A", "Jenkins House"]
        }
        
        # get key based on a specifc place
        def look_up(self, hsu_location):
                for key, contents in self._locations.items():
                        if hsu_location in contents:
                                return key

