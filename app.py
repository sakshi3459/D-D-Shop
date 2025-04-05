from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

SHOP_DATA_FILE = 'shop-data.json'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/admin')
def admin():
    return render_template('admin.html')

@app.route('/shop-data.json')
def get_shop_data():
    with open(SHOP_DATA_FILE) as f:
        return jsonify(json.load(f))

@app.route('/update-shop', methods=['POST'])
def update_shop():
    data = request.json
    with open(SHOP_DATA_FILE, 'w') as f:
        json.dump(data, f, indent=2)
    return jsonify({'status': 'success'})

if __name__ == '__main__':
    app.run(debug=True)
