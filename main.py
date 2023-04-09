from flask import Flask, render_template, request

main = Flask(__name__)


@main.route('/')
def index():
    return render_template('index.html')


@main.route('/result', methods=['POST'])
def result():
    restaurant_type = request.form.get('restaurant_type')
    # 從資料庫中查詢符合條件的餐廳
    # ...
    # 返回查詢結果
    return render_template('result.html', restaurant_type=restaurant_type, restaurants=restaurants)


if __name__ == '__main__':
    main.run()
