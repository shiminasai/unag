# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *

# Register your models here.
class AfiliadoAdmin(admin.ModelAdmin):
    search_fields = ['nombre','municipio','comunidad']
    list_filter = ['sexo',]
    list_display = ['nombre','cedula','municipio','comunidad']

admin.site.register(Afiliado,AfiliadoAdmin)

class DatosGeneralesInline(admin.TabularInline):
    model = DatosGenerales
    max_num = 1
    can_delete = False

class EscolaridadInline(admin.TabularInline):
    model = Escolaridad
    can_delete = False
    max_num = 1

class ProfesionInline(admin.TabularInline):
    model = Profesion
    max_num = 1
    can_delete = False

class PersonasDependenInline(admin.TabularInline):
    model = PersonasDependen
    max_num = 5
    extra = 1

class DatosFamiliaresInline(admin.TabularInline):
    model = DatosFamiliares
    extra = 1

class FamiliaEmigraInline(admin.TabularInline):
    model = FamiliaEmigra
    max_num = 1
    can_delete = False

class AreasFincaInline(admin.TabularInline):
    model = AreasFinca
    extra = 1

class OtrasTierrasInline(admin.TabularInline):
    model = OtrasTierras
    extra = 1

class OrigenPropiedadInline(admin.TabularInline):
    model = OrigenPropiedad
    max_num = 1
    can_delete = False

class FormaTenenciaInline(admin.TabularInline):
    model = FormaTenencia
    max_num = 1
    can_delete = False

class DocumentoPropiedadInline(admin.TabularInline):
    model = DocumentoPropiedad
    max_num = 1
    can_delete = False

class SistemaAguaInline(admin.TabularInline):
    model = SistemaAgua
    max_num = 1
    can_delete = False

class EnergiaElectricaInline(admin.TabularInline):
    model = EnergiaElectrica
    max_num = 1
    can_delete = False

class InventarioAnimalesInline(admin.TabularInline):
    model = InventarioAnimales
    extra = 1

class ProduccionHuevosLecheInline(admin.TabularInline):
    model = ProduccionHuevosLeche
    extra = 1
    max_num = 8

class AgriculturaInline(admin.TabularInline):
    model = Agricultura
    extra = 1

class VendeProduccionInline(admin.TabularInline):
    model = VendeProduccion
    max_num = 1
    can_delete = False

class ManoObraInline(admin.TabularInline):
    model = ManoObra
    max_num = 1
    can_delete = False

class TablaEmpleoInline(admin.TabularInline):
    model = TablaEmpleo
    extra = 1

class InfraestructuraInline(admin.TabularInline):
    model = Infraestructura
    extra = 1

class CotizacionInline(admin.TabularInline):
    model = Cotizacion
    max_num = 1
    can_delete = False

class RespuestaSiCotizaInline(admin.TabularInline):
    model = RespuestaSiCotiza
    max_num = 1
    can_delete = False

class RespuestaSiCotizaInline(admin.TabularInline):
    model = RespuestaSiCotiza
    max_num = 1
    can_delete = False

class MiembroCooperativaInline(admin.TabularInline):
    model = MiembroCooperativa
    max_num = 1
    can_delete = False

class BeneficiadoProyectoInline(admin.TabularInline):
    model = BeneficiadoProyecto
    max_num = 1
    can_delete = False

class CreditoInline(admin.TabularInline):
    model = Credito
    max_num = 1
    can_delete = False

class CotizacionOrganizacionInline(admin.TabularInline):
    model = CotizacionOrganizacion
    max_num = 1
    can_delete = False

class EncuestaAdmin(admin.ModelAdmin):
    inlines = [DatosGeneralesInline,EscolaridadInline,ProfesionInline,PersonasDependenInline,
                DatosFamiliaresInline,FamiliaEmigraInline,AreasFincaInline,
                OtrasTierrasInline,OrigenPropiedadInline,FormaTenenciaInline,
                DocumentoPropiedadInline,SistemaAguaInline,EnergiaElectricaInline,InventarioAnimalesInline,
                ProduccionHuevosLecheInline,AgriculturaInline,VendeProduccionInline,ManoObraInline,
                TablaEmpleoInline,InfraestructuraInline,CotizacionInline,RespuestaSiCotizaInline,
                MiembroCooperativaInline,BeneficiadoProyectoInline,CreditoInline,CotizacionOrganizacionInline]

    class Media:
        css = {
            'all': ('css/admin.css',)
        }
        js = ('js/admin.js',)

admin.site.register(Encuesta,EncuestaAdmin)
