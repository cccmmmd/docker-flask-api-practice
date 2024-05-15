import flask
from flask import request, jsonify
app = flask.Flask(__name__)

app.config["DEBUG"] = True


products = [
    {
        "id": 1,
        "isbn":"10000320013",
        "title":"A9+濕拖無線吸塵器A9N-LITEMOP(銀)",
        "subtitle":"吸力、續航力、輕薄三大升級",
        "brand":"LG 樂金 追蹤",
        "created":"2024-05-04T00:00:00.000Z",
        "price": 9499,
        "description":"吸力、續航力、輕薄三大升級<br/>電動濕拖吸頭+五道過濾系統<br/>智慧變頻馬達10年保固",
    },
    {
        "id": 2,
        "isbn":"10000320014",
        "title":"10公斤Essential Clean溫水洗脫烘變頻滾筒洗衣機(WEHC10BBS)",
        "subtitle":"8小時自動清新除皺",
        "brand":"Whirlpool 惠而浦",
        "created":"2019-01-16T00:00:00.000Z",
        "price": 10900,
        "description":"8小時自動清新除皺<br/>15°C護色洗滌<br/>金級省水標章",
    },
    {
        "id": 3,
        "isbn":"10000320015",
        "title":"新一代★智能雙效UV-C滅菌/RO過濾瞬熱淨水機(ADD6910 主機內含濾芯)",
        "subtitle":"UV-C殺菌防止水箱二次汙染",
        "brand":"Philips 飛利浦",
        "created":"2023-04-21T00:00:00.000Z",
        "price": 11111,
        "description":"UV-C殺菌防止水箱二次汙染<br/> 免安裝<br/> 三秒瞬熱<br/> 四種溫度<br/> 五重深濾110種有害物質",
    }
]
@app.route('/', methods=['GET'])
def home():
    return '''<h1>Product API</h1>
                <p>A flask api implementation for 電器資訊.   </p>
                <ul>
                    <li><b>GET</b>     /api/v1/prod/all</li>
                    <li><b>GET</b>     /api/v1/prod</li>
                    <li><b>POST</b>    /api/v1/prod</li>
                    <li><b>DELETE</b>  /api/v1/prod/<id></li>
                </ul>   
                '''


@app.route('/api/v1/prod/all', methods=['GET'])
def api_all():
    return jsonify(products)

@app.route('/api/v1/prod', methods=['GET'])
def api_id():
    if 'id' in request.args:
        id = int(request.args['id'])
    else:
        return "Error: No product for the id"
    
    results = []
    for prod in products:
        if prod['id'] == id:
            results.append(prod)
            return jsonify(results)
        
@app.route("/api/v1/prod",  methods = ['POST'])
def api_add():
    prod = request.get_json()
    products.append(prod)
    return "Success! Product information has been added."

@app.route("/api/v1/prod/<id>", methods=["DELETE"])
def api_delete(id):
    for prod in products:
        if prod['id'] == int(id):
            products.remove(prod)
    return "Success! Product information has been deleted."

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8888)