# Data Manipulation

## Overview

Data manipulation is a crucial process for organizing and interpreting data, with applications spanning various industries, including accounting, finance, programming, banking, sales, marketing, and real estate.

## Task 1: Calculating Total and Average Sales

This task involves working with lists and performing mathematical operations to calculate the total and average sales for a given list of sales amounts.

### Code:

```python
sales = [1000, 2000, 3000, 4000, 5000]
total_sales = 0

for i in range(len(sales)):
    total_sales = total_sales + sales[i]

average = total_sales / len(sales)
print("The total sales is ", total_sales)
print("The average of sales is ", average)

## Task 2: Calculating Total Cost with Discount

This task involves implementing a function that calculates the total cost of a given basket of products, applying a 10% discount.

### Code:

```python
def calculate_total_and_discount(dcr):
    total = 0

    for i in dcr.values():
        total = total + i

    print("The total cost of the basket of products is ", total)
    total_dis = (total * 10) / 100
    print("The total cost of the basket of products after discount is ", total_dis)

mydcr= {
    "Car": 5000,
    "Laptop": 4000,
    "Iphone": 3000,
    "Raspberry pi": 2000,
    "SIM808": 1000
}
calculate_total_and_discount(mydcr)

## Task 3 and 4:(Heading 2)
Define a class Product with attributes like name, price, and quantity. Create an instance of the class and showcase its usage. (Heading 2)
Extend the Product class to include a method that calculates the total cost of a certain quantity of that product. (Heading 2)
During this task, we dealt with Class and operations on them, in addition to mathematical operations. (Heading 3)
### Code:
```python
class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.total = 0
    def total_cost(self):
        self.total = self.quantity * self.price
    def get_show(self):
        print("The Name is ", self.name)
        print("The Price is ", self.price)
        print("The Quantity is ", self.quantity)
        print("The Total Cost is", self.total)

p1 = Product('PC',100,5)
p1.total_cost()
p1.get_show()

## Task 5: 
Read a CSV file containing sales data (columns: product_name, quantity, price).  Calculate the total revenue and average price per item.  Save the results to a new CSV file. (Heading 2)
During this task, files were dealt with and how to read and write from them, in addition to mathematical operations. (Heading 3)
### Code:
```python
import pandas as pd

input_file_path = 'sales_data.csv'
output_file_path = 'results.csv'
df = pd.read_csv(input_file_path)
df['total_revenue'] = df['quantity'] * df['price']
total_revenue = df['total_revenue'].sum()
average_price_per_item = df['price'].mean()
print(f'Total Revenue: ${total_revenue:.2f}')
print(f'Average Price Per Item: ${average_price_per_item:.2f}')
result_df = pd.DataFrame({'Total Revenue': [total_revenue], 'Average Price Per Item': [average_price_per_item]})
result_df.to_csv(output_file_path, index=False)
print(f'Results saved to {output_file_path}')
