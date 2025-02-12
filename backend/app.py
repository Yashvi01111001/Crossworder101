from flask import Flask, request, jsonify
from flask_cors import CORS


app = Flask(__name__)
CORS(app)  # Allows frontend to make requests

crossword = [
    ['C', 'A', 'T', 'L', 'P', 'X', 'S', 'U', 'N', 'D'],
    ['M', 'O', 'R', 'E', 'Z', 'Q', 'A', 'B', 'A', 'V'],
    ['D', 'O', 'G', 'S', 'N', 'T', 'R', 'E', 'E', 'K'],
    ['J', 'H', 'A', 'W', 'U', 'I', 'M', 'X', 'E', 'Y'],
    ['V', 'F', 'T', 'C', 'O', 'G', 'P', 'H', 'A', 'T'],
    ['Y', 'B', 'O', 'O', 'K', 'S', 'R', 'U', 'I', 'W'],
    ['U', 'N', 'A', 'B', 'Y', 'H', 'O', 'U', 'S', 'E'],
    ['B', 'I', 'R', 'D', 'T', 'L', 'N', 'O', 'N', 'C'],
    ['X', 'W', 'N', 'O', 'M', 'A', 'P', 'R', 'D', 'J'],
    ['Q', 'G', 'K', 'I', 'T', 'E', 'F', 'L', 'O', 'S']
]

directions = [(0,1), (1,0), (0,-1), (-1,0), (1,1), (-1,-1), (1,-1), (-1,1)]

def search_word(word):
    for r in range(10):
        for c in range(10):
            if crossword[r][c] == word[0]:
                for dr, dc in directions:
                    path = []
                    nr, nc = r, c
                    for i in range(len(word)):
                        if 0 <= nr < 10 and 0 <= nc < 10 and crossword[nr][nc] == word[i]:
                            path.append((nr, nc))
                            nr += dr
                            nc += dc
                        else:
                            break
                    if len(path) == len(word):
                        return {"word": word, "positions": path}
    return {"word": word, "positions": []}

# def search_word(word):
#     print(f"Searching for: {word}")  # Debugging
#     for r in range(10):
#         for c in range(10):
#             if crossword[r][c] == word[0]:  # Found the first letter
#                 print(f"First letter found at: ({r},{c})")  # Debugging
#                 for dr, dc in directions:
#                     path = []
#                     nr, nc = r, c
#                     for i in range(len(word)):
#                         if 0 <= nr < 10 and 0 <= nc < 10 and crossword[nr][nc] == word[i]:
#                             path.append((nr, nc))
#                             nr += dr
#                             nc += dc
#                         else:
#                             break
#                     if len(path) == len(word):
#                         print(f"Found {word} at {path}")  # Debugging
#                         return {"word": word, "positions": path}
#     print(f"{word} not found!")  # Debugging
#     return {"word": word, "positions": []}

@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Welcome to Crossworder101 API! Use POST to find words."})

@app.route('/find', methods=['POST'])
def find():
    data = request.json
    word = data.get("word")
    print(f"Received word: {word}")  # Debugging
    result = search_word(word.upper())
    print(f"Search result: {result}")  # Debugging
    return jsonify(result)

# @app.route("/", methods=["GET"])  # Only handles GET requests
# def home():
#     print('in the home')
#     return jsonify({"message": "Welcome to the home page"})

if __name__ == '__main__':
    app.run(debug=True)