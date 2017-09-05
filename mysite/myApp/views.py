from django.shortcuts import render
from django.http import HttpResponse
from myApp.models import *
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import *
import json

@csrf_exempt
def addSchool(request):
	if request.method == 'POST':
		pass
	else:
		return JsonResponse({"result":{"msg":"choose POST method","status": 2},"id":"connect","error": "no post"})



@csrf_exempt
def connect(request):
	if request.method == 'POST':
		requestBody = json.loads(request.body.decode('utf-8'))
		ids = requestBody['params']['id']
		password = requestBody['params']['password']
		if User.objects.filter(idd=ids, password=password):
			logs = LoginLog(username=ids,
						password = password)
			logs.save()
			return JsonResponse({"result":{"msg":"success",
								"status": 1},
								 "error": "null"})
		else:
			return JsonResponse({"result":{"msg":"not ql","status": 2},"id":"connect","error": "no user"})
	else:
		return JsonResponse({"result":{"msg":"choose POST method","status": 2},"id":"connect","error": "no post"})

@csrf_exempt
def getUsers(request):
	if request.method == 'POST':
		usersList = []
		for user in User.objects.all():
			usersList.append({ 'idd'		: user.idd,
							   'username' 	: user.username,
							   'credit' 	: user.credit,
							   })
		return JsonResponse({"result":{"msg":"success",
								"status": 1, "users":usersList},
								 "error": "null"})
	else:
		return JsonResponse({"result":{"msg":"choose POST method","status": 2},"id":"getUsers","error": "no post"})	

@csrf_exempt
def addUser(request):
	if request.method == 'POST':
		requestBody = json.loads(request.body.decode('utf-8'))
		users = requestBody['params']['users']
		for user in users:
			if not User.objects.filter(idd = user['id']):
				u = User(idd = user['id'],
						 username = user['name'],
						 password = user['password'],
						 credit = user['credit'])
				u.save()
		return JsonResponse({"result":{"msg":"success","status": 1},"id":"addUser","error": "null"})
	else:
		return JsonResponse({"result":{"msg":"choose POST method","status": 2},"id":"addUser","error": "no post"})

@csrf_exempt
def addFoodList(request):
	if request.method == 'POST':
		requestBody = json.loads(request.body.decode('utf-8'))
		food_list = requestBody['food_menu']
		for food in food_list:
			if food not in FoodList.objects.all():
				fl = FoodList(pic_id	= food['pic_id'],
					 		  name		= food['name'],
					 		  price		= food['price'])
				fl.save()
		return JsonResponse({"result":{"msg":"success","status": 1},"id":"addFoodList","error": "null"})
	else:
		return JsonResponse({"result":{"msg":"choose POST method","status": 2},"id":"addFoodList","error": "no post"})


@csrf_exempt
def getFoodList(request):
	if request.method == 'POST':
		food_list = []
		for food in FoodList.objects.all():
			food_list.append({ 'pic_id'		: food.pic_id,
							   'name'		: food.name,
							   'price'		: food.price,})
		return JsonResponse({"result":{"msg":"success",
								"status": 1, "food_list":food_list},
								 "error": "null"})
	else:
		return JsonResponse({"result":{"msg":"choose POST method","status": 2},"id":"getFoodList","error": "no post"})

@csrf_exempt
def pay(request):
	if request.method == 'POST':
		requestBody = json.loads(request.body.decode('utf-8'))
		ids 	= requestBody['params']['id']
		amount 	= requestBody['params']['amount']
		current_credit = getattr(User.objects.get(idd= ids), "credit")
		if (current_credit - amount) < 0:
			return JsonResponse({"result":{"msg":"not enough credit","status": 0},"id":"pay","error": "null"})
		else:
			User.objects.filter(idd=ids).update(credit= (current_credit - amount))
			return JsonResponse({"result":{"msg":"success","status": 1},"id":"pay","error": "null"})
	else:
		return JsonResponse({"result":{"msg":"choose POST method","status": 2},"id":"pay","error": "no post"})

@csrf_exempt
def addFoodPurchaseLog(request):
	if request.method == 'POST':
		requestBody = json.loads(request.body.decode('utf-8'))
		ids 			= requestBody['params']['id']
		username		= requestBody['params']['username']
		food_purchased 	= []

		for food in requestBody['params']['purchased_food']:
			pl = PurchaseLog(user 		= User.objects.get(username=username),
							 name 		= food['name'],
							 quantity 	= food['quantity'],
							 price   	= food['price'],
							 time 		= food['time'],
							 )
			pl.save()
		for o in PurchaseLog.objects.filter(user = User.objects.get(username=username)):
			food_purchased.append({ 'name'	: o.name,
									'quantity' : o.quantity,
									'price' : o.price,
									'time' : o.time, })
		return JsonResponse({"result":{"msg":"success","food_purchased":food_purchased ,"status": 1},"id":"addFoodPurchaseLog","error": "null"})
	else:
		return JsonResponse({"result":{"msg":"choose POST method","status": 2},"id":"addFoodPurchaseLog","error": "no post"})

