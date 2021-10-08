from django.shortcuts import render
from Bigflow.Transaction.Model import mFET, mSales
from Bigflow.Master.Model import mMasters
from django.http import JsonResponse
from datetime import date
import json
import time
import datetime
import pandas as pd
import Bigflow.Core.models as common

today = date.today()
today == date.fromtimestamp(time.time())
ddaate = date(today.year, 4, 1)


def add_schdle(request):
    if request.method == 'POST':
        obj_add_schedule = mFET.FET_model()
        jsondata = json.loads(request.body.decode('utf-8'))
        if jsondata.get('parms').get('TYPE') == 'SCHEDULE':
            obj_add_schedule.action = 'Insert'
            obj_add_schedule.type = 'SINGLE'
            obj_add_schedule.sechedule_gid = 0
            obj_add_schedule.jsonData_sec = json.dumps(jsondata.get('parms').get('customer_gid'))
            obj_add_schedule.customer_gid = jsondata.get('parms').get('customer_gid')
            obj_add_schedule.followup_reason_gid = 0
            obj_add_schedule.schedule_ref_gid = 0
            obj_add_schedule.sch_remark = 'Direct'
            if jsondata.get('parms').get('emp_gid') != None:
                if jsondata.get('parms').get('emp_gid') != 0:
                    obj_add_schedule.employee_gid = jsondata.get('parms').get('emp_gid')
            else:
                obj_add_schedule.employee_gid = request.session['Emp_gid']
            obj_add_schedule.date = common.convertDate(jsondata.get('parms').get('Date'))
            obj_add_schedule.schedule_type_gid = jsondata.get('parms').get('schedule_type_gid')
            obj_add_schedule.entity_gid = 1
            obj_add_schedule.resechedule_date = ''
            obj_add_schedule.create_by = request.session['Emp_gid']
            out_message = obj_add_schedule.set_schedule()
            if (out_message != ''):
                output = out_message
                return JsonResponse(json.dumps(output), safe=False)

        elif jsondata.get('parms').get('TYPE') == 'LEADS':
            obj_add_schedule.customer_name = jsondata.get('parms').get('customer_name')
            obj_add_schedule.address_1 = jsondata.get('parms').get('address')
            obj_add_schedule.mobile_no = jsondata.get('parms').get('mobile_no')
            obj_add_schedule.landline_no = jsondata.get('parms').get('landline_no')


        elif jsondata.get('parms').get('TYPE') == 'RESCHEDULE' or jsondata.get('parms').get('TYPE') == 'Reschedule_all':
            obj_add_schedule.action = jsondata.get('parms').get('TYPE')
            obj_add_schedule.type = 'SINGLE'
            obj_add_schedule.sch_remark = jsondata.get('parms').get('ls_Remarks')
            obj_add_schedule.resechedule_date = convertDate(jsondata.get('parms').get('ls_reschdul_date'))
            obj_add_schedule.sechedule_gid = jsondata.get('parms').get('schedule_gid')
            if jsondata.get('parms').get('schedule_gid') == 0:
                obj_add_schedule.date = common.convertDate(jsondata.get('parms').get('sch_date'))
                obj_add_schedule.jsonData = json.dumps(jsondata.get('parms').get('cust_gid'))
            obj_add_schedule.create_by = request.session['Emp_gid']
            out_message = outputReturn(obj_add_schedule.set_schedule(), 1)
            return JsonResponse(out_message, safe=False)

        elif jsondata.get('parms').get('TYPE') == 'SCHEDULE_BULK':
            obj_add_schedule.action = 'Insert'
            obj_add_schedule.type='SCHEDULE_BULK'
            obj_add_schedule.sechedule_gid = 0
            obj_add_schedule.jsonData_sec = json.dumps(jsondata.get('parms').get('customer_gid'))
            obj_add_schedule.followup_reason_gid = 0
            obj_add_schedule.schedule_ref_gid = 0
            obj_add_schedule.sch_remark = 'Direct'
            if jsondata.get('parms').get('emp_gid') != 0:
                obj_add_schedule.employee_gid = jsondata.get('parms').get('emp_gid')
            obj_add_schedule.date = common.convertDate(jsondata.get('parms').get('Date'))
            obj_add_schedule.entity_gid = 1
            obj_add_schedule.resechedule_date = ''
            obj_add_schedule.create_by = request.session['Emp_gid']
            out_message = obj_add_schedule.set_schedule()
            if (out_message != ''):
                output = out_message
                return JsonResponse(out_message, safe=False)

        elif jsondata.get('parms').get('TYPE') == 'UPDATE':
            obj_add_schedule.action = 'Update'
            obj_add_schedule.type = 'SINGLE'
            obj_add_schedule.sechedule_gid = jsondata.get('parms').get('schedule_gid')
            obj_add_schedule.customer_gid = jsondata.get('parms').get('cust_gid')
            obj_add_schedule.followup_reason_gid = jsondata.get('parms').get('followupreason_gid')
            obj_add_schedule.schedule_ref_gid = jsondata.get('parms').get('sechedule_ref')
            obj_add_schedule.date = jsondata.get('parms').get('Date')
            obj_add_schedule.schedule_type_gid = jsondata.get('parms').get('schedule_type_gid')
            obj_add_schedule.entity_gid = 1
            obj_add_schedule.sch_remark = 'Update'
            obj_add_schedule.create_by = request.session['Emp_gid']
            obj_add_schedule.man = jsondata.get('parms').get('ls_followup_date')
            if jsondata.get('parms').get('ls_followup_date') != None and jsondata.get('parms').get(
                    'ls_followup_date') != '':
                obj_add_schedule.ls_followup_date = convertDate(jsondata.get('parms').get('ls_followup_date'))
            else:
                obj_add_schedule.ls_followup_date = ''
            out_message = outputReturn(obj_add_schedule.set_schedule(), 0)
            return JsonResponse(out_message, safe=False)

        elif jsondata.get('parms').get('TYPE') == 'INDATE':
            obj_add_schedule.action = 'Update'
            obj_add_schedule.type = 'SINGLE'
            obj_add_schedule.sechedule_gid = jsondata.get('parms').get('schedule_gid')
            obj_add_schedule.customer_gid = jsondata.get('parms').get('cust_gid')
            obj_add_schedule.followup_reason_gid = jsondata.get('parms').get('followupreason_gid')
            obj_add_schedule.schedule_ref_gid = jsondata.get('parms').get('sechedule_ref')
            obj_add_schedule.date = jsondata.get('parms').get('Date')
            obj_add_schedule.schedule_type_gid = jsondata.get('parms').get('schedule_type_gid')
            obj_add_schedule.entity_gid = 1
            obj_add_schedule.sch_remark = jsondata.get('parms').get('ls_Remarks')
            obj_add_schedule.create_by = request.session['Emp_gid']

            if jsondata.get('parms').get('ls_followup_date') != None:
                obj_add_schedule.ls_followup_date = datetime.datetime.strptime(
                    jsondata.get('parms').get('ls_followup_date'), "%d/%m/%Y").strftime("%Y-%m-%d")
            else:
                obj_add_schedule.ls_followup_date = ''
                out_message = obj_add_schedule.set_schedule()
                if (out_message != ''):
                    output = out_message
                    return JsonResponse(json.dumps(output), safe=False)

            obj_add_schedule.resechedule_date = jsondata.get('parms').get('resechedule_date')
            out_message = outputReturn(obj_add_schedule.set_schedule(), 1)
            return JsonResponse(out_message, safe=False)

        elif jsondata.get('parms').get('TYPE') == 'DELETE':
            obj_add_schedule.action = 'Delete'
            obj_add_schedule.type = 'SINGLE'
            obj_add_schedule.sechedule_gid = jsondata.get('parms').get('schedule_gid')
            obj_add_schedule.customer_gid = 0
            obj_add_schedule.followup_reason_gid = 0
            obj_add_schedule.schedule_ref_gid = 0
            obj_add_schedule.date = ''
            obj_add_schedule.schedule_type_gid = 0
            obj_add_schedule.entity_gid = 1
            obj_add_schedule.resechedule_date = ''
            obj_add_schedule.create_by = request.session['Emp_gid']
            out_message = obj_add_schedule.set_schedule()
            return JsonResponse(json.dumps(out_message), safe=False)

    else:
        return render(request, "FET/fet_addschedule.html")


