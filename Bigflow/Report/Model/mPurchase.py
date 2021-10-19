
from django.db import connection
import pandas as pd
import json
from Bigflow.Master.Model import mVariable
class PurchaseModel(mVariable.variable):
    def get_prpo_query(self):
        cursor = connection.cursor()
        parameters = (self.type, self.sub_type, self.filter_json, self.json_classification, '')
        cursor.callproc('sp_PRPO_Query_Get', parameters)
        columns = [x[0] for x in cursor.description]
        rows = cursor.fetchall()
        cursor.execute('select @_sp_PRPO_Query_Get_4')
        outmsg_sp = cursor.fetchone()
        rows = list(rows)
        df_fa = pd.DataFrame(rows, columns=columns)
        return {"DATA": df_fa, "MESSAGE": outmsg_sp[0]}

    def get_attendance_mis(self):
        cursor = connection.cursor()
        parameters = (self.Type, self.SubType, self.Filter, self.json_classification, '')
        cursor.callproc('sp_OutstandingCustomer_Get', parameters)
        columns = [x[0] for x in cursor.description]
        rows = cursor.fetchall()
        cursor.execute('select @_sp_OutstandingCustomer_Get_4')
        out_put = cursor.fetchone()
        rows = list(rows)
        df_preschedule = pd.DataFrame(rows, columns=columns)
        return df_preschedule


    def get_followup_mis(self):
        cursor = connection.cursor()
        json1 = json.dumps(self.data)
        Parameters = (self.Type, self.SubType, json1, self.json_classification, '')
        cursor.callproc('sp_CustomerFollowUp_Get', Parameters)
        columns = [x[0] for x in cursor.description]
        rows = cursor.fetchall()
        cursor.execute('select @_sp_CustomerFollowUp_Get_4')
        out_put = cursor.fetchone()
        rows = list(rows)
        df_followups = pd.DataFrame(rows, columns=columns)
        return df_followups

    def get_followup90_mis(self):
        cursor = connection.cursor()
        json1 = json.dumps(self.data)
        Parameters = (self.Type, self.SubType, json1, self.json_classification, '')
        cursor.callproc('sp_CustomerFollowUp_Get', Parameters)
        columns = [x[0] for x in cursor.description]
        rows = cursor.fetchall()
        cursor.execute('select @_sp_CustomerFollowUp_Get_4')
        out_put = cursor.fetchone()
        rows = list(rows)
        df_followups = pd.DataFrame(rows, columns=columns)
        return df_followups

    def invoicesummary_get(self):
        cursor = connection.cursor()
        parameters = (self.type, self.subtype,self.json_Data,self.json_classification, '')
        cursor.callproc('sp_OutstandingCustomer_Get', parameters)
        columns = [x[0] for x in cursor.description]
        rows = cursor.fetchall()
        cursor.execute('select @_sp_OutstandingCustomer_Get_4')
        out_put = cursor.fetchone()
        rows = list(rows)
        df_inv = pd.DataFrame(rows, columns=columns)
        return df_inv

    def branchsummary_get(self):
        cursor = connection.cursor()
        parameters = (self.type, self.subtype,self.json_Datas,self.json_classification, '')
        cursor.callproc('sp_OutstandingCustomer_Get', parameters)
        columns = [x[0] for x in cursor.description]
        rows = cursor.fetchall()
        cursor.execute('select @_sp_OutstandingCustomer_Get_4')
        out_put = cursor.fetchone()
        rows = list(rows)
        df_brnch = pd.DataFrame(rows, columns=columns)
        return df_brnch

    def invoicesummaryy_get(self):
        cursor = connection.cursor()
        json1 = json.dumps(self.data)
        parameters = (self.type, self.subtype,json1,self.json_classification, '')
        cursor.callproc('sp_OutstandingCustomer_Get', parameters)
        columns = [x[0] for x in cursor.description]
        rows = cursor.fetchall()
        cursor.execute('select @_sp_OutstandingCustomer_Get_4')
        out_put = cursor.fetchone()
        rows = list(rows)
        df_invv = pd.DataFrame(rows, columns=columns)
        return df_invv



    def custgrp_get(self):
        cursor = connection.cursor()
        parameters = (self.type, self.subtype, self.json_Data, self.json_classification, '')
        cursor.callproc('sp_SalesHist_Get', parameters)
        columns = [x[0] for x in cursor.description]
        rows = cursor.fetchall()
        cursor.execute('select @_sp_SalesHist_Get_4')
        out_put = cursor.fetchone()
        rows = list(rows)
        df_custt = pd.DataFrame(rows, columns=columns)
        return df_custt


    def cust_get(self):
        cursor = connection.cursor()
        parameters = (self.type, self.subtype, self.jsonDatas, self.json_classification, '')
        cursor.callproc('sp_SalesHist_Get', parameters)
        columns = [x[0] for x in cursor.description]
        rows = cursor.fetchall()
        cursor.execute('select @_sp_SalesHist_Get_4')
        out_put = cursor.fetchone()
        rows = list(rows)
        df_cust = pd.DataFrame(rows, columns=columns)
        return df_cust

    def empname_get(self):
        cursor = connection.cursor()
        parameters = (self.type, self.subtype, self.json_Data, self.json_classification, '')
        cursor.callproc('sp_OutstandingCustomer_Get', parameters)
        columns = [x[0] for x in cursor.description]
        rows = cursor.fetchall()
        cursor.execute('select @_sp_OutstandingCustomer_Get_4')
        out_put = cursor.fetchone()
        rows = list(rows)
        df_empname = pd.DataFrame(rows, columns=columns)
        return df_empname


    def get_followup90_mis(self):
        cursor = connection.cursor()
        json1 = json.dumps(self.data)
        Parameters = (self.Type, self.SubType, json1, self.json_classification, '')
        cursor.callproc('sp_CustomerFollowUp_Get', Parameters)
        columns = [x[0] for x in cursor.description]
        rows = cursor.fetchall()
        cursor.execute('select @_sp_CustomerFollowUp_Get_4')
        out_put = cursor.fetchone()
        rows = list(rows)
        df_followups = pd.DataFrame(rows, columns=columns)
        return df_followups

    def invoicesummary_get(self):
        cursor = connection.cursor()
        parameters = (self.type, self.subtype,self.json_Data,self.json_classification, '')
        cursor.callproc('sp_OutstandingCustomer_Get', parameters)
        columns = [x[0] for x in cursor.description]
        rows = cursor.fetchall()
        cursor.execute('select @_sp_OutstandingCustomer_Get_4')
        out_put = cursor.fetchone()
        rows = list(rows)
        df_empup = pd.DataFrame(rows, columns=columns)
        return df_empup



    def get_cheques_mis(self):
        cursor = connection.cursor()
        json1 = json.dumps(self.data)
        Parameters = (self.Action, self.Type, json1, self.json_classification,self.ls_create_by, '')
        cursor.callproc('sp_ChqinClear_Get', Parameters)
        columns = [x[0] for x in cursor.description]
        rows = cursor.fetchall()
        cursor.execute('select @sp_ChqinClear_Get_5')
        out_put = cursor.fetchone()
        rows = list(rows)
        df_followups = pd.DataFrame(rows, columns=columns)
        return df_followups


    def get_Outstanding_comparison(self):
        cursor = connection.cursor()
        parameters = (self.type, self.sub_type, '{}', self.jsondata, '')
        cursor.callproc('sp_DailyPaymentReport_Get', parameters)
        columns = [x[0] for x in cursor.description]
        rows = cursor.fetchall()
        cursor.execute('select @_sp_DailyPaymentReport_Get_4')
        out_put = cursor.fetchone()
        rows = list(rows)
        df_preschedule = pd.DataFrame(rows, columns=columns)
        return df_preschedule

    def get_Outstanding_comparison(self):
        cursor = connection.cursor()
        parameters = (self.type, self.sub_type, '{}', self.jsondata, '')
        cursor.callproc('sp_DailyPaymentReport_Get', parameters)
        columns = [x[0] for x in cursor.description]
        rows = cursor.fetchall()
        cursor.execute('select @_sp_DailyPaymentReport_Get_4')
        out_put = cursor.fetchone()
        rows = list(rows)
        df_preschedule = pd.DataFrame(rows, columns=columns)
        return df_preschedule
