#!/usr/bin/env python3
"""
Daily News Runner Script
Automatically fetches and saves daily news to a file
Can be scheduled with cron or task scheduler
"""

import os
import sys
from datetime import datetime
from news_feed import NewsFeedApp


def run_daily_news(output_dir='daily_news', categories=None):
    """
    Fetch and save daily news automatically.
    
    Args:
        output_dir: Directory to save news files (default: 'daily_news' in current directory)
        categories: List of categories to fetch (default: all major categories)
    """
    # Default categories if none specified
    if categories is None:
        categories = ['general', 'business', 'technology', 'science', 'health']
    
    # Create output directory if it doesn't exist
    os.makedirs(output_dir, exist_ok=True)
    
    # Get API key
    api_key = os.getenv('NEWS_API_KEY')
    
    if not api_key:
        print("WARNING: No API key found. Running in demo mode.")
        print("Set NEWS_API_KEY environment variable for real news.")
    
    # Initialize app
    app = NewsFeedApp(api_key)
    
    # Get current date
    date_str = datetime.now().strftime('%Y-%m-%d')
    
    print(f"\n{'='*80}")
    print(f"Daily News Runner - {date_str}")
    print(f"{'='*80}\n")
    
    # Fetch and save news for each category
    for category in categories:
        print(f"Fetching {category} news...")
        
        try:
            # Fetch news
            data = app.fetch_top_headlines(
                country='us',
                category=category,
                page_size=20
            )
            
            # Save to file
            filename = os.path.join(
                output_dir,
                f"news_{category}_{date_str}.json"
            )
            app.save_to_file(data, filename=filename)
            
            # Print summary
            total = data.get('totalResults', 0)
            articles_fetched = len(data.get('articles', []))
            print(f"  ✓ {category.capitalize()}: {articles_fetched} articles saved")
            
        except Exception as e:
            print(f"  ✗ Error fetching {category} news: {e}")
    
    # Also fetch top headlines
    print("\nFetching top headlines...")
    try:
        data = app.fetch_top_headlines(country='us', page_size=30)
        filename = os.path.join(output_dir, f"news_top_headlines_{date_str}.json")
        app.save_to_file(data, filename=filename)
        
        articles_fetched = len(data.get('articles', []))
        print(f"  ✓ Top Headlines: {articles_fetched} articles saved")
    except Exception as e:
        print(f"  ✗ Error fetching top headlines: {e}")
    
    print(f"\n{'='*80}")
    print(f"Daily news saved to: {output_dir}")
    print(f"{'='*80}\n")


if __name__ == "__main__":
    # Parse command line arguments
    output_dir = sys.argv[1] if len(sys.argv) > 1 else 'daily_news'
    
    # Run daily news fetch
    run_daily_news(output_dir=output_dir)