def status_qty(request):
    if request.method == 'POST':
        obj_qty = mFET.FET_model()
        jsondata = json.loads(request.body.decode('utf-8'))
        obj_qty.action = 'Insert'
        obj_qty.employee_gid = request.session['Emp_gid']
        obj_qty.customer_gid = jsondata.get('parms').get('custid')
        obj_qty.from_date = common.convertdbDate(request.session['date'])
        obj_qty.to_date = common.convertdbDate(request.session['date'])
        obj_qty.entity_gid = request.session['Entity_gid']
        df_obj_add_schedule = obj_qty.get_qty()
        jdata = df_obj_add_schedule.to_json(orient='records')
        return JsonResponse(json.loads(jdata), safe=False)


def convertDate(stringDate):
    return datetime.datetime.strptime(stringDate, "%d/%m/%Y").strftime("%Y-%m-%d")


def status_get(request):
    if request.method == 'POST':
        obj_status = mFET.FET_model()
        jsondata = json.loads(request.body.decode('utf-8'))
        obj_status.action = 'Reschedule'
        obj_status.employee_gid = request.session['Emp_gid']
        obj_status.customer_gid = jsondata.get('parms').get('customer_gid')
        obj_status.from_date = common.convertdbDate(request.session['date'])
        obj_status.to_date = common.convertdbDate(request.session['date'])
        obj_status.entity_gid = request.session['Entity_gid']
        df_obj_add_schedule = obj_status.get_schedul()
        jdata = df_obj_add_schedule.to_json(orient='records')
        return JsonResponse(json.loads(jdata), safe=False)


def serviceIndex(request):
    return render(request, "FET/fet_service.html")


def pcollectionIndex(request):
    return render(request, "FET/fet_Collection.html")


def preschdleIndex(request):
    return render(request, "FET/fet_preschedule.html")


def pre_schedule_get(request):
    if request.method == 'GET':
        obj_preschedule_get = mFET.FET_model()
        obj_preschedule_get.employee_gid = request.session['Emp_gid']
        obj_preschedule_get.action = request.GET['action']
        obj_preschedule_get.date = datetime.datetime.strptime(request.GET['f_date'], "%d/%m/%Y").strftime("%Y-%m-%d")
        obj_preschedule_get.create_by = request.session['Emp_gid']
        df_preschedule = obj_preschedule_get.get_preschedule_fet()
        jdata = df_preschedule.to_json(orient='records')
        return JsonResponse(json.loads(jdata), safe=False)
    elif request.method == 'POST':
        obj_preschedule_get = mFET


def empvsschedule_get(request):
    if request.method == 'GET':
        data = {}
        obj_empvsschedule = mFET.FET_model()

        obj_empvsschedule.action = request.GET['action']
        if request.GET['emp_gid'] == '0':
            data['employee_gid'] = request.session['Emp_gid']
        else:
            data['employee_gid'] = request.GET['emp_gid']
        if (request.GET['f_date'] != ''):
            data['fromdate'] = common.convertDate(request.GET['f_date'])
        if (request.GET['t_date'] != ''):
            data['todate'] = common.convertDate(request.GET['t_date'])
        data['customer_gid'] = request.GET['cus_gid']
        data['scheduletype_gid'] = request.GET['scheduletype_gid']
        obj_empvsschedule.jsonData = json.dumps(data)
        obj_empvsschedule.entity_gid = 1
        df_preschedule = obj_empvsschedule.get_empvsSchedule()
        df_preschedule['login_gid'] = request.session['Emp_gid']
        jdata = df_preschedule.to_json(orient='records')
        return JsonResponse(json.loads(jdata), safe=False)


def followup_reason(request):
    if request.method == 'GET':
        obj_followup_reason = mFET.FET_model()
        obj_followup_reason.schedule_type_gid = request.GET['schType_gid']
        obj_followup_reason.entity_gid = request.session['Entity_gid']
        df_followup_reason = obj_followup_reason.get_followup_reason_fet()
        jdata = df_followup_reason.to_json(orient='records')
        return JsonResponse(json.loads(jdata), safe=False)


def schedule_type(request):
    if request.method == 'GET':
        obj_schedule_type = mFET.FET_model()
        obj_schedule_type.entity_gid = request.session['Entity_gid']
        df_schedule_type = obj_schedule_type.get_schedule_type()
        jdata = df_schedule_type.to_json(orient='records')
        return JsonResponse(json.loads(jdata), safe=False)


