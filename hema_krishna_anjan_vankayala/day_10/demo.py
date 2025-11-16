#!/usr/bin/env python3
"""
Quick Start Guide for Library Management System
Run this script to see a demo of the LMS capabilities
"""

import library
import storage

def demo():
    print("\n" + "=" * 70)
    print("🎓 LIBRARY MANAGEMENT SYSTEM - QUICK DEMO 🎓")
    print("=" * 70)
    
    # 1. Show books
    print("\n📚 1. DISPLAYING ALL BOOKS IN LIBRARY:")
    print("-" * 70)
    books = library.list_books()
    print(f"Total Books Available: {len(books)}")
    print("\nFirst 5 Books:")
    for i, book in enumerate(books[:5], 1):
        print(f"  {i}. {book['title']} by {book['authors']}")
        print(f"     Copies: {book['available_copies']}/{book['total_copies']}")
    
    # 2. Show users
    print("\n\n👥 2. DISPLAYING ALL USERS IN SYSTEM:")
    print("-" * 70)
    users = library.list_users()
    print(f"Total Users Registered: {len(users)}")
    print("\nFirst 5 Users:")
    for i, user in enumerate(users[:5], 1):
        print(f"  {i}. {user['name']} (ID: {user['user_id']})")
        print(f"     Status: {user['status']} | Max Loans: {user['max_loans']}")
    
    # 3. Search books
    print("\n\n🔍 3. SEARCHING FOR BOOKS:")
    print("-" * 70)
    search_results = library.search_books("python")
    print(f"Search Results for 'python': {len(search_results)} books found")
    for book in search_results[:3]:
        print(f"  • {book['title']}")
    
    # 4. Get specific user
    print("\n\n👤 4. RETRIEVING USER DETAILS:")
    print("-" * 70)
    user = library.get_user('U2001')
    if isinstance(user, dict):
        print(f"User Name: {user['name']}")
        print(f"Email: {user['email']}")
        print(f"Status: {user['status']}")
        print(f"Max Loans: {user['max_loans']}")
        print(f"Active Loans: {user.get('active_loans', 0)}")
    
    # 5. Get specific book
    print("\n\n📖 5. RETRIEVING BOOK DETAILS:")
    print("-" * 70)
    book = library.get_book('B1001')
    if isinstance(book, dict):
        print(f"Title: {book['title']}")
        print(f"Author(s): {book['authors']}")
        print(f"ISBN: {book['isbn']}")
        print(f"Tags: {book['tags']}")
        print(f"Available: {book['available_copies']}/{book['total_copies']}")
    
    # 6. Statistics
    print("\n\n📊 6. LIBRARY STATISTICS:")
    print("-" * 70)
    total_copies = sum(int(b.get('total_copies', 0)) for b in books)
    available_copies = sum(int(b.get('available_copies', 0)) for b in books)
    active_users = len([u for u in users if u.get('status') == 'active'])
    
    print(f"Total Books: {len(books)}")
    print(f"Total Users: {len(users)}")
    print(f"Active Users: {active_users}")
    print(f"Books Available: {available_copies}/{total_copies}")
    print(f"Utilization Rate: {((total_copies - available_copies) / total_copies * 100):.1f}%")
    
    print("\n" + "=" * 70)
    print("✅ DEMO COMPLETE!")
    print("=" * 70)
    print("\n💡 TIP: Run 'python lms.py' to start the interactive application!")
    print("\n")

if __name__ == "__main__":
    try:
        demo()
    except Exception as e:
        print(f"\n❌ Error during demo: {str(e)}")
        print("Please check if all data files are in place.")
