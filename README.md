Goldie Shopee sale data analytics project
This project was made to analyze the customer shopping patterns on Goldie's Shopee site
Deliverables: Top/Bottom sale items and each group's similar factors
              Peak time/slow season difference, and which factors affect it the most
              Product Categories Distribution

Data Preparation and Process:
First, I collected monthly data files from Goldie's Shopee because a month is the longest period that Shopee allows to extract data at once, then combined them with Python into an Excel file
After that, I standardized the order date column, hidden columns that are not relate or help the analytics like customer information columns (Shopee already masked that info)
I filled out the orders that had missed information due to the lack of POS data synchronization. For the orders that couldn't be filled, I removed them to avoid skewing the analytics


