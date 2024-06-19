from flask import Blueprint, render_template, redirect, url_for, flash, request
from app import db
from app.models import Post
from app.forms import PostForm

main = Blueprint('main', __name__)

@main.route('/')
def home():
    posts = Post.query.all()
    return render_template('home.html', posts=posts)

@main.route('/post/<int:post_id>', methods=['GET'])
def show_post(post_id):
    post = Post.query.get_or_404(post_id)
    return render_template('show_post.html', post=post)

@main.route('/post/new', methods=['GET', 'POST'])
def create_post():
    form = PostForm()
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        post = Post(title=title, content=content)
        db.session.add(post)
        db.session.commit()
        flash('Post created successfully!', 'success')
        return redirect(url_for('main.home'))
    return render_template('create_post.html', form=form)

@main.route('/post/edit/<int:post_id>', methods=['GET', 'POST'])
def edit_post(post_id):
    post = Post.query.get_or_404(post_id)
    if request.method == 'POST':
        post.title = request.form['title']
        post.content = request.form['content']
        db.session.commit()
        flash('Post updated successfully!', 'success')
        return redirect(url_for('main.home'))
    return render_template('edit_post.html', post=post)

@main.route('/post/delete/<int:post_id>', methods=['POST'])
def delete_post(post_id):
    post = Post.query.get_or_404(post_id)
    db.session.delete(post)
    db.session.commit()
    flash('Post deleted successfully!', 'success')
    return redirect(url_for('main.home'))
