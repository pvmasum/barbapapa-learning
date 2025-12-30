# Practice JSON string 

market_json = """
{
  "market": "TSE",
  "data_provider": "MockAPI",
  "timestamp": "2025-01-01T10:30:00Z",
  "symbols": [
    {
      "symbol": "FOLD",
      "price": 2150,
      "volume": 340000,
      "currency": "IRR"
    },
    {
      "symbol": "SHASTA",
      "price": 1240,
      "volume": 890000,
      "currency": "IRR"
    },
    {
      "symbol": "KHEZAR",
      "price": 1785,
      "volume": 120000,
      "currency": "IRR"
    }
  ]
}
"""

import json

# Convert JSON string to Python dictionary
market_data = json.loads(market_json)

# Check type
print(type(market_data))


# Convert Python dict back to JSON string
market_json_output = json.dumps(market_data, indent=2)

print(market_json_output)

# Accessing nested data
print("Market:", market_data["market"])
print("Timestamp:", market_data["timestamp"])




















