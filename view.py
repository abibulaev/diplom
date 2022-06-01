

from __future__ import annotations
from array import array
from distutils.log import error
from turtle import title
from unicodedata import name
from venv import create
from flask_login import login_required, login_user, current_user, logout_user
from werkzeug.utils import redirect , secure_filename
from app import app, create_avatars, create_project, login_manager
from model import *
from flask import render_template, request, send_file, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from operator import and_, itemgetter, attrgetter, methodcaller
import os
import json
@login_manager.user_loader
def load_user(user_id):
    return Users.query.get(user_id)

@app.route('/',methods=['GET', 'POST'])
def index():
    itemss=Users.query.order_by(Users.user_rating).all()
    data=[]
    items=Users.query.all()
    files=FileUrl.query.all()
    for i in files:
        for n in items:
            if i.user_id==n.id:
                data.append([i,n])
                
   
                   
                    
    
    monogdat=[]
    monograf= Users.query.all()
    monog=FileMonUrl.query.all()     
    for i in monog:
        for n in monograf:
            if i.user_id==n.id:
                monogdat.append([i,n])
               
            
    slovodat=[]
    slovar=Users.query.all()
    slov=SlovarUrl.query.all()
    for i in slov:
        for n in slovar:
            if i.user_id==n.id:
                slovodat.append([i,n])
    kol_dess=len(files)
    kol_mon=len(monog)           
    kol_slov=len(slov)

                
   

    
    return render_template("base.html",kol_dess=kol_dess,kol_mon=kol_mon,kol_slov=kol_slov, data=data, monogdat=monogdat,slovodat=slovodat,items=list(reversed(itemss)))
@app.route('/rabots', methods=['GET', 'POST'])
def rabots():
    name=request.args["name"]
    user_prep_id=Users.query.filter_by(name=name).first().id
    a=FileUrl.query.filter_by(user_id=user_prep_id).all()
    b=FileMonUrl.query.filter_by(user_id=user_prep_id).all()
    c=SlovarUrl.query.filter_by(user_id=user_prep_id).all()
    if request.method=='POST':
        c=request.form.get("pizrbpot")
        print(c)
        try:
            return send_file(c, as_attachment=True)
        except Exception as e:
            return str(e)
    return render_template("rabots.html",name=a,nameb=b,namec=c,user=name)
@app.route('/about',methods=['GET', 'POST'])
def about():
    name= request.args["name"]
    items=Users.query.filter_by(status="Преподаватель",kafedra=name).all()
    return render_template("about.html",items=items)
@app.route('/rating')
def rating():
    items=Users.query.order_by(Users.user_rating).all()
    
    print(type(items))
  
    return render_template("rating.html",items=list(reversed(items)))
@app.route('/fakultebl',methods=['GET', 'POST'])
def fakultebl():
    name=request.args["name"]
    id_work= FileUrl.query.filter_by(id=name).first()
    ocenka=int(id_work.down)+int(1)
    id_work.down=ocenka
    db.session.add(id_work)
    db.session.commit()
    
        
  
    return render_template("fakultebl.html",id_work=id_work)
@app.route('/prosmnon',methods=['GET', 'POST'])
def prosmnon():
    
    name=request.args["name"]
   
    id_work=FileMonUrl.query.filter_by(id=name).first()
    
    ocenka=int(id_work.down)+int(1) 
    id_work.down=ocenka
    
    db.session.add(id_work)
    db.session.commit()
  
   
  
    
        
    
    return render_template("prosmnon.html",id_work=id_work)
@app.route('/prosmslov',methods=['GET', 'POST'])
def prosmslov():
    
    name=request.args["name"]
   
    id_work=SlovarUrl.query.filter_by(id=name).first()
    ocenka=int(id_work.down)+int(1) 
    id_work.down=ocenka
    db.session.add(id_work)
    db.session.commit()
    
   
  
    
        
    
    return render_template("prosmslov.html",id_work=id_work)
