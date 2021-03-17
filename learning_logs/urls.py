"""Defines URL patterns for learning_logs"""

from django.urls import path

from . import views

app_name = 'learning_logs'
urlpatterns = [
	# Home page
	path('', views.index, name = 'index'),
	# Page that shows all topics
	path('topics/', views.topics, name = 'topics'),
	# Detail page for single topic
	path('topics/<int:topic_id>', views.topic, name = 'topic'),
	# New topic page
	path('new_topic/', views.new_topic, name = 'new_topic'),
	# New entry page
	path('new_entry/<int:topic_id>/', views.new_entry, name = 'new_entry'),
	# Page to edit a particular entry
	path('edit_entry/<int:entry_id>/', views.edit_entry, name = 'edit_entry'),
]