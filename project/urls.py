from django.urls import path, re_path

from project import views


urlpatterns = [
    path("add/new", views.add_new_project, name="new_project"),
    path("all/projects", views.project_list, name="project_list"),
    path("lgas/", views.load_lgas, name="ajax_load_lgas"),
    

    # path("login/", views.login_user, name="login"),
    # path("logout/", views.logout_user, name="logout"),
    # path("profile/<str:pk>/", views.profile, name="profile"),
    # path("profile/", views.profile, name="profile"),
    # path("email/confirmation/", views.activation_message,
    #      name="activation_message"),
    # re_path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
    #         views.activate_email, name='activate'),
    # path("sampletemp/", views.sampletemp, name="sampletemp"),
    # path("personal/<str:pk>/details/",
    #      views.PersonalDetailsView.as_view(), name="personal_details"),
    # path("origin/<str:pk>/details/",
    #      views.OriginDetailsView.as_view(), name="origin_details"),
    # path("nysc/<str:pk>/details/",
    #      views.NYSCDetailsView.as_view(), name="nysc_details"),
    # path("professional/<str:pk>/details/",
    #      views.ProfessionalDetailsView.as_view(), name="profesional_details"),
    # path("picture/<str:pk>/details/",
    #      views.PhotosView.as_view(), name="profile_picture"),

    path('', views.ProjectListView.as_view(), name='project_test_list'),
    path('add/', views.ProjectCreateView.as_view(), name='project_test_add'),
    path('<int:pk>/', views.ProjectUpdateView.as_view(), name='project_test_change'),
]


#*346#