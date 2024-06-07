from flask import Flask, request, jsonify
from flask_cors import CORS


app = Flask(__name__)
CORS(app)


campaign_data = [
    {
        "campaign_id": 1,
        "campaign_code": "AL-0005-7356",
        "campaign_name": "Shinjuku Campaign",
        "banner_url": "https://example.com/img/5",
        "no_of_stamps": 4,
        "start_date": "2024-05-22T18:36:00",
        "end_date": "2024-05-22T18:36:00",
        "created_on": "2024-06-03T13:02:46",
    }
]


@app.route("/show-campaigns", methods=["GET"])
def show_campaigns():
    token = request.get_json("token")
    if not token:
        return jsonify({"error": "Token Expired"}), 401
    return jsonify({"all_campaigns": campaign_data}), 200


if __name__ == "__main__":
    app.run(debug=True)
