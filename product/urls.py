from django.urls import path
from product.views import *

urlpatterns = [
    path('func_get/', get_product),
    path('func_post/', post_product),

    path('generic_get/', ProductListGenericView.as_view()),
    path('generic_post/', ProductCreateGenericView.as_view()),
    path('generic_get_post/', ProductListCreateGenericView.as_view()),

    path('apiview_get_post/', ProductAPIView.as_view()),
]
