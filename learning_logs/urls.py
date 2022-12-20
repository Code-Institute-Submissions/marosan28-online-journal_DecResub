from django.urls import path
from django.contrib import admin
from . import views

app_name = 'learning_logs'
urlpatterns = [
    path('admin/', admin.site.urls),
    # Home page
    path('', views.index, name='index'),

    # Page that shows all topics
    path('topics/', views.topics, name='topics'),

    # Specific section for a certain topic
    path('topics/<int:topic_id>', views.topic, name='topic'),

    # Adding new topic
    path('new_topic/', views.new_topic, name='new_topic'),

    # Entry page for new entries
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),

    # Editing an entry
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),

    # Deleting an entry
    path('entry/<int:entry_id>/delete/', views.delete_entry, name='delete_entry'),

    # Deleting a topic
    path('topics/<int:topic_id>/delete/', views.delete_topic, name='delete_topic'),
    
    # Newsletter
     path("newsletter", views.newsletter, name="newsletter"),

]
