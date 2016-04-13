# -*- coding: utf-8 -*-

from openerp import models, fields, api


class Idea(models.Model):
    _name = 'idea.idea'

    nombre = fields.Char(required=True)
    descripcion = fields.Text()
    grupo = fields.Integer()
    fecha_inicio = fields.Date(required=True)
    fecha_fin = fields.Date(required=True)
    voto_ids = fields.One2many('idea.voto', 'idea_id', 'Votos')
    calificacion = fields.Float()
    create_uid = fields.Many2one('res.users', 'Created By', readonly=True)


class Voto(models.Model):
    _name = 'idea.voto'

    calificacion = fields.Float(required=True, digits=(0, 10))
    opiniones = fields.Text()
    idea_id = fields.Many2one('idea.idea', 'Idea')
    fecha_voto = fields.Date(default=fields.Date.today)


class Grupo(models.Model):
    _name = 'idea.grupo'

    nombre = fields.Char(required=True)
