from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog,QWidget,QCalendarWidget,QVBoxLayout
import sys
import mainui as mn
import mydb
import mydb
import Database

class Control:
    def __init__(self):
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        self.ui = mn.Ui_MainWindow()
        self.ui.setupUi(MainWindow)

        self.ui.pushButton_10.clicked.connect(self.registration)
        self.ui.pushButton_11.clicked.connect(self.loginPage)
        self.ui.pushButton_6.clicked.connect(self.registrationpage)
        self.ui.pushButton_3.clicked.connect(self.carbookingpage)
        self.ui.pushButton_2.clicked.connect(self.Hotelbookingpage)
        self.ui.pushButton_21.clicked.connect(self.Homepage)
        self.ui.pushButton_20.clicked.connect(self.mainpage)
        self.ui.pushButton_13.clicked.connect(self.show_calendar)
        self.ui.pushButton_15.clicked.connect(self.show_calendar)
        self.ui.pushButton_22.clicked.connect(self.Flightpage)
        self.ui.pushButton.clicked.connect(self.get_flight)
        self.ui.pushButton.clicked.connect(self.ShowFlights)


        self.details = Database.CheapFlights()
        self.passenger = mydb.Auth()

        MainWindow.show()
        sys.exit(app.exec_())
       

    def loginPage(self):
        Un = self.ui.lineEdit_42.text()
        print("Username:", Un)
        Ps = self.ui.lineEdit_44.text()
        print("Password:", Ps)
        status = self.passenger.loginpage(Un,Ps)
        print("Login Status:",status)  
        if status:
            print("Login Successfully")
            self.ui.stackedWidget_2.setCurrentWidget(self.ui.stackedWidget_2Page1)
        else:
            print("Invalid username and password")
    def registrationpage(self):
        self.ui.stackedWidget_2.setCurrentWidget(self.ui.stackedWidget_2Page2)
    def carbookingpage(self):
        self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_2)
    def Hotelbookingpage(self):
        self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_3)  
    def Homepage(self):
        self.ui.stackedWidget_2.setCurrentWidget(self.ui.stackedWidget_2Page1)  
    def mainpage(self):
        self.ui.stackedWidget_2.setCurrentWidget(self.ui.stackedWidget_2Page1) 
    def ShowFlights(self):
        self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_5)       
    def show_calendar(self):
        self.calendar_popup = CalendarPopup(self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_3))
        if self.calendar_popup.exec_():  # Show calendar as a modal dialog
            print("Calendar Closed")
    def show_calendar(self):
        self.calendar_popup = CalendarPopup(self.ui.stackedWidget_2.setCurrentWidget(self.ui.page_3))
        if self.calendar_popup.exec_():  # Show calendar as a modal dialog
            print("Calendar Closed")
    def registration(self):

        fn = self.ui.lineEdit_28.text()
        print(fn)
        ln = self.ui.lineEdit_36.text()
        print(ln)
        Em = self.ui.lineEdit_30.text()
        print(Em)
        ps = self.ui.lineEdit_27.text()
        print(ps)
        Pn = self.ui.lineEdit_32.text()
        print(Pn)
        Ag = self.ui.lineEdit_34.text()
        print(Ag)
        if fn and ln and Em and ps and Pn and Ag:
            self.passenger.passenger(Firstname=fn,Lastname=ln,EmailID=Em,password=ps,PhoneNO=Pn,Age=Ag)
            print("Registered successfully")
        else:
          print("All fields are required")

    def Flightpage(self):
        DP = self.ui.lineEdit.text()
        print(DP)
        OP = self.ui.lineEdit_2.text()
        print(OP)
        DT = self.ui.lineEdit_3.text()
        print(DT)
        OT = self.ui.lineEdit_4.text()
        print(OT)
        DD = self.ui.lineEdit_7.text()
        print(DD)
        OD = self.ui.lineEdit_8.text()
        print(OD)
        PR = self.ui.lineEdit_9.text()
        print(PR)
        AR = self.ui.lineEdit_10.text()
        print(AR)
        DU = self.ui.lineEdit_13.text()
        print(DU)
        if DP and OP and DT and OT and DD and OD and PR and AR and DU:
            self.details.Flights(DepartureAirport=DP, OriginTime=OT, OriginAirport=OP,DepartureTime=DT, DepartureDate=DD, OriginDate=OD, Price = PR, Airlines=AR, Duration=DU)
            print("Details saved")
        else:
            print("all feild required")    


    def get_flight(self):
        DA = self.ui.lineEdit_5.text()
        print(DA)
        OA = self.ui.lineEdit_6.text()
        print(OA)
        data = self.details.get_flight(DA, OA)
        print(data)
       

    



class CalendarPopup(QDialog):
     def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Select Date")
        self.setGeometry(100, 100, 300, 250)

        self.calendar = QCalendarWidget(self)
        self.calendar.clicked.connect(self.date_selected)

        layout = QVBoxLayout()
        layout.addWidget(self.calendar)
        self.setLayout(layout)

        self.selected_date = None

     def date_selected(self, date):
        self.selected_date = date.toString("yyyy-MM-dd")
        print(f"Selected Date: {self.selected_date}")
        self.accept()  # Close the popup

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt5 Calendar Integration")
        self.setGeometry(100, 100, 500, 400)

        self.stack = self.ui.stackedWidget_2(self)

        # Page 1 with PushButton_13
        self.page_1 = QWidget()
        layout1 = QVBoxLayout()
        self.pushButton_13 = QPushButton("Open Calendar")
        self.pushButton_13.clicked.connect(self.show_calendar)
        layout1.addWidget(self.pushButton_13)
        self.page_1.setLayout(layout1)

        # Page 3 (target page)
        self.page_3 = QWidget()
        layout3 = QVBoxLayout()
        self.label = QLabel("This is Page 3 - Date Selected!")
        layout3.addWidget(self.label)
        self.page_3.setLayout(layout3)

        # Add pages to stacked widget
        self.stack.addWidget(self.page_1)  # index 0
        self.stack.addWidget(self.page_3)  # index 1

        # Set initial layout
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.stack)
        self.setLayout(main_layout)

    def show_calendar(self):
        calendar_popup = CalendarPopup(self)
        if calendar_popup.exec_():
            # If a date was selected and dialog closed
            print("Calendar Closed")
            print(f"Date chosen: {calendar_popup.selected_date}")
            self.stack.setCurrentWidget(self.page_3) 




    
if __name__ == '__main__':
    Control()
    #def showhome(self):
       # self.ui

