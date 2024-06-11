Vehicle Data Analysis and Visualization

Project Overview
This project provides a web application for analyzing and visualizing vehicle advertisements data. Users can explore various aspects of the dataset, such as pricing trends, distributions, and correlations, through interactive charts and graphs.

Features
Interactive Histograms: Visualize the distribution of data with options for normalization.
Scatter Plots: Explore relationships between two numerical variables.
Bar Charts: Compare categorical data such as manufacturers or fuel types.

Visualizations
1. Histograms
 <!-- Replace with actual path -->

Visualize the distribution of numerical data. You can normalize the histogram to show proportions.

2. Scatter Plots
 <!-- Replace with actual path -->

Explore the relationship between two numerical variables.

3. Bar Charts
 <!-- Replace with actual path -->

Compare different categories, such as vehicle types or fuel types.

Configuration
Page Layout: The app uses a wide layout for better display of charts.
Page Title and Icon: Customize the title and icon by editing the st.set_page_config in app.py.
Data
The dataset used in this project is vehicles_us.csv, which contains the following columns:

price: Price of the vehicle.
model_year: Year the vehicle model was manufactured.
model: Model of the vehicle.
condition: Condition of the vehicle (e.g., new, used).
cylinders: Number of cylinders in the vehicle's engine.
fuel: Type of fuel the vehicle uses.
odometer: Distance the vehicle has traveled.
transmission: Type of transmission (e.g., manual, automatic).
type: Type of vehicle (e.g., sedan, SUV).
paint_color: Color of the vehicle.
is_4wd: Indicates if the vehicle has four-wheel drive.
date_posted: Date when the vehicle ad was posted.
days_listed: Number of days the vehicle was listed before it was sold or removed.