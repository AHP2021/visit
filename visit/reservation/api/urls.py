from django.urls import path
from reservation.api.view.class_based_views import *
from reservation.api.view.function_based_views import *
from django.conf.urls.static import static
from reservation import views
from visit import settings

urlpatterns = [
                  path('doctor', DoctorView.as_view(), name='doctor'),
                  path('doctor/login', d_login),
                  path('doctor/<int:doctor_id>', DoctorView.as_view()),
                  path('customer', CustomerView.as_view(), name='customer'),
                  path('customer/login', c_login),
                  path('customer/<int:customer_id>', CustomerView.as_view()),
                  path('comment', Commentview.as_view(), name='comment'),
                  path('comment/<int:comment_id>', Commentview.as_view()),
                  path('visit', Visitview.as_view(), name='visit'),
                  path('visit/<int:visit_id>', Visitview.as_view()),
                  path('specialty', SpecialtyView.as_view(), name='specialty'),
                  path('specialty/<int:specialty_id>', SpecialtyView.as_view()),
                  path('listvisit', ListVisitView.as_view(), name='listvisit'),
                  path('listvisit/<int:list_visit_id>', ListVisitView.as_view()),
                  path('listcomment', ListCommentView.as_view(), name='listcomment'),
                  path('listcomment/<int:list_comment_id>', ListCommentView.as_view()),
                  path('customer/search/v1', c_search_by_visittime),
                  path('customer/search/v2', c_search_by_doctorname),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
