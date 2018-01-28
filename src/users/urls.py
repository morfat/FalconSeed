from .views import * 


patterns=(('/users',ListCreateView()),
          ('/users/{user_id}',DetailView()),
         )
