#!/usr/bin/env python
"""
Database Viewer for BussuTech
View all users and form submissions in the database
"""

from backend.app import app
from backend.models import User, FormSubmission
from datetime import datetime

def print_users():
    """Display all users"""
    print("\n" + "="*80)
    print("👥 USERS IN DATABASE")
    print("="*80)
    
    users = User.query.all()
    
    if not users:
        print("No users yet.\n")
        return
    
    print(f"\nTotal Users: {len(users)}\n")
    print(f"{'ID':<5} {'Name':<25} {'Email':<30} {'Newsletter':<12} {'Created':<20}")
    print("-"*92)
    
    for user in users:
        name = f"{user.first_name} {user.last_name}"
        newsletter = "Yes" if user.newsletter_subscribed else "No"
        created = user.created_at.strftime("%Y-%m-%d %H:%M:%S") if user.created_at else "N/A"
        print(f"{user.id:<5} {name:<25} {user.email:<30} {newsletter:<12} {created:<20}")
    print()

def print_submissions():
    """Display all form submissions"""
    print("\n" + "="*80)
    print("📝 FORM SUBMISSIONS IN DATABASE")
    print("="*80)
    
    submissions = FormSubmission.query.all()
    
    if not submissions:
        print("No submissions yet.\n")
        return
    
    print(f"\nTotal Submissions: {len(submissions)}\n")
    
    for idx, sub in enumerate(submissions, 1):
        status_emoji = {
            'new': '🆕',
            'read': '👀',
            'replied': '✉️',
            'resolved': '✅'
        }.get(sub.status, '❓')
        
        print(f"{idx}. {status_emoji} {sub.subject}")
        print(f"   From: {sub.name} ({sub.email})")
        print(f"   Category: {sub.category}")
        print(f"   Status: {sub.status}")
        print(f"   Date: {sub.created_at.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"   Message: {sub.message[:60]}{'...' if len(sub.message) > 60 else ''}")
        print()

def print_statistics():
    """Print database statistics"""
    print("\n" + "="*80)
    print("📊 DATABASE STATISTICS")
    print("="*80)
    
    user_count = User.query.count()
    submission_count = FormSubmission.query.count()
    newsletter_count = User.query.filter_by(newsletter_subscribed=True).count()
    
    submission_statuses = {}
    for status in ['new', 'read', 'replied', 'resolved']:
        count = FormSubmission.query.filter_by(status=status).count()
        submission_statuses[status] = count
    
    print(f"\n📌 Users: {user_count}")
    print(f"📌 Newsletter Subscribers: {newsletter_count}")
    print(f"📌 Form Submissions: {submission_count}")
    print(f"   - New: {submission_statuses['new']}")
    print(f"   - Read: {submission_statuses['read']}")
    print(f"   - Replied: {submission_statuses['replied']}")
    print(f"   - Resolved: {submission_statuses['resolved']}")
    print()

def delete_all_data():
    """Delete all data from database"""
    from backend.models import db
    
    print("\n⚠️  WARNING: This will DELETE all users and submissions!")
    response = input("Are you sure? Type 'yes' to confirm: ").strip().lower()
    
    if response == 'yes':
        with app.app_context():
            db.session.query(FormSubmission).delete()
            db.session.query(User).delete()
            db.session.commit()
        print("✅ All data deleted!\n")
    else:
        print("❌ Cancelled.\n")

def delete_user(user_id):
    """Delete a specific user"""
    with app.app_context():
        user = User.query.get(user_id)
        if not user:
            print(f"❌ User {user_id} not found.\n")
            return
        
        name = f"{user.first_name} {user.last_name}"
        response = input(f"Delete user '{name}'? (yes/no): ").strip().lower()
        
        if response == 'yes':
            from backend.models import db
            db.session.delete(user)
            db.session.commit()
            print(f"✅ User {user_id} deleted!\n")
        else:
            print("❌ Cancelled.\n")

def delete_submission(sub_id):
    """Delete a specific submission"""
    with app.app_context():
        sub = FormSubmission.query.get(sub_id)
        if not sub:
            print(f"❌ Submission {sub_id} not found.\n")
            return
        
        response = input(f"Delete submission '{sub.subject}'? (yes/no): ").strip().lower()
        
        if response == 'yes':
            from backend.models import db
            db.session.delete(sub)
            db.session.commit()
            print(f"✅ Submission {sub_id} deleted!\n")
        else:
            print("❌ Cancelled.\n")

def update_submission_status(sub_id, new_status):
    """Update submission status"""
    valid_statuses = ['new', 'read', 'replied', 'resolved']
    
    if new_status not in valid_statuses:
        print(f"❌ Invalid status. Must be one of: {', '.join(valid_statuses)}\n")
        return
    
    with app.app_context():
        sub = FormSubmission.query.get(sub_id)
        if not sub:
            print(f"❌ Submission {sub_id} not found.\n")
            return
        
        sub.status = new_status
        from backend.models import db
        db.session.commit()
        print(f"✅ Submission {sub_id} status updated to '{new_status}'!\n")

def main():
    """Main menu"""
    with app.app_context():
        while True:
            print("\n" + "="*80)
            print("🗄️  BussuTech Database Viewer")
            print("="*80)
            print("\nOptions:")
            print("1. View all users")
            print("2. View all form submissions")
            print("3. View database statistics")
            print("4. Update submission status")
            print("5. Delete specific user")
            print("6. Delete specific submission")
            print("7. Delete ALL data (⚠️ careful!)")
            print("8. Exit")
            print()
            
            choice = input("Select option (1-8): ").strip()
            
            if choice == '1':
                print_users()
            elif choice == '2':
                print_submissions()
            elif choice == '3':
                print_statistics()
            elif choice == '4':
                sub_id = input("Submission ID: ").strip()
                new_status = input("New status (new/read/replied/resolved): ").strip()
                try:
                    update_submission_status(int(sub_id), new_status)
                except ValueError:
                    print("❌ Invalid ID.\n")
            elif choice == '5':
                user_id = input("User ID to delete: ").strip()
                try:
                    delete_user(int(user_id))
                except ValueError:
                    print("❌ Invalid ID.\n")
            elif choice == '6':
                sub_id = input("Submission ID to delete: ").strip()
                try:
                    delete_submission(int(sub_id))
                except ValueError:
                    print("❌ Invalid ID.\n")
            elif choice == '7':
                delete_all_data()
            elif choice == '8':
                print("\nGoodbye! 👋\n")
                break
            else:
                print("❌ Invalid option. Please try again.\n")

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nExiting...\n")
