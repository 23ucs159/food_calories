#### the app was deployed in streamlit 
demo link:
(https://foodcalories-xma6hanp64rqgcpbnelgtn.streamlit.app/)

Enter a food item name (example: Apple, Banana, Burger)
Click on Analyze Food button

# 1.1 PROJECT OVERVIEW

The AI Food Nutrition & Health Analyzer is a machine learning-based application developed to help users understand the nutritional value of different food items and make healthier dietary choices. The system allows users to enter the name of a food item and instantly receive detailed nutritional information such as calories, protein, carbohydrates, fat, iron, and vitamin C content.

The application uses a trained Random Forest Machine Learning model to analyze nutritional features and classify food items into three categories: Healthy, Moderate, or Unhealthy. Along with the prediction, the system calculates a health score and provides personalized diet, hydration, lifestyle, and exercise recommendations to encourage better nutrition and overall well-being.

The project is built using Python, Streamlit, Pandas, Scikit-Learn, and Matplotlib. The user-friendly interface displays nutritional information through interactive charts and allows users to download a detailed PDF report of the analysis.

This system aims to promote health awareness by providing quick and easy access to food nutrition analysis, enabling users to make informed decisions about their daily diet and lifestyle.

# 1.2 PROJECT OBJECTIVES

* To analyze the nutritional content of food items.
* To predict whether a food item is Healthy, Moderate, or Unhealthy using Machine Learning.
* To provide nutritional information including calories, protein, carbohydrates, fat, iron, and vitamin C.
* To generate a health score based on nutritional values.
* To offer personalized diet and exercise recommendations.
* To visualize nutritional information using graphs and charts.
* To generate downloadable nutrition reports for users.

# 1.3 PROBLEM STATEMENT

Many people consume food without understanding its nutritional value and health impact. There is often a lack of awareness regarding calories, protein, fat, and essential nutrients present in daily foods. This project addresses this problem by developing an intelligent nutrition analysis system that evaluates food items, predicts their health category, and provides useful recommendations to support healthier eating habits.

# 1.4 EXPECTED OUTCOME

The developed system will allow users to:

* Search food items by name.
* View complete nutritional information.
* Identify whether a food item is healthy or unhealthy.
* Understand the nutritional strengths and weaknesses of foods.
* Receive practical diet and exercise suggestions.
* Visualize nutrition data through graphs.
* Download a nutrition analysis report in PDF format.

  
1.5 HOW TO RUN THE PROJECT

Step 1: Install Required Libraries
Open Command Prompt and install the required Python libraries using:

pip install streamlit pandas scikit-learn matplotlib joblib fpdf

Step 2: Open Project Folder
Navigate to your project directory using Command Prompt:

cd path/to/your/project-folder

Step 3: Run the Application
Run the Streamlit application using:

streamlit run app.py

If the file name is different (example: app1.py), use:

streamlit run app1.py

Step 4: Access the Application
The application will automatically open in the default web browser.
If it does not open, copy the URL shown in Command Prompt and paste it into a browser.

Step 5: Analyze Food

View nutritional information, health prediction, health score, and recommendations

Step 6: Download Report
Click on Download Report button to generate and save a PDF report of the analysis.
