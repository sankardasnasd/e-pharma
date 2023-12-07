import datetime

from django.core.files.storage import FileSystemStorage
from django.db.models import F, Q
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from E_PHARMA.models import *


def login(request):
    return render(request,"1login.html")

def login_post(request):
    username=request.POST['textfield']
    password=request.POST['textfield2']
    var=Login.objects.filter(Username=username,Password=password)
    if var.exists():
        var2=Login.objects.get(Username=username,Password=password)
        request.session['lid']=var2.id
        if var2.Type=='Admin':
            return HttpResponse('''<script> alert("WELCOME!!!");window.location="/E_PHARMA/admin_home/"</script>''')
        elif var2.Type=='Customer' :
            return HttpResponse('''<script> alert("WELCOME!!!");window.location="/E_PHARMA/customer_home/"</script>''')
        else:

            return HttpResponse('''<script> alert("INVALID!!!");window.location="/E_PHARMA/login/"</script>''')
    else:

        return HttpResponse('''<script> alert("INVALID!!!");window.location="/E_PHARMA/login/"</script>''')

def logout(request):
    request.session['lid']=""
    return HttpResponse('''<script> alert("You have been logged out successfully!!!!");window.location="/E_PHARMA/login/"</script>''')


def admin_home(request):
    if request.session['lid']=="":
        return HttpResponse('''<script> alert("you are Logout!!!");window.location="/E_PHARMA/login/"</script>''')

    return render(request,"admin/adminindex.html")


def verify_customer(request):
    if request.session['lid']=="":
        return HttpResponse('''<script> alert("you are Logout!!!");window.location="/E_PHARMA/login/"</script>''')
    res=Customer.objects.filter(Status="pending")
    return render(request,"admin/2VerifyCustomers.html",{'data':res})
def verifycustomer_post(request):
    if request.session['lid']=="":
        return HttpResponse('''<script> alert("you are Logout!!!");window.location="/E_PHARMA/login/"</script>''')
    search=request.POST['textfield']
    res = Customer.objects.filter(Status='Pending', Name__icontains=search)
    # res = Customer.objects.filter(Name__icontains=search)
    return render(request,"admin/2VerifyCustomers.html",{'data':res})

def approve_customer(request,id):
    if request.session['lid']=="":
        return HttpResponse('''<script> alert("you are Logout!!!");window.location="/E_PHARMA/login/"</script>''')
    res=Customer.objects.filter(LOGIN=id).update(Status='Approved')
    res2=Login.objects.filter(id=id).update(Type='Customer')
    return HttpResponse('''<script> alert("APPROVED!!!");window.location="/E_PHARMA/admin_verify_customers/"</script>''')


def view_approved_customers(request):
    if request.session['lid']=="":
        return HttpResponse('''<script> alert("you are Logout!!!");window.location="/E_PHARMA/login/"</script>''')
    res = Customer.objects.filter(Status='Approved')
    return render(request,"admin/4Viewapprovedcustomers.html",{'data':res})

def view_approvedcustomer_post(request):
    if request.session['lid']=="":
        return HttpResponse('''<script> alert("you are Logout!!!");window.location="/E_PHARMA/login/"</script>''')
    search=request.POST['textfield']
    res = Customer.objects.filter(Status='Approved',Name__icontains=search)
    return render(request,"admin/4Viewapprovedcustomers.html",{'data':res})




def reject_customer(request,id):
    if request.session['lid']=="":
        return HttpResponse('''<script> alert("you are Logout!!!");window.location="/E_PHARMA/login/"</script>''')
    res=Customer.objects.filter(id=id).update(Status='Rejected')
    return HttpResponse('''<script> alert("REJECTED!!!");window.location="/E_PHARMA/admin_verify_customers/"</script>''')




def view_rejected_customers(request):
    if request.session['lid']=="":
        return HttpResponse('''<script> alert("you are Logout!!!");window.location="/E_PHARMA/login/"</script>''')
    res = Customer.objects.filter(Status='Rejected')
    return render(request,"admin/Viewrejectedcustomers.html",{'data':res})

def view_rejectedcustomer_post(request):
    if request.session['lid']=="":
        return HttpResponse('''<script> alert("you are Logout!!!");window.location="/E_PHARMA/login/"</script>''')
    search=request.POST['textfield']
    res = Customer.objects.filter(Status='Rejected',Name__icontains=search)
    return render(request,"admin/Viewrejectedcustomers.html",{'data':res})



def add_stock(request):
    if request.session['lid']=="":
        return HttpResponse('''<script> alert("you are Logout!!!");window.location="/E_PHARMA/login/"</script>''')
    return render(request,"admin/5AddStock.html")

def addstock_post(request):
    if request.session['lid']=="":
        return HttpResponse('''<script> alert("you are Logout!!!");window.location="/E_PHARMA/login/"</script>''')
    # p_code=request.POST['textfield']
    p_name = request.POST['textfield2']
    m_name = request.POST['textfield3']
    category= request.POST['select']
    qty = request.POST['textfield4']
    type=request.POST['select2']
    netvoldos=request.POST['textfield5']
    price = request.POST['textfield6']
    type_sub=request.POST['type']

    st = Stocks()
    # st.Product_Code=p_code
    st.Product_Name=p_name
    p_image=request.FILES['image']
    fs = FileSystemStorage()
    import datetime
    dt = 'medicines/' + datetime.datetime.now().strftime("%Y%m%d%H%M%S") + ".jpeg"
    fs.save(dt, p_image)
    path=fs.url(dt)
    st.Product_image = path
    st.Manufacturer_Name=m_name
    st.Category=category
    st.Product_Type=type
    st.Quantity=qty
    st.Netvoldos=netvoldos+type_sub
    st.Price=price
    st.save()
    return HttpResponse('''<script> alert("SUCCESSFULLY ADDED!!!");window.location="/E_PHARMA/admin_add_stock/"</script>''')


