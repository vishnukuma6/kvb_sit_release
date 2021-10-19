from django.urls import path
from Bigflow.ATMA import views
urlpatterns = [

    path('ATMA_PartnerSummary/', views.ATMA_PartnerSummary, name='ATMA_PartnerSummary'),
    path('AtmaPartnerDeactivationRequest/',views.AtmaPartnerDeactivationRequest, name='AtmaPartnerDeactivationRequest'),
    path('AtmaPartnerActivationRequest/',views.AtmaPartnerActivationRequest, name='AtmaPartnerActivationRequest'),
    path('partdisapproval_get/', views.partdisapproval_get, name='partdisapproval_get'),
    path('AtmaPartnerTerminationRequest/',views.AtmaPartnerTerminationRequest, name='AtmaPartnerTerminationRequest'),
    path('partnerdeactivate_set/', views.partnerdeactivate_set, name='partnerdeactivate_set'),
    path('partapproval_get/', views.partapproval_get, name='partapproval_get'),
    path('atma_getdata/', views.atma_getdata, name='atma_getdata'),
    path('atma_getdirectordata/', views.atma_getdirectordata, name='atma_getdirectordata'),
    path('atma_viewdata/', views.atma_viewdata, name='atma_viewdata'),
    path('atma_partneradd/', views.atma_partneradd, name='atma_partneradd'),
    path('atmadocgroupset/', views.atma_docgroupset , name='atma_docgroupset'),
    path('atmaPartnerPayment_Set/', views.atmaPartnerPayment_Set, name='atmaPartnerPayment_Set'),
    path('atma_addpayment/', views.atma_addpayment, name='atma_addpayment'),
    path('atma_branchdetailsdropdown/', views.atma_branchdetailsdropdown, name='atma_branchdetailsdropdown'),
    path('atma_doc_get/', views.atma_doc_get, name='atma_doc_get'),
    path('atma_attachmentupload/', views.atma_attachmentupload, name='atma_attachmentupload'),
    path('atma_gettaxdetails/', views.atma_gettaxdetails, name='atma_gettaxdetails'),
    path('atma_taxdetailsfileupload/', views.atma_taxdetailsfileupload, name='atma_taxdetailsfileupload'),
    # path('atma_taxviewpage/', views.atma_taxviewpage, name='atma_taxviewpage'), # commented by Ramesh May 10 - 2020 - VAPT - no template
    path('atma_tax_details/', views.atma_tax_details, name='atma_tax_details'),
    path('atma_updateattacment_details/', views.atma_updateattacment_details, name='atma_updateattacment_details'),
    path('atma_paymentdetails/', views.atma_paymentdetails, name='atma_paymentdetails'),
    path('atma_attachmentdetails/', views.atma_attachmentdetails, name='atma_attachmentdetails'),

    path('atma_activity_get/', views.atma_activity_get, name='atma_activity_get'),
    path('atma_ProductCatSubCat_get/', views.atma_ProductCatSubCat_get, name='atma_ProductCatSubCat_get'),
    path('atma_activityadd/', views.atma_activityaddIndex, name='atma_activityadd'),
    path('atma_activityaddedit/', views.atma_activityaddedit , name='atma_activityaddedit'),

    path('atma_activitydetails/', views.atma_activitydetails, name='atma_activitydetails'),
    path('atma_activitydetailsview/', views.atma_activitydetailsview, name='atma_activitydetailsview'),
    path('atma_activitydetailsedit/', views.atma_activitydetailsedit, name='atma_activitydetailsedit'),
    path('atma_activitydetailsget/', views.atma_activitydetailsget, name='atma_activitydetailsget'),
    path('atma_activitydetailsset/', views.atma_activitydetailsset , name='atma_activitydetailsset'),
    # path('atma_Activitydetails/',views.atma_ActivitydetailsIndex, name='atma_Activitydetails'),

    path('atma_profilepage/', views.atma_profilepage , name='atma_profilepage'),
    path('atma_Productdetails/', views.atma_Productdetails , name='atma_Productdetails'),
    path('atma_profileproduct_get/', views.atma_profileproduct_get , name='atma_profileproduct_get'),
    path('atma_profileproduct_set/', views.atma_profileproduct_set , name='atma_profileproduct_set'),
    path('atma_Branchdetails/', views.atma_Branchdetails , name='atma_Branchdetails'),
    path('atma_Clientdetails/', views.atma_Clientdetails , name='atma_Clientdetails'),
    path('atma_Contractdetails/', views.atma_Contractdetails , name='atma_Contractdetails'),
    path('atma_SetClientdetails/', views.atma_SetClientdetails , name='atma_SetClientdetails'),
    path('atma_SetContractdetails/', views.atma_SetContractdetails , name='atma_SetContractdetails'),
    path('atma_SetBranchdetails/', views.atma_SetBranchdetails , name='atma_SetBranchdetails'),
    path('atma_BasicProfilDetails/', views.atma_BasicProfilDetails , name='atma_BasicProfilDetails'),
    path('atma_Setbasicprofildedetails/', views.atma_Setbasicprofildedetails , name='atma_Setbasicprofildedetails'),
    path('atma_PartnerCheckerPage/', views.atma_PartnerCheckerPage , name='atma_PartnerCheckerPage'),
    path('atma_PartnerCheckerApprovalPage/', views.atma_PartnerCheckerApprovalPage , name='atma_PartnerCheckerApprovalPage'),
    path('atma_CheckerDetails/', views.atma_CheckerDetails , name='atma_CheckerDetails'),
    path('atma_Catalogcreation/',views.atma_catalogcreation, name='atma_catalogcreation'),
    path('atmacatalogset/', views.atmacatalogset, name='atmacatalogset'),
    path('atmacatalog_get/', views.atmacatalog_get, name='atmacatalog_get'),
    path('AtmaPartnerMaker/',views.AtmaPartnerMaker, name='AtmaPartnerMaker'),
    path('prmakerset/', views.prmakerset , name='prmakerset'),
    path('prmaker_get/', views.prmaker_get, name='prmaker_get'),

    # Atma approval_or_Reject_ Page
    path('atma_Approval_Summary_Page/', views.atma_Approval_Summary_Page, name='atma_Approval_Summary_Page'),
    path('atma_Approval_ViewDetails_Page/', views.atma_Approval_ViewDetails_Page,name='atma_Approval_ViewDetails_Page'),
    path('atma_Approval_Taxdetails_Page/', views.atma_Approval_Taxdetails_Page, name='atma_Approval_Taxdetails_Page'),
    path('atma_Approval_Paymentdetails_Page/', views.atma_Approval_Paymentdetails_Page,name='atma_Approval_Paymentdetails_Page'),
    path('atma_Approval_Attachmentdetails_Page/', views.atma_Approval_Attachmentdetails_Page,name='atma_Approval_Attachmentdetails_Page'),
    path('atma_Approval_ProfileBasic_Page/', views.atma_Approval_ProfileBasic_Page,name='atma_Approval_ProfileBasic_Page'),
    path('atma_Approval_ProfileBranch_Page/', views.atma_Approval_ProfileBranch_Page,name='atma_Approval_ProfileBranch_Page'),
    path('atma_Approval_ProfileClient_Page/', views.atma_Approval_ProfileClient_Page,name='atma_Approval_ProfileClient_Page'),
    path('atma_Approval_ProfileContract_Page/', views.atma_Approval_ProfileContract_Page,name='atma_Approval_ProfileContract_Page'),
    path('atma_Approval_ProfileProduct/', views.atma_Approval_ProfileProduct,name='atma_Approval_ProfileProduct'),
    path('atma_Approval_ActivityDetails_Page/', views.atma_Approval_ActivityDetails_Page,name='atma_Approval_ActivityDetails_Page'),
    path('atma_Approval_ActivityDetails_Summary/', views.atma_Approval_ActivityDetails_Summary,name='atma_Approval_ActivityDetails_Summary'),
    path('atma_Approval_Catalogcreation/', views.atma_Approval_Catalogcreation,name='atma_Approval_Catalogcreation'),
    path('atma_Approval_Stages/', views.atma_Approval_Stages,name='atma_Approval_Stages'),
    path('atma_Approval_Request_Change/', views.atma_Approval_Request_Change,name='atma_Approval_Request_Change'),
    path('atma_ApprovedPartner_Get/', views.atma_ApprovedPartner_Get,name='atma_ApprovedPartner_Get'),
    path('atma_changerequest_activationupdate/', views.atma_changerequest_activationupdate,name='atma_changerequest_activationupdate'),
    path('atma_changerequest_summarypage/', views.atma_changerequest_summarypage,name='atma_changerequest_summarypage'),
    path('create_activity_details/', views.create_activity_details,name='create_activity_details'),
    path('create_catalog_details/', views.create_catalog_details,name='create_catalog_details'),
    path('Partner_Address/', views.Partner_Address,name='Partner_Address'),
    path('Partner_Contact/', views.Partner_Contact,name='Partner_Contact'),
    path('atma_ProductCatSubCat_get/', views.atma_ProductCatSubCat_get, name='atma_ProductCatSubCat_get'),
    path('Query_Page/', views.Query_Page,name='Query_Page'),
    path('Renewal_Page/', views.Renewal_Page,name='Renewal_Page'),
    path('Bankbranch_Add/', views.Bankbranch_Add,name='Bankbranch_Add'),
    path('Bankbranch_summary/', views.Bankbranch_summary,name='Bankbranch_summary'),
    path('Bankbranch_setdetails/', views.Bankbranch_setdetails,name='Bankbranch_setdetails'),
    path('BankGL_Summary/', views.BankGL_Summary,name='BankGL_Summary'),
    path('BankGL_Edit/', views.BankGL_Edit,name='BankGL_Edit'),


]