def reportupdateIndex(request):
    return render(request, "FET/fet_reportupdate.html")


def schedule_collectionIndex(request):
    return render(request, "FET/fet_ScheduleCollection.html")


def mapped_customer(request):
    if request.method == 'GET':
        obj_mapped_customer = mFET.FET_model()
        obj_mapped_customer.employee_gid = request.session['Emp_gid']
        obj_mapped_customer.entity_gid = request.session['Entity_gid']
        df_mapped_customer = obj_mapped_customer.get_mapped_customer()
        jdata = df_mapped_customer.to_json(orient='records')
        return JsonResponse(json.loads(jdata), safe=False)


def emp_mapped_customer(request):
    if request.method == 'GET':
        obj_empmapped_customer = mFET.FET_model()
        obj_empmapped_customer.employee_gid = request.GET['emp_gid']
        obj_empmapped_customer.entity_gid = request.session['Entity_gid']
        df_mapped_customer = obj_empmapped_customer.get_mapped_customer()
        jdata = df_mapped_customer.to_json(orient='records')
        return JsonResponse(json.loads(jdata), safe=False)


def customer_ddl(request):
    if request.method == 'GET':
        obj_customer_ddl = mFET.FET_model()
        obj_customer_ddl.customer_gid = 0
        obj_customer_ddl.entity_gid = request.session['Entity_gid']
        df_customer_ddl = obj_customer_ddl.get_customer()
        jdata = df_customer_ddl.to_json(orient='records')
        return JsonResponse(json.loads(jdata), safe=False)


def productcategory_ddl(request):
    if request.method == 'GET':
        obj_producategory_ddl = mFET.FET_model()
        obj_producategory_ddl.productcat_gid = 1
        df_customer_ddl = obj_producategory_ddl.get_productcategory()
        jdata = df_customer_ddl.to_json(orient='records')
        return JsonResponse(json.loads(jdata), safe=False)


def producttype_ddl(request):
    if request.method == 'GET':
        obj_producttype_ddl = mFET.FET_model()
        obj_producttype_ddl.producttype_gid = 1
        df_customer_ddl = obj_producttype_ddl.get_producttype()
        jdata = df_customer_ddl.to_json(orient='records')
        return JsonResponse(json.loads(jdata), safe=False)


def Productjson(request):
    if request.method == 'GET':
        form = mFET.FET_model
        jdata = form.get_product(request)
        if request.method == 'GET':
            return JsonResponse(json.dumps(jdata), safe=False)
        else:
            return render(request, "", {'form': jdata})


def TA_detailsIndex(request):
    return render(request, "FET/fet_TAdetails.html")


def sales_orderIndex(request):
    return render(request, "FET/fet_salesorder.html")


def sales_fav_product(request):
    if request.method == 'POST':
        obj_sales_fav_pdct = mFET.FET_model()
        jsondata = json.loads(request.body.decode('utf-8'))
        obj_sales_fav_pdct.customer_gid = jsondata.get('parms').get('custid')
        obj_sales_fav_pdct.product_type = 1
        obj_sales_fav_pdct.entity_gid = request.session['Entity_gid']
        df_sales_fav_pdct = obj_sales_fav_pdct.get_sales_fav_product()
        jdata = df_sales_fav_pdct.to_json(orient='records')
        return JsonResponse(json.loads(jdata), safe=False)


def sales_order_set(request):
    if request.method == 'POST':
        obj_sales = mSales.Sales_Model()
        jsondata = json.loads(request.body.decode('utf-8'))
        if jsondata.get('parms').get('ACTION') == 'Insert':
            obj_sales.customer_gid = jsondata.get('parms').get('custid')
            obj_sales.employee_gid = request.session['Emp_gid']
            obj_sales.entity_gid = 1
            obj_sales.So_Header_date = common.convertdbDate(request.session['date'])
            obj_sales.Channel = 'c'
            obj_sales.action = 'Insert'
            obj_sales.sodetails = jsondata.get('parms').get('data')
            setsales_order = outputReturn(obj_sales.set_sales_order(), 0)
            return JsonResponse(setsales_order, safe=False)
        elif jsondata.get('parms').get('ACTION') == 'Update':
            obj_sales.customer_gid = jsondata.get('parms').get('custid')
            obj_sales.employee_gid = request.session['Emp_gid']
            obj_sales.entity_gid = 1
            # obj_sales.quantity=x.get('quantity')
            obj_sales.So_Header_date = common.convertdbDate(request.session['date'])
            obj_sales.Channel = 'c'
            obj_sales.action = 'Update'
            obj_sales.sodetails = jsondata.get('parms').get('data')
            setsales_order = outputReturn(obj_sales.set_sales_order(), 1)
            # jdata = setsales_order.to_json(orient='records')
            return JsonResponse(setsales_order, safe=False)
        elif jsondata.get('parms').get('ACTION') == 'DIRECTSALE_DELETE':
            obj_sales.customer_gid = jsondata.get('parms').get('custid')
            obj_sales.employee_gid = request.session['Emp_gid']
            obj_sales.entity_gid = 1
            obj_sales.soheader_gid = jsondata.get('parms').get('soheader_gid')
            obj_sales.So_Header_date = common.convertdbDate(request.session['date'])
            obj_sales.Channel = 'c'
            obj_sales.action = 'DIRECTSALE_DELETE'
            obj_sales.sodetails = jsondata.get('parms').get('data')
            setsales_order = outputReturn(obj_sales.set_sales_order(), 1)
            return JsonResponse(setsales_order, safe=False)
        elif jsondata.get('parms').get('ACTION') == 'Delete':
            obj_sales.customer_gid = jsondata.get('parms').get('custid')
            obj_sales.employee_gid = request.session['Emp_gid']
            obj_sales.entity_gid = 1
            # obj_sales.quantity=x.get('quantity')
            obj_sales.So_Header_date = common.convertdbDate(request.session['date'])
            obj_sales.Channel = 'c'
            obj_sales.action = 'Delete'
            obj_sales.sodetails = jsondata.get('parms').get('data')
            setsales_order = outputReturn(obj_sales.set_sales_order(), 1)
            # jdata = setsales_order.to_json(orient='records')
            return JsonResponse(setsales_order, safe=False)


def outputReturn(tubledtl, index):
    temp = tubledtl[0].split(',')
    if (len(temp) > 1):
        if (index == 0):
            return int(temp[0])
        else:
            return temp[1]
    else:
        return temp[0]


