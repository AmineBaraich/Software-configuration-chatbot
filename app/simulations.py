import numpy as np

def monte_carlo_simulation(initial_investment, market_fluctuation, years, num_simulations=1000):
    results = []
    for _ in range(num_simulations):
        simulated_fluctuation = np.random.normal(market_fluctuation, 0.05)  # Some variance
        future_value = initial_investment * np.power(1 + simulated_fluctuation, years)
        results.append(future_value)
    
    return {
        'mean': np.mean(results),
        '10th_percentile': np.percentile(results, 10),
        '90th_percentile': np.percentile(results, 90)
    }