def view_stocks(request):
    if request.session['lid']=="":
        return HttpResponse('''<script> alert("you are Logout!!!");window.location="/E_PHARMA/login/"</script>''')
    st1=Stocks.objects.all()
    return render(request,"admin/6ViewStocks.html",{'data':st1})

def viewstocks_post(request):
    if request.session['lid']=="":
        return HttpResponse('''<script> alert("you are Logout!!!");window.location="/E_PHARMA/login/"</script>''')
    search=request.POST['textfield']
    res = Stocks.objects.filter(
        Q(Product_Name__icontains=search) | Q(Product_Type__icontains=search)
    )
    # res = Stocks.objects.filter(Product_Name__contains=search and Category__icontains=search )
    return render(request,"admin/6ViewStocks.html",{'data':res})

def edit_stock(request,did):
    if request.session['lid']=="":
        return HttpResponse('''<script> alert("you are Logout!!!");window.location="/E_PHARMA/login/"</script>''')
    res=Stocks.objects.get(id=did)
    m=res.Netvoldos
    m1=m[0:len(m)-2]
    print(m1,"hii33")
    m2=m[len(m)-2:]
    print(m2,"hii")
    return render(request,"admin/7EditStock.html",{'data':res,"m1":m1,"m2":m2})

def editstock_post(request):
    if request.session['lid']=="":
        return HttpResponse('''<script> alert("you are Logout!!!");window.location="/E_PHARMA/login/"</script>''')
    id=request.POST['id']
    # p_code=request.POST['textfield']
    p_name = request.POST['textfield2']
    m_name = request.POST['textfield3']
    category = request.POST['select']
    qty = request.POST['textfield4']
    type = request.POST['select2']
    nvd=request.POST['textfield5']
    price =request.POST['textfield6']
    type_sub = request.POST['type']

    st = Stocks.objects.get(id=id)

    if 'image' in request.FILES:
        p_image = request.FILES['image']
        dt = 'medicines/' + datetime.datetime.now().strftime("%Y%m%d%H%M%S") + ".jpeg"
        fs = FileSystemStorage()
        fs.save(dt,p_image)
        path = fs.url(dt)
        st.Product_image=path


    # st.Product_Code = p_code
    st.Product_Name = p_name
    st.Manufacturer_Name = m_name
    st.Category = category
    st.Quantity = qty
    st.Product_Type=type
    st.Netvoldos=nvd+type_sub
    st.Price = price
    st.save()
    return HttpResponse('''<script> alert("SUCCESSFULLY UPDATED!!!");window.location="/E_PHARMA/admin_view_stocks/"</script>''')

def admin_delete_stocks(request,id):
    if request.session['lid']=="":
        return HttpResponse('''<script> alert("you are Logout!!!");window.location="/E_PHARMA/login/"</script>''')
    res=Stocks.objects.get(id=id)
    res.delete()
    return HttpResponse('''<script> alert("SUCCESSFULLY DELETED!!!");window.location="/E_PHARMA/admin_view_stocks/"</script>''')


def add_inventory(request):
    if request.session['lid']=="":
        return HttpResponse('''<script> alert("you are Logout!!!");window.location="/E_PHARMA/login/"</script>''')
    var=Stocks.objects.all()
    dt = datetime.date.today()
    return render(request,"admin/8AddInventory.html",{'data':var, 'dt':str(dt)})

def addinventory_post(request):
    if request.session['lid']=="":
        return HttpResponse('''<script> alert("you are Logout!!!");window.location="/E_PHARMA/login/"</script>''')
    p_id = request.POST['select']
    expiry_date = request.POST['textfield3']
    s_code= request.POST['textfield4']
    s_row= request.POST['textfield5']
    s_col= request.POST['textfield6']

    inv=Inventory()
    inv.PRODUCT_id=p_id
    inv.Expiry_Date=expiry_date
    inv.Shelf_Code=s_code
    inv.Shelf_Rowno=s_row
    inv.Shelf_Colno=s_col
    inv.save()
    return HttpResponse('''<script> alert("SUCCESSFULLY ADDED!!!");window.location="/E_PHARMA/admin_add_inventory/"</script>''')


def view_inventory(request):
    if request.session['lid']=="":
        return HttpResponse('''<script> alert("you are Logout!!!");window.location="/E_PHARMA/login/"</script>''')
    st1 = Inventory.objects.all()
    return render(request,"admin/9ViewInventory.html",{'data':st1})

def viewinventory_post(request):
    if request.session['lid']=="":
        return HttpResponse('''<script> alert("you are Logout!!!");window.location="/E_PHARMA/login/"</script>''')
    search=request.POST['textfield']
    res = Inventory.objects.filter(PRODUCT__Product_Name__icontains=search)
    return render(request,"admin/9ViewInventory.html",{'data':res})


