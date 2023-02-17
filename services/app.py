from flask import Flask

app = Flask(__name__)

@app.route('/users/<id>', methods=['GET'])
def get_user_by_id(id: str):
    result = client["db"]["collection"].find_one({"id": id})

    if result is not None:
        return list(result)[0], 200

    else:
        return None, 404
