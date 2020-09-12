#!/usr/bin/python
#coding=utf8

#import Init 
import sys
import web 
import json
import uniout
import urllib2

sys.path.append('../')
from config import conf 
from libs import helps
from models import mysql
import init 

web.config.debug = conf.web_debug

class Linecheck():
    def POST(self):
        indata = web.input(linename='')
        rs = mysql.conn.select('gt_line', where={'name':indata.linename})
        if(len(rs)):
            return init.jsonerr('此线路已经存在!') 
        else:
            return init.jsonok('可添加')

class Line:
    def GET(self):
        adminer = init.checkadmin(False)
        rs = mysql.conn.select('gt_line', order = 'id desc')
        return init.render.line(rs, adminer)

class Linedit:
    def GET(self):
        init.checkadmin()
        data = {}
        data['status'] = conf.status
        #modify
        indata = web.input(id='0')
        if(indata.id.isdigit() and indata.id != '0'):
            oridata = mysql.conn.select('gt_line', where="id="+indata.id)
            if(len(oridata) <1 ):
                return init.render.error('id参数有误') 
            oridata = oridata[0]
        else:
            id='0'
            oridata= web.Storage()
        return init.render.linedit(data, oridata)

    def POST(self):
        init.checkadmin()
        data = web.input()

        longkm = int(data.longkm)
        speed = int(data.speed) 
        onspeed = int(data.onspeed) 
        keychar = data.namechar.lower().replace(' ', '')

        id = data.get('id', '0')
        #return id
        if(id == '0'):
            mysql.conn.insert('gt_line', keychar=keychar, name=data.name, fullname=data.fullname, namechar=data.namechar, statusc=data.statusc, speed=speed, building=data.building, longkm=longkm, onspeed=onspeed, color=data.color)
        else:
            rs = mysql.conn.select('gt_line', where="id="+id)
            if(not len(rs)):
                return init.render.error('参数有误!') 
            rs = rs[0]

            admin = init.checkadmin()
            if(rs.locking and not admin):
                raise web.seeother('/line')

            if(rs.locking):
                raise web.seeother('/line')
            if(not init.checkadmin() and rs.locking==1):
                return init.render.error('您不能修改已有内容!')
            mysql.conn.update('gt_line', where='id = $id', vars = locals(), keychar=keychar, name=data.name, fullname=data.fullname, namechar=data.namechar, statusc=data.statusc, speed=speed, building=data.building, longkm=longkm, onspeed=onspeed,color=data.color)
        raise web.seeother('/line');
        pass
