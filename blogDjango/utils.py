from rest_framework.permissions import IsAuthenticated

class IsAuthenticatedForPostOnly(IsAuthenticated):
    def has_permission(self, request, view):
        # Allow unauthenticated access for GET requests
        if request.method == 'GET':
            return True
        # Apply authentication for other methods (e.g., POST)
        return super().has_permission(request, view)
