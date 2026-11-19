# Software Engineering and Project Management Lab

## TY IT -- Semester V \| Academic Year 2026--27

### Practical Question Bank -- Consolidated Record Notes

> **How to use this file:** Practical 1--20 contain UML diagram content
> in tables so that the actors, classes, activities, states,
> participants, relationships and messages can be transferred to Visual
> Paradigm. Practical 21--25 contain the process-model, SRS, RMMM,
> estimation and project-planning material. The diagrams are represented
> as structured content, not as rendered UML images.

------------------------------------------------------------------------

# Part A -- UML Practicals

## Practical 1 -- Online Examination Management System

**Aim:** Design a Use Case Diagram representing the functional
requirements and user interactions.

### Actors

  Actor     Role
  --------- -------------------------------------------------
  Student   Registers, takes examinations and views results
  Admin     Manages examination setup and question papers

### Use cases

  -----------------------------------------------------------------------
  Use case                Actor(s)                Purpose
  ----------------------- ----------------------- -----------------------
  Student Registration    Student                 Create a student
                                                  account

  Examination Scheduling  Admin                   Schedule examinations

  Question Paper          Admin                   Prepare/generate
  Generation                                      question papers

  Online Examination      Student                 Attempt the examination

  Automatic Evaluation    System (internal        Evaluate submitted
                          function)               answers

  Result Generation       System (internal        Generate examination
                          function)               results

  View Result             Student                 View the published
                                                  result
  -----------------------------------------------------------------------

### Actor--use-case associations

  Actor     Connect to
  --------- -------------------------------------------------------
  Student   Student Registration, Online Examination, View Result
  Admin     Examination Scheduling, Question Paper Generation

**Diagram notes:** Draw the system boundary labelled *Online Examination
Management System*. Put use cases inside it and actors outside.
Automatic Evaluation and Result Generation are system functions; they do
not need human actors.

**Result:** Use Case Diagram content for the Online Examination
Management System is prepared.

------------------------------------------------------------------------

## Practical 2 -- Library Management System

**Aim:** Develop a Class Diagram showing major classes, attributes,
operations and relationships.

### Classes

  -----------------------------------------------------------------------
  Class                   Attributes              Methods
  ----------------------- ----------------------- -----------------------
  Student                 studentId:int,          register(),
                          name:String,            borrowBook(),
                          department:String       returnBook(),
                                                  reserveBook()

  Book                    bookId:int,             checkAvailability(),
                          title:String,           issueBook(),
                          author:String,          returnBook()
                          status:String           

  Librarian               librarianId:int,        addBook(),
                          name:String,            removeBook(),
                          email:String            issueBook(),
                                                  acceptReturn()

  Issue                   issueId:int,            issueBook(),
                          issueDate:Date,         returnBook(),
                          dueDate:Date,           calculateOverdue()
                          returnDate:Date         

  Reservation             reservationId:int,      reserveBook(),
                          reservationDate:Date,   cancelReservation()
                          status:String           

  Fine                    fineId:int,             calculateFine(),
                          amount:double,          payFine()
                          paymentStatus:String    
  -----------------------------------------------------------------------

### Relationships and multiplicities

  ------------------------------------------------------------------------
  Class 1                   Multiplicity Class 2          Meaning
  ---------------- --------------------- ---------------- ----------------
  Student                              1 Issue            Each issue
                                                          record belongs
                                                          to one student

  Issue                            0..\* Student          A student can
                                                          have many issue
                                                          records

  Book                                 1 Issue            Each issue
                                                          record refers to
                                                          one book

  Issue                            0..\* Book             A book can be
                                                          issued many
                                                          times over time

  Librarian                            1 Issue            Each issue is
                                                          handled by one
                                                          librarian

  Issue                            0..\* Librarian        A librarian
                                                          handles many
                                                          issues

  Student                              1 Reservation      Each reservation
                                                          belongs to one
                                                          student

  Reservation                      0..\* Student          A student can
                                                          make many
                                                          reservations

  Book                                 1 Reservation      Each reservation
                                                          is for one book

  Reservation                      0..\* Book             A book may have
                                                          multiple
                                                          reservation
                                                          records

  Issue                                1 Fine             A fine belongs
                                                          to one issue
                                                          record

  Fine                              0..1 Issue            An issue may
                                                          have zero or one
                                                          fine
  ------------------------------------------------------------------------

**Diagram notes:** Draw each class as a three-compartment rectangle:
class name, attributes, methods. Use solid association lines and show
multiplicities near the ends. Multiplicity is best read from the
opposite end: one student can have many issue records.

**Result:** Class Diagram content for the Library Management System is
prepared.

------------------------------------------------------------------------

## Practical 3 -- College ERP System

**Aim:** Identify actors and their interactions with the College ERP
system using a Use Case Diagram.

### Actors

  Actor        Role
  ------------ ------------------------------------------------------------
  Student      Uses admission, attendance, examination and fee facilities
  Faculty      Manages attendance and examination-related activities
  Admin        Manages admission and faculty records
  Accountant   Manages fee-related operations

### Use cases and associations

  Use case             Actor(s)
  -------------------- ---------------------
  Manage Admission     Student, Admin
  Manage Attendance    Student, Faculty
  Manage Examination   Student, Faculty
  Manage Fees          Student, Accountant
  Manage Faculty       Admin

**Diagram notes:** Draw the system boundary as *College ERP System*.
Connect each actor to the relevant use cases. A use case represents a
service/function offered by the system, not an internal automation step.

**Result:** Use Case Diagram content for the College ERP System is
prepared.

------------------------------------------------------------------------

## Practical 4 -- Online Shopping Management System

**Aim:** Design a Class Diagram for customer registration, product
search, cart, order, payment and delivery.

