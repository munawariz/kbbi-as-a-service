from django.contrib import admin
from django.urls import path
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from graphene_django.views import GraphQLView
from KBBI.schema import schema

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', csrf_exempt(GraphQLView.as_view(graphiql=True, schema=schema))),
]
