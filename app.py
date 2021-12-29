from flask import Flask, request, render_template
from functions import load_data, get_target_post, search_posts, search_user_posts, search_tag_posts

posts, comments, bookmarks = load_data()


app = Flask(__name__)


@app.route('/')
def page_index():
    return render_template('index.html', posts=posts)


@app.route('/posts/<pk>')
def page_post(pk):
    post = get_target_post(posts, int(pk))
    post_comments = post['comments']
    return render_template('post.html', post=post, pk=pk, comments=post_comments)


@app.route('/search/')
def page_search():
    s = request.args.get('s')
    searched_post = search_posts(posts, s)
    count_posts = len(searched_post)
    return render_template('search.html', searched_post=searched_post, s=s, count_posts=count_posts)


@app.route('/users/<username>')
def page_users(username):
    user_posts = search_user_posts(posts, username)
    return render_template('user-feed.html', user_posts=user_posts)


@app.route('/tag/<tag>')
def page_tag(tag):
    tag_posts = search_tag_posts(posts, tag)
    return render_template('tag.html', tag_posts=tag_posts, tag=tag)


if __name__ == '__main__':
    app.run(debug=True)
