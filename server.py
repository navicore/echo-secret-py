from flask import Flask, request, jsonify
import os  # Import the os module

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

@app.route('/echo/secret', methods=['POST'])
def echo():
    if request.method == 'POST':
        # Parse the JSON input
        data = request.json
        messages = data.get("messages", [])

        # Check if messages are provided
        if not messages:
            return jsonify({"error": "No messages provided"}), 400

        try:
            # Retrieve MY_SECRET from environment variables
            my_secret = os.getenv('MY_SECRET', 'default_secret')  # Use a default value if MY_SECRET is not set

            # Insert 'secret' field into each message
            for message in messages:
                message['secret'] = my_secret

            # Return the modified messages
            return jsonify({"response": messages})
        except Exception as e:
            return jsonify({"error": str(e)}), 500

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "ok", "message": "secret echo service is ready"}), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