def edit_inventory(request,id):
    if request.session['lid']=="":
        return HttpResponse('''<script> alert("you are Logout!!!");window.location="/E_PHARMA/login/"</script>''')
    var=Stocks.objects.all()
    res =Inventory.objects.get(id=id)
    return render(request,"admin/10EditInventory.html",{'data':res,'var':var})

def editinventory_post(request):
    if request.session['lid']=="":
        return HttpResponse('''<script> alert("you are Logout!!!");window.location="/E_PHARMA/login/"</script>''')
    id = request.POST['id']
    p_id=request.POST['select2']
    expiry_date = request.POST['textfield3']
    s_code= request.POST['textfield4']
    s_row= request.POST['textfield5']
    s_col= request.POST['textfield6']

    inv = Inventory.objects.get(id=id)
    inv.PRODUCT_id = p_id
    inv.Expiry_Date = expiry_date
    inv.Shelf_Code = s_code
    inv.Shelf_Rowno = s_row
    inv.Shelf_Colno = s_col
    inv.save()
    return HttpResponse('''<script> alert("SUCCESSFULLY UPDATED!!!");window.location="/E_PHARMA/admin_view_inventory/"</script>''')

def admin_delete_inventory(request,id):
    if request.session['lid']=="":
        return HttpResponse('''<script> alert("you are Logout!!!");window.location="/E_PHARMA/login/"</script>''')
    res1=Inventory.objects.get(id=id)
    res1.delete()
    return HttpResponse('''<script> alert("SUCCESSFULLY DELETED!!!");window.location="/E_PHARMA/admin_view_inventory/"</script>''')


def view_prescription(request):
    if request.session['lid']=="":
        return HttpResponse('''<script> alert("you are Logout!!!");window.location="/E_PHARMA/login/"</script>''')
    res=Prescription.objects.all()
    return render(request,"admin/11Viewprescription.html",{'data':res})

def viewprescription_post(request):
    if request.session['lid']=="":
        return HttpResponse('''<script> alert("you are Logout!!!");window.location="/E_PHARMA/login/"</script>''')
    f_date=request.POST['textfield']
    t_date = request.POST['textfield2']
    var = OrderSub.objects.filter(Date__range=[f_date, t_date])
    return render(request,"admin/11Viewprescription.html",{'data':var})

# def admin_delete_orders(request,id):
#     res1=Prescription.objects.get(id=id)
#     res1.delete()
#     return HttpResponse('''<script> alert("SUCCESSFULLY DELETED!!!");window.location="/E_PHARMA/admin_view_prescription/"</script>''')


def update_availability_status(request,id):
    if request.session['lid']=="":
        return HttpResponse('''<script> alert("you are Logout!!!");window.location="/E_PHARMA/login/"</script>''')
    pobj=Stocks.objects.all()
    return render(request,"admin/12AvailabilityStatus.html",{'data':pobj,'id':id})

def updateavailability_post(request):
    if request.session['lid']=="":
        return HttpResponse('''<script> alert("you are Logout!!!");window.location="/E_PHARMA/login/"</script>''')
    # prescription_id= request.POST['select']
    id=request.POST['id']
    product_id = request.POST['select']
    status = request.POST['select2']
    qty = request.POST['quantity']


    ap=Available_Products()
    ap.PRESCRIPTION_id=id
    ap.PRODUCT_id=product_id
    ap.Status=status
    ap.Quantity=qty
    ap.save()
    return HttpResponse('''<script> alert("SUCCESSFULLY UPDATED!!!");window.location="/E_PHARMA/admin_view_prescription/"</script>''')


def view_orders(request):
    if request.session['lid']=="":
        return HttpResponse('''<script> alert("you are Logout!!!");window.location="/E_PHARMA/login/"</script>''')
    res=Order.objects.filter(Status='Ordered')
    return render(request,"admin/13ViewOrders.html",{'data':res})


# def admin_delete_orders(request,id):
#     res1=Order.objects.get(id=id)
#     res1.delete()
#     return HttpResponse('''<script> alert("SUCCESSFULLY DELETED!!!");window.location="/E_PHARMA/admin_view_orders/"</script>''')
#




def vieworder_post(request):
    if request.session['lid']=="":
        return HttpResponse('''<script> alert("you are Logout!!!");window.location="/E_PHARMA/login/"</script>''')
    f_date=request.POST['textfield']
    t_date = request.POST['textfield2']
    var = Order.objects.filter(Date__range=[f_date, t_date])

    return render(request,"admin/13ViewOrders.html",{'data':var})

def view_suborders(request,id):
    if request.session['lid']=="":
        return HttpResponse('''<script> alert("you are Logout!!!");window.location="/E_PHARMA/login/"</script>''')
    res = OrderSub.objects.filter(ORDER_id=id)
    return render(request,"admin/13ViewSubOrders.html",{'data':res})

def delivered(request,id):
    if request.session['lid']=="":
        return HttpResponse('''<script> alert("you are Logout!!!");window.location="/E_PHARMA/login/"</script>''')
    res=Order.objects.filter(id=id).update(Status='Delivered')
    return HttpResponse('''<script> alert("Succesfully Delivered!!!");window.location="/E_PHARMA/admin_view_orders/"</script>''')

