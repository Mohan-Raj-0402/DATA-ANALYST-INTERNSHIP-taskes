from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import pickle


# Initialize the Flask app
app = Flask(__name__)

# Load the trained model and scaler
with open('model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

# Assuming you have a saved scaler for preprocessing the data
with open('scaler.pkl', 'rb') as scaler_file:
    scaler = pickle.load(scaler_file)

# Sample data for insights (you can load and compute these from your dataset)
df = pd.read_excel('SuperStore Sales DataSet.xlsx')

@app.route('/')
def index():
    # Compute key insights (like return rates by product category, customer segment, etc.)
    return_rates_by_category = df.groupby('Category')['Returns'].mean().sort_values(ascending=False)
    return_rates_by_segment = df.groupby('Segment')['Returns'].mean().sort_values(ascending=False)
    
    return render_template('index.html', 
                           return_rates_by_category=return_rates_by_category,
                           return_rates_by_segment=return_rates_by_segment)

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Get user input
        order_id = request.form['Order_ID']
        product_id = request.form['Product_ID']
        quantity = int(request.form['Quantity'])
        profit = float(request.form['Profit'])
        
        # Prepare data for prediction (ensure the columns are in the right order and match your training data)
        user_input = pd.DataFrame({
            'Product_ID': [product_id],
            'Quantity': [quantity],
            'Profit': [profit],
            # Add other features here if necessary
        })
        
        # Scale the input using the pre-fitted scaler
        user_input_scaled = scaler.transform(user_input)  # Use transform, not fit_transform
        
        # Predict the return probability
        return_probability = model.predict_proba(user_input_scaled)[:, 1]  # Assuming binary classification (return/no-return)

        # Return the result to the template
        return render_template('result.html', return_probability=return_probability[0])

if __name__ == '__main__':
    app.run(debug=True)