def get_addScheduleDtl(request):
    schedule = []
    if request.method == 'GET':
        obj_mapped_customer1 = mFET.FET_model()
        obj_mapped_customer1.employee_gid = request.session['Emp_gid']
        obj_mapped_customer1.entity_gid = request.session['Entity_gid']
        df_mapped_customer = obj_mapped_customer1.get_mapped_customer()

        obj_mapped_customer1.action = request.GET['action']
        obj_mapped_customer1.date = datetime.datetime.strptime(request.GET['f_date'], "%d/%m/%Y").strftime("%Y-%m-%d")
        obj_mapped_customer1.create_by = request.session['Emp_gid']
        obj_mapped_customer1.entity_gid = request.session['Entity_gid']
        df_preschedule = obj_mapped_customer1.get_preschedule()

        df_schedule_type = obj_mapped_customer1.get_schedule_type()
        total_schCount = df_preschedule['schedule_customer_gid'].unique().size
        sch_count = []
        for x, cus in df_mapped_customer.iterrows():

            schlist = []
            for y, sch in df_schedule_type.iterrows():
                sch_type = {'sch_type': sch['scheduletype_name'], 'schType_gid': sch['scheduletype_gid']}
                d = df_preschedule[(df_preschedule['schedule_customer_gid'] == cus['customer_gid'])
                                   & (df_preschedule['schedule_scheduletype_gid'] == sch['scheduletype_gid'])]
                if d.empty:
                    sch_type['sch_gid'] = ''
                    sch_type['sch_status'] = ''
                    sch_type['sch_ischecked'] = False
                else:
                    sch_type['sch_gid'] = d['schedule_gid'].iloc[0]
                    sch_type['sch_status'] = d['schedule_status'].iloc[0]
                    sch_type['sch_ischecked'] = True
                schlist.append(sch_type)
            schedule.append(schlist)
            sch_count.append(total_schCount)
        df_mapped_customer['schedule'] = schedule
        df_mapped_customer['sch_count'] = sch_count
        jdata = df_mapped_customer.to_json(orient='records')

        return JsonResponse(json.loads(jdata), safe=False)


def sales_order_get(request):
    if request.method == 'POST':
        obj_salesget = mSales.Sales_Model()
        jsondata = json.loads(request.body.decode('utf-8'))
        obj_salesget.action = jsondata.get('parms').get('action')
        obj_salesget.customer_gid = jsondata.get('parms').get('custid')
        obj_salesget.employee_gid = request.session['Emp_gid']
        obj_salesget.date = common.convertdbDate(request.session['date'])
        obj_salesget.limit = 30
        setsales_order = obj_salesget.get_sales_order()
        jdata = setsales_order.to_json(orient='records')
        return JsonResponse(json.loads(jdata), safe=False)


def serviceFET_set(request):
    if request.method == 'POST':
        obj_add_service = mFET.FET_model()
        jsondata = json.loads(request.body.decode('utf-8'))
        customer_gid = jsondata.get('parms').get('custid')
        lst_salesdata = jsondata.get('parms').get('data')
        for x in lst_salesdata:
            obj_add_service.employee_gid = request.session['Emp_gid']
            obj_add_service.code = '1'
            obj_add_service.customer_gid = customer_gid
            obj_add_service.date = common.convertdbDate(request.session['date'])
            obj_add_service.product_gid = x.get('product_gid')
            obj_add_service.product_stockcode = x.get('product_stock_code')
            obj_add_service.remark = x.get('remarks')
            out_message = obj_add_service.set_service()
        if (out_message != ''):
            output = out_message
            return JsonResponse(json.dumps(output), safe=False)
        return out_message


def collection_set(request):
    if request.method == 'POST':
        obj_add_collection = mFET.FET_model()

        jsondata = json.loads(request.body.decode('utf-8'))
        obj_add_collection.customer_gid = jsondata.get('cust_gid')
        obj_add_collection.employee_gid = request.session['Emp_gid']
        obj_add_collection.mode = jsondata.get('collection_mode')
        obj_add_collection.amount = jsondata.get('collection_amount')
        obj_add_collection.date = jsondata.get('date')
        obj_add_collection.cheque_no = jsondata.get('cheque_no')  # OPtional
        if jsondata.get('collection_mode') == 'Cheque':
            obj_add_collection.jsonData = json.dumps(jsondata.get('cheque_data'))
        obj_add_collection.entity_gid = 1

        out_message = outputReturn(obj_add_collection.set_collection(), 0)
        return JsonResponse(out_message, safe=False)


def outstanding_fet_get(request):
    if request.method == 'POST':
        obj_outstanding_fet = mFET.FET_model()
        jsondata = json.loads(request.body.decode('utf-8'))
        if jsondata.get('parms').get('ACTION') == 'outstandingemployee':
            obj_outstanding_fet.customer_gid = 0
            obj_outstanding_fet.from_date = ''
            obj_outstanding_fet.to_date = ''
            obj_outstanding_fet.employee_gid = request.session['Emp_gid']
            obj_outstanding_fet.limit = 0
            obj_outstanding_fet.action = 'outstandingemployee'
            obj_outstanding_fet.entity_gid = request.session['Entity_gid']
            df_outstanding_fet = obj_outstanding_fet.get_FEToutstanding_fet()
            jdata = df_outstanding_fet.to_json(orient='records')
            return JsonResponse(json.loads(jdata), safe=False)
        elif jsondata.get('parms').get('ACTION') == 'outstandingcustomer':
            obj_outstanding_fet.customer_gid = jsondata.get('parms').get('customer_gid')
            obj_outstanding_fet.from_date = ''
            obj_outstanding_fet.to_date = ''
            obj_outstanding_fet.employee_gid = request.session['Emp_gid']
            obj_outstanding_fet.limit = 5
            obj_outstanding_fet.action = 'outstandingcustomer'
            obj_outstanding_fet.entity_gid = request.session['Entity_gid']
            df_outstanding_fet = obj_outstanding_fet.get_FEToutstanding_fet()
            jdata = df_outstanding_fet.to_json(orient='records')
            return JsonResponse(json.loads(jdata), safe=False)
    elif request.method == 'GET':
        obj_outstanding_fet = mFET.FET_model()
        obj_outstanding_fet.action = request.GET['action']
        obj_outstanding_fet.customer_gid = request.GET['cust_gid']
        obj_outstanding_fet.from_date = common.convertDate(request.GET['f_date']) if request.GET['f_date']!='' else ''
        obj_outstanding_fet.to_date = common.convertDate(request.GET['t_date']) if request.GET['t_date']!='' else ''
        obj_outstanding_fet.employee_gid = request.GET['emp_gid']
        obj_outstanding_fet.entity_gid=1
        obj_outstanding_fet.limit = request.GET['row_limit']
        obj_outstanding_fet.entity_gid = request.session['Entity_gid']
        df_outstanding_fet = obj_outstanding_fet.get_FEToutstanding_fet()
        jdata = df_outstanding_fet.to_json(orient='records')
        return JsonResponse(json.loads(jdata), safe=False)