# def viewsuborder_post(request):
#     if request.session['lid']=="":
#         return HttpResponse('''<script> alert("you are Logout!!!");window.location="/E_PHARMA/login/"</script>''')
#     # res = Payment.objects.filter(id=id)
#     # res = res[0]
#     # r = res.ORDER
#     # rr = OrderSub.objects.filter(ORDER=r)
#     # print(rr, "hhbkj")
#     # ar = []
#     # for i in rr:
#     #     ar.append({
#     #         "PRODUCTS": i.PRODUCT.Product_Name,
#     #         "PRICE": i.PRODUCT.Price,
#     #         "QUANTITY": i.Quantity
#     #     })
#     f_date=request.POST['textfield']
#     t_date = request.POST['textfield2']
#     var = OrderSub.objects.filter(Date__range=[f_date, t_date])
#     return render(request,"admin/13ViewSubOrders.html",{'data':var})

def view_payment_status(request):
    if request.session['lid']=="":
        return HttpResponse('''<script> alert("you are Logout!!!");window.location="/E_PHARMA/login/"</script>''')
    res = Payment.objects.all()
    return render(request,"admin/14ViewPaymentStatus.html",{'data':res})

def view_pstatus_post(request):
    if request.session['lid'] == "":
        return HttpResponse('''<script> alert("you are Logout!!!");window.location="/E_PHARMA/login/"</script>''')

    f_date=request.POST['textfield']
    t_date = request.POST['textfield2']
    var = Payment.objects.filter(Date__range=[f_date, t_date])
    return render(request,"admin/14ViewPaymentStatus.html",{'data':var})


def view_more(request,id):
    if request.session['lid']=="":
        return HttpResponse('''<script> alert("you are Logout!!!");window.location="/E_PHARMA/login/"</script>''')
    res = Payment.objects.filter(id=id)
    res=res[0]
    r=res.ORDER
    rr=OrderSub.objects.filter(ORDER=r)
    print(rr,"hhbkj")
    ar=[]
    for i in rr:
        ar.append({
            "PRODUCTS":i.PRODUCT.Product_Name,
            "PRICE":i.PRODUCT.Price,
            "QUANTITY":i.Quantity
        })
    return render(request,"admin/15Viewmore.html",{'data':ar})



def view_complaint(request):
    if request.session['lid']=="":
        return HttpResponse('''<script> alert("you are Logout!!!");window.location="/E_PHARMA/login/"</script>''')
    res = Complaint.objects.all()
    return render(request,"admin/16ViewComplaint.html",{'data':res})

def viewcomplaint_post(request):
    if request.session['lid']=="":
        return HttpResponse('''<script> alert("you are Logout!!!");window.location="/E_PHARMA/login/"</script>''')
    f_date=request.POST['textfield']
    t_date = request.POST['textfield2']
    var = Complaint.objects.filter(Date__range=[f_date, t_date])
    return render(request,"admin/16ViewComplaint.html",{'data':var})


def send_reply(request,id):
    if request.session['lid']=="":
        return HttpResponse('''<script> alert("you are Logout!!!");window.location="/E_PHARMA/login/"</script>''')
    var=Complaint.objects.get(id=id)
    return render(request,"admin/17SendReply.html",{'data':var,'id':id})

def sendreply_post(request,id):
    if request.session['lid']=="":
        return HttpResponse('''<script> alert("you are Logout!!!");window.location="/E_PHARMA/login/"</script>''')
    reply=request.POST['textarea']
    Complaint.objects.filter(id=id).update(Reply=reply,Status="replyed")
    return HttpResponse('''<script> alert("REPLY SEND!!!");window.location="/E_PHARMA/admin_view_complaint/"</script>''')


def view_feedback(request):
    if request.session['lid']=="":
        return HttpResponse('''<script> alert("you are Logout!!!");window.location="/E_PHARMA/login/"</script>''')
    res = Feedback.objects.all()
    return render(request,"admin/admin_view_feedback.html",{'data':res})

def viewfeedback_post(request):
    if request.session['lid']=="":
        return HttpResponse('''<script> alert("you are Logout!!!");window.location="/E_PHARMA/login/"</script>''')
    f_date=request.POST['textfield']
    t_date = request.POST['textfield2']
    var = Feedback.objects.filter(Date__range=[f_date, t_date])
    return render(request,"admin/admin_view_feedback.html",{'data':var})







########################user

def customer_registeration(request):
    return render(request,"customer/signupindex.html")
def customerreg_post(request):
    name=request.POST['textfield']
    phone = request.POST['textfield2']
    email = request.POST['textfield3']
    house_name= request.POST['textfield4']
    place= request.POST['textfield5']
    post= request.POST['textfield6']
    district= request.POST['textfield7']
    pin= request.POST['textfield8']
    # print(pin,"pinnn")
    password= request.POST['textfield10']
    c_password= request.POST['textfield11']

    res=Login.objects.filter(Username=email)
    if res.exists():
        return HttpResponse(
            '''<script> alert("Email already exist!!!");window.location="/E_PHARMA/customer_registeration/"</script>''')
    else:

        if password==c_password:
            obj1=Login()
            obj1.Username=email
            obj1.Password=c_password
            obj1.Type="Pending"
            obj1.save()
            cust=Customer()
            cust.Name=name
            cust.Phone=phone
            cust.Email=email
            cust.House_Name=house_name
            cust.Place=place
            cust.Post=post
            cust.District=district
            cust.Pin=pin
            cust.Status='Pending'
            cust.LOGIN=obj1
            cust.save()
            return HttpResponse(
                '''<script> alert("SUCCESSFULLY REGISTERED!!!");window.location="/E_PHARMA/login/"</script>''')
        else:
            return HttpResponse(
                '''<script> alert("Password mismatch!!!");window.location="/E_PHARMA/customer_registeration/"</script>''')


