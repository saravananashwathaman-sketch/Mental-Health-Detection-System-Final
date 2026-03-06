from flask import Blueprint, render_template
from app.routes.auth import login_required

games_bp = Blueprint("games", __name__)

@games_bp.route("/games")
@login_required
def index():
    """Render the main Games Hub dashboard."""
    return render_template("games/index.html")

@games_bp.route("/games/bubble-pop")
@login_required
def bubble_pop():
    """Route for individual game if needed, though we can handle them in one template."""
    return render_template("games/bubble_pop.html")

@games_bp.route("/games/memory-match")
@login_required
def memory_match():
    return render_template("games/memory_match.html")

@games_bp.route("/games/breath-harmony")
@login_required
def breath_harmony():
    return render_template("games/breath_harmony.html")

@games_bp.route("/games/snake")
@login_required
def snake():
    return render_template("games/snake.html")
