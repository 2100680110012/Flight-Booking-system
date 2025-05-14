import sqlite3

class CheapFlights:
    def __init__(self):
        
        self.conn = sqlite3.connect("flightdetails.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute("""create table if not exists Flights(
                            DepartureAirport varchar (50),
                            OriginAirport varchar(50),
                            DepartureTime varchar (5),
                            OriginTime varchar (5),
                            DepartureDate varchar (8),
                            OriginDate varchar (8),
                            Price varchar(7),
                            Airlines varchar(20),
                            Duration varchar(7)

        )""")
        

    def Flights(self, **u):
        print("Details saved")

        self.cursor.execute(""" INSERT INTO Flights (DepartureAirport, OriginAirport, DepartureTime, OriginTime, DepartureDate, OriginDate, Price, Airlines, Duration)Values (?,?,?,?,?,?,?,?,?)""", (u["DepartureAirport"], u["OriginAirport"], u["DepartureTime"], u["OriginTime"], u["DepartureDate"], u["OriginDate"], u["Price"], u["Airlines"], u["Duration"]))
        self.conn.commit()


    def get_flight(self, DA, OA):

        
        query = """
            SELECT * FROM Flights
            WHERE 
                DepartureAirport = ? AND
                OriginAirport = ?
                
        """
        values = (DA, OA)
        self.cursor.execute(query, values)
        results = self.cursor.fetchall()
        return results


    def getAllFlights(self):
        self.cursor.execute("select * from Flights")
        result = self.cursor.fetchall()
        print(result)


if __name__ == '__main__':
    obj = CheapFlights()
    obj.getAllFlights()

    


    
    
    # Insert sample data
    #self.cursor.execute("""
        #INSERT INTO FlightBookingpage VALUES 
        #('Delhi', 'Mumbai', '2025-06-01', '2025-06-10', 'Economy', 2, 1)
    #""")
    
    #self.conn.commit()
    #self.conn.close()


# # Function to get flight
# def get_flight(DA, OA, DD, RD, CC, AD, CH):
#     conn = sqlite3.connect("flights.db")
#     cursor = conn.cursor()
    
#     query = """
#         SELECT * FROM FlightBookingpage
#         WHERE 
#             [Departure Airport] = ? AND
#             [Origin Airport] = ? AND
#             [Departure Date] = ? AND
#             [Return Date] = ? AND
#             [Class] = ? AND
#             [Adults] = ? AND
#             [Children] = ?
#     """
#     values = (DA, OA, DD, RD, CC, AD, CH)
#     cursor.execute(query, values)
#     results = cursor.fetchall()
    
#     conn.close()
#     return results


# # Call everything

# flights = get_flight("Delhi", "Mumbai", "2025-06-01", "2025-06-10", "Economy", 2, 1)

# # Show results
# for flight in flights:
#     print(flight)