### Classes

  -------------------------------------------------------------------------
  Class                   Attributes                Methods
  ----------------------- ------------------------- -----------------------
  Customer                customerId:int,           register(), login(),
                          name:String,              searchProduct(),
                          email:String,             placeOrder()
                          address:String            

  Admin                   adminId:int, name:String, addProduct(),
                          email:String              updateProduct(),
                                                    deleteProduct()

  Product                 productId:int,            displayProduct(),
                          productName:String,       checkStock(),
                          price:double, stock:int   updateStock()

  Cart                    cartId:int,               addItem(),
                          totalAmount:double        removeItem(),
                                                    calculateTotal()

  CartItem                cartItemId:int,           updateQuantity(),
                          quantity:int,             calculateSubtotal()
                          subtotal:double           

  Order                   orderId:int,              placeOrder(),
                          orderDate:Date,           cancelOrder(),
                          totalAmount:double,       trackOrder()
                          orderStatus:String        

  OrderItem               orderItemId:int,          calculateSubtotal()
                          quantity:int,             
                          price:double              

  Payment                 paymentId:int,            makePayment(),
                          amount:double,            verifyPayment(),
                          paymentMode:String,       refundPayment()
                          paymentStatus:String      

  Delivery                deliveryId:int,           assignDelivery(),
                          deliveryAddress:String,   updateStatus(),
                          deliveryStatus:String     trackDelivery()
  -------------------------------------------------------------------------

### Relationships and multiplicities

  ------------------------------------------------------------------------
  Class 1                   Multiplicity Class 2          Meaning
  ---------------- --------------------- ---------------- ----------------
  Customer                             1 Cart             One customer has
                                                          one cart

  Cart                                 1 Customer         One cart belongs
                                                          to one customer

  Customer                             1 Order            Each order
                                                          belongs to one
                                                          customer

  Order                            0..\* Customer         A customer can
                                                          place many
                                                          orders

  Admin                                1 Product          Product is
                                                          managed by an
                                                          admin

  Product                          0..\* Admin            An admin can
                                                          manage many
                                                          products

  Cart                                 1 CartItem         Each cart item
                                                          belongs to one
                                                          cart

  CartItem                         0..\* Cart             A cart can
                                                          contain many
                                                          cart items

  Product                              1 CartItem         Each cart item
                                                          refers to one
                                                          product

  CartItem                         0..\* Product          A product can
                                                          appear in many
                                                          cart items

  Order                                1 OrderItem        Each order item
                                                          belongs to one
                                                          order

  OrderItem                        1..\* Order            An order
                                                          contains one or
                                                          more items

  Product                              1 OrderItem        Each order item
                                                          refers to one
                                                          product

  OrderItem                        0..\* Product          A product can
                                                          appear in many
                                                          order items

  Order                                1 Payment          A payment record
                                                          belongs to one
                                                          order

  Payment                           0..1 Order            An order may
                                                          have zero or one
                                                          payment record

  Order                                1 Delivery         A delivery
                                                          record belongs
                                                          to one order

  Delivery                          0..1 Order            An order may
                                                          have zero or one
                                                          delivery record
  ------------------------------------------------------------------------

**Diagram notes:** Draw all nine classes and connect them using
association lines. Put multiplicities at both ends. These are conceptual
multiplicities for the model.

**Result:** Class Diagram content for the Online Shopping Management
System is prepared.

------------------------------------------------------------------------

## Practical 5 -- ATM Transaction System

**Aim:** Design an Activity Diagram for an ATM cash withdrawal,
including PIN validation, balance checking, receipt generation and card
ejection.

### Activity flow

  ------------------------------------------------------------------------
                          Step Activity / Decision   Next step
  ---------------------------- --------------------- ---------------------
                             1 Initial node          Insert ATM Card

                             2 Insert ATM Card       Enter PIN

                             3 Enter PIN             Validate PIN

                             4 Validate PIN --       Yes → Select
                               decision: PIN         Withdrawal; No →
                               correct?              Display Error

                             5 Display Error         Re-enter PIN (or
                                                     terminate after
                                                     limited attempts)

                             6 Select Withdrawal     Enter Amount

                             7 Enter Amount          Check Account Balance

                             8 Check Balance --      Yes → Dispense Cash;
                               decision: sufficient  No → Display
                               balance?              Insufficient Balance

                             9 Dispense Cash         Update Account
                                                     Balance

                            10 Update Account        Generate Receipt
                               Balance               

                            11 Generate Receipt      Eject Card

                            12 Display Insufficient  Eject Card
                               Balance               

                            13 Eject Card            Final node
  ------------------------------------------------------------------------

### Symbols

  Symbol                Use
  --------------------- -------------------
  Filled circle         Initial node
  Rounded rectangle     Activity/action
  Diamond               Decision or merge
  Arrow                 Control flow
  Bullseye/final node   End of activity

**Diagram notes:** Put guard labels such as `[Yes]` and `[No]` on
outgoing arrows from decision diamonds. Connect all completed paths to
the final node.

**Result:** Activity Diagram flow for ATM cash withdrawal is prepared.

------------------------------------------------------------------------

## Practical 6 -- Railway Reservation System

**Aim:** Model online railway ticket booking with seat availability and
payment-failure alternatives.

### Activity flow

  ------------------------------------------------------------------------
                          Step Activity / Decision   Next step
  ---------------------------- --------------------- ---------------------
                             1 Initial node          Enter Journey Details

                             2 Enter Journey Details Search Train

                             3 Search Train          Select Train

                             4 Select Train          Check Seat
                                                     Availability

                             5 Decision: Seat        Yes → Enter Passenger
                               available?            Details; No → Display
                                                     Seat Unavailable

                             6 Enter Passenger       Make Payment
                               Details               

                             7 Make Payment          Decision: Payment
                                                     successful?

                             8 Payment successful    Yes → Generate Ticket

                             9 Payment failed        No → Display Payment
                                                     Failure

                            10 Generate Ticket       Confirm Booking

                            11 Confirm Booking /     Final node
                               failure message       
  ------------------------------------------------------------------------

**Diagram notes:** Use a diamond for each decision and label the
outgoing arrows `[Yes]` and `[No]`. The unavailable-seat and
failed-payment branches should show an appropriate failure message and
terminate.

**Result:** Activity Diagram flow for Railway Reservation is prepared.

------------------------------------------------------------------------

## Practical 7 -- Online Banking Application

**Aim:** Design a State Machine Diagram for the lifecycle of a bank
transaction.

### States and transitions

  Current state        Event / condition       Next state
  -------------------- ----------------------- --------------------
  Initial              Open application        Logged Out
  Logged Out           Submit login details    Authenticating
  Authenticating       Valid credentials       Logged In
  Authenticating       Invalid credentials     Logged Out
  Logged In            Select fund transfer    Transfer Initiated
  Transfer Initiated   Confirm transaction     Processing
  Processing           Transaction completed   Successful
  Processing           Transaction error       Failed
  Successful           Return to dashboard     Logged In
  Failed               Return to dashboard     Logged In
  Logged In            Logout                  Logged Out
  Logged Out           Exit application        Final

