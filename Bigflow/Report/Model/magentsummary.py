from django.db import connection
import pandas as pd
from Bigflow.Master.Model import mVariable
class control(mVariable.variable):
    def Agentsummary_Get(self):
        cursor = connection.cursor()
        Parameters = (self.action, self.type, self.main, self.enty, '')
        cursor.callproc('sp_Agentsummary_Get', Parameters)
        columns = [x[0] for x in cursor.description]
        rows = cursor.fetchall()
        rows = list(rows)
        df_customer = pd.DataFrame(rows, columns=columns)
        return {"DATA": df_customer, "MESSAGE": "FOUND"}

    def sp_PPR_Data_Get_frm_gen_Bussiness(self):
        cursor = connection.cursor()
        Parameters = (self.action, self.jsonData, self.dataw, '')
        cursor.callproc('sp_PPR_Data_Get', Parameters)
        columns = [x[0] for x in cursor.description]
        rows = cursor.fetchall()
        cursor.execute('select @_sp_PPR_Data_Get_3')
        outmsg_sp = cursor.fetchone()
        rows = list(rows)
        df_sales = pd.DataFrame(rows, columns=columns).to_dict(orient='records')
        return {"DATA": df_sales, "MESSAGE": outmsg_sp[0]}


    def sp_AllTableValues_Get_frm_gen(self):
        cursor = connection.cursor()
        Parameters = ('', self.jsonData, self.entity_gid, '')
        cursor.callproc('sp_AllTableValues_Get', Parameters)
        columns = [x[0] for x in cursor.description]
        rows = cursor.fetchall()
        cursor.execute('select @_sp_AllTableValues_Get_3')
        outmsg_sp = cursor.fetchone()
        rows = list(rows)
        df_sales = pd.DataFrame(rows, columns=columns).to_dict(orient='records')
        return {"DATA": df_sales, "MESSAGE": outmsg_sp[0]}

    def sp_PPR_Data_Get_frm_gen(self):
        cursor = connection.cursor()
        Parameters = (self.action, self.jsonData, self.dataw, '')
        cursor.callproc('sp_PPR_Data_Get', Parameters)
        columns = [x[0] for x in cursor.description]
        rows = cursor.fetchall()
        cursor.execute('select @_sp_PPR_Data_Get_3')
        outmsg_sp = cursor.fetchone()
        rows = list(rows)
        df_sales = pd.DataFrame(rows, columns=columns).to_dict(orient='records')
        return {"DATA": df_sales, "MESSAGE": outmsg_sp[0]}

    def sp_PPR_Data_Set_frm_gen(self):
        cursor = connection.cursor()
        Parameters = (self.action, self.jsonData, self.dataw, '')
        cursor.callproc('sp_PPR_Data_Set', Parameters)
        cursor.execute('select @_sp_PPR_Data_Set_3')
        outmsg_sp = cursor.fetchone()
        return {"MESSAGE": outmsg_sp[0]}

    def sp_PPR_Budget_Get_frm_gen(self):
        cursor = connection.cursor()
        Parameters = (self.action,self.type, self.jsonData, self.dataw, '')
        cursor.callproc('sp_PPR_Budget_Get', Parameters)
        columns = [x[0] for x in cursor.description]
        rows = cursor.fetchall()
        cursor.execute('select @_sp_PPR_Budget_Get_4')
        outmsg_sp = cursor.fetchone()
        rows = list(rows)
        df_sales = pd.DataFrame(rows, columns=columns).to_dict(orient='records')
        if columns[0] == '@finaldata':
            return {"DATA": df_sales[0], "MESSAGE": outmsg_sp[0]}
        return {"DATA": df_sales, "MESSAGE": outmsg_sp[0]}

    def sp_PPR_Budget_Set_frm_gen(self):
        cursor = connection.cursor()
        Parameters = (self.action, self.jsonData, self.dataw, '')
        cursor.callproc('sp_PPR_Budget_Set', Parameters)
        cursor.execute('select @_sp_PPR_Budget_Set_3')
        outmsg_sp = cursor.fetchone()
        return {"MESSAGE": outmsg_sp[0]}

    def sp_PPR_BudgetReviewer_Get_frm_gen(self):
        cursor = connection.cursor()
        Parameters = (self.action, self.jsonData, self.dataw, '')
        cursor.callproc('sp_PPR_ReviwerData', Parameters)
        columns = [x[0] for x in cursor.description]
        rows = cursor.fetchall()
        cursor.execute('select @_sp_PPR_ReviwerData_3')
        outmsg_sp = cursor.fetchone()
        rows = list(rows)
        df_sales = pd.DataFrame(rows, columns=columns).to_dict(orient='records')
        return {"DATA": df_sales, "MESSAGE": outmsg_sp[0]}

    def sp_PPR_BudgetReviewer_set_frm_gen(self):
        cursor = connection.cursor()
        Parameters = (self.action, self.jsonData, self.dataw, '')
        cursor.callproc('sp_PPR_BudgetReviewer_Set', Parameters)
        cursor.execute('select @_sp_PPR_BudgetReviewer_Set_3')
        outmsg_sp = cursor.fetchone()
        return {"MESSAGE": outmsg_sp[0]}

    def sp_PPR_mono_micro_Get(self):
        cursor = connection.cursor()
        Parameters = (self.action, self.jsonData, self.dataw, '')
        cursor.callproc('sp_PPR_Mono_Micro_GET', Parameters)
        columns = [x[0] for x in cursor.description]
        rows = cursor.fetchall()
        cursor.execute('select @_sp_PPR_Mono_Micro_GET_3')
        outmsg_sp = cursor.fetchone()
        if outmsg_sp[0] == 'NOT FOUND':
            return {"DATA": [], "MESSAGE": outmsg_sp[0]}
        rows = list(rows)
        df_sales = pd.DataFrame(rows, columns=columns).to_dict(orient='records')
        return {"DATA": df_sales, "MESSAGE": outmsg_sp[0]}