def sales_history_fet_get(request):
    if request.method == 'POST':
        obj_sales_history = mFET.FET_model()
        jsondata = json.loads(request.body.decode('utf-8'))
        obj_sales_history.customer_gid = jsondata.get('parms').get('customer_gid')
        obj_sales_history.from_date = ''
        obj_sales_history.to_date = ''
        obj_sales_history.entity_gid = request.session['Entity_gid']
        df_sales_history = obj_sales_history.get_sales_history_fet()
        jdata = df_sales_history.to_json(orient='records')
        return JsonResponse(json.loads(jdata), safe=False)


def collection_history_fet(request):
    if request.method == 'POST':
        obj_collection_history = mFET.FET_model()
        jsondata = json.loads(request.body.decode('utf-8'))
        obj_collection_history.action = 'Scheduleview'
        obj_collection_history.customer_gid = jsondata.get('parms').get('custid')
        obj_collection_history.employee_gid = request.session['Emp_gid']
        obj_collection_history.from_date = (datetime.date.today() + datetime.timedelta(-6*365/12)).isoformat()
        obj_collection_history.to_date = common.convertdbDate(request.session['date'])
        df_collection_history = obj_collection_history.get_collection_history_fet()
        jdata = df_collection_history.to_json(orient='records')
        return JsonResponse(json.loads(jdata), safe=False)


def schedule_view_fet_get(request):
    if request.method == 'POST':
        obj_schedule_view = mFET.FET_model()
        jsondata = json.loads(request.body.decode('utf-8'))
        obj_schedule_view.customer_gid = jsondata.get('parms').get('customer_gid')
        obj_schedule_view.from_date = ''
        obj_schedule_view.to_date = ''
        obj_schedule_view.limit = 30
        obj_schedule_view.entity_gid = request.session['Entity_gid']
        df_schedule_view = obj_schedule_view.get_schedule_view_fet()
        jdata = df_schedule_view.to_json(orient='records')
        return JsonResponse(json.loads(jdata), safe=False)


def leadrequest_set(request):
    if request.method == 'POST':
        obj_leadsrequest = mFET.FET_model()
        jsondata = json.loads(request.body.decode('utf-8'))
        obj_leadsrequest.action = jsondata.get('parms').get('action')
        obj_leadsrequest.leadref_gid = jsondata.get('parms').get('leadref_gid')
        obj_leadsrequest.customer_name = jsondata.get('parms').get('customer_name')
        obj_leadsrequest.mobile_no = jsondata.get('parms').get('mobile_no')
        obj_leadsrequest.address1 = jsondata.get('parms').get('address')
        obj_leadsrequest.entity_gid = 1
        obj_leadsrequest.employee_gid = request.session['Emp_gid']
        out_message = outputReturn(obj_leadsrequest.set_leadrequest(), 1)
        return JsonResponse(out_message, safe=False)


def leadrequest_approve(request):
    if request.method == 'POST':
        obj_lead_approve = mFET.FET_model()
        jsondata = json.loads(request.body.decode('utf-8'))
        obj_lead_approve.action = jsondata.get('parms').get('action')
        obj_lead_approve.leadref_gid = jsondata.get('parms').get('leadref_gid')
        obj_lead_approve.status = jsondata.get('parms').get('status')
        obj_lead_approve.reason = jsondata.get('parms').get('reason')
        obj_lead_approve.employee_gid = request.session['Emp_gid']
        out_message = outputReturn(obj_lead_approve.set_leadrequest(), 1)
        return JsonResponse(out_message, safe=False)


def leadrequest_get(request):
    if request.method == 'GET':
        obj_leadsrequest_get = mFET.FET_model()
        obj_leadsrequest_get.leadref_gid = request.GET['leadref_gid']
        obj_leadsrequest_get.leadref_name = request.GET['leadref_name']
        obj_leadsrequest_get.status = request.GET['leadref_status']
        obj_leadsrequest_get.mobile_no = request.GET['mobile_no']
        obj_leadsrequest_get.entity_gid = request.session['Entity_gid']
        df_lead_view = obj_leadsrequest_get.get_leadrequest()
        jdata = df_lead_view.to_json(orient='records')
        return JsonResponse(json.loads(jdata), safe=False)


def Schedule_reportIndex(request):
    return render(request, "FET/fet_ScheduleReport.html")


def Schedule_reportget(request):
    if request.method == 'GET':
        obj_Schdul_det = mFET.FET_model()
        params = json.loads(request.GET['details'])
        obj_Schdul_det.from_date = convertDate(params.get('fdata'))
        obj_Schdul_det.to_date = convertDate(params.get('tdate'))
        obj_Schdul_det.employee_gid = params.get('Emp_gid')
        obj_Schdul_det.customer_gid = params.get('cust_gid')
        obj_Schdul_det.limit = 10000
        obj_Schdul_det.entity_gid = request.session['Entity_gid']
        dt_shedul = obj_Schdul_det.get_schedule_view_fet()
        df = pd.DataFrame(dt_shedul)
        df_filtered = df.query('schedule_status=="CLOSED"')
        obj_Schdul_det.date = params.get('resh_date')
        obj_Schdul_det.entity_gid = request.session['Entity_gid']
        dt_salesorder = obj_Schdul_det.get_sales_history_fet()
        obj_Schdul_det.action = 'OutstandingCustomer'
        dtsales = pd.merge(df_filtered, dt_salesorder, how='left', left_on='Schedule_ref_gid',
                           right_on='soheader_gid')
        dtsales["collection_amount"] = 0
        dtsales["Outstanding_amount"] = ''
        for index, row in dtsales.iterrows():
            schedule_type = row['scheduletype_name']
            Schedule_ref_gid = row['Schedule_ref_gid']
            obj_Schdul_det.from_date = ''
            obj_Schdul_det.to_date = row['schedule_date'].date()
            obj_Schdul_det.customer_gid = row['schedule_customer_gid']
            dt_outstanding = obj_Schdul_det.get_outstanding_fet()
            outstand = pd.DataFrame(dt_outstanding)
            dtsales.set_value(index, 'Outstanding_amount', outstand['pending'].sum())
            if (schedule_type == 'COLLECTION'):
                if (pd.notnull(Schedule_ref_gid)):
                    obj_Schdul_det.collectionheader_gid = Schedule_ref_gid
                    colln_data = obj_Schdul_det.get_collection_amt()
                    coll = pd.DataFrame(colln_data)
                    dtsales.set_value(index, 'collection_amount', coll['fetcollectionheader_amount'])
        jdata = dtsales.to_json(orient='records')
        return JsonResponse(jdata, safe=False)


