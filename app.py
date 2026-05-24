from flask import Flask, jsonify, request

app = Flask(__name__)

# Simulated data
class Event:
    def __init__(self, id, title):
        self.id = id
        self.title = title

    def to_dict(self):
        return {"id": self.id, "title": self.title}

# In-memory "database"
events = [
    Event(1, "Tech Meetup"),
    Event(2, "Python Workshop")
]

# Helper function
def find_event(event_id):
    for event in events:
        if event.id == event_id:
            return event
    return None

# TODO: Task 1 - Define the Problem
# Create a new event from JSON input
@app.route("/events", methods=["POST"])
def create_event():
    # TODO: Task 2 - Design and Develop the Code
    # TODO: Task 3 - Implement the Loop and Process Each Element
    # TODO: Task 4 - Return and Handle Results
    data = request.get_json()

    # Validate title exists
    if not data or "title" not in data:
        return jsonify({"error": "Title is required"}), 400

    # Create new ID
    new_id = max([event.id for event in events], default=0) + 1

    # Create event
    new_event = Event(new_id, data["title"])

    # Add to list
    events.append(new_event)

    return jsonify(new_event.to_dict()), 201


# TODO: Task 1 - Define the Problem
# Update the title of an existing event
@app.route("/events/<int:event_id>", methods=["PATCH"])
def update_event(event_id):
    # TODO: Task 2 - Design and Develop the Code
    # TODO: Task 3 - Implement the Loop and Process Each Element
    # TODO: Task 4 - Return and Handle Results
    
    event = find_event(event_id)

    # Event not found
    if not event:
        return jsonify({"error": "Event not found"}), 404

    data = request.get_json()

    # Validate title exists
    if not data or "title" not in data:
        return jsonify({"error": "Title is required"}), 400

    # Update title
    event.title = data["title"]

    return jsonify(event.to_dict()), 200


# TODO: Task 1 - Define the Problem
# Remove an event from the list
@app.route("/events/<int:event_id>", methods=["DELETE"])
def delete_event(event_id):
    # TODO: Task 2 - Design and Develop the Code
    # TODO: Task 3 - Implement the Loop and Process Each Element
    # TODO: Task 4 - Return and Handle Results
    event = find_event(event_id)

    # Event not found
    if not event:
        return jsonify({"error": "Event not found"}), 404

    # Remove event
    events.remove(event)

    return "", 204

if __name__ == "__main__":
    app.run(debug=True)
