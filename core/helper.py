# ========== IMPORTS ==========
from django.utils import translation
# =============================

# ========== SET USER LANGUAGE ==========
def set_user_language(request):
    """
    Set the user's language based on the 'lang' parameter in the request.

    Args:
    - request (HttpRequest): The HTTP request object.

    Returns:
    - None
    """
    try:
        # Default language
        user_language = request.LANGUAGE_CODE

        # Check if 'lang' parameter is in the request
        if 'lang' in request.GET:
            user_language = request.GET['lang']

        # Activate and store the user's language preference
        translation.activate(user_language)
        request.session[translation.LANGUAGE_SESSION_KEY] = user_language
    except Exception as e:
        # Log the error or print it
        print(str(e))
# =======================================
