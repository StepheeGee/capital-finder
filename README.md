# LAB - Class 16

## Project: Serverless Functions

## Author: Stephanie G. Johnson

## Date: 01-29-2024

### Links and Resources

[Rest Countries API](https://restcountries.com/v3.1/all?fields=name,flags)

[Vercel Documentation](https://vercel.com/docs/functions/serverless-functions/runtimes/python)

### Serverless Function: Capital Finder

This serverless function helps you find the capital by providing the country name or find the country by providing the capital name.

### Usage

#### Find the Capital by Country

- **Endpoint:** `/api/capital-finder?country={country_name}`
- **Example:** [https://stephs-capital-finder.vercel.app/api/capital-finder?country=Chile](https://stephs-capital-finder.vercel.app/api?country=Chile)
- **Response:** `The capital of Chile is Santiago`

#### Find the Country by Capital

- **Endpoint:** `/api/capital-finder?capital={capital_name}`
- **Example:** [https://stephs-capital-finder.vercel.app/api/capital-finder?capital=Santiago](https://stephs-capital-finder.vercel.app/api?capital=Santiago)
- **Response:** `Santiago is the capital of Chile`

### Deployed URLs

- **Vercel App:** [https://stephs-capital-finder.vercel.app/](https://stephs-capital-finder.vercel.app/)
- **Capital Finder API:** [https://stephs-capital-finder.vercel.app/api/capital-finder](https://stephs-capital-finder.vercel.app/api)

### Virtual Environment Setup

1. Create a virtual environment: `python -m venv venv`
2. Activate the virtual environment:
   - On Windows: `.\venv\Scripts\activate`
   - On macOS/Linux: `source venv/bin/activate`
3. Install dependencies: `pip install -r requirements.txt`
4. Install requests library: `pip install requests`

### How to Run

1. Activate the virtual environment (if not already activated).
2. Run the serverless function: `vercel dev`

### Tests

No specific tests are provided for this serverless function. Feel free to create tests using your preferred testing framework.
