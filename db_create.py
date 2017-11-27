# -*- coding: utf-8 -*-

from app.models import User, Party
from app import db

db.create_all()
db.session.commit()

admon = User('tomer', 'admon',545454)
tomer = User(u'תומר', u'אדמון',12345)

john = User(u'John', u'Vituli',123456)
michale = User(u'מיכאל', u'נמוי',543321)


avoda = Party(u'העבודה', 'https://www.am-1.org.il/wp-content/uploads/2015/03/%D7%94%D7%A2%D7%91%D7%95%D7%93%D7%94.-%D7%A6%D7%99%D7%9C%D7%95%D7%9D-%D7%99%D7%97%D7%A6.jpg')
likud = Party(u'הליכוד', 'https://upload.wikimedia.org/wikipedia/commons/thumb/5/50/Likud_Logo.svg/250px-Likud_Logo.svg.png')
lavan = Party(u'פתק לבן', 'https://www.weberthai.com/fileadmin/user_upload/01_training-elements/02.4_others/02.5_color_cards/05_color_mosaic/images/1.jpg')

db.session.add(avoda)
db.session.add(likud)
db.session.add(lavan)
db.session.add(admon)
db.session.add(tomer)
db.session.add(john)
db.session.add(michale)

db.session.commit()
users = User.query.all()
print (users)