def customer_home(request):
    if request.session['lid']=="":
        return HttpResponse('''<script> alert("you are Logout!!!");window.location="/E_PHARMA/login/"</script>''')
    return render(request,"customer/cindex.html")

def view_profile(request):
    if request.session['lid']=="":
        return HttpResponse('''<script> alert("you are Logout!!!");window.location="/E_PHARMA/login/"</script>''')
    res = Customer.objects.get(LOGIN=request.session['lid'])
    return render(request,"customer/viewprofile.html",{'data':res})

def viewprofile_post(request):
    if request.session['lid']=="":
        return HttpResponse('''<script> alert("you are Logout!!!");window.location="/E_PHARMA/login/"</script>''')
    return render(request,"customer/viewprofile.html")

def search_products(request):
    if request.session['lid']=="":
        return HttpResponse('''<script> alert("you are Logout!!!");window.location="/E_PHARMA/login/"</script>''')
    res = Stocks.objects.filter( Quantity__gt=0)
    return render(request,"customer/product_search.html",{'data':res})

def csearchproduct_post(request):
    if request.session['lid']=="":
        return HttpResponse('''<script> alert("you are Logout!!!");window.location="/E_PHARMA/login/"</script>''')
    search=request.POST['textfield']
    res = Stocks.objects.filter(Product_Name__icontains=search, Quantity__gt=0)
    return render(request,"customer/product_search.html",{'data':res})

# def add_quantity(request,id):
# return render(request,"customer/addquantity.html",{'id':id})



# def addquantity_post(request):
#     quantity=request.POST['textfield']
#     pid=request.POST['pid']
#     place = request.POST['textfield4']
#     landmark = request.POST['textfield5']
#     post = request.POST['textfield6']
#     district = request.POST['textfield7']
#     pin = request.POST['textfield8']
#     ordm = Order()
#     ordr=OrderSub()
#     ordr.Quantity=quantity
#     ordr.PRODUCT_id=pid
#     c=Customer.objects.get(LOGIN_id=request.session['lid'])
#     ordr.ORDER_id=Order.objects.get(CUSTOMER_id=c)
#     ordr.save()
#     return HttpResponse('''<script> alert("Ordered!!!");window.location="/E_PHARMA/customer_home/"</script>''')



def upload_prescription(request):
    if request.session['lid']=="":
        return HttpResponse('''<script> alert("you are Logout!!!");window.location="/E_PHARMA/login/"</script>''')
    return render(request,"customer/19UploadPrescription.html")

def upload_post(request):
    if request.session['lid']=="":
        return HttpResponse('''<script> alert("you are Logout!!!");window.location="/E_PHARMA/login/"</script>''')
    # prescription=request.POST['image']

    pre=Prescription()
    prescription = request.FILES['fileField']
    fs = FileSystemStorage()
    import datetime
    dt = 'prescription/' + datetime.datetime.now().strftime("%Y%m%d%H%M%S") + ".jpeg"
    fs.save(dt, prescription)
    path = fs.url(dt)
    pre.File = path
    pre.USER = Customer.objects.get(LOGIN_id=request.session['lid'])
    pre.Date=datetime.datetime.now().strftime('%Y-%m-%d')
    pre.save()
    return HttpResponse('''<script> alert("UPLOADED SUCCESSFULLY!!!");window.location="/E_PHARMA/customer_upload_prescription/"</script>''')


def view_availability_status(request):
    if request.session['lid']=="":
        return HttpResponse('''<script> alert("you are Logout!!!");window.location="/E_PHARMA/login/"</script>''')
    from datetime import datetime
    d=datetime.now()
    var = Available_Products.objects.filter(PRESCRIPTION__USER__LOGIN__id=request.session['lid'],PRESCRIPTION__Date__gte=d)
    return render(request,"customer/20ViewAvailability.html",{'data':var})


def availabilityview_post(request):
    if request.session['lid']=="":
        return HttpResponse('''<script> alert("you are Logout!!!");window.location="/E_PHARMA/login/"</script>''')
    request.session['cnf']=request.POST.getlist("med")
    confirm=request.POST.getlist("med")
    print(confirm)
    # cnf = []
    cnf = ''
    ttl=0

    for i in confirm:
        cnf= cnf+','+i

        ttl=ttl+(float(Available_Products.objects.get(id=i).Quantity)*float(Available_Products.objects.get(id=i).PRODUCT.Price))
        # cnf.append(i)

    return render(request, "customer/21ConfirmOrder.html",{'confirm':cnf, 'ttl':str(ttl)})

def confirm_order(request):
    if request.session['lid']=="":
        return HttpResponse('''<script> alert("you are Logout!!!");window.location="/E_PHARMA/login/"</script>''')
    return render(request,"customer/21ConfirmOrder.html")

