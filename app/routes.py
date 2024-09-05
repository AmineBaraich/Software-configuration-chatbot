from flask import Blueprint, request, jsonify
from transformers import pipeline
from .simulations import monte_carlo_simulation

# Create a blueprint for the routes
main = Blueprint('main', __name__)

# Load pre-trained sentiment analysis model from Hugging Face
nlp_model = pipeline("sentiment-analysis")

# Chat route to handle AI-powered conversation
@main.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message', '')
    
    # Process user input with the AI model
    nlp_result = nlp_model(user_input)

    # Example basic handling of the NLP results
    if "simulate" in user_input.lower():
        return jsonify({
            "response": "Please provide the initial investment, market fluctuation, and duration in years."
        })
    elif nlp_result[0]['label'] == 'POSITIVE':
        return jsonify({
            "response": "You sound positive! How can I help you with financial scenarios?"
        })
    else:
        return jsonify({
            "response": "I'm here to help with financial simulations. Type 'simulate' to start."
        })

# Simulation route to handle scenario analysis
@main.route('/simulate', methods=['POST'])
def simulate():
    data = request.json
    initial_investment = data.get('initial_investment', 10000)
    market_fluctuation = data.get('market_fluctuation', 0.05)
    years = data.get('years', 5)

    # Run Monte Carlo simulation
    simulation_results = monte_carlo_simulation(initial_investment, market_fluctuation, years)

    return jsonify(simulation_results)
