from . import shop
from flask import render_template


## Shop routes
@shop.route('/shop', methods=["GET", "POST"])
def shop_page():
    products = get_products_database()
    return render_template('shop.html'products=products)

@shop.route('/add_to_cart/< int:product_id>')
def add_to_cart(product_id):
    product =
    get_product_by_id(product_id)
    if 'cart' not in session:
        session['cart'] = []

    session['cart'].append(product)
    return redirect('/shop')

@shop.route('/cart')
def view_cart():
    cart = session.get('cart',[])
    total = calculate_total(cart)
    return render_template('cart.html', cart=cart, total=total)

@app.route('/checkout')
def checkout():
    cart= session.get('cart',[])
    total = calculate_total(cart)