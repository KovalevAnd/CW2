import json


def load_data():

    with open("data/data.json", "r", encoding='utf-8') as fp:
        posts = json.load(fp)

    with open('data/comments.json', 'r', encoding='utf-8') as fc:
        comments = json.load(fc)

    posts = modified_posts(posts, comments)

    with open('data/bookmarks.json', 'r', encoding='utf-8') as fb:
        bookmarks = json.load(fb)

    return posts, comments, bookmarks


def modified_posts(posts, comments):
    for i, post in enumerate(posts):
        pk = post['pk']
        post_comments = []
        for comment in comments:
            if comment['post_id'] == pk:
                post_comments.append(comment)
        posts[i]['comment_count'] = len(post_comments)
        posts[i]['content'] = tagify_content(posts[i]['content'])
        posts[i]['less_letters'] = posts[i]['content'][0:50] + '...'
        posts[i]['comments'] = post_comments
    return posts


def tagify_content(content):
    words = content.split(' ')
    for i, word in enumerate(words):
        if word.startswith('#'):
            tag = word.replace('#', '')
            link = f'<a href="/tag/{tag}">{word}</a>'
            words[i] = link
    return ' '.join(words)


def get_target_post(posts, pk):
    target_post = {}
    for post in posts:
        if post['pk'] == pk:
            target_post = post
    return target_post


def search_posts(posts, s):
    searched_posts = []
    for post in posts:
        if str(s) in post['content']:
            searched_posts.append(post)
    return searched_posts[0:9]


def search_user_posts(posts, username):
    searched_user_posts = []
    for post in posts:
        if username == post['poster_name']:
            searched_user_posts.append(post)
    return searched_user_posts


def search_tag_posts(posts, tag):
    searched_tag_posts = []
    for post in posts:
        if f'#{tag}' in post['content']:
            searched_tag_posts.append(post)
    return searched_tag_posts
