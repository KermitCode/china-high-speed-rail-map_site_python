#!/usr/bin/python
#coding=utf8

#import Init 
import sys
import web 
import json
import uniout

sys.path.append('../')
from config import conf 
from libs import helps
from models import mysql
import init 

web.config.debug = conf.web_debug

class Linestats:
    def GET(self, lid='0'):
        init.checkadmin()
        data = {}
        data['statarr']= mysql.getstatArr()
        line = mysql.conn.select("gt_line", where="id= " + lid)
        if(len(line) <1 ):
            return init.render.error('id参数有误') 
        line = line[0]
        rs = mysql.conn.query("select gl.id,province,city,cid,station,stat_id,line_id from gt_linestats gl left join gt_station gt on gl.stat_id = gt.id left join gt_citys gc on gt.cid = gc.id where gl.line_id = %s order by gl.sort asc,gl.id asc" % lid)
        return init.render.linestats(line, rs, data)


    def POST(self, lid='0'):
        adminer = init.checkadmin()
        line = mysql.conn.select("gt_line", where="id= " + lid)
        if(len(line) <1 ):
            return init.jsonerr('无效参数')
        
        linedata = line[0]
        if (not adminer and linedata.locking == 1):
            return init.jsonerr('此线路已经完善，不能再编辑.')

        indata = web.input()
        sid = indata.get('sid', '0')
        if(not sid.isdigit() or sid == '0' ):
            return init.jsonerr('无效参数sid')


        #do sort
        sort = indata.get('sort', '0')
        if(sort.isdigit() and sort !='0'):
            rs = mysql.conn.select("gt_linestats", order="sort asc,id asc",where="line_id="+lid)             
            index = 0 
            sort = int(sort)
            for row in rs:
                if(row.id == int(sid)):
                    continue
                index+=1
                if(index == sort):
                    mysql.conn.update("gt_linestats", where="id="+sid, sort = index)  
                    index+=1
                mysql.conn.update("gt_linestats", where="id="+str(row.id), sort = index)  
            return init.jsonok('顺序调整完成')

        station = mysql.conn.select("gt_station", where="id= " + sid)
        if(len(station) <1 ):
            return init.jsonerr('无效参数') 

        mysql.conn.query("insert ignore into gt_linestats(line_id, stat_id) values(%s, %s)" % (lid, sid))
        return init.jsonok('添加成功')
