CREATE TABLE Customers (
    Customer_Id INTEGER PRIMARY KEY,
    Customer_City TEXT,
    Customer_Country TEXT,
    Customer_Segment TEXT
);

CREATE TABLE Orders (
    Order_Id INTEGER PRIMARY KEY,
    Customer_Id INTEGER,
    Order_Date TEXT,
    Shipping_Date TEXT,
    Shipping_Mode TEXT,
    Order_Status TEXT,
    Late_Delivery_Risk INTEGER,
    FOREIGN KEY (Customer_Id) REFERENCES Customers(Customer_Id)
);