@app.route('/kafedrs',methods=['GET', 'POST'])
def kafedrs():
    prep=[]
    name= request.args["name"]
    items=[]
    kaf1=["Экономика","Менеджмент","Прикладная информатика","Педагогическое образование","Образование и педагогические науки"]
    kaf2=["Педагогическое образование","Психология"]
    kaf3=["Журналистика. Программа широкого профиля","Педагогическое образование. Профиль «Музыкальное образование»","История. Программа широкого профиля","Вокальное искусство. Профиль «Академическое пение»"]
    kaf4=["Преподавание филологических дисциплин (английский язык и литература, русский язык и литература)","Преподавание филологических дисциплин (английский язык и литература, украинский язык и литература)","Зарубежная филология (английский язык и литература, немецкий язык и литература)","Зарубежная филология (английский язык и литература, турецкий язык и литература)"]
    kaf5=["Машиностроение","Конструкторско-технологическое обеспечение машиностроительных производств","Техносферная безопасность","Эксплуатация транспортно-технологических машин и комплексов","Профессиональное обучение"]
   
    if name == "'Факультет экономики, менеджмента и информационных технологий'":
        for i in kaf1:
            items.append(i)
    if name == "'Факультет психологии и педагогического образования'":        
        for i in kaf2:
            items.append(i)
    if name == "'Факультет истории, искусств и крымскотатарского языка и литературы'":        
        for i in kaf3:
            items.append(i)
    if name == "'Филологический факультет'":
        for i in kaf4:
            items.append(i)
    if name == "'Инженерно-технологический факультет'":
        for i in kaf5:
            items.append(i)
    if request.method=='POST':
          trig= request.form["skrittreger"]
          print(trig)
          prep=Users.query.filter_by(kafedra=trig).all()
    
    return render_template("kafedrs.html",items=items, prep=prep)
@app.route('/registr', methods=["POST", "GET"])
def registr():
    if request.method == 'POST':
        name= request.form["user_name"]
        data= request.form["data"]
        status= request.form["position"]
        work= request.form["work"]
        fakultet=request.form["fakultet"]
        kafedra=request.form["kafedra"]
        tel= request.form["tel"]
        email= request.form["email"]
        user_rating=0
        passw= generate_password_hash(request.form["psw"])
        user = Users.query.filter_by(email=request.form['email']).first()

        create_avatars(email)
               
                
        file=request.files['file']
        filename=secure_filename(file.filename)
           
        foto_url='static/'+'img/'+str(email)
            
        create_project(email)
        file.save(os.path.join('static/'+'img/'+str(email), filename))

        if user is None:
            user= Users(name=name,foto_url=foto_url,avatar=filename, data=data,status=status,work=work,telephone=tel,email=email,passw=passw,fakultet=fakultet, kafedra= kafedra,user_rating=user_rating )
            db.session.add(user)
            db.session.commit()
            return redirect("/reg")   
    return render_template("registr.html")
@app.route('/reg', methods=["POST", "GET"])
def reg():
    if request.method =='POST':
        email= request.form["email"]
        passw= request.form["psw"]
        if email and passw :
            user = Users.query.filter_by(email=email).first()
            if check_password_hash(user.passw, passw):
                login_user(user)
                return redirect("/")
    return render_template("authorization.html")
@app.route('/profile',methods=['GET', 'POST'])
@login_required
def profile():
    diss = FileUrl.query.filter_by(user_id=current_user.id).all()
    mon = FileMonUrl.query.filter_by(user_id=current_user.id).all()
    slov = SlovarUrl.query.filter_by(user_id=current_user.id).all()
    return render_template("profile.html", user=current_user, diss = diss, mon=mon, slov=slov)
