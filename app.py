from flask import Flask, request, jsonify, send_from_directory
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
CORS(app)

# Database configuration (SQLite)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///invitations.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

# Directory to store uploaded images
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Define the database model
class Invitation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    location = db.Column(db.String(200), nullable=False)
    picture_url = db.Column(db.String(300), nullable=False)

# Create the database tables
with app.app_context():
    db.create_all()

@app.route('/send-invite', methods=['POST'])
def send_invite():
    name = request.form.get("name")
    age = request.form.get("age")
    location = request.form.get("location")
    picture = request.files.get("picture")

    if not name or not age or not location or not picture:
        return jsonify({"error": "All fields are required!"}), 400

    # Save the uploaded image
    picture_filename = f"{name.replace(' ', '_')}_picture.jpg"
    picture_path = os.path.join(app.config["UPLOAD_FOLDER"], picture_filename)
    picture.save(picture_path)

    # Save invitation in database
    new_invite = Invitation(name=name, age=int(age), location=location, picture_url=f"/uploads/{picture_filename}")
    db.session.add(new_invite)
    db.session.commit()

    return jsonify({"message": "Invitation sent successfully!", "invitation": {
        "name": name, "age": age, "location": location, "picture_url": f"/uploads/{picture_filename}"
    }})

@app.route('/invitations', methods=['GET'])
def get_invitations():
    invitations = Invitation.query.all()
    return jsonify({
        "invitations": [
            {"name": inv.name, "age": inv.age, "location": inv.location, "picture_url": inv.picture_url} 
            for inv in invitations
        ]
    })

# Route to serve uploaded images
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config["UPLOAD_FOLDER"], filename)

if __name__ == '__main__':
    app.run(debug=True)