**Diagram notes:** Use rounded state boxes, a filled initial circle,
directed transition arrows labelled with events, and a final-state
symbol. The second Logged Out state is the same state; do not create a
duplicate unless it helps layout.

**Result:** State Machine Diagram content for Online Banking is
prepared.

------------------------------------------------------------------------

## Practical 8 -- Hospital Management System

**Aim:** Model appointment states such as requested, scheduled,
confirmed, completed, cancelled and rescheduled.

### States and transitions

  Current state   Event / condition                  Next state
  --------------- ---------------------------------- -------------
  Initial         Book appointment                   Requested
  Requested       Request submitted                  Pending
  Pending         Doctor accepts                     Confirmed
  Pending         Doctor rejects / patient cancels   Cancelled
  Confirmed       Patient cancels                    Cancelled
  Confirmed       Patient arrives                    Checked In
  Confirmed       Patient requests another time      Rescheduled
  Rescheduled     New slot assigned                  Confirmed
  Checked In      Consultation starts                In Progress
  In Progress     Consultation finishes              Completed
  Completed       Appointment closed                 Final
  Cancelled       Appointment closed                 Final

**Diagram notes:** The question uses the terms requested, scheduled,
confirmed, completed, cancelled and rescheduled. `Pending` and
`Checked In` are included to make the operational flow clearer. If
keeping strictly to the question, rename `Pending` to `Scheduled`.

**Result:** State Machine Diagram content for Hospital Appointment
Management is prepared.

------------------------------------------------------------------------

## Practical 9 -- Online Food Ordering System

**Aim:** Design a Sequence Diagram showing interactions during food
ordering and delivery.

### Participants / lifelines

  Participant            Responsibility
  ---------------------- -------------------------------
  Customer               Browses menu and places order
  Food Ordering System   Coordinates the order
  Restaurant             Accepts and prepares food
  Payment Gateway        Processes payment
  Delivery Partner       Delivers the order

### Messages in order

    No. From → To                                 Message
  ----- ----------------------------------------- -------------------------
      1 Customer → Food Ordering System           Browse Menu
      2 Customer → Food Ordering System           Place Order
      3 Food Ordering System → Restaurant         Send Order Details
      4 Restaurant → Food Ordering System         Accept Order
      5 Food Ordering System → Payment Gateway    Process Payment
      6 Payment Gateway → Food Ordering System    Payment Successful
      7 Food Ordering System → Restaurant         Confirm Order
      8 Restaurant → Food Ordering System         Food Prepared
      9 Food Ordering System → Delivery Partner   Assign Delivery
     10 Delivery Partner → Food Ordering System   Delivery Completed
     11 Food Ordering System → Customer           Send Order Confirmation

**Diagram notes:** Place participants across the top with vertical
lifelines. Draw messages from top to bottom in chronological order. Use
activation bars if required by the tool.

**Result:** Sequence Diagram message flow for Online Food Ordering is
prepared.

------------------------------------------------------------------------

## Practical 10 -- Online Banking Fund Transfer System

**Aim:** Design the interaction flow for transferring funds between two
bank accounts.

### Participants

  Participant              Responsibility
  ------------------------ -----------------------------------------
  Customer                 Initiates the transfer
  Banking System           Coordinates the transfer
  Authentication Service   Verifies credentials
  Account                  Provides balance and account operations
  Payment Gateway          Processes the transfer
  Notification Service     Sends transaction notification

### Messages

  ------------------------------------------------------------------------
                           No. From → To             Message
  ---------------------------- --------------------- ---------------------
                             1 Customer → Banking    Login
                               System                

                             2 Banking System →      Verify Credentials
                               Authentication        
                               Service               

                             3 Authentication        Authentication
                               Service → Banking     Successful
                               System                

                             4 Customer → Banking    Enter Transfer
                               System                Details

                             5 Banking System →      Check Balance
                               Account               

                             6 Account → Banking     Balance Available
                               System                

                             7 Banking System →      Process Transfer
                               Payment Gateway       

                             8 Payment Gateway →     Debit and Credit
                               Account               Amount

                             9 Account → Payment     Transaction
                               Gateway               Successful

                            10 Payment Gateway →     Transfer Confirmation
                               Banking System        

                            11 Banking System →      Send Notification
                               Notification Service  

                            12 Notification Service  Transfer Successful
                               → Customer            Message
  ------------------------------------------------------------------------

**Diagram notes:** Draw lifelines in participant order and messages from
top to bottom. The transfer should only proceed after authentication and
balance validation.

**Result:** Sequence Diagram content for Online Banking Fund Transfer is
prepared.

------------------------------------------------------------------------

## Practical 11 -- Student Attendance Management System

**Aim:** Represent interactions among faculty, student, attendance
system and database using a Communication Diagram.

### Objects

    No. Object
  ----- -------------------------------------
      1 `student:Student`
      2 `attendanceSystem:AttendanceSystem`
      3 `faculty:Faculty`
      4 `database:Database`
      5 `reportGenerator:ReportGenerator`

### Communication links

  Object 1            Object 2            Purpose
  ------------------- ------------------- -----------------------------
  Student             Attendance System   Request/view attendance
  Attendance System   Faculty             Attendance operations
  Attendance System   Database            Read and save attendance
  Attendance System   Report Generator    Generate attendance report
  Report Generator    Database            Retrieve attendance records

### Numbered messages

    No. From → To                              Message
  ----- -------------------------------------- --------------------
      1 Student → Attendance System            Request Attendance
    1.1 Attendance System → Database           Fetch Attendance
    1.2 Database → Attendance System           Return Attendance
      2 Attendance System → Student            Display Attendance
      3 Faculty → Attendance System            Mark Attendance
    3.1 Attendance System → Database           Save Attendance
    3.2 Database → Attendance System           Confirm Saved
      4 Faculty → Attendance System            Generate Report
    4.1 Attendance System → Report Generator   Request Report
    4.2 Report Generator → Database            Fetch Records
    4.3 Report Generator → Attendance System   Return Report
      5 Attendance System → Faculty            Display Report

