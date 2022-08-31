from.models import users
from django.db.models import Q
from .import connection

class login_repo():
    def login_check_repo(self,request):
        data=users.objects.filter(Q(email_id__iexact=request.data['email_id']) & Q(password__iexact=request.data['password'])
        & Q(is_deleted=False))
        if data.exists():
            user_mail=request.data['email_id']
            user_data=self.user_query(user_mail)
            return user_data
        else:
            return 0


    def user_query(self,user_mail):
        con = connection.databaseConn.getConnectionPostgres(self)
        query="select * from public.login_app_users where is_deleted=false and email_id= '"+str(user_mail)+"'"
        result= connection.databaseConn.getResultSet_named_params(self,con,query)
        return result

  

