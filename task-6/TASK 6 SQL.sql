SELECT * FROM ecom.`online_sale report`;

-- a. Extract Month and Year from Order Date
SELECT 
    EXTRACT(YEAR FROM STR_TO_DATE(`Order Date`, '%d-%m-%Y')) AS Year,
    EXTRACT(MONTH FROM STR_TO_DATE(`Order Date`, '%d-%m-%Y')) AS Month
FROM ecom.`online_sale report`;

-- b. Group by Year/Month and c. Sum Revenue and d. Count Order Volume and e. Sort Results and f. Limit to Specific Time Period
SELECT 
    EXTRACT(YEAR FROM STR_TO_DATE(`Order Date`, '%d-%m-%Y')) AS Year,
    EXTRACT(MONTH FROM STR_TO_DATE(`Order Date`, '%d-%m-%Y')) AS Month,
    SUM(Amount) AS Revenue,
    COUNT(DISTINCT `Order ID`) AS Order_Volume
FROM ecom.`online_sale report`
WHERE 
    STR_TO_DATE(`Order Date`, '%d-%m-%Y') BETWEEN '2016-01-01' AND '2017-12-31' -- Adjust dates as needed
GROUP BY Year, Month
ORDER BY Year, Month
LIMIT 10; -- Optional: Limit the number of results