**Diagram notes:** A Communication Diagram uses object rectangles
connected by links; messages are numbered to show order. If Visual
Paradigm Online does not provide a Communication Diagram template, use a
blank UML Class Diagram canvas as a drawing workaround. Use object
labels and connectors with numbered message labels; do not use
sequence-diagram lifelines.

**Result:** Communication Diagram content for Student Attendance is
prepared.

------------------------------------------------------------------------

## Practical 12 -- Hotel Reservation System

**Aim:** Model interactions between customer, hotel booking system, room
availability service and payment service during reservation and
cancellation.

### Objects

    No. Object
  ----- ---------------------------------------------------
      1 `customer:Customer`
      2 `reservationSystem:ReservationSystem`
      3 `hotel:Hotel`
      4 `roomAvailabilityService:RoomAvailabilityService`
      5 `paymentService:PaymentService`
      6 `notificationService:NotificationService`

### Communication links

  -----------------------------------------------------------------------
  Object 1                Object 2                Purpose
  ----------------------- ----------------------- -----------------------
  Customer                Reservation System      Search, reserve and
                                                  cancel room

  Reservation System      Room Availability       Check and update room
                          Service                 availability

  Reservation System      Hotel                   Confirm booking details

  Reservation System      Payment Service         Process payment/refund

  Reservation System      Notification Service    Send
                                                  booking/cancellation
                                                  message
  -----------------------------------------------------------------------

### Numbered messages -- reservation

  ------------------------------------------------------------------------
                           No. From → To             Message
  ---------------------------- --------------------- ---------------------
                             1 Customer →            Search Rooms
                               Reservation System    

                           1.1 Reservation System →  Check Availability
                               Room Availability     
                               Service               

                           1.2 Room Availability     Return Available
                               Service → Reservation Rooms
                               System                

                             2 Reservation System →  Display Available
                               Customer              Rooms

                             3 Customer →            Select Room
                               Reservation System    

                           3.1 Reservation System →  Hold Selected Room
                               Room Availability     
                               Service               

                           3.2 Room Availability     Room Hold Confirmed
                               Service → Reservation 
                               System                

                             4 Customer →            Enter Guest Details
                               Reservation System    

                             5 Customer →            Confirm Booking
                               Reservation System    

                           5.1 Reservation System →  Process Payment
                               Payment Service       

                           5.2 Payment Service →     Payment Successful
                               Reservation System    

                           5.3 Reservation System →  Confirm Reservation
                               Hotel                 

                           5.4 Hotel → Reservation   Booking Confirmed
                               System                

                             6 Reservation System →  Send Confirmation
                               Notification Service  

                           6.1 Notification Service  Booking Confirmation
                               → Customer            
  ------------------------------------------------------------------------

### Numbered messages -- cancellation

  ------------------------------------------------------------------------
                           No. From → To             Message
  ---------------------------- --------------------- ---------------------
                             7 Customer →            Request Cancellation
                               Reservation System    

                           7.1 Reservation System →  Cancel Reservation
                               Hotel                 

                           7.2 Hotel → Reservation   Cancellation
                               System                Confirmed

                           7.3 Reservation System →  Process Refund (if
                               Payment Service       applicable)

                           7.4 Payment Service →     Refund Status
                               Reservation System    

                             8 Reservation System →  Release Room
                               Room Availability     
                               Service               

                             9 Reservation System →  Send Cancellation
                               Notification Service  Notice

                           9.1 Notification Service  Cancellation
                               → Customer            Confirmation
  ------------------------------------------------------------------------

**Diagram notes:** The question specifically names a room availability
service and payment service, so include both as separate objects. A
Communication Diagram uses object rectangles, links and numbered
messages. If the dedicated option is unavailable in Visual Paradigm
Online, use the Class Diagram canvas as a manual drawing workaround.

**Result:** Communication Diagram content for Hotel Reservation,
including reservation and cancellation, is prepared.

------------------------------------------------------------------------

## Practical 13 -- College Admission Management System

**Aim:** Design an Activity Diagram for online admission.

### Activity flow

  ------------------------------------------------------------------------
                          Step Activity / Decision   Next step
  ---------------------------- --------------------- ---------------------
                             1 Initial node          Register Student

                             2 Register Student      Login

                             3 Login                 Fill Application Form

                             4 Fill Application Form Upload Documents

                             5 Upload Documents      Verify Documents

                             6 Decision: Documents   Yes → Check
                               valid?                Eligibility; No →
                                                     Display Rejection

                             7 Check Eligibility     Decision: Eligible?

                             8 Eligible              Yes → Pay Admission
                                                     Fees; No → Display
                                                     Rejection

                             9 Pay Admission Fees    Confirm Admission

                            10 Confirm Admission /   Final node
                               Display Rejection     
  ------------------------------------------------------------------------

**Diagram notes:** Use decision diamonds for document validity and
eligibility. Label outgoing branches `[Yes]` and `[No]`.

**Result:** Activity Diagram flow for College Admission is prepared.

------------------------------------------------------------------------

## Practical 14 -- Employee Payroll Management System

**Aim:** Represent the lifecycle of payroll calculation, approval and
payment using a State Machine Diagram.

### States and transitions

  Current state          Event / condition     Next state
  ---------------------- --------------------- ----------------------
  Initial                Create payroll        Draft
  Draft                  Record attendance     Attendance Collected
  Attendance Collected   Calculate salary      Salary Calculated
  Salary Calculated      Submit for approval   Pending Approval
  Pending Approval       Manager approves      Approved
  Pending Approval       Manager rejects       Rejected
  Rejected               Correct payroll       Draft
  Approved               Initiate payment      Payment Processing
  Payment Processing     Payment successful    Paid
  Payment Processing     Payment error         Payment Failed
  Payment Failed         Retry payment         Payment Processing
  Paid                   Payroll completed     Final

**Diagram notes:** Draw states as rounded rectangles and label arrows
with events. Rejected payroll returns to Draft for correction; failed
payment can be retried.

**Result:** State Machine Diagram content for Employee Payroll is
prepared.

------------------------------------------------------------------------

## Practical 15 -- Online Ticket Booking System

**Aim:** Design a Sequence Diagram for customer, booking system, seat
availability, payment and ticket generation.

