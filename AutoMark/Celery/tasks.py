from __future__ import absolute_import, unicode_literals
from AutoMark.celery import app
from AutoMark.InstaPy.instapy import InstaPy

#
# @app.task
# def add(x, y):
#     return x + y
#
#
# @app.task
# def mul(x, y):
#     return x * y


@app.task
def insta_py(settings):
    session = InstaPy(username=settings['username'],
                      password=settings['password'],
                      headless_browser=True,
                      multi_logs=True,)
    try:
        # set these if you're locating the library in the /usr/lib/pythonX.X/ directory
        # Settings.database_location = '/path/to/instapy.db'
        # Settings.browser_location = '/path/to/chromedriver'

        session.login()

        # default enabled=False, follows ~ 10% of the users from the images, times=1
        session.set_do_follow(enabled=True, percentage=10, times=2)
        session.set_use_clarifai(enabled=False)
        # settings
        session.set_upper_follower_count(limit=1500)
        session.set_do_comment(True, percentage=10)
        session.set_comments(settings['comments'])
        # actions
        session.like_by_tags(settings['tags'], amount=15)
        # Follow user based on hashtags (without liking the image)
        session.follow_by_tags(['tag1', 'tag2'], amount=10)

    finally:
        # end the bot session
        session.end()
    return
