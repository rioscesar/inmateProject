from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from models import AWSModel
from .forms import AWSForm, AWSHomeForm
from django.http import HttpResponse
from django.contrib.auth.models import User
import json
import boto
from django.views.generic import TemplateView
from django.http import HttpResponse
from django.db import connection

from aws import AWS

def aws(request):
     
    #Get the user Id of logged in user 
    usr_id = request.user.id
  
    #Mathch the user Id against user_id column of aws table
    try:
        aws_result = AWSModel.objects.get(user_id=usr_id)
    except:
        aws_result = None   
     

    #If the logged in user Id matches against user_id inside aws table, that means the user has already entered and
    #saved the aws key and secret key in database, therefore the AWS dashboard is shown to user
    if aws_result is not None:
         return render_to_response("aws_home.html", {}, context_instance=RequestContext(request))

    #Else If the user Id does not mataches against user_id of aws table, we will now show the AWS form in which user can
    #save his/her aws credentials     
    else:
         #If the request method is POST that means user has filled the form so now the aws key and aws secret of 
         #user will be saved in databae
         if request.method == 'POST':
             print "it is post"
             form = AWSForm(request.POST or None)
             if form.is_valid():
                 aws_key = form.cleaned_data['aws_access_key']
                 aws_secret = form.cleaned_data['aws_secret_key']
                 keys = AWSModel(user_id=usr_id,aws_access_key=aws_key,aws_secret_key=aws_secret)
                 save_keys = AWSModel.save(keys)
                 print "AWS KEYS HAS BEEN SAVED IN AWS TABLE"
                 return render_to_response("aws_home.html", {}, context_instance=RequestContext(request))
         #Else if the request method is GET that means user is visiting the AWS Signup form, therefore AWS 
         #sign up form is shown to the user   
         else:
             form = AWSForm()
         
             context = {
                      "form": form,
                   }

             return render_to_response("AWS_CP.html", context, context_instance=RequestContext(request))


def aws_create(request): 
       
    #If the request method is Get, show the create form to the user   

    if request.method == 'POST':
         
        return render_to_response("aws_create.html", {}, context_instance = RequestContext(request))

    #else if the request methos is POST that means user has filled the form and posting the data in order to 
    #create an instance, therefore fetching the POST values from the aws_create.html and calling the create_instance
    #function in order to create a new instance        
    else:
        zone = request.POST.get("zone")
        region = request.POST.get("region")
        image = request.POST.get("image")
        min = request.POST.get("min")
        max = request.POST.get("max")
        key_name = request.POST.get("key_name")
        inst_type = request.POST.get("inst_type")
        check_status = request.POST.get("check_status")

        print zone, region, image, min, max, key_name, inst_type, check_status

        #Get AWS Access key and secret key from database
        usr_id = request.user.id
        aws_result = AWSModel.objects.get(user_id=usr_id)
        access_key = aws_result.aws_access_key
        secret_key = aws_result.aws_secret_key

        #Instantiate AWS class aws->aws.py and calling the launch_instance function
        aws = AWS(access_key,secret_key)

        aws.launch_instance(min,max,key_name,inst_type,check_status)

        
 
        #return HttpResponse(json.dumps({'message': "Success"}), content_type="application/json")

    return render_to_response("aws_create.html", {}, context_instance = RequestContext(request)) 

def aws_home(request):
    print "aws_inst **************************"

    # if request.method == 'POST':
    # user_id = request.user.id
    # print user_id
    # # aws_model = AWS()
    # # print aws_model.all()
    # aws_access_key_id = ''
    # aws_secret_access_key = ''
    # ec2 = boto.connect_ec2(aws_access_key_id=aws_access_key_id,
    # aws_secret_access_key=aws_secret_access_key)
    # parsed_data = []
    # user_Data = {}
    # # checking all zones
    # # data   = list(ec2.get_all_zones())
    # list_data = list(boto.ec2.regions())
    # # dict_data = dict(list_data)
    # # print list_data
    # list_data = [(1, 'region1'), (2, 'region2'), (3,'region3')]
    # # data = {key: i for i , key in enumerate(list_data)}
    # form = AWSHomeForm(my_choices = list_data)
    # context = {
    # "form" : form,
    # }
    # aws_get_keys()
    # test = request.POST.get("zone", "region", "image", "min_count", "max_count", "key_name", "inst_type", "monitoring")
    if request.is_ajax():
        print "it's ajax"
    if request.method == 'POST':
        print "I am here inside post"

        selectOP = request.POST.get("selectOP")

        print selectOP

    return render_to_response("aws_home.html", {}, context_instance = RequestContext(request))
    # return HttpResponse(json.dumps(response_data),content_type="application/json")

def aws_delete(request):
    print "aws_delete **************************"

    if request.is_ajax():
        print "it's ajax"
    if request.method == 'POST':
        print "I am here inside post"

        instance = request.POST.get("instance")

        print instance

    return render_to_response("aws_delete.html", {}, context_instance = RequestContext(request))


def aws_get_keys():
    aws = AWS.objects.raw("Select * from aws where user_id = 4")
    for val in aws:
        access_key = val.aws_access_key
        secret_key = val.aws_secret_key
        print access_key, secret_key
