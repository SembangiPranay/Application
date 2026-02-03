#!/usr/bin/env python3
"""
Test script for News Feed Application
"""

import sys
import tempfile
import os
from news_feed import NewsFeedApp


def test_news_feed_app():
    """Test the news feed application functionality."""
    print("Testing News Feed Application...")
    print("-" * 80)
    
    # Test 1: Initialize app without API key
    print("\n[Test 1] Initialize app without API key...")
    app = NewsFeedApp()
    assert app is not None
    print("✓ Passed: App initialized successfully")
    
    # Test 2: Initialize app with API key
    print("\n[Test 2] Initialize app with API key...")
    app = NewsFeedApp(api_key="test_key_123")
    assert app.api_key == "test_key_123"
    print("✓ Passed: App initialized with API key")
    
    # Test 3: Get demo news
    print("\n[Test 3] Get demo news...")
    demo_data = app._get_demo_news()
    assert demo_data['status'] == 'ok'
    assert 'articles' in demo_data
    assert len(demo_data['articles']) > 0
    print(f"✓ Passed: Got {len(demo_data['articles'])} demo articles")
    
    # Test 4: Display articles
    print("\n[Test 4] Display articles...")
    try:
        app.display_articles(demo_data)
        print("✓ Passed: Articles displayed successfully")
    except Exception as e:
        print(f"✗ Failed: {e}")
        return False
    
    # Test 5: Save to file
    print("\n[Test 5] Save to file...")
    test_filename = os.path.join(tempfile.gettempdir(), "test_news.json")
    try:
        app.save_to_file(demo_data, filename=test_filename)
        print(f"✓ Passed: News saved to {test_filename}")
        
        # Verify file exists
        if os.path.exists(test_filename):
            print("✓ Passed: File exists")
            os.remove(test_filename)  # Clean up
        else:
            print("✗ Failed: File not created")
            return False
    except Exception as e:
        print(f"✗ Failed: {e}")
        return False
    
    # Test 6: Fetch top headlines (will use demo mode without internet)
    print("\n[Test 6] Fetch top headlines...")
    try:
        data = app.fetch_top_headlines(country="us")
        assert 'articles' in data
        print("✓ Passed: Headlines fetched successfully")
    except Exception as e:
        print(f"✗ Failed: {e}")
        return False
    
    # Test 7: Search news (will use demo mode without internet)
    print("\n[Test 7] Search news...")
    try:
        data = app.fetch_everything(query="technology")
        assert 'articles' in data
        print("✓ Passed: News search completed successfully")
    except Exception as e:
        print(f"✗ Failed: {e}")
        return False
    
    print("\n" + "=" * 80)
    print("All tests passed! ✓")
    print("=" * 80)
    return True


if __name__ == "__main__":
    success = test_news_feed_app()
    sys.exit(0 if success else 1)
