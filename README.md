# Greetings
Hare Krshn

# About
Prints random sloak from श्रीमद्भगवद्गीता (Bhagavad Gita) 


There are two scripts
[main.py](/main.py) - This creates a binary file in python which contains all the lessons of Bhagavad Gita .
[shloka](/shloka)  - Prints a random verse from Bhagavad Gita .

Most of the code is copied from [this](https://github.com/sayampradhan/Bhagvad-Geeta-Quotes) repo.

# Feature
Can print random verses from Bhagavad Gita offline once downloaded  

## Prerequisites

- Python 3.x
- `requests` library (install using `pip install requests`)

## Installation

1. Clone the repository:
```git clone https://github.com/your_username/your_repository.git```

2. Change to the project directory:
```cd your_repository```

3. Install the required `requests` library:
```pip install requests```

## Usage
Run the main.py script with an active internet connection using the following command:
```python3 main.py```
After the completion of download you can now run shloka using the following command:
```python3 shloka```
And it will print a random verse each time.

## API Key
To use the Bhagavad Gita API, you need an API key. Follow the steps below to obtain one:

1. Visit the RapidAPI Bhagavad Gita API page.
2. Sign up for a RapidAPI account (if you don't have one).
3. Subscribe to the Bhagavad Gita API and obtain your API key.
4. Replace the placeholder API key in the Python script with your actual API key.

```headers = {
    "X-RapidAPI-Key": "your_api_key",
    "X-RapidAPI-Host": "bhagavad-gita3.p.rapidapi.com"
}
```
Make sure to keep your API key secure and avoid committing it to version control.

## Contributing
Contributions are welcome! If you have any suggestions or improvements, please open an issue or submit a pull request.

## [License](/LICENSE)
This project is licensed under the MIT License. 

## Security side
Please don't accept any [pickled binary file](https://docs.python.org/3/library/pickle.html) from anyone as it has a potential [vulnerability](https://docs.python.org/3/library/pickle.html) always create your own binary file by using [main.py](/main.py)