def report_collection(request):
    if request.method == 'POST':
        obj_Schdul_det = mFET.FET_model()
        jsondata = json.loads(request.body.decode('utf-8'))
        obj_Schdul_det.collectionheader_gid = jsondata.get('params').get('collectionheader_gid')
        colln_data = obj_Schdul_det.get_collection_amt()
        jdata = colln_data.to_json(orient='records')
        return JsonResponse(jdata, safe=False)


def bank_detail(request):
    if request.method == 'GET':
        obj_bank_detail = mFET.FET_model()
        obj_bank_detail.entity_gid = request.session['Entity_gid']
        df_bank_view = obj_bank_detail.get_bankdetails()
        jdata = df_bank_view.to_json(orient='records')
        return JsonResponse(json.loads(jdata), safe=False)


def directIndex(request):
    return render(request, "FET/fet_DirectSale.html")

def directentryIndex(request):
    return render(request, "FET/fet_DirectEntry.html")

def salecreateIndex(request):
    return render(request, "FET/fet_SaleCreate.html")


def collectioncreateIndex(request):
    return render(request, "FET/fet_CollectionCreate.html")


def fetapprovalIndex(request):
    return render(request, "FET/fet_Approval.html")


def fetprospctIndex(request):
    return render(request, 'FET/fet_Prospect.html')


def getEditSchedule(request):
    if request.method == 'GET':
        obj_scheduleEdit = mFET.FET_model()
        obj_scheduleEdit.schedule_gid = request.GET['schedule_gid']
        obj_scheduleEdit.entity_gid = request.session['Entity_gid']
        df_scheduledtl = obj_scheduleEdit.get_scheduleEdit()
        jdata = df_scheduledtl.to_json(orient='records')
        return JsonResponse(json.loads(jdata), safe=False)

def getEditdrct(request):
    if request.method == 'GET':
        obj_scheduleEdit = mFET.FET_model()
        obj_scheduleEdit.action = request.GET['action']
        obj_scheduleEdit.SO_Header_gid = request.GET['SO_Header_gid']
        obj_scheduleEdit.entity_gid = request.session['Entity_gid']
        df_scheduledtl = obj_scheduleEdit.get_drctEdit()
        jdata = df_scheduledtl.to_json(orient='records')
        return JsonResponse(json.loads(jdata), safe=False)

def getCustomerFilterlist(request):
    if request.method == 'GET':
        employee = json.loads(request.GET['emp_gid'])
        routedtl = json.loads(request.GET['route_gid'])
        clusterdtl = json.loads(request.GET['cluster_gid'])
        # employee
        obj_hirEmpList = mFET.FET_model()
        obj_hirEmpList.employee_gid = request.session['Emp_gid']
        obj_hirEmpList.employee_name = ''
        obj_hirEmpList.cluster_gid = 1
        obj_hirEmpList.entity_gid = request.session['Entity_gid']
        df_emp = obj_hirEmpList.getHierarchy_employeeList()
        tee = df_emp[df_emp['employee_gid'] == request.session['Emp_gid']]
        tee1 = tee['employee_supervisor_gid'].tolist()[0]
        emp_tree = getempTree(df_emp, tee1)
        # route
        obj_hirEmpList.action = 'ROUTE_FILTER'
        obj_hirEmpList.route_gid = 0
        obj_hirEmpList.route_name = ''
        obj_hirEmpList.route_code = ''
        if (len(employee) != 0):
            employee = json.loads(request.GET['emp_gid'])
        else:
            employee = df_emp['employee_gid'].tolist()

        obj_hirEmpList.json_employee_gid = json.dumps({'routeemp_gid': employee})
        obj_hirEmpList.entity_gid = request.session['Entity_gid']
        df_route = obj_hirEmpList.getRoute()
        route_tree = getrouteTree(df_route)
        # territory
        obj_clustertree = mMasters.Masters()
        obj_clustertree.action = 'PARENT_ROUTE'
        obj_clustertree.cluster_parent_gid = 0
        obj_clustertree.hierarchy_gid = 0
        obj_clustertree.employee_gid = 0
        obj_clustertree.entity_gid = request.session['Entity_gid']
        obj_clustertree.jsonData = json.dumps(
            {'FILTER': [{'Employee_gid': employee, 'Cluster_gid': clusterdtl, 'Route_header_gid': routedtl}]})
        df_cluster = obj_clustertree.get_cluster()
        te = getmenutree(df_cluster, 0)
        # customer

        obj_hirEmpList.action = 'ADD_SCHEDULE'
        obj_hirEmpList.entity_gid = request.session['Entity_gid']
        obj_hirEmpList.jsonData = json.dumps(
            {'FILTER': [{'Employee_gid': employee, 'Cluster_gid': clusterdtl, 'Route_header_gid': routedtl}]})

        df_custall = obj_hirEmpList.getcustomer()
        df_custall['type'] = 'ALL'
        obj_hirEmpList.action = 'ROUTE_MAP'
        today = common.convertdbDate(request.session['date'])
        fdate = datetime.datetime.strptime(request.GET['f_date'], "%d/%m/%Y").strftime("%A")
        obj_hirEmpList.jsonData = json.dumps(
            {'FILTER': [{'Employee_gid': employee, 'Cluster_gid': clusterdtl, 'Route_header_gid': routedtl}],
             'ROUTE_MAP': [{'Employee_gid': employee, 'Day_plan': fdate, 'Schedule_date': today}]})
        obj_hirEmpList.entity_gid = request.session['Entity_gid']
        df_custroute = obj_hirEmpList.getcustomer()
        df_custroute['type'] = 'ROUTE'
        df_cust = pd.concat([df_custall, df_custroute], ignore_index=True)
        data = {}
        df_size = (df_cust[['customer_size', 'customer_size_gid']]).groupby(
            ['customer_size', 'customer_size_gid']).size().reset_index();
        df_type = (df_cust[['customer_type']]).groupby(['customer_type']).size().reset_index();
        df_category = (df_cust[['custcategory_name', 'customer_category_gid']]).groupby(
            ['custcategory_name', 'customer_category_gid']).size().reset_index();
        df_constitution = (df_cust[['customer_constitution', 'customer_constitution_gid']]).groupby(
            ['customer_constitution', 'customer_constitution_gid']).size().reset_index();
        df_mode = (df_cust[['customer_salemode', 'customer_salemode_gid']]).groupby(
            ['customer_salemode', 'customer_salemode_gid']).size().reset_index();

        obj_hirEmpList.action = request.GET['action']
        obj_hirEmpList.date = convertDate(request.GET['f_date'])

        # obj_hirEmpList.employee_gid=employee
        obj_hirEmpList.create_by = request.session['Emp_gid']
        obj_hirEmpList.entity_gid = request.session['Entity_gid']
        df_preschedule = obj_hirEmpList.get_preschedule()
        df_schedule_type = obj_hirEmpList.get_schedule_type()
        data['employee'] = emp_tree
        data['route'] = route_tree
        data['terrirtory'] = te
        data['size'] = json.loads(df_size.to_json(orient='records'))
        data['type'] = json.loads(df_type.to_json(orient='records'))
        data['categroy'] = json.loads(df_category.to_json(orient='records'))
        data['constitution'] = json.loads(df_constitution.to_json(orient='records'))
        data['mode'] = json.loads(df_mode.to_json(orient='records'))
        data['customer'] = json.loads(
            get_filteredCustomer(df_cust, df_preschedule, df_schedule_type).to_json(orient='records'))
        jdata = data
        return JsonResponse(jdata, safe=False)


