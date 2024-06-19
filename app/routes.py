from flask import Blueprint, render_template, url_for, flash, redirect
from app.forms import PostForm
from app.models import Post
from app import db

main = Blueprint('main', __name__)

@main.route('/')
@main.route('/home')
def home():
    posts = Post.query.all()
    return render_template('home.html', posts=posts)

@main.route('/post/new', methods=['GET', 'POST'])
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data)
        db.session.add(post)
        db.session.commit()
        flash('Your post has been created!', 'success')
        return redirect(url_for('main.home'))
    return render_template('create_post.html', title='New Post', form=form)
