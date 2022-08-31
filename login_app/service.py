from .import repository
from .import connection


class login_service():
    def login_check_service(self,request):
        return repository.login_repo().login_check_repo(request)

    
    def url_query(self,request):
        con = connection.databaseConn.getConnectionPostgres(self)
        query="select id,url_link from public.login_app_admin_url where is_deleted=false and is_logout_link=false and is_logout_link=false"
        result= connection.databaseConn.getResultSet_named_params(self,con,query)
        return result

    def user_non_adim_query(self,user_mail):
        con = connection.databaseConn.getConnectionPostgres(self)
        query="select id,url_link from public.login_app_admin_url where is_deleted=false and is_logout_link=true"
        result= connection.databaseConn.getResultSet_named_params(self,con,query)
        return result