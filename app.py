from flask import Flask, render_template, request

app = Flask(__name__)

# 假設這是你的餐廳資料庫，這裡只有範例資料
restaurant_data = {
    '中式料理': ['鼎泰豐', '南京三甲', '魚大一', '美而美'],
    '日式料理': ['壽司郎', '和民', '鳥貴族', '熊吉'],
    '西式料理': ['Tony Roma', 'TGIFriday', 'Pancake House', 'Vapiano'],
}


@app.route('/')
def index():
    return render_template('index.html', restaurant_data=restaurant_data)


@app.route('/search', methods=['POST'])
def search():
    # 從前端取得使用者選擇的餐廳類型
    selected_type = request.form.get('restaurant_type')

    # 從資料庫中取得符合條件的餐廳資料
    if selected_type in restaurant_data:
        restaurants = restaurant_data[selected_type]
    else:
        restaurants = []

    # 顯示符合條件的餐廳列表
    return render_template('result.html', selected_type=selected_type, restaurants=restaurants)


if __name__ == '__main__':
    app.run()
