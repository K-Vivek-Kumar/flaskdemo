from flask import Flask, request, jsonify
from flask_cors import CORS


from dummy import campaign_data, detailed_campaign_data


app = Flask(__name__)
CORS(app)


@app.route("/show-campaigns", methods=["GET"])
def show_campaigns():
    token = request.get_json("token")
    if not token:
        return jsonify({"error": "Invalid Input"}), 401
    if token == "expired":
        return jsonify({"error": "Token Expired"}), 401
    return jsonify({"all_campaigns": campaign_data}), 200


@app.route("/detailed-campaigns", methods=["GET"])
def details_campaigns():
    token = request.get_json("token")
    if not token:
        return jsonify({"error": "Invalid Input"}), 401
    if token == "expired":
        return jsonify({"error": "Token Expired"}), 401
    return jsonify(detailed_campaign_data), 200


if __name__ == "__main__":
    app.run(debug=True)
