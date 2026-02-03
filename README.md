# Daily News Feed Application

A Python application that fetches and displays daily news from various sources using the NewsAPI.

## Features

- 📰 Fetch top headlines from various countries
- 🔍 Search news by topic or keyword
- 📑 Browse news by category (business, technology, sports, etc.)
- 💾 Save news articles to JSON files
- 🎯 Simple command-line interface
- 🔄 Daily news updates

## Installation

1. Clone the repository:
```bash
git clone https://github.com/SembangiPranay/Application.git
cd Application
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. (Optional) Get a free API key from [NewsAPI.org](https://newsapi.org) and configure it:
```bash
cp .env.example .env
# Edit .env and add your API key
```

Alternatively, set the environment variable directly:
```bash
export NEWS_API_KEY=your_api_key_here
```

## Usage

Run the application:
```bash
python news_feed.py
```

Or make it executable:
```bash
chmod +x news_feed.py
./news_feed.py
```

### Options

The application provides several options:
1. **Top Headlines (US)** - Get the latest top headlines from the United States
2. **Top Headlines by Category** - Filter news by category (business, technology, sports, etc.)
3. **Search News by Topic** - Search for specific news topics or keywords
4. **Exit** - Close the application

### Demo Mode

If no API key is configured, the application runs in demo mode with sample news articles. This allows you to test the application without signing up for an API key.

## Examples

### Fetch Top Headlines
```python
from news_feed import NewsFeedApp

app = NewsFeedApp(api_key="your_api_key")
data = app.fetch_top_headlines(country="us")
app.display_articles(data)
```

### Search for Specific Topics
```python
app = NewsFeedApp(api_key="your_api_key")
data = app.fetch_everything(query="technology")
app.display_articles(data)
```

### Save News to File
```python
app = NewsFeedApp(api_key="your_api_key")
data = app.fetch_top_headlines()
app.save_to_file(data, filename="today_news.json")
```

## Requirements

- Python 3.6+
- requests
- python-dotenv

## API Information

This application uses the [NewsAPI](https://newsapi.org/) service:
- Free tier: 100 requests per day
- Supports 150+ news sources
- Coverage of 50+ countries

## Project Structure

```
Application/
├── news_feed.py          # Main application file
├── requirements.txt      # Python dependencies
├── .env.example         # Configuration template
├── .gitignore           # Git ignore rules
└── README.md            # This file
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is open source and available under the MIT License.
