# Stock Market Data Web Application

- [Stock Market Data Web Application](#stock-market-data-web-application)
	- [Overview](#overview)
	- [Implemented Functionalities](#implemented-functionalities)
	- [Additional Functionalities Implemented](#additional-functionalities-implemented)
	- [Repository Structure](#repository-structure)


## Overview

This web application is built using Python and Django framework to visualize stock market data. It provides functionalities to view, edit, create, and delete stock market data records. Additionally, it includes interactive chart visualizations for better analysis.

## Implemented Functionalities

1. **Table Visualization:** Displays stock market data in a tabular format on the home page.
2. **Editable Rows/CRUD Functionality:** Allows users to perform CRUD (Create, Read, Update, Delete) operations on stock market data records. Among them create, update, and delete operations are protected by user authentication.
3. **Multi-axis Chart:** Accommodates both line and bar chart visualizations together with the 'close' column represented in the line chart and the 'volume' column in the bar chart.
4. **Dropdown Selection:** Includes a dropdown menu in the chart to choose the 'trade_code' column, which updates the data in the line chart.

## Additional Functionalities Implemented

- **Additional Visualization:** Incorporates a **candlestick chart** for stock market data visualization, offering additional insights into the market trends.
- **Dark Mode Support:** Includes support for dark mode, allowing users to switch between light and dark themes for better viewing experience.
- **User Authentication:** Implements user authentication using Django's built-in authentication system to secure CRUD operations and access control.
- **Pagination:** Implements pagination for better navigation and performance, ensuring smooth user experience even with large datasets.
- **Session Management:** Uses session management to store user preferences, such as dark mode setting, across different pages.

## Repository Structure

The project repository is organized into the following directories:

- **stockview:** Contains Django app files, including models, views, templates, and static files.
- **stockview\scripts\run_seed.py:** Script to seed the SQL database with stock market data from the provided JSON file. Command to run the script: `python manage.py runscript run_seed`.
