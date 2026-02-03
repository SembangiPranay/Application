#!/usr/bin/env python3
"""
Example usage script for the Daily News Feed Application
Demonstrates various ways to use the news feed programmatically
"""

from news_feed import NewsFeedApp
import os
import tempfile


def example_top_headlines():
    """Example: Fetch and display top headlines."""
    print("\n" + "="*80)
    print("EXAMPLE 1: Fetching Top Headlines")
    print("="*80)
    
    api_key = os.getenv('NEWS_API_KEY')
    app = NewsFeedApp(api_key)
    
    # Fetch top headlines from US
    data = app.fetch_top_headlines(country='us', page_size=5)
    app.display_articles(data)


def example_category_news():
    """Example: Fetch news by category."""
    print("\n" + "="*80)
    print("EXAMPLE 2: Fetching Technology News")
    print("="*80)
    
    api_key = os.getenv('NEWS_API_KEY')
    app = NewsFeedApp(api_key)
    
    # Fetch technology news
    data = app.fetch_top_headlines(country='us', category='technology', page_size=5)
    app.display_articles(data)


def example_search_news():
    """Example: Search for specific topics."""
    print("\n" + "="*80)
    print("EXAMPLE 3: Searching for 'Python Programming'")
    print("="*80)
    
    api_key = os.getenv('NEWS_API_KEY')
    app = NewsFeedApp(api_key)
    
    # Search for Python programming news
    data = app.fetch_everything(query='Python programming', page_size=5)
    app.display_articles(data)


def example_save_to_file():
    """Example: Fetch news and save to file."""
    print("\n" + "="*80)
    print("EXAMPLE 4: Saving News to File")
    print("="*80)
    
    api_key = os.getenv('NEWS_API_KEY')
    app = NewsFeedApp(api_key)
    
    # Fetch and save business news
    data = app.fetch_top_headlines(country='us', category='business', page_size=10)
    app.display_articles(data)
    
    # Save to file
    filename = os.path.join(tempfile.gettempdir(), 'business_news.json')
    app.save_to_file(data, filename=filename)
    print(f"\nNews saved to: {filename}")


def main():
    """Run all examples."""
    print("Daily News Feed - Usage Examples")
    print("="*80)
    print("\nNote: These examples will use demo mode if no API key is set.")
    print("To use real news, set the NEWS_API_KEY environment variable.")
    
    # Run examples
    example_top_headlines()
    
    input("\nPress Enter to continue to the next example...")
    example_category_news()
    
    input("\nPress Enter to continue to the next example...")
    example_search_news()
    
    input("\nPress Enter to continue to the next example...")
    example_save_to_file()
    
    print("\n" + "="*80)
    print("Examples completed!")
    print("="*80)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nExiting examples...")
