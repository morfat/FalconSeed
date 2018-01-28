import time

from utils.pagination import get_paginated_response

from src.settings import PAGINATION

class BaseService:
    table_class=None
    ordering=''
    group_by=''


    def __init__(self,db,url,query_params):
        self.db=db
        self.url=url
        self.query_params=query_params
        self.table=self.table_class()


    def all(self,pagination=None):
        fields=','.join(self.table.get_display_fields())
        sql="SELECT %s FROM %s  "%(fields,self.table.name)
        if len(self.ordering)>0:
            sql=sql+" ORDER BY %s "%(self.ordering)

        if len(self.group_by)>0:
            sql=sql+" ORDER BY %s "%(self.group_by)
            
        if pagination:
            sql,pagination=self.paginate(sql)

        self.db.execute(sql)

        return (self.db.fetchall(),pagination,)


    def count(self,sql=None):
        if not sql:
            self.db.execute("SELECT count(*) as total_count FROM %s "%(self.table.name))
        else:
            sql_count='SELECT count(*) as total_count '+sql[sql.find('FROM'):]
            self.db.execute(sql_count)

        result=self.db.fetchone()
        return result.get('total_count')


    def paginate(self,sql):
        page=int(self.query_params.get('page',1))

        page_size=int(self.query_params.get('page_size',PAGINATION.get('page_size')))

        offset=(page-1)*page_size
        limit=page_size

        count=self.count(sql=sql)
        
        #real query
        sql=sql+' LIMIT %s , %s '%(offset,limit)
        pagination=get_paginated_response(self.url,page_size,page,offset,limit,count)
        return (sql,pagination,)

    def get_uuid(self):
        return uuid.uuid4().hex

    def get_unix_timestamp(self):
        return  str(time.time()).split('.')[0]



