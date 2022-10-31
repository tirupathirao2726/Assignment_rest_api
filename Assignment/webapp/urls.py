from django.urls import path
from webapp import views
from rest_framework.urlpatterns import format_suffix_patterns
urlpatterns=[
    path('users/',views.user_info_list,name='get_post'),
    path('users/<int:id>',views.user_info_detail,name='put_delete')
]

urlpatterns=format_suffix_patterns(urlpatterns )
