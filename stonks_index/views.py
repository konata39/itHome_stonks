from django.shortcuts import render
from django.http import JsonResponse #剛剛的JsonResponse套件
from stonks_index.models import stonks_DB #從models.py import DBTest 物件
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
@csrf_exempt
def set_stonks_data(request):

    #取得post data
    data = request.POST

    #檢查所有欄位是否都有值，若有欄位沒有值，回傳400
    if 'comp_id' not in data:
        return JsonResponse({"status": False, "message": "comp_id column cannot be empty"}, status=400)
    if 'year' not in data:
        return JsonResponse({"status": False, "message": "year column cannot be empty"}, status=400)
    if 'season' not in data:
        return JsonResponse({"status": False, "message": "season column cannot be empty"}, status=400)
    if 'balance_sheet' not in data:
        return JsonResponse({"status": False, "message": "balance_sheet column cannot be empty"}, status=400)
    if 'income_statement' not in data:
        return JsonResponse({"status": False, "message": "income_statement column cannot be empty"}, status=400)

    #建立新的DBTest object
    new_obj = stonks_DB()

    #一個蘿蔔一個坑
    new_obj.comp_id = data.get('comp_id', None)
    new_obj.year = data.get('year', None)
    new_obj.season = data.get('season', None)
    new_obj.balance_sheet = data.get('balance_sheet', None)
    new_obj.income_statement = data.get('income_statement', None)

    #儲存object
    new_obj.save()

    #回傳200,這裡使用JsonResponse
    return JsonResponse(data={'msg':'add object success.'}, status=200)

@csrf_exempt
def get_stonks_data(request):

    data = request.POST

    #檢查每欄位是否有值，若有一欄位沒有值，回傳400
    if 'comp_id' not in data:
        return JsonResponse({"status": False, "message": "comp_id column cannot be empty"}, status=400)
    if 'year' not in data:
        return JsonResponse({"status": False, "message": "year column cannot be empty"}, status=400)
    if 'season' not in data:
        return JsonResponse({"status": False, "message": "season column cannot be empty"}, status=400)

    #將每個request之欄位撈出
    post_comp_id = data.get('comp_id', None)
    post_year = data.get('year', None)
    post_season = data.get('season', None)

    #搜尋符合條件之object
    filter_obj = stonks_DB.objects.filter(comp_id = post_comp_id, year = post_year, season = post_season)

    #如無符合條件之data，回傳400
    if filter_obj.count() == 0:
        return JsonResponse({"status": False, "message": "cannot find package"}, status=400)

    #取出第一筆資料
    filter_obj = filter_obj.first()

    #將撈出之data變成dict, 記得內容要轉成json
    return_dict = {'balance_sheet':json.loads(filter_obj.balance_sheet), 'income_statement':json.loads(filter_obj.income_statement)}

    #回傳200,這裡使用JsonResponse, 把dict之資料變成JSON
    return JsonResponse(data=return_dict, status=200)
