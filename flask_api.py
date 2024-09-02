# Task 2
from flask import Flask, request, jsonify
from binary_sort_algos import binary_search, merge_sorted, search_video

app = Flask(__name__)

# Sample video titles list
video_titles = [
    "The Art of Coding",
    "Exploring the Cosmos",
    "Cooking Masterclass: Italian Cuisine",
    "History Uncovered: Ancient Civilizations",
    "Fitness Fundamentals: Strength Training",
    "Digital Photography Essentials",
    "Financial Planning for Beginners",
    "Nature's Wonders: National Geographic",
    "Artificial Intelligence Revolution",
    "Travel Diaries: Discovering Europe"
]



# Route for searching videos via POST with request body
@app.route('/search_video', methods=['POST'])
def search_video_api():
    # Get the 'title' from the JSON body
    data = request.get_json()
    
    if not data or 'title' not in data:
        return jsonify({"error": "No video title provided"}), 400

    target_title = data['title']
    
    # Perform the video search
    result = search_video(video_titles, target_title)
    
    # Return the result as a JSON response
    if result != "Video not found":
        return jsonify({"video_found": result}), 200
    else:
        return jsonify({"error": "Video not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
