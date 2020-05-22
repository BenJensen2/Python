from django.shortcuts import render, HttpResponse, redirect
from .models import Message, Comment, User, UserManager


def index(request):
    current_user = request.session['user_email']
    # View Filter Query oldest to newest and newest to oldest
    # Messages.all()
    context = {
        'first_name' : request.session['fname'],
        'messages' : Message.objects.all() #User.objects.get(email_address=current_user).user_messages.all(),
        # 'message_comments' : User.objects.get(email_address=current_user).user_messages.all().message_comments.all()
    }
    return render(request,'wall.html',context)

# def post_message(request):
# Message user must get user name
# Store date time
def message(request):
    current_user = request.session['user_email']
    print('Message')
    msg = request.POST['posted_message']
    message_user = User.objects.get(email_address=current_user)
    Message.objects.create(message=msg,user=message_user)
    return redirect('/wall')



# Function Post Comment
# Comment user must get User name
def comment(request):
    current_user = request.session['user_email']
    print('Comment')
    comment = request.POST['posted_comment']
    comment_user = User.objects.get(email_address=current_user)
    message_id = request.POST['message_id']
    current_message = Message.objects.get(id=message_id)
    Comment.objects.create(comment=comment,user=comment_user,message=current_message)
    return redirect('/wall')