def confirmorder_post(request):
    if request.session['lid']=="":
        return HttpResponse('''<script> alert("you are Logout!!!");window.location="/E_PHARMA/login/"</script>''')
    print(request.POST)
    place = request.POST['textfield4']
    landmark = request.POST['textfield5']
    post = request.POST['textfield6']
    district = request.POST['textfield7']
    pin = request.POST['textfield8']
    pmode=request.POST['select']
    conf = request.POST['confirm']
    ttl = request.POST['ttl']

    if float(ttl) >=float(100):

        if pmode=='cod':
            # confirm = request.session['cnf']
            # confirm = request.POST.getlist('confirm')
            confirm = str(request.POST['confirm']).split(',')
            # print(confirm)
            prc=[]
            for i in confirm:
                if i == '':
                    continue
                if Available_Products.objects.filter(id=i).exists():
                    if Available_Products.objects.get(id=i).PRESCRIPTION_id in prc:
                        continue
                    prc.append(Available_Products.objects.get(id=i).PRESCRIPTION_id)
            # print(prc)
            for i in prc :
                # print(i)
            # for i in prc :

                ord=Order()
                ord.Place=place
                ord.Landmark=landmark
                ord.Post=post
                ord.District=district
                ord.Pin=pin
                ord.Date=datetime.date.today()
                ord.CUSTOMER=Customer.objects.get(LOGIN_id=request.session['lid'])
                ord.PRESCRIPTION_id = i
                ord.Total_Amount=0

                ord.Status='Ordered'
                ord.save()
                tmt=0
                for j in confirm:
                    if j == '':
                        continue
                    if Available_Products.objects.filter(id=j).exists():
                        # print(j)
                        tmt=tmt+(float(Available_Products.objects.get(id=j).Quantity)*float(Available_Products.objects.get(id=j).PRODUCT.Price))
                        obj = OrderSub()
                        obj.Quantity = Available_Products.objects.get(id=j).Quantity
                        obj.PRODUCT_id = Available_Products.objects.get(id=j).PRODUCT_id
                        obj.ORDER=ord
                        obj.save()
                Order.objects.filter(id=ord.id).update(Total_Amount=tmt)
                return HttpResponse('''<script> alert("Order Confirmed!!!");window.location="/E_PHARMA/customer_home/"</script>''')
        else:
            return render(request, "customer/23Payment.html", {'confirm': conf, 'place': place,
                                                               'landmark': landmark, 'post': post,
                                                               'district': district, 'pin': pin,'ttl':ttl
                                                               })
    elif float(ttl)<100:
        if pmode == 'cod':
            # confirm = request.session['cnf']
            # confirm = request.POST.getlist('confirm')
            confirm = str(request.POST['confirm']).split(',')
            # print(confirm)
            prc = []
            for i in confirm:
                if i == '':
                    continue
                if Available_Products.objects.filter(id=i).exists():
                    if Available_Products.objects.get(id=i).PRESCRIPTION_id in prc:
                        continue
                    prc.append(Available_Products.objects.get(id=i).PRESCRIPTION_id)
            # print(prc)
            for i in prc:
                # print(i)
                # for i in prc :

                ord = Order()
                ord.Place = place
                ord.Landmark = landmark
                ord.Post = post
                ord.District = district
                ord.Pin = pin
                ord.Date = datetime.date.today()
                ord.CUSTOMER = Customer.objects.get(LOGIN_id=request.session['lid'])
                ord.PRESCRIPTION_id = i
                ord.Total_Amount = 0

                ord.Status = 'Ordered'
                ord.save()
                tmt = 0
                for j in confirm:
                    if j == '':
                        continue
                    if Available_Products.objects.filter(id=j).exists():
                        # print(j)
                        tmt = tmt + (float(Available_Products.objects.get(id=j).Quantity) * float(
                            Available_Products.objects.get(id=j).PRODUCT.Price))
                        obj = OrderSub()
                        obj.Quantity = Available_Products.objects.get(id=j).Quantity
                        obj.PRODUCT_id = Available_Products.objects.get(id=j).PRODUCT_id
                        obj.ORDER = ord
                        obj.save()
                Order.objects.filter(id=ord.id).update(Total_Amount=tmt)
                return HttpResponse(
                    '''<script> alert("Order Confirmed!!!");window.location="/E_PHARMA/customer_home/"</script>''')
        else:
            return render(request, "customer/23Payment.html", {'confirm': conf, 'place': place,
                                                               'landmark': landmark, 'post': post,
                                                               'district': district, 'pin': pin, 'ttl': float(ttl)+50
                                                               })

