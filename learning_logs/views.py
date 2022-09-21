from django.shortcuts import render, redirect

from .models import Topic
from .forms import TopicForm


def index(request):
    """The home page"""
    return render(request, 'learning_logs/index.html')


def topics(request):
    """Show all topics."""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)


def topic(request, topic_id):
    """Display only one topic."""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)

def new_topic(request):
    """Introduce a new topic."""
    if request.method == 'POST':
        # POST data entered, process.
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topics')
    else:
        # No data submitted return blank form.
        form = TopicForm()
    # Show a blank or incomplete form.
    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)
