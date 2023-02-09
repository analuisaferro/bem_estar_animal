

from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('cadastro/completar', views.cadastro_tutor, name='completar_cadastro'),
    path('animal/cadastrar', views.cadastrar_animal, name='cadastrar_animal'),
    path('animal/editar/<id>', views.editar_animal, name='editar_animal'),
    path('animal/deletar/<id>', views.deletar_animal, name='deletar_animal'),
    path('animal/cadastrar-errante', views.cadastrar_errante, name='cadastrar_errante'),
    path('tutor/', views.listar_tutor, name='listar_tutor'),
    path('tutor/<tutor_id>/animais/', views.listar_animal_tutor, name='listar_animais_tutor'),
    path('tutor/<tutor_id>/animais/<animal_id>', views.cad_infos_extras, name='cadastrar_info'),
    path('catalogo/', views.catalogo, name='catalogo'),
    path('catalogo/cadastrar', views.cad_catalogo_animal, name='cadastrar_catalogo'),
    path('catalogo/<id>/entrevista-previa', views.entrevistaAdocao, name='entrevista_adocao'),
    path('adm/gerar-token', views.gerarToken, name='gerar_token'),
    path('adm/descontar-token', views.descontarToken, name='descontar_token'),
    path('teste', views.teste, name='teste')
]
