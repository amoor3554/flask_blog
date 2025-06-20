from flask import Blueprint
from blog.controllers import MainController, AuthController, SubscriptionController




"""For The Main Controller """

MainRoute = Blueprint("MainRoute", __name__)

MainRoute.route('/')(MainController.home)






"""For The Auth Controller """

AutherRoute = Blueprint("AuthRoute", __name__, url_prefix='/auth')


AutherRoute.route('/login', methods=['POST', 'GET'])(AuthController.user_login)
AutherRoute.route('/register', methods=['POST', 'GET'])(AuthController.user_register)
AutherRoute.route('/account', methods=['GET'])(AuthController.user_account)
AutherRoute.route('/logout', methods=['GET'])(AuthController.user_logout)
AutherRoute.route('/reset_password', methods=['POST', 'GET'])(AuthController.reset_request)
AutherRoute.route('/reset_password/<token>', methods=['POST', 'GET'])(AuthController.reset_password)



"""For The Subscribe Controller """

SubscribeRoute = Blueprint("SubscriptionRoute", __name__)

SubscribeRoute.route('/test', methods=['GET', 'POST'])(SubscriptionController.strip_test)

SubscribeRoute.route('/subscription', methods=['GET'])(SubscriptionController.subscription)
SubscribeRoute.route('/subscription_create', methods=['GET', "POST"])(SubscriptionController.subscription_create)
SubscribeRoute.route('/public-key', methods=['GET'])(SubscriptionController.get_publishable_key)
SubscribeRoute.route('/webhook', methods=['POST'])(SubscriptionController.webhook_received) #type:ignore
SubscribeRoute.route('/post_price_id', methods=['GET'])(SubscriptionController.post_price_id)



"""For The Article Controller """

ArticleRoute = Blueprint("ArticleRoute", __name__, url_prefix='/article')


ArticleRoute.route('/add', methods=['POST', 'GET'])(MainController.article_add)
ArticleRoute.route('/<int:id>/update', methods=["GET","POST"])(MainController.article_update)
ArticleRoute.route('/list', methods=["GET"])(MainController.articles_list)
ArticleRoute.route('/<int:id>/show', methods=['GET'])(MainController.article)
ArticleRoute.route('/<int:id>/like', methods=["PUT"])(MainController.article_like)
ArticleRoute.route('/<int:id>/delete', methods=["GET","POST"])(MainController.article_delete)



