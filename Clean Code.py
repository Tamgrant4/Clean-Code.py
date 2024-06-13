# Q1
#Task1

class Book:
  """
  This class represents a book in the online bookstore system.
  """

  def __init__(self, title, author, price, stock):
    """
    Initializes a Book object with its attributes.

    Args:
      title (str): The title of the book.
      author (str): The author of the book.
      price (float): The price of the book.
      stock (int): The current stock of the book.
    """
    self.title = title
    self.author = author
    self.price = price
    self.stock = stock

  def get_title(self):
    """
    Returns the title of the book.
    """
    return self.title

  def set_title(self, new_title):
    """
    Updates the title of the book.

    Args:
      new_title (str): The new title for the book.
    """
    self.title = new_title

  def get_author(self):
    """
    Returns the author of the book.
    """
    return self.author

  def set_author(self, new_author):
    """
    Updates the author of the book.

    Args:
      new_author (str): The new author for the book.
    """
    self.author = new_author

  def get_price(self):
    """
    Returns the price of the book.
    """
    return self.price

  def set_price(self, new_price):
    """
    Updates the price of the book.

    Args:
      new_price (float): The new price for the book.
    """
    self.price = new_price

  def get_stock(self):
    """
    Returns the current stock of the book.
    """
    return self.stock

  def decrease_stock(self, amount):
    """
    Reduces the stock of the book by a specified amount.

    Args:
      amount (int): The amount to decrease the stock.

    Raises:
      ValueError: If the amount is greater than the current stock.
    """
    if amount > self.stock:
      raise ValueError("Insufficient stock to decrease.")
    self.stock -= amount

  def increase_stock(self, amount):
    """
    Increases the stock of the book by a specified amount.

    Args:
      amount (int): The amount to increase the stock.
    """
    self.stock += amount

# Example usage
new_book = Book("The Hitchhiker's Guide to the Galaxy", "Douglas Adams", 12.99, 10)
print(f"Book title: {new_book.get_title()}")
new_book.decrease_stock(2)
print(f"Remaining stock: {new_book.get_stock()}")

# Q2
#Task1

class WeatherData:
  """
  This class represents weather data for a city.
  """

  def __init__(self, city, temperature, condition, humidity):
    self.city = city
    self.temperature = temperature
    self.condition = condition
    self.humidity = humidity

  @classmethod
  def from_dict(cls, data):
    """
    Creates a WeatherData object from a dictionary.

    Args:
      data (dict): Dictionary containing weather data.

    Returns:
      WeatherData: A WeatherData object or None if data is invalid.
    """
    if not all(key in data for key in ("city", "temperature", "condition", "humidity")):
      return None
    return cls(data["city"], data["temperature"], data["condition"], data["humidity"])

# Replace this with your actual API interaction code
# (assuming a simulated API for simplicity)

SIMULATED_DATA = {
    "New York": {"temperature": 70, "condition": "Sunny", "humidity": 50},
    "London": {"temperature": 60, "condition": "Cloudy", "humidity": 65},
    "Tokyo": {"temperature": 75, "condition": "Rainy", "humidity": 70}
}

def fetch_weather_data(city):
  """
  Fetches weather data for a city (simulated for now).

  Args:
    city (str): The city name.

  Returns:
    dict: A dictionary containing weather data or None if not found.
  """
  return SIMULATED_DATA.get(city, None)

from weather_data import WeatherData

def parse_weather_data(data):
  """
  Parses weather data and creates a formatted string.

  Args:
    data (dict): Dictionary containing weather data.

  Returns:
    str: A formatted weather report or "Weather data not available" if invalid.
  """
  weather_object = WeatherData.from_dict(data)
  if not weather_object:
    return "Weather data not available"
  return f"Weather in {weather_object.city}: {weather_object.temperature} degrees, {weather_object.condition}, Humidity: {weather_object.humidity}%"

from weather_api import fetch_weather_data
from weather_forecast import parse_weather_data

def get_detailed_forecast(city):
  """
  Provides a detailed weather forecast for a city.

  Args:
    city (str): The city name.

  Returns:
    str: A formatted weather report.
  """
  data = fetch_weather_data(city)
  return parse_weather_data(data)

def display_weather(city):
  """
  Displays the basic weather forecast for a city.

  Args:
    city (str): The city name.

  Returns:
    str: A formatted weather report or a message indicating no data.
  """
  data = fetch_weather_data(city)
  return parse_weather_data(data)

def main():
  while True:
    city = input("Enter the city to get the weather forecast or 'exit' to quit: ")
    if city.lower() == 'exit':
      break
    detailed = input("Do you want a detailed forecast? (yes/no): ").lower()
    if detailed == 'yes':
      forecast = get_detailed_forecast(city)
    else:
      forecast = display_weather(city)
    print(forecast)

if __name__ == "__main__":
  main()
