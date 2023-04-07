from flask import Flask, jsonify, request

app = Flask(__name__)

items = [
    {"id": 1, "name": "product1", "category": "category1", "price": 10.0, "instock": 100},
    {"id": 2, "name": "product2", "category": "category2", "price": 20.0, "instock": 200},
    {"id": 3, "name": "product3", "category": "category1", "price": 30.0, "instock": 300}
]

def _find_next_id(id):
    data = [x for x in items if x['id']==id]
    return data

@app.route('/item/<int:id>', methods=["DELETE"])
def get_item(id: int):
    
    data = _find_next_id(id)
    if not data:
        return {"error": "item not found"}, 404
    else:
        items.remove(data[0])
        return "item deleted successfuly", 200
    
@app.route('/patch_item/<int:p_id>', methods=["PATCH"])
def patch_item(p_id):
    id = request.form.get('id')
    global items
    name = request.form.get('name')
    category = request.form.get('category')
    price = request.form.get('price')
    instock = request.form.get('instock')

    data = _find_next_id(id)
    if not data:
        return {"error": "item not found"}, 404

    name.form.get('name')
    category = form.get('category')
    price = form.get('price')
    instock = form.get('instock')

    if name:
        data['name'] = name
    if category:
        data['category'] = category
    return {"message": "category updated successfully"}, 200
    if price:
        data['price'] = price
    return {"message": "price updated successfully"}, 200
    if category:
        data['instock'] = instock
    return {"message": "instock updated successfully"}, 200

@app.route('/item', methods=["get"])
def get_item():
    return jsonify(items)

@app.route('/item/<id>', methods=["GET"])
def get_item_id(id):
    data = _find_next_id(id)
    return jsonify(data)

@app.route('/item', methods=["POST"])
def post_item():
    id = request.form.get('id')
    name = request.form.get('name')
    category = request.form.get('category')
    price = request.form.get('price')
    instock = request.form.get('instock')

    new_data = {
        "id": id,
        "name": name,
        "category": category,
        "price" : price,
        "instock" : instock
    }

    if (_find_next_id(id)):
        return {"error": "Bad Request"}, id
    else:
        items.append(new_data)
        return jsonify(items)
    
@app.route('/put_item/<int:c_id>', methods=["PUT"])
def update_item(c_id):
    global items
    name = request.form.get('name')
    category = request.form.get('category')
    price = request.form.get('price')
    instock = request.form.get('instock')

    update_data = {
        "name" : name,
        "category": category,
        "price" : price,
        "instock" : instock
    }
    
    for item in items:
        if c_id == item.get("id"):
            item["name"] = str(name)
            item["category"] = str(category)
            item["price"] = str(price)
            item["instock"] = str(instock)
            return jsonify(items)

    else:
        return "Error", 404

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000, debug=True)