def confirmorder_pay_post(request):
    if request.session['lid']=="":
        return HttpResponse('''<script> alert("you are Logout!!!");window.location="/E_PHARMA/login/"</script>''')


    place = request.POST['place']
    landmark = request.POST['landmark']
    post = request.POST['post']
    district = request.POST['district']
    pin = request.POST['pin']
    # conf = request.POST['confirm']
    # confirm = request.session['cnf']
    # confirm = request.POST.getlist('confirm')
    accno=request.POST['textfield']
    cardno=request.POST['textfield3']
    accholder=request.POST['textfield2']
    cvv=request.POST['textfield4']
    if Bank.objects.filter(Account_Number=accno,Card_Number=cardno,Account_Holder=accholder,CVV=cvv).exists():
        confirm = str(request.POST['confirm']).split(',')
        print(confirm)
        prc = []
        for i in confirm:
            if i == '':
                continue
            if Available_Products.objects.filter(id=i).exists():
                if Available_Products.objects.get(id=i).PRESCRIPTION_id in prc:
                    continue
                prc.append(Available_Products.objects.get(id=i).PRESCRIPTION_id)
        # print(prc)
        for i in prc:
            # print(i)
            # for i in prc :

            ord = Order()
            ord.Place = place
            ord.Landmark = landmark
            ord.Post = post
            ord.District = district
            ord.Pin = pin
            ord.Date = datetime.date.today()
            ord.CUSTOMER = Customer.objects.get(LOGIN_id=request.session['lid'])
            ord.PRESCRIPTION_id = i
            ord.Total_Amount = 0
            ord.Status = 'Ordered'
            ord.save()
            tmt = 0
            for j in confirm:
                if j == '':
                    continue
                if Available_Products.objects.filter(id=j).exists():
                        tmt = tmt + (float(Available_Products.objects.get(id=j).Quantity) * float(
                        Available_Products.objects.get(id=j).PRODUCT.Price))
                        obj = OrderSub()
                        obj.Quantity = Available_Products.objects.get(id=j).Quantity
                        obj.PRODUCT_id = Available_Products.objects.get(id=j).PRODUCT_id
                        obj.ORDER = ord
                        s=Stocks.objects.get(id=Available_Products.objects.get(id=j).PRODUCT_id)
                        tlq = int(s.Quantity)-int(Available_Products.objects.get(id=j).Quantity)
                        s.Quantity = str(tlq)
                        s.save()
                        obj.save()

            if tmt >= float(100):
                Order.objects.filter(id=ord.id).update(Total_Amount=tmt)
                pobj = Payment()
                pobj.ORDER=ord
                pobj.Total_Amount=tmt
                pobj.Date=datetime.date.today()
                pobj.CUSTOMER=Customer.objects.get(LOGIN_id=request.session['lid'])
                pobj.Status='Paid'
                pobj.save()

            elif tmt < float(100):
                Order.objects.filter(id=ord.id).update(Total_Amount=tmt)
                pobj = Payment()
                pobj.ORDER = ord
                pobj.Total_Amount = tmt+float(50)
                pobj.Date = datetime.date.today()
                pobj.CUSTOMER = Customer.objects.get(LOGIN_id=request.session['lid'])
                pobj.Status = 'Paid'
                pobj.save()

        return HttpResponse(
            '''<script> alert("Payment Successfull!!!! Order Confirmed!!!");window.location="/E_PHARMA/customer_home/"</script>''')
    else:
        return HttpResponse(
            '''<script> alert("Invalid Bank details!!!");window.location="/E_PHARMA/customer_home/"</script>''')




def view_order_status(request):
    if request.session['lid']=="":
        return HttpResponse('''<script> alert("you are Logout!!!");window.location="/E_PHARMA/login/"</script>''')
    var = Order.objects.filter(CUSTOMER__LOGIN__id=request.session['lid'])
    return render(request,"customer/22ViewOrderStatus.html",{'data':var})

def vieworderstatus_post(request):
    if request.session['lid']=="":
        return HttpResponse('''<script> alert("you are Logout!!!");window.location="/E_PHARMA/login/"</script>''')
    f_date=request.POST['textfield']
    t_date = request.POST['textfield2']
    var =Order.objects.filter(Date__range=[f_date, t_date])
    return render(request,"customer/22ViewOrderStatus.html",{'data':var})

def view_order_statussub(request,id):
    if request.session['lid']=="":
        return HttpResponse('''<script> alert("you are Logout!!!");window.location="/E_PHARMA/login/"</script>''')
    res=OrderSub.objects.filter(ORDER_id=id)

    return render(request,"customer/vieworderstatusSub.html",{'data':res})

def vieworderstatussub_post(request):

    if request.session['lid']=="":
        return HttpResponse('''<script> alert("you are Logout!!!");window.location="/E_PHARMA/login/"</script>''')
    # f_date=request.POST['textfield']
    # t_date = request.POST['textfield2']

    return render(request,"customer/vieworderstatusSub.html",{'data':var})

def payment(request):
    if request.session['lid'] == "":
        return HttpResponse('''<script> alert("you are Logout!!!");window.location="/E_PHARMA/login/"</script>''')
    return render(request,"customer/23Payment.html")

def payment_post(request):

     acc_no=request.POST['textfield']
     acc_holder = request.POST['textfield2']
     c_number = request.POST['textfield3']
     cvv = request.POST['textfield4']
     amount = request.POST['textfield5']
     return render(request,"customer/23Payment.html")

def view_payment_history(request):
    if request.session['lid'] == "":
        return HttpResponse('''<script> alert("you are Logout!!!");window.location="/E_PHARMA/login/"</script>''')
    var=Payment.objects.filter(CUSTOMER__LOGIN__id=request.session['lid'])
    return render(request,"customer/24PaymentHistory.html",{'data':var})
def viewpaymenthistory_post(request):
    if request.session['lid'] == "":
        return HttpResponse('''<script> alert("you are Logout!!!");window.location="/E_PHARMA/login/"</script>''')
    f_date=request.POST['textfield']
    t_date = request.POST['textfield2']
    var = Payment.objects.filter(Date__range=[f_date, t_date])
    return render(request,"customer/24PaymentHistory.html",{'data':var})