def get_filteredCustomer(customerList, scheduleList, scheduleTypeList):
    schedule = []
    df_mapped_customer = customerList
    df_preschedule = scheduleList
    df_schedule_type = scheduleTypeList
    total_schCount = df_preschedule['schedule_customer_gid'].unique().size
    sch_count = []
    orderby = []
    status=[]
    nnme=[]
    editflag = []
    ordertype = []
    schlistempty=[];
    for y, sch in df_schedule_type.iterrows():
        sch_type = {'sch_type': sch['scheduletype_name'], 'schType_gid': sch['scheduletype_gid'],'schtype_order':sch['scheduletype_order']}
        sch_type['sch_gid'] = ''
        sch_type['sch_status'] = ''
        sch_type['sch_empname'] = ''
        sch_type['sch_edit'] = ''
        sch_type['schtype_order'] = ''
        sch_type['sch_ischecked'] = False
        schlistempty.append(sch_type)

    for x, cus in df_mapped_customer.iterrows():
          schlist = []
          order_by = 1
          status_det = ""
          empnme = ""
          edit =""
          schorder =""
          per = df_preschedule[(df_preschedule['schedule_customer_gid'] == cus['customer_gid'])];
          if not per.empty:
            for y, sch in df_schedule_type.iterrows():
                sch_type = {'sch_type': sch['scheduletype_name'], 'schType_gid': sch['scheduletype_gid'],'schtype_order':sch['scheduletype_order']}
                d = df_preschedule[(df_preschedule['schedule_customer_gid'] == cus['customer_gid'])
                                   & (df_preschedule['schedule_scheduletype_gid'] == sch['scheduletype_gid'])]
                if d.empty:
                    sch_type['sch_gid'] = ''
                    sch_type['sch_status'] = ''
                    sch_type['sch_empname'] = ''
                    sch_type['sch_edit'] = ''
                    sch_type['schtype_order'] = ''
                    sch_type['sch_ischecked'] = False
                else:
                    status_det=d['schedule_status'].iloc[0]
                    empnme = d['employee_name'].iloc[0]
                    if d['Is_Edit'].iloc[0] =='Y':
                        edit = d['IS_FOLLOW_UP_EDIT'].iloc[0]
                    else:
                        edit = d['Is_Edit'].iloc[0]
                    schorder = d['scheduletype_order'].iloc[0]
                    if d['Order_by'].iloc[0] == '0' and order_by == 1:
                        order_by = 0
                    sch_type['sch_gid'] = d['schedule_gid'].iloc[0]
                    sch_type['sch_status'] = d['schedule_status'].iloc[0]
                    sch_type['sch_empname'] = d['employee_name'].iloc[0]
                    if d['Is_Edit'].iloc[0] =='Y':
                        sch_type['sch_edit'] =  d['IS_FOLLOW_UP_EDIT'].iloc[0]
                    else:
                        sch_type['sch_edit'] = d['Is_Edit'].iloc[0]
                    sch_type['schtype_order'] = d['scheduletype_order'].iloc[0]
                    sch_type['sch_ischecked'] = True
                schlist.append(sch_type)
            schedule.append(schlist)
            status.append(status_det)
            nnme.append(empnme)
            editflag.append(edit)
            ordertype.append(schorder)
            orderby.append(order_by)
            sch_count.append(total_schCount)
          else:
            schedule.append(schlistempty)
            status.append(status_det)
            nnme.append(empnme)
            editflag.append(edit)
            ordertype.append(schorder)
            orderby.append(order_by)
            sch_count.append(total_schCount)
    df_mapped_customer['sch_status']=status
    df_mapped_customer['sch_empname']=nnme
    df_mapped_customer['schedule'] = schedule
    df_mapped_customer['sch_count'] = sch_count
    df_mapped_customer['sch_edit'] = editflag
    df_mapped_customer['schtype_order'] = ordertype
    df_mapped_customer['Order_by'] = orderby
    return df_mapped_customer.sort_values(['Order_by', 'customer_name'])

def getClusterTree(request):
    if request.method == 'GET':
        obj_clustertree = mMasters.Masters()
        obj_clustertree.action = 'ALL'
        obj_clustertree.cluster_parent_gid = 0
        obj_clustertree.hierarchy_gid = 0
        obj_clustertree.employee_gid = 0
        obj_clustertree.entity_gid = request.session['Entity_gid']
        df_cluster = obj_clustertree.get_cluster()
        jdata = df_cluster.to_json(orient='records')
        te = getmenutree(df_cluster, 0)
        return JsonResponse(te, safe=False)