@app.route('/adddoc',methods=['POST',"GET"])
@login_required
def adddoc():
    specilalist=Users.query.filter_by(id=current_user.id).first().fakultet
    if specilalist == "Факультет экономики, менеджмента и информационных технологий":
        spis="listspecial"
    if specilalist == "Факультет психологии и педагогического образования":        
        spis="listspecial2"
    if specilalist == "Факультет истории, искусств и крымскотатарского языка и литературы":        
        spis="listspecial3"
    if specilalist == "Филологический факультет":
        spis="listspecial4"
    if specilalist == "Инженерно-технологический факультет":
        spis="listspecial5"
    if request.method=="POST": 
        skritpole=request.form['skritpole']
        print(skritpole)
        if skritpole=="Диссертация":
            file=request.files['file']
            filename=secure_filename(file.filename)
            url='static/'+'project/'+str(current_user.email)
            type_dess=request.form["typedes"]
            if type_dess=="Докторская":
                type_work="Докторская"
            if type_dess=="Кандидатская":
                type_work="Кандидатская"
            special=request.form["special"]
            tema=request.form["tema"]
            nauch_ruk=request.form["nauchruk"]
            down=0
            annotations=request.form["anotation"]
            data=request.form["data"]
            city=request.form["gorod"]
            user_url=FileUrl(annotation=annotations,url=url,down=down,city=city,data=data,nauch_ruk=nauch_ruk,filname=filename,tema=tema,special=special,type_dess=type_dess,user_id=current_user.id)
            db.session.add(user_url)
            db.session.commit()
            file.save(os.path.join('static/'+'project/'+str(current_user.email), filename))
        if skritpole=="Монография":
            temam= request.form["tema"]
            type_work="Монография"
            soavtorm=request.form["nauchruk"]
            citym=request.form["gorod"]
            izdatm=request.form["izdat"]
            kolstran=request.form["kolstran"]
            stranm=request.form["stran"]
            down=0
            isbn=request.form["ISBN"]
            datam=request.form["data"]
            filem=request.files['file']
            annotations=request.form["anotation"]
            filenamem=secure_filename(filem.filename)
            mon_url='static/'+'project/'+str(current_user.email)
            mono_url=FileMonUrl(annotation=annotations,down=down,type_work=type_work,url=mon_url,monname=temam,soavtor=soavtorm,city=citym,izpat=izdatm,kol_stran=kolstran,stranic=stranm,isbn=isbn,data=datam,filenamem=filenamem,user_id=current_user.id)
            db.session.add(mono_url)
            db.session.commit()
            filem.save(os.path.join('static/'+'project/'+str(current_user.email), filenamem))
        if skritpole=="Словарь":
            temam= request.form["tema"]
            type_work="Словарь"
            soavtorm=request.form["nauchruk"]
            annotations=request.form["anotation"]
            citym=request.form["gorod"]
            izdatm=request.form["izdat"]
            down=0
            kolstran=request.form["kolstran"]
            isbn=request.form["ISBN"]
            datam=request.form["data"]
            filem=request.files['file']
            filenamem=secure_filename(filem.filename)
            mon_url='static/'+'project/'+str(current_user.email)
            mono_url=SlovarUrl(annotation=annotations,down=down,type_work=type_work,url=mon_url,monnames=temam,soavtors=soavtorm,citys=citym,izpats=izdatm,kol_strans=kolstran,isbns=isbn,datas=datam,filenames=filenamem,user_id=current_user.id)
            db.session.add(mono_url)
            db.session.commit()
            filem.save(os.path.join('static/'+'project/'+str(current_user.email), filenamem))
        user_ball=Users.query.filter_by(id=current_user.id).first()
        ball=Rating.query.filter_by(nauch_rab=type_work).first()
        ocenka=int(user_ball.user_rating)+int(ball.grade)
        user_ball.user_rating=ocenka
        db.session.add(user_ball)
        db.session.commit()
    return render_template("adddoc.html",name=current_user.name , spis=spis)
@app.route('/download')
def download():
    url=request.args["url"]
    filename=request.args["filename"]
    
    return send_file( url+"/"+filename,as_attachment=True)
@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect("/")