### Participants

  Participant            Responsibility
  ---------------------- ------------------------------------
  Customer               Searches and books a ticket
  Booking System         Coordinates booking
  Event/Travel Service   Provides event/travel availability
  Seat Management        Checks and reserves seats
  Payment Gateway        Processes payment
  Notification Service   Sends ticket confirmation

### Messages

  ------------------------------------------------------------------------
                           No. From → To             Message
  ---------------------------- --------------------- ---------------------
                             1 Customer → Booking    Search Tickets
                               System                

                             2 Booking System →      Check Availability
                               Event/Travel Service  

                             3 Event/Travel Service  Available Tickets
                               → Booking System      

                             4 Customer → Booking    Select Ticket
                               System                

                             5 Booking System → Seat Check Seat
                               Management            Availability

                             6 Seat Management →     Seat Available
                               Booking System        

                             7 Customer → Booking    Confirm Booking
                               System                

                             8 Booking System →      Process Payment
                               Payment Gateway       

                             9 Payment Gateway →     Payment Successful
                               Booking System        

                            10 Booking System → Seat Reserve Seat
                               Management            

                            11 Seat Management →     Seat Reserved
                               Booking System        

                            12 Booking System →      Send Confirmation
                               Notification Service  

                            13 Notification Service  Booking Confirmed /
                               → Customer            Ticket Details
  ------------------------------------------------------------------------

**Diagram notes:** Draw participant lifelines and arrange messages from
top to bottom. Ticket generation/confirmation follows successful payment
and seat reservation.

**Result:** Sequence Diagram content for Online Ticket Booking is
prepared.

------------------------------------------------------------------------

## Practical 16 -- Vehicle Rental Management System

**Aim:** Identify classes, relationships and multiplicities for a
vehicle rental system.

### Classes

  -----------------------------------------------------------------------
  Class                   Attributes              Methods
  ----------------------- ----------------------- -----------------------
  Customer                customerId:int,         register(),
                          name:String,            bookVehicle()
                          phone:String,           
                          address:String          

  Admin                   adminId:int,            addVehicle(),
                          name:String,            removeVehicle(),
                          email:String            manageBooking()

  Vehicle                 vehicleId:int,          checkAvailability(),
                          model:String,           updateStatus()
                          type:String,            
                          rentPerDay:double,      
                          availability:String     

  Booking                 bookingId:int,          createBooking(),
                          bookingDate:Date,       cancelBooking()
                          startDate:Date,         
                          endDate:Date,           
                          status:String           

  Payment                 paymentId:int,          makePayment(),
                          amount:double,          verifyPayment()
                          paymentMode:String,     
                          status:String           

  Rental Agreement        rentalId:int,           startRental(),
                          pickupDate:Date,        completeRental()
                          returnDate:Date,        
                          totalAmount:double      
  -----------------------------------------------------------------------

### Relationships and multiplicities

  ------------------------------------------------------------------------
  Class 1                   Multiplicity Class 2          Meaning
  ---------------- --------------------- ---------------- ----------------
  Customer                             1 Booking          Each booking
                                                          belongs to one
                                                          customer

  Booking                          0..\* Customer         A customer can
                                                          make many
                                                          bookings

  Admin                                1 Vehicle          Vehicle is
                                                          managed by an
                                                          admin

  Vehicle                          0..\* Admin            An admin can
                                                          manage many
                                                          vehicles

  Vehicle                              1 Booking          Each booking is
                                                          for one vehicle

  Booking                          0..\* Vehicle          A vehicle can
                                                          have many
                                                          bookings over
                                                          time

  Booking                              1 Payment          Payment is
                                                          associated with
                                                          a booking

  Payment                           0..1 Booking          A booking may
                                                          have zero or one
                                                          payment

  Booking                              1 Rental Agreement Agreement
                                                          belongs to one
                                                          booking

  Rental Agreement                  0..1 Booking          A booking may
                                                          have zero or one
                                                          agreement

  Customer                             1 Rental Agreement Agreement
                                                          belongs to one
                                                          customer

  Rental Agreement                 0..\* Customer         A customer can
                                                          have multiple
                                                          agreements over
                                                          time

  Vehicle                              1 Rental Agreement Agreement refers
                                                          to one vehicle

  Rental Agreement                 0..\* Vehicle          A vehicle can
                                                          have multiple
                                                          agreements over
                                                          time
  ------------------------------------------------------------------------

**Diagram notes:** Use a class rectangle with three compartments for
each class. Draw association lines and add multiplicities. The
`Rental Agreement` class is named as required in the practical question.

**Result:** Class Diagram content for Vehicle Rental Management is
prepared.

------------------------------------------------------------------------

## Practical 17 -- Pharmacy Management System

**Aim:** Design a Use Case Diagram supporting medicine inventory,
prescription verification, billing, supplier management and sales.

### Actors

  Actor        Role
  ------------ ---------------------------------------------------
  Admin        Manages inventory and suppliers
  Pharmacist   Verifies prescriptions and handles medicine sales
  Customer     Purchases medicines and makes payment
  Supplier     Supplies medicines to the pharmacy

### Use cases and associations

  Use case                    Actor(s)
  --------------------------- -------------------
  Manage Medicine Inventory   Admin, Pharmacist
  Manage Suppliers            Admin
  Verify Prescription         Pharmacist
  Generate Bill               Pharmacist
  Manage Sales                Pharmacist
  Purchase Medicines          Customer
  Make Payment                Customer
  Supply Medicines            Supplier

**Diagram notes:** Customer connects to Purchase Medicines and Make
Payment. Pharmacist connects to Generate Bill and Manage Sales. Supplier
connects to Supply Medicines. Do not connect Supplier to Manage Sales or
Customer to Generate Bill.

**Result:** Use Case Diagram content for Pharmacy Management is
prepared.

------------------------------------------------------------------------

## Practical 18 -- Courier Tracking Management System

**Aim:** Model the lifecycle of a courier parcel from booking and pickup
through dispatch, delivery or return.

### States and transitions

  Current state      Event / condition            Next state
  ------------------ ---------------------------- ------------------
  Initial            Place order/book parcel      Booked
  Booked             Courier collected parcel     Picked Up
  Picked Up          Dispatch courier             In Transit
  In Transit         Parcel reaches sorting hub   Arrived at Hub
  Arrived at Hub     Dispatched to next hub       In Transit
  Arrived at Hub     Sent for local delivery      Out for Delivery
  Out for Delivery   Successful delivery          Delivered
  Out for Delivery   Recipient unavailable        Delivery Failed
  Delivery Failed    Retry delivery               Out for Delivery
  Delivery Failed    Return to sender             Returned
  Booked             Booking cancelled            Cancelled
  Delivered          Close tracking               Final
  Returned           Close tracking               Final
  Cancelled          Close tracking               Final

**Diagram notes:** Use a state box for each status. The parcel may
revisit In Transit when moving between sorting hubs. Delivered, Returned
and Cancelled are terminal outcomes.

**Result:** State Machine Diagram content for Courier Tracking is
prepared.

------------------------------------------------------------------------

## Practical 19 -- Online Learning Management System

**Aim:** Design a Use Case Diagram showing interactions between
students, instructors and the LMS.

### Actors

  -----------------------------------------------------------------------
  Actor                               Role
  ----------------------------------- -----------------------------------
  Student                             Enrols in courses, accesses content
                                      and submits assignments

  Instructor                          Manages course content and
                                      assessments
  -----------------------------------------------------------------------

### Use cases and associations

  Use case                    Actor(s)
  --------------------------- ------------
  Enrol in Course             Student
  Access Learning Content     Student
  Submit Assignment           Student
  Participate in Assessment   Student
  Manage Course Content       Instructor
  Evaluate Assignments        Instructor
  Conduct Assessment          Instructor

**Diagram notes:** Draw Student and Instructor outside the LMS system
boundary. Place the use cases inside and connect each actor to the
relevant functions.

**Result:** Use Case Diagram content for Online Learning Management is
prepared.

------------------------------------------------------------------------

## Practical 20 -- Online Bus Reservation System

**Aim:** Design a Sequence Diagram representing interactions among
passengers, bus operators, reservation system and payment gateway during
seat selection and ticket booking.

### Participants

  Participant              Responsibility
  ------------------------ ---------------------------------------
  Passenger                Searches buses and books a seat
  Reservation System       Coordinates reservation
  Bus Service / Operator   Provides bus and schedule information
  Seat Management          Checks and reserves seats
  Payment Gateway          Processes payment
  Notification Service     Sends ticket confirmation

### Messages

  ------------------------------------------------------------------------
                           No. From → To             Message
  ---------------------------- --------------------- ---------------------
                             1 Passenger →           Search Buses
                               Reservation System    

                             2 Reservation System →  Check Bus
                               Bus Service           Availability

                             3 Bus Service →         Display Available
                               Reservation System    Buses

                             4 Passenger →           Select Bus
                               Reservation System    

                             5 Reservation System →  Check Seat
                               Seat Management       Availability

                             6 Seat Management →     Seat Available
                               Reservation System    

                             7 Passenger →           Enter Passenger
                               Reservation System    Details

                             8 Passenger →           Confirm Booking
                               Reservation System    

                             9 Reservation System →  Process Payment
                               Payment Gateway       

                            10 Payment Gateway →     Payment Successful
                               Reservation System    

                            11 Reservation System →  Reserve Seat
                               Seat Management       

                            12 Seat Management →     Seat Reserved
                               Reservation System    

                            13 Reservation System →  Generate/Send Ticket
                               Notification Service  

                            14 Notification Service  Send Booking
                               → Passenger           Confirmation
  ------------------------------------------------------------------------

**Diagram notes:** Draw participant lifelines and place messages in
chronological order. Seat reservation and ticket confirmation follow
successful payment.

**Result:** Sequence Diagram content for Online Bus Reservation is
prepared.

------------------------------------------------------------------------

# Part B -- Software Engineering and Project Management Practicals

## Practical 21 -- Online Examination Management System: Process Model

**Aim:** Compare software process models, select a suitable model and
represent its phases and deliverables.

### Requirements

  Requirement                Description
  -------------------------- ------------------------------------------------
  Student registration       Students create accounts and log in
  Question bank management   Admin stores and manages questions
  Examination scheduling     Admin schedules exams
  Online assessment          Students attempt exams online
  Result generation          System evaluates answers and publishes results

### Process model comparison

  -----------------------------------------------------------------------
  Model                   Main idea               Suitability
  ----------------------- ----------------------- -----------------------
  Waterfall               Sequential phases       Less flexible when
                                                  requirements change

  Prototyping             Build an early model to Useful for UI feedback
                          clarify requirements    

  Spiral                  Iterative development   Useful for high-risk
                          with risk analysis      projects

  Incremental             Deliver the system in   Suitable for staged
                          functional parts        feature delivery
  -----------------------------------------------------------------------

### Selected model: Incremental Model

**Justification:** The system can be divided into functional increments.
Each increment can be developed, tested and demonstrated separately.
Early releases provide useful functionality, and feedback can be
incorporated in later increments.

### Proposed increments

    Increment Features delivered
  ----------- --------------------------------------------
            1 Student registration and login
            2 Question bank management
            3 Examination scheduling
            4 Online examination
            5 Automatic evaluation and result generation

### Phases and deliverables

  -----------------------------------------------------------------------
  Phase                   Main work               Deliverable
  ----------------------- ----------------------- -----------------------
  Requirement Analysis    Gather and document     SRS
                          requirements            

  System Design           Architecture, database  Design document / UML
                          and interface design    diagrams

  Implementation          Develop each increment  Source code / working
                                                  increment

  Testing                 Unit, integration and   Test cases and test
                          system testing          report

  Deployment              Install and release the Deployed application
                          system                  

  Maintenance             Fix defects and improve Updated software /
                          features                maintenance report
  -----------------------------------------------------------------------

### Advantages

-   Working features are delivered early.
-   Testing and debugging can be done increment by increment.
-   User feedback can be included in later releases.
-   Changes are easier to manage than in a strictly sequential approach.

**Result:** Incremental Model is selected and its increments, phases and
deliverables are documented.

------------------------------------------------------------------------

## Practical 22 -- Hospital Management System: IEEE SRS

**Aim:** Prepare an IEEE-style Software Requirements Specification for a
Hospital Management System.

### 1. Introduction

  -----------------------------------------------------------------------
  Heading                             Content
  ----------------------------------- -----------------------------------
  Purpose                             Define requirements for a system
                                      that manages hospital activities

  Scope                               Patient registration, appointments,
                                      doctors, billing, pharmacy and
                                      medical records

  Intended audience                   Developers, testers, hospital
                                      administrators, doctors and users
  -----------------------------------------------------------------------

### 2. Overall Description

  -----------------------------------------------------------------------
  Heading                             Content
  ----------------------------------- -----------------------------------
  Product perspective                 Centralized software system for
                                      hospital operations

  Product functions                   Patient registration, appointment
                                      scheduling, doctor management,
                                      billing, pharmacy and records

  User characteristics                Admin staff, doctors,
                                      receptionists, pharmacists and
                                      patients

  Operating environment               Web-based application, server,
                                      database and network

  Constraints                         Access control, data privacy,
                                      hardware/network availability

  Assumptions and dependencies        Users have valid accounts; database
                                      and network services are available
  -----------------------------------------------------------------------

### 3. Functional Requirements

  ID    Requirement
  ----- ---------------------------------------------------------------
  FR1   The system shall register and maintain patient details
  FR2   The system shall schedule, update and cancel appointments
  FR3   The system shall maintain doctor profiles and availability
  FR4   The system shall store and retrieve patient medical records
  FR5   The system shall generate bills and record payments
  FR6   The system shall manage medicine inventory and pharmacy sales

### 4. Non-Functional Requirements

  -----------------------------------------------------------------------
  Category                            Requirement
  ----------------------------------- -----------------------------------
  Performance                         Common operations should respond
                                      within an acceptable time

  Security                            Only authorized users may access
                                      protected records

  Reliability                         Data should be stored accurately
                                      and backed up

  Usability                           Interfaces should be clear and easy
                                      to use

  Availability                        The system should be available
                                      during hospital operating hours and
                                      planned service windows

  Maintainability                     The system should support updates
                                      and bug fixes
  -----------------------------------------------------------------------

### 5. External Interface Requirements

  -----------------------------------------------------------------------
  Interface                           Description
  ----------------------------------- -----------------------------------
  User interface                      Forms, dashboards, appointment
                                      screens and billing screens

  Hardware interface                  Computers, printers and supported
                                      hospital devices

  Software interface                  Database, operating system and any
                                      integrated hospital software

  Communication interface             Secure network communication
                                      between clients and server
  -----------------------------------------------------------------------

### 6. Constraints, assumptions and conclusion

-   Patient data must be protected and accessed only by authorized
    users.
-   System operation depends on the availability of the server, database
    and network.
-   The SRS provides a common reference for design, implementation,
    testing and acceptance.

**Result:** IEEE-style SRS content for the Hospital Management System is
prepared.

------------------------------------------------------------------------

## Practical 23 -- College ERP System: RMMM Plan

**Aim:** Identify technical, operational, financial and security risks
and prepare a Risk Mitigation, Monitoring and Management plan.

**RMMM:** Risk Mitigation, Monitoring and Management.

### Risk analysis and response

  ---------------------------------------------------------------------------------------------------------------------------
  ID      Risk           Probability   Impact   Risk           Mitigation        Monitoring        Contingency /  Owner
                                                exposure\*                       indicator         management     
                                                                                                   action         
  ------- -------------- ------------- -------- -------------- ----------------- ----------------- -------------- -----------
  R1      Data loss      Medium        High     High           Regular automated Backup            Restore latest Database
                                                               backups           success/failure   verified       Admin
                                                                                 logs              backup         

  R2      Security       Medium        High     High           Authentication,   Failed logins and Block access,  Security
          attack /                                             authorization and security alerts   investigate    Admin
          unauthorized                                         encryption                          and patch      
          access                                                                                                  

  R3      Server failure Medium        High     High           Redundant server  Uptime and server Switch to      System
                                                               and recovery plan health            backup server  Admin

  R4      Requirement    High          Medium   Medium--High   Requirement       Change requests   Re-plan scope  Project
          changes                                              review and change per phase         and schedule   Manager
                                                               control                                            

  R5      Lack of user   Medium        Medium   Medium         User training and Support requests  Conduct        Training
          training                                             documentation     and feedback      additional     Lead
                                                                                                   training       

  R6      Module         Medium        High     High           Early interface   Failed            Debug          Technical
          integration                                          definition and    integration test  interfaces and Lead
          failure                                              integration tests cases             repeat tests   

  R7      Budget overrun Medium        High     High           Cost estimation   Actual vs planned Reprioritize   Project
                                                               and periodic      cost              scope and seek Manager
                                                               review                              approval       
  ---------------------------------------------------------------------------------------------------------------------------

\*Risk exposure is shown qualitatively here. If numerical risk exposure
is required, calculate `Probability × Impact` using a defined numeric
scale.

### Risk priority

  -----------------------------------------------------------------------
  Priority                            Risks
  ----------------------------------- -----------------------------------
  High                                Data loss, security attack, server
                                      failure, integration failure

  Medium                              Requirement changes, lack of user
                                      training, budget overrun
  -----------------------------------------------------------------------

**Result:** RMMM plan for College ERP is prepared with risks,
probability, impact, mitigation, monitoring, contingency and ownership.

------------------------------------------------------------------------

## Practical 24 -- Online Food Delivery Application: Size, Effort, Duration and Cost Estimation

**Aim:** Estimate project size, development effort, duration and cost
using Function Points and Basic COCOMO.

> **Important:** The figures below are illustrative assumptions for a
> practical exercise. Actual estimates depend on detailed requirements,
> complexity, technology, team productivity and local cost rates.

### 1. Function Point estimation

  Function type                            Count   Weight (assumed)     Total
  -------------------------------------- ------- ------------------ ---------
  External Inputs (EI)                         6                  4        24
  External Outputs (EO)                        4                  5        20
  External Inquiries (EQ)                      4                  4        16
  Internal Logical Files (ILF)                 4                 10        40
  External Interface Files (EIF)               2                  7        14
  **Unadjusted Function Points (UFP)**                                **114**

Assume Value Adjustment Factor (VAF) = 1.0.

`FP = UFP × VAF = 114 × 1.0 = 114 FP`

### 2. Convert Function Points to LOC

Assume Java conversion factor = 53 LOC per FP.

`LOC = 114 × 53 = 6,042 LOC`

`KLOC = 6,042 / 1,000 = 6.042 KLOC`

### 3. Basic COCOMO effort estimation

Assume Organic mode:

`Effort = 2.4 × (KLOC)^1.05`

`Effort = 2.4 × (6.042)^1.05 ≈ 15.87 person-months`

### 4. Development duration

`Time = 2.5 × (Effort)^0.38`

`Time = 2.5 × (15.87)^0.38 ≈ 7.15 months`

### 5. Development cost

Assume cost = ₹50,000 per person-month.

`Cost = 15.87 × ₹50,000 = ₹7,93,500`

### Summary

  Metric                             Estimated value
  ---------------------------- ---------------------
  Unadjusted Function Points                     114
  Adjusted Function Points                    114 FP
  Estimated LOC                                6,042
  Estimated size                          6.042 KLOC
  Effort                         15.87 person-months
  Duration                               7.15 months
  Cost                                     ₹7,93,500

**Justification:** Function Points estimate software size from
user-visible functionality and are less dependent on programming
language than raw LOC. COCOMO is then used to estimate effort and
schedule from the estimated KLOC.

**Result:** Illustrative size, effort, duration and cost estimates for
the Online Food Delivery Application are calculated.

------------------------------------------------------------------------

## Practical 25 -- Student Management System: WBS and Gantt Chart

**Aim:** Prepare a project schedule with activities, durations,
dependencies, milestones and a Gantt chart.

### Work Breakdown Structure (WBS)

  -----------------------------------------------------------------------
  WBS ID                  Activity                Sub-activities
  ----------------------- ----------------------- -----------------------
  1.0                     Student Management      Overall project
                          System                  

  1.1                     Requirement Analysis    1.1.1 Collect
                                                  requirements; 1.1.2
                                                  Prepare SRS

  1.2                     System Design           1.2.1 Design
                                                  architecture; 1.2.2
                                                  Design database

  1.3                     Implementation          1.3.1 Develop frontend;
                                                  1.3.2 Develop backend

  1.4                     Testing                 1.4.1 Unit testing;
                                                  1.4.2 Integration
                                                  testing

  1.5                     Deployment              1.5.1 Install system;
                                                  1.5.2 User training

  1.6                     Maintenance             1.6.1 Fix bugs; 1.6.2
                                                  Update system
  -----------------------------------------------------------------------

### Activity schedule

  Activity                              Duration     Start    Finish Dependency
  ---------------------- ----------------------- --------- --------- ----------------------
  Requirement Analysis                   2 weeks    Week 1    Week 2 None
  System Design                          2 weeks    Week 3    Week 4 Requirement Analysis
  Implementation                         4 weeks    Week 5    Week 8 System Design
  Testing                                2 weeks    Week 9   Week 10 Implementation
  Deployment                              1 week   Week 11   Week 11 Testing
  Maintenance              1 week (initial plan)   Week 12   Week 12 Deployment

### Text Gantt chart

  ----------------------------------------------------------------------------------------
  Activity          W1    W2    W3    W4    W5    W6    W7    W8    W9    W10   W11   W12
  ---------------- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- ----- -----
  Requirement        ■     ■                                                         
  Analysis                                                                           

  System Design                  ■     ■                                             

  Implementation                             ■     ■     ■     ■                     

  Testing                                                            ■     ■         

  Deployment                                                                     ■   

  Maintenance                                                                          ■
  ----------------------------------------------------------------------------------------

### Milestones

  Milestone                    Target
  ---------------------------- ----------------
  Requirements approved        End of Week 2
  Design approved              End of Week 4
  Coding completed             End of Week 8
  Testing completed            End of Week 10
  System deployed              End of Week 11
  Initial maintenance review   End of Week 12

### Project metrics

  -----------------------------------------------------------------------
  Metric                              Value / description
  ----------------------------------- -----------------------------------
  Total planned duration              12 weeks

  Major phases                        6

  WBS work packages                   12 sub-activities

  Critical dependency chain           Requirements → Design →
                                      Implementation → Testing →
                                      Deployment

  Maintenance                         Continues after initial 12-week
                                      schedule in a real project
  -----------------------------------------------------------------------

**Diagram notes:** In a WBS, connect the main project box to the six
major work packages, then connect each work package to its subtasks. WBS
shows hierarchical scope decomposition, not chronological flow. In a
Gantt chart, time is on the horizontal axis and activities are on the
vertical axis.

**Result:** WBS, activity schedule, dependencies, milestones and Gantt
chart content for the Student Management System are prepared.

------------------------------------------------------------------------

# Quick Reference -- UML Diagram Symbols

  -----------------------------------------------------------------------
  Diagram type            Main elements           What it represents
  ----------------------- ----------------------- -----------------------
  Use Case                Actors, ovals, system   User-visible system
                          boundary, association   functions
                          lines                   

  Class                   Class rectangles,       Static structure of a
                          attributes, methods,    system
                          associations,           
                          multiplicities          

  Activity                Initial/final nodes,    Workflow and control
                          actions, arrows,        flow
                          decision diamonds       

  State Machine           States, transition      Lifecycle of an
                          arrows, events,         object/process
                          initial/final states    

  Sequence                Participants,           Time-ordered
                          lifelines, activation   interactions
                          bars, ordered messages  

  Communication           Object rectangles,      Object interactions and
                          links, numbered         message order
                          messages                
  -----------------------------------------------------------------------

## Common multiplicities in Class Diagrams

  Multiplicity    Meaning
  --------------- --------------
  `1`             Exactly one
  `0..1`          Zero or one
  `*` or `0..*`   Zero or many
  `1..*`          One or many

## Important drawing reminders

1.  Use a system boundary for Use Case Diagrams; actors stay outside it.
2.  Use three compartments in Class Diagram rectangles: class name,
    attributes and methods.
3.  Use diamonds for Activity Diagram decisions and label branches such
    as `[Yes]` and `[No]`.
4.  State Machine arrows must have meaningful event/condition labels.
5.  Sequence Diagram messages are arranged from top to bottom along
    lifelines.
6.  Communication Diagram messages are numbered and placed on links
    between objects; they do not use sequence lifelines.
7.  Add multiplicities near the ends of Class Diagram associations.
8.  Add a title and result statement to each practical record.

------------------------------------------------------------------------

**End of consolidated practical notes.**
