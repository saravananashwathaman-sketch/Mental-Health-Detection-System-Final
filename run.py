"""
run.py — Application entry point.
Run this file to start the Flask development server.

Usage:
    python run.py
"""

from app import create_app
import os

# Allow OAuth over plain HTTP in local development.
# REMOVE this line (or set to 0) in production where HTTPS is used.
os.environ.setdefault("OAUTHLIB_INSECURE_TRANSPORT", "1")


app = create_app()

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