def phistoryview_more(request,id):
    if request.session['lid']=="":
        return HttpResponse('''<script> alert("you are Logout!!!");window.location="/E_PHARMA/login/"</script>''')
    res = Payment.objects.filter(id=id)
    res=res[0]
    r=res.ORDER
    rr=OrderSub.objects.filter(ORDER=r)
    print(rr,"yes")
    ar=[]
    for i in rr:
        ar.append({
            "PRODUCTS":i.PRODUCT.Product_Name,
            "PRICE":i.PRODUCT.Price,
            "QUANTITY":i.Quantity
        })
    return render(request,"customer/paymentviewmore.html",{'data':ar, 'ttl':res.Total_Amount})

def send_complaint(request):
    if request.session['lid']=="":
        return HttpResponse('''<script> alert("you are Logout!!!");window.location="/E_PHARMA/login/"</script>''')
    return render(request,"customer/25SendComplaint.html")

def sendcomplaint_post(request):
    if request.session['lid']=="":
        return HttpResponse('''<script> alert("you are Logout!!!");window.location="/E_PHARMA/login/"</script>''')
    complaint=request.POST['textarea']
    com=Complaint()
    com.Complaint = complaint
    com.Reply='Pending'

    com.CUSTOMER=Customer.objects.get(LOGIN__id=request.session['lid'])
    from datetime import datetime
    com.Date=datetime.now().strftime('%Y-%m-%d')
    com.Status='Pending'
    com.save()
    return HttpResponse('''<script> alert("COMPLAINT SEND!!!");window.location="/E_PHARMA/customer_send_complaint/"</script>''')


def view_reply(request):
    if request.session['lid']=="":
        return HttpResponse('''<script> alert("you are Logout!!!");window.location="/E_PHARMA/login/"</script>''')
    res = Complaint.objects.filter(CUSTOMER__LOGIN__id=request.session['lid'])
    return render(request,"customer/27Viewreply.html",{'data':res})
def viewreply_post(request):
    if request.session['lid']=="":
        return HttpResponse('''<script> alert("you are Logout!!!");window.location="/E_PHARMA/login/"</script>''')
    f_date=request.POST['textfield']
    t_date = request.POST['textfield2']
    var = Complaint.objects.filter(Date__range=[f_date,t_date])
    return render(request,"customer/27Viewreply.html",{'data':var})

def send_feedback(request):
    if request.session['lid']=="":
        return HttpResponse('''<script> alert("you are Logout!!!");window.location="/E_PHARMA/login/"</script>''')
    return render(request,"customer/26SendFeedback.html")
def sendfeedback_post(request):
    feedback=request.POST['textarea']

    fe=Feedback()
    fe.Feedback=feedback
    fe.CUSTOMER = Customer.objects.get(LOGIN__id=request.session['lid'])
    from datetime import datetime
    fe.Date = datetime.now().strftime('%Y-%m-%d')
    fe.save()
    return HttpResponse('''<script> alert("FEEDBACK SEND SUCCESSFULLY!!!");window.location="/E_PHARMA/customer_send_feedback/"</script>''')

def edit_profile(request,id):
    if request.session['lid']=="":
        return HttpResponse('''<script> alert("you are Logout!!!");window.location="/E_PHARMA/login/"</script>''')
    res = Customer.objects.get(id=id)
    return render(request,"customer/28EditProfile.html",{'data':res,'id':id})
def editprofile_post(request):
    id = request.POST['id']
    name=request.POST['textfield']
    phone = request.POST['textfield2']
    email = request.POST['textfield3']
    house_name= request.POST['textfield4']
    place= request.POST['textfield5']
    post= request.POST['textfield6']
    district= request.POST['textfield7']
    pin= request.POST['textfield8']
    Customer.objects.filter(id=id).update(Name=name,Phone=phone,Email=email,House_Name=house_name,Place=place,Post=post,District=district,Pin=pin)


    return HttpResponse('''<script> alert("SUCCESSFULLY UPDATED!!!");window.location="/E_PHARMA/view_profile/"</script>''')








def load_on_type(request):
    cid=request.POST["cid"]

    print(cid)
    tt=""

    if cid == "Tablet":
        tt="no"
    elif cid == "Syrup":
        tt="ml"
    elif cid =="Antiseptic":
        tt="ml"
    elif cid == "Ointment":
        tt="gm"
    elif cid == "Balm":
        tt="gm"
    elif cid == "Inhaler":
        tt= "gm"
    elif cid == "Diaper":
        tt="no"
    elif cid == "SanitaryNapkin":
        tt="no"
    elif cid =="haircare":
        tt="ml"
    elif cid == "Skincare":
        tt="ml"

    print(tt,"hloo")



    # print(cid)
    # dd=division.objects.filter(CLASS_id=cid)
    # l=[]
    # for i in dd:
    #     l.append({"id":i.id,"div":i.class_division})
    # print(l)
    # ss=subject.objects.filter(CLASS_id=cid)
    # b=[]
    # for i in ss:
    #     b.append({"sid":i.id,"sub":i.subject_name})

    # return JsonResponse({"data":l,"data1":b})
    return JsonResponse({"data":tt})
