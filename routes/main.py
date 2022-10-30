from app import app
from flask import render_template
from models.models import Plant


@app.route("/")
def main():
    plants = Plant.query.order_by(Plant.id.desc()).all()#allбере всі обєкти
    # plants = Plant.query.filter(Plant.location == "Zrini 65")#filter бере по фільтру в нашому випадку в класі Plant  по локації (location) - Zrini 65
    return render_template('index.html', plants=plants)


