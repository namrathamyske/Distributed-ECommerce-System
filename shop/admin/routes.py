from flask import render_template,session, request,redirect,url_for,flash
from shop import app,db,bcrypt
from .forms import RegistrationForm,LoginForm
from .models import User
from .models import SellerProducts
from shop.products.models import SoldProducts
from shop import start_timer, stop_timer


from shop.products.models import Addproduct,Category,Brand
import zeep
import time
from flask_login import current_user, logout_user, login_user

@app.route('/admin')
def admin():
    resp_time= start_timer()
    products = Addproduct.query.all()
    stop_timer(resp_time, "seller_landing_page_loading")
    return render_template('admin/index.html', title='Admin page',products=products)

@app.route('/admin/brands')
def brands():
    resp_time= start_timer()
    brands = Brand.query.order_by(Brand.id.desc()).all()
    stop_timer(resp_time, "seller_brand")
    return render_template('admin/brand.html', title='brands',brands=brands)


@app.route('/admin/categories')
def categories():
    resp_time= start_timer()
    categories = Category.query.order_by(Category.id.desc()).all()
    stop_timer(resp_time, "seller_cat")
    return render_template('admin/brand.html', title='categories',categories=categories)

@app.route('/admin/register', methods=['GET', 'POST'])
def admin_register():
    resp_time= start_timer()
    form = RegistrationForm()
    if form.validate_on_submit():
        hash_password = bcrypt.generate_password_hash(form.password.data)
        user = User(name=form.name.data,username=form.username.data, email=form.email.data,
                    password=hash_password)
        db.session.add(user)

        sellerproducts = SellerProducts(name=form.name.data,email=form.email.data, products= form.products.data)
        db.session.add(sellerproducts)
        # print('sellerproducts', sellerproducts)
        # print('db', SellerProducts.query.filter_by(name= form.name.data).all())
        flash(f'welcome {form.name.data} Thanks for registering','success')
        db.session.commit()
        stop_timer(resp_time, "seller_register")
        return redirect(url_for('admin_login'))
    return render_template('admin/register.html',title='Register user', form=form)


@app.route('/admin/login', methods=['GET','POST'])
def admin_login():
    resp_time= start_timer()
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            # session["user"]= user
            session['email'] = form.email.data
            next = request.args.get('next')
            flash(f'welcome {form.email.data} you are logged in now','success')
            stop_timer(resp_time, "seller_login")
            return redirect(next or url_for('admin'))
        else:
            flash(f'Wrong email and password', 'success')
            return redirect(url_for('admin_login'))
    return render_template('admin/login.html',title='Login page',form=form)


@app.route('/seller/productslist', methods=['GET','POST'])
def seller_products():
    resp_time= start_timer()
    if current_user.is_authenticated:
        name= current_user.name
        products= SellerProducts.query.filter_by(name= name).all()
        # products_= SellerProducts.query.filter_by(name= name).getprod()
        print('products', products)
        # print(products_)
        stop_timer(resp_time, "seller_products_view")
        return render_template('admin/seller_products.html', title='Seller Products', products=products, name= name)
        

@app.route('/seller/soldproducts', methods=['GET','POST'])
def sold_products():
    resp_time= start_timer()
    if current_user.is_authenticated:
        name= current_user.name
        soldproducts= SoldProducts.query.filter_by(name= name).all()
        sold_quant={}
        current_stock= {}
        for s in soldproducts:
            print("soldproducts: ",s.name, 'product:', s.product, 'quantity sold:', s.quantity_sold, 'stock')#, s.stock)
            sold= s.get_sold(sellername= s.name, prod= s.product)
            sold_quant[s.product]= s.quantity_sold
            stock_prod= Addproduct.query.filter_by(name=s.product).first()
            current_stock[s.product]=stock_prod.stock
        print(current_stock)
        stop_timer(resp_time, "view_sold_products")
        return render_template('admin/sold_products.html', title='Sold Products', name= name, sold=sold_quant, current_stock= current_stock)#, product=soldproducts.product)

        
@app.route('/seller/logout')
def seller_logout():
    resp_time= start_timer()
    logout_user()
    session.clear()
    stop_timer(resp_time, "seller_logout")
    return redirect(url_for('admin'))