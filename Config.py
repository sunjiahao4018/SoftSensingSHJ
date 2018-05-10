# -*- coding: utf-8 -*-
import ConfigParser

def getConfigOptions():
    try:
        cf = ConfigParser.ConfigParser()
        cf.read('Caloric.conf')

        ## return all section
        #secs = cf.sections()

        opts = cf.options('Caloric')

        # kvs = cf.items('Caloric')
        CaloricConfig = {}
        for ot in opts:
            CaloricConfig[ot] = cf.get('Caloric',ot)
        #caloric_dsn = cf.get('Caloric', 'caloric_dsn')
    except:
        cf_default = ConfigParser.ConfigParser()
        cf_default.add_section('Caloric')
        cf_default.set('Caloric','caloric_dsn','SongHUaJiangDataSource')
        cf_default.set('Caloric','caloric_user','sa')
        cf_default.set('Caloric','caloric_password','Hoken123456')
        cf_default.set('Caloric','caloric_realtimeTable','realtimeTable')
        cf_default.set('Caloric','caloric_historydatatable','caloric')
        cf_default.set('Caloric','caloric_realtime','False')
        cf_default.set('Caloric','caloric_history','True')
        cf_default.set('Caloric','caloric_starttime','2016-10-01')
        cf_default.set('Caloric','caloric_endtime','2016-11-01')
        file = open('Caloric.conf','w')
        cf_default.write(file)
        file.close()

        opts = cf_default.options('Caloric')
        CaloricConfig = {}
        for ot in opts:
            CaloricConfig[ot] = cf.get('Caloric',ot)

    return CaloricConfig