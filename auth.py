import os
from dotenv import load_dotenv
from supabase import create_client

# Load environment variables from .env file
load_dotenv()

# Retrieve Supabase config from environment
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")

# Create Supabase client
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

def sign_in(email, password):
    """Sign in user via Supabase"""
    return supabase.auth.sign_in_with_password({
        "email": email,
        "password": password
    })

def sign_up(email, password):
    """Register user via Supabase"""
    return supabase.auth.sign_up({
        "email": email,
        "password": password
    })

def get_user_role(user):
    """Return 'pro' if user is authenticated; else 'guest'"""
    if user:
        return "pro"
    return "guest"
