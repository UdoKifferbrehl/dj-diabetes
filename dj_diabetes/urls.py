from django.conf.urls import patterns, include, url

from dj_diabetes.views import GlucosesCreateView, GlucosesUpdateView, GlucosesDeleteView,\
    AppointmentsCreateView, AppointmentsUpdateView, AppointmentsDeleteView,\
    IssuesCreateView, IssuesUpdateView, IssuesDeleteView,\
    WeightsCreateView, WeightsUpdateView, WeightsDeleteView,\
    MealsCreateView, MealsUpdateView, MealsDeleteView,\
    ExercisesCreateView, ExercisesUpdateView, ExercisesDeleteView,\
    ExamsCreateView, ExamsUpdateView, ExamsDeleteView

from django.contrib import admin

admin.autodiscover()

urlpatterns =\
    patterns('',
        url(r'^admin/', include(admin.site.urls)),
        # ****************************************
        # auth module
        # ****************************************
        url(r'^accounts/', include('django.contrib.auth.urls')),
        # ****************************************
        # customized lgout action
        # ****************************************
        url(r'^logout/$', 'dj_diabetes.views.logout_view', name='logout'),
        url(r'^$', GlucosesCreateView.as_view(), name='home'),
        url(r'^glucose/edit/(?P<pk>\d+)$', GlucosesUpdateView.as_view(),
            name='glucose_edit'),
        url(r'^glucose/delete/(?P<pk>\d+)$', GlucosesDeleteView.as_view(),
            name='glucose_delete'),
        url(r'^appoints/$', AppointmentsCreateView.as_view(),
            name='appointments'),
        url(r'^appoints/edit/(?P<pk>\d+)$', AppointmentsUpdateView.as_view(),
            name='appointment_edit'),
        url(r'^appoints/delete/(?P<pk>\d+)$', AppointmentsDeleteView.as_view(),
            name='appointment_delete'),
        url(r'^issues/$', IssuesCreateView.as_view(), name='issues'),
        url(r'^issues/edit/(?P<pk>\d+)$', IssuesUpdateView.as_view(),
            name='issue_edit'),
        url(r'^issues/delete/(?P<pk>\d+)$', IssuesDeleteView.as_view(),
            name='issue_delete'),
        url(r'^weights/$', WeightsCreateView.as_view(), name='weights'),
        url(r'^weights/edit/(?P<pk>\d+)$', WeightsUpdateView.as_view(),
            name='weight_edit'),
        url(r'^weights/delete/(?P<pk>\d+)$', WeightsDeleteView.as_view(),
            name='weight_delete'),
        url(r'^meals/$', MealsCreateView.as_view(), name='meals'),
        url(r'^meals/edit/(?P<pk>\d+)$', MealsUpdateView.as_view(),
            name='meal_edit'),
        url(r'^meals/delete/(?P<pk>\d+)$', MealsDeleteView.as_view(),
            name='meal_delete'),
        url(r'^exams/$', ExamsCreateView.as_view(), name='exams'),
        url(r'^exams/edit/(?P<pk>\d+)$', ExamsUpdateView.as_view(),
            name='exam_edit'),
        url(r'^exams/delete/(?P<pk>\d+)$', ExamsDeleteView.as_view(),
            name='exam_delete'),
        url(r'^exercises/$', ExercisesCreateView.as_view(), name='exercises'),
        url(r'^exercises/edit/(?P<pk>\d+)$', ExercisesUpdateView.as_view(),
            name='exercise_edit'),
        url(r'^exercises/delete/(?P<pk>\d+)$', ExercisesDeleteView.as_view(),
            name='exercise_delete'),
        url(r'^pref/$', GlucosesCreateView.as_view(), name='pref'),
        #url(r'^$', 'dj_diabetes.views.glucose_create', name='home'),
        # url(r'^blog/', include('blog.urls')),
        url(
            regex=r'^chart_data_json/$',
            view='dj_diabetes.views.chart_data_json',
            name='chart_data_json',
        ),
)