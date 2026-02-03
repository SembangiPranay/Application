#!/usr/bin/env python3
"""
Daily News Feed Application
Fetches and displays the latest news articles from various sources.
"""

import requests
import json
import os
from datetime import datetime
from typing import List, Dict, Optional


class NewsFeedApp:
    """A simple news feed application that fetches daily news."""
    
    def __init__(self, api_key: Optional[str] = None):
        """
        Initialize the News Feed application.
        
        Args:
            api_key: Optional API key for NewsAPI. If not provided, will use free tier.
        """
        self.api_key = api_key
        self.base_url = "https://newsapi.org/v2"
        
    def fetch_top_headlines(self, country: str = "us", category: Optional[str] = None, 
                           page_size: int = 10) -> Dict:
        """
        Fetch top headlines from NewsAPI.
        
        Args:
            country: Country code (e.g., 'us', 'gb', 'in')
            category: News category (e.g., 'business', 'technology', 'sports')
            page_size: Number of articles to fetch (max 100)
            
        Returns:
            Dictionary containing articles and metadata
        """
        endpoint = f"{self.base_url}/top-headlines"
        params = {
            'country': country,
            'pageSize': page_size
        }
        
        if category:
            params['category'] = category
            
        if self.api_key:
            params['apiKey'] = self.api_key
        
        try:
            response = requests.get(endpoint, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching news: {e}")
            return self._get_demo_news()
    
    def fetch_everything(self, query: str, page_size: int = 10) -> Dict:
        """
        Search for news articles by query.
        
        Args:
            query: Search query
            page_size: Number of articles to fetch
            
        Returns:
            Dictionary containing articles and metadata
        """
        endpoint = f"{self.base_url}/everything"
        params = {
            'q': query,
            'pageSize': page_size,
            'sortBy': 'publishedAt'
        }
        
        if self.api_key:
            params['apiKey'] = self.api_key
        
        try:
            response = requests.get(endpoint, params=params)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error searching news: {e}")
            return self._get_demo_news()
    
    def _get_demo_news(self) -> Dict:
        """
        Return demo news data when API is unavailable or no API key is provided.
        
        Returns:
            Dictionary with demo news articles
        """
        return {
            'status': 'ok',
            'totalResults': 3,
            'articles': [
                {
                    'source': {'id': 'demo', 'name': 'Demo Source'},
                    'author': 'Demo Author',
                    'title': 'Welcome to News Feed Application',
                    'description': 'This is a demo article. Configure your NewsAPI key to fetch real news.',
                    'url': 'https://newsapi.org',
                    'publishedAt': datetime.now().isoformat(),
                    'content': 'To get real news, sign up at newsapi.org and set your API key.'
                },
                {
                    'source': {'id': 'demo', 'name': 'Demo Source'},
                    'author': 'Demo Author',
                    'title': 'Daily News Feed Features',
                    'description': 'Fetch top headlines, search news, and stay updated.',
                    'url': 'https://newsapi.org',
                    'publishedAt': datetime.now().isoformat(),
                    'content': 'This application supports fetching top headlines and searching for specific topics.'
                },
                {
                    'source': {'id': 'demo', 'name': 'Demo Source'},
                    'author': 'Demo Author',
                    'title': 'Getting Started',
                    'description': 'Easy to use command-line interface for daily news.',
                    'url': 'https://newsapi.org',
                    'publishedAt': datetime.now().isoformat(),
                    'content': 'Run the application from command line to get your daily news feed.'
                }
            ]
        }
    
    def display_articles(self, data: Dict) -> None:
        """
        Display news articles in a formatted way.
        
        Args:
            data: Dictionary containing articles from API response
        """
        if data.get('status') != 'ok':
            print("Error: Unable to fetch news")
            return
        
        articles = data.get('articles', [])
        total_results = data.get('totalResults', 0)
        
        print("\n" + "="*80)
        print(f"📰 DAILY NEWS FEED - {datetime.now().strftime('%B %d, %Y')}")
        print(f"Total Results: {total_results}")
        print("="*80 + "\n")
        
        for i, article in enumerate(articles, 1):
            print(f"[{i}] {article.get('title', 'No title')}")
            print(f"    Source: {article.get('source', {}).get('name', 'Unknown')}")
            
            if article.get('author'):
                print(f"    Author: {article.get('author')}")
            
            if article.get('description'):
                print(f"    Description: {article.get('description')}")
            
            published_at = article.get('publishedAt', '')
            if published_at:
                try:
                    dt = datetime.fromisoformat(published_at.replace('Z', '+00:00'))
                    print(f"    Published: {dt.strftime('%Y-%m-%d %H:%M:%S')}")
                except:
                    print(f"    Published: {published_at}")
            
            if article.get('url'):
                print(f"    URL: {article.get('url')}")
            
            print()
    
    def save_to_file(self, data: Dict, filename: str = None) -> None:
        """
        Save news articles to a JSON file.
        
        Args:
            data: Dictionary containing articles
            filename: Output filename (default: news_YYYYMMDD.json)
        """
        if filename is None:
            filename = f"news_{datetime.now().strftime('%Y%m%d')}.json"
        
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            print(f"\n✓ News saved to {filename}")
        except Exception as e:
            print(f"Error saving to file: {e}")


def main():
    """Main function to run the news feed application."""
    print("Daily News Feed Application")
    print("-" * 80)
    
    # Try to load API key from environment variable
    api_key = os.getenv('NEWS_API_KEY')
    
    if not api_key:
        print("Note: No API key found. Using demo mode.")
        print("To use real news, get a free API key from https://newsapi.org")
        print("and set the NEWS_API_KEY environment variable.\n")
    
    # Create news feed app
    app = NewsFeedApp(api_key)
    
    # Display menu
    print("\nSelect an option:")
    print("1. Top Headlines (US)")
    print("2. Top Headlines by Category")
    print("3. Search News by Topic")
    print("4. Exit")
    
    try:
        choice = input("\nEnter your choice (1-4): ").strip()
        
        if choice == '1':
            print("\nFetching top headlines...")
            data = app.fetch_top_headlines()
            app.display_articles(data)
            
            save = input("\nSave to file? (y/n): ").strip().lower()
            if save == 'y':
                app.save_to_file(data)
        
        elif choice == '2':
            print("\nCategories: business, entertainment, general, health, science, sports, technology")
            category = input("Enter category: ").strip().lower()
            
            print(f"\nFetching {category} headlines...")
            data = app.fetch_top_headlines(category=category)
            app.display_articles(data)
            
            save = input("\nSave to file? (y/n): ").strip().lower()
            if save == 'y':
                app.save_to_file(data)
        
        elif choice == '3':
            query = input("Enter search topic: ").strip()
            
            print(f"\nSearching for '{query}'...")
            data = app.fetch_everything(query)
            app.display_articles(data)
            
            save = input("\nSave to file? (y/n): ").strip().lower()
            if save == 'y':
                app.save_to_file(data)
        
        elif choice == '4':
            print("\nGoodbye!")
            return
        
        else:
            print("\nInvalid choice!")
    
    except KeyboardInterrupt:
        print("\n\nExiting...")
    except Exception as e:
        print(f"\nAn error occurred: {e}")


if __name__ == "__main__":
    main()
