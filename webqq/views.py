from django.shortcuts import render, HttpResponse
from django.contrib.auth.decorators import login_required
import json, datetime
import utils , models
# Create your views here.

global_msg_dic = {}

@login_required
def index(request):
    return render(request, 'webqq/chat.html')

def send_msg(request):
    print request.POST
    data = request.POST.get('data')
    data = json.loads(data)
    data['date'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    to_id = data.get('to_id')
    user_obj = models.my_models.User_Profile.objects.get(id=to_id)
    contact_type = data.get('contact_type')
    if contact_type == 'single':
        if not global_msg_dic.has_key(to_id):
            global_msg_dic[to_id] = utils.Chat()
        global_msg_dic[to_id].msg_queue.put(data)
        # print '\033[32;1mPush msg [%s] into user [%s] queue' % (data['msg'], user_obj.name)
    elif contact_type == 'group':
        group_obj = models.QQgroup.objects.get(id=to_id)
        for member in group_obj.members.select_related():
            if member.id != request.user.user_profile.id:
                if not global_msg_dic.has_key(member.id):
                    global_msg_dic[member.id] = utils.Chat()
                global_msg_dic[member.id].msg_queue.put(data)
    return HttpResponse("ok!")


def get_msg(request):
    uid = request.GET.get('uid')
    if uid:
        res = []
        if not global_msg_dic.has_key(uid):
            global_msg_dic[uid] = utils.Chat()
        res = global_msg_dic[uid].get_msg(request)
        return HttpResponse(json.dumps(res))
    else:
        return HttpResponse(json.dumps("uid not provided!!"))