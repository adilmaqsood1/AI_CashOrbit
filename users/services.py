from django.contrib.auth.models import User
from django.db.models import Q


class UserService:
    """
    Service class for handling user-related business logic.
    This separates business logic from views for better maintainability.
    """
    
    def get_dashboard_data(self, user):
        """
        Retrieve dashboard data specific to the user.
        This will be expanded as more apps are integrated.
        """
        return {
            'user_info': {
                'username': user.username,
                'full_name': f"{user.first_name} {user.last_name}",
                'email': user.email,
                'date_joined': user.date_joined,
                'last_login': user.last_login
            },
            # Placeholder for financial summary data
            'financial_summary': {
                'total_income': 0,
                'total_expenses': 0,
                'balance': 0,
                'pending_invoices': 0
            },
            # Placeholder for recent activity
            'recent_activity': [],
            # Placeholder for upcoming tasks/reminders
            'upcoming_tasks': []
        }
    
    def search_users(self, query):
        """
        Search for users based on a query string.
        Useful for admin features or team collaboration.
        """
        return User.objects.filter(
            Q(username__icontains=query) |
            Q(first_name__icontains=query) |
            Q(last_name__icontains=query) |
            Q(email__icontains=query)
        )


# Create a singleton instance for import in other modules
user_service = UserService()