def getmenutree(list, parent_gid):
    # te = getmenutree(df_cluster, 0)
    de = []
    re = list[list['cluster_parent_gid'] == parent_gid]
    for x, main in re.iterrows():
        te = {}
        te['menu_id'] = main['cluster_gid']
        te['menu_name'] = main['cluster_name']
        te['menu_parent'] = main['cluster_parent_gid']
        te['cluster_hierarchygid'] = main['cluster_hierarchygid']
        te['child_list'] = getmenutree(list, main['cluster_gid'])
        de.append(te)
    return de


def getempTree(list, parent_gid):
    de = []
    re = list[list['employee_supervisor_gid'] == parent_gid]
    for x, main in re.iterrows():
        te = {}
        te['emp_gid'] = main['employee_gid']
        te['emp_name'] = main['employee_name']
        te['child_list'] = getempTree(list, main['employee_gid'])
        de.append(te)
    return de


def getrouteTree(list):
    de = []
    ter = (list[['routeheader_name', 'routeheader_gid']]).groupby(
        ['routeheader_name', 'routeheader_gid']).size().reset_index();
    for x, main in ter.iterrows():
        te = {}
        te['route_gid'] = main['routeheader_gid']
        te['route_name'] = main['routeheader_name']
        ter1 = list[list['routeheader_gid'] == main['routeheader_gid']]
        ter2 = (ter1[['cluster_name', 'cluster_gid']]).groupby(
            ['cluster_name', 'cluster_gid']).size().reset_index();
        te['child_list'] = json.loads(ter2.to_json(orient='records'))
        de.append(te)
    return de


def stocktakenIndex(request):
    return render(request, "FET/fet_stocktaken.html")


def stockget(request):
    if request.method == 'POST':
        obj_stock = mFET.FET_model()
        jsondata = json.loads(request.body.decode('utf-8')).get('parms')
        obj_stock.action = jsondata.get('action')
        obj_stock.employee_gid = request.session['Emp_gid']
        obj_stock.customer_gid = jsondata.get('custid')
        obj_stock.from_date = ddaate.replace(today.year - 3)
        obj_stock.to_date = date.today()
        obj_stock.date = jsondata.get('todaydate')
        obj_stock.type = jsondata.get('type')
        obj_stock.entity_gid = request.session['Entity_gid']
        df_obj_add_schedule = obj_stock.get_stock()
        jdata = df_obj_add_schedule.to_json(orient='records')
        return JsonResponse(json.loads(jdata), safe=False)


def stockeditget(request):
    if request.method == 'POST':
        obj_stock = mFET.FET_model()
        jsondata = json.loads(request.body.decode('utf-8')).get('parms')
        obj_stock.action = jsondata.get('action')
        obj_stock.employee_gid = request.session['Emp_gid']
        obj_stock.customer_gid = jsondata.get('custid')
        obj_stock.from_date = ddaate.replace(today.year - 3)
        obj_stock.to_date = date.today()
        obj_stock.date = common.convertDate(jsondata.get('todaydate'))
        obj_stock.type = jsondata.get('type')
        obj_stock.entity_gid = request.session['Entity_gid']
        df_obj_add_schedule = obj_stock.get_stock()
        jdata = df_obj_add_schedule.to_json(orient='records')
        return JsonResponse(json.loads(jdata), safe=False)


def stockset(request):
    if request.method == 'POST':
        obj_leadsrequest = mFET.FET_model()
        jsondata = json.loads(request.body.decode('utf-8')).get('parms')
        obj_leadsrequest.action = jsondata.get('action')
        obj_leadsrequest.customer_gid = jsondata.get('custid')
        obj_leadsrequest.date = common.convertDate(jsondata.get('todaydate'))
        obj_leadsrequest.employee_gid = request.session['Emp_gid']
        obj_leadsrequest.entity_gid = 1
        obj_leadsrequest.stckdet = json.dumps(jsondata.get('stckdet'))
        out_message = outputReturn(obj_leadsrequest.set_stock(), 0)
        return JsonResponse(out_message, safe=False)


def emptrackingIndex(request):
    return render(request, "FET/fet_emp_tracking.html")

def stockcreateIndex(request):
    return render(request, "FET/fet_Stockcreate.html")

def schedulereviewIndex(request):
    return render(request, "FET/fet_rep_review.html")


def sale_approval(request):
    if request.method == 'POST':
        obj_lead_approve = mFET.FET_model()
        jsondata = json.loads(request.body.decode('utf-8'))
        obj_lead_approve.action = jsondata.get('parms').get('action')
        obj_lead_approve.soheader_gid = jsondata.get('parms').get('headergid')
        obj_lead_approve.remark = jsondata.get('parms').get('reason')
        obj_lead_approve.create_by = request.session['Emp_gid']
        obj_lead_approve.entity_gid = 1
        out_message = outputReturn(obj_lead_approve.set_saleaprve(), 1)
        return JsonResponse(out_message, safe=False)


def sale_order_get(request):
    if request.method == 'GET':
        obj_leadsrequest_get = mSales.Sales_Model()
        obj_leadsrequest_get.action = request.GET['action']
       # obj_leadsrequest_get.date = common.convertdbDate(request.session['date'])
        obj_leadsrequest_get.customer_gid = request.GET['custid']
        obj_leadsrequest_get.employee_gid = request.GET['empid']
        obj_leadsrequest_get.limit = request.GET['limit']
        df_lead_view = obj_leadsrequest_get.get_sales_order()
        jdata = df_lead_view.to_json(orient='records')
        return JsonResponse(json.loads(jdata), safe=False)


def setschedule_review(request):
    if request.method == 'POST':
        jsondata = json.loads(request.body.decode('utf-8'))
        obj_schReview = mFET.FET_model()
        obj_schReview.action = jsondata.get('parms').get('action')
        obj_schReview.jsonData = json.dumps(jsondata.get('parms').get('data'))
        obj_schReview.entity_gid = 1
        obj_schReview.create_by = request.session['Emp_gid']
        out_message = common.outputReturn(obj_schReview.set_schedulereview(), 0)
        return JsonResponse(out_message, safe=False)
# Ramesh