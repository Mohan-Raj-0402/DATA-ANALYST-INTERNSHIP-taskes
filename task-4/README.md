## plan to design your Interactive Dashboard:
### 🎯 Objective
Create a visually interactive sales and customer dashboard to help business stakeholders track Sales, Profit, and Growth trends.

### 📊 Right KPIs to include
KPIs as cards or top-level metrics:
Total Sales (sales)
Average Daily Rate (ADR)
Customer Rating (average)
Number of Transactions
Number of Guests (can use rep_guest)
Sales Growth (month-over-month or YoY if possible)
Cancellation Rate (d_s column = 'Refunded')

### 📈 Visualizations (Time-Series & Summary)
Line/Area Chart: Sales over time (arrival_date)
Bar Chart: Sales by hotel (hotel_name)
Pie Chart: Sales distribution by state
Stacked Bar: Membership level vs. sales
Heatmap: ADR vs Customer Rating by Sales Person

### 🎛️ Add Interactivity with Slicers/Filters
Use filters/slicers for:
Date Range (arrival_date)
Hotel Name (hotel_name)
Sales Person
Membership Level
Customer Rating

datasetlink ---> https://www.kaggle.com/datasets/tianrongsim/hotel-sales-2024?select=transactions+%281%29.xlsx

### About Dataset
These data sets contain the information on 6050 hotel bookings between in the year of 2024. Each observation represents a hotel booking. The dataset contains 6,050 hotel transactions with 36 columns, covering various aspects of hotel bookings, customer details, sales performance, and financial metrics.

### The Key Features included:
* Hotel Information: Hotel Name, Region, State, Hotel Type
* Customer Details: Customer Name, Phone Number, Email, Repeated Guest, Previous Cancellations
* Booking Information: Reservation Status, Check-in & Check-out Dates, Number of Guests (Adults/Children), Room Type, Duration (Nights)
* Financial Data: Price Per Room, Gross Sales, Discounts, Net Sales, Payment Method, Deposit Amount & Status, Commission
* Customer Feedback: Customer Rating, Customer Review
* Sales Performance: Sales Person, Position
