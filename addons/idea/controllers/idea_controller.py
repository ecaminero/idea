# -*- coding: utf-8 -*-
from openerp import http


class IdeaController(http.Controller):

    @http.route('/idea/idea/', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/idea/crear/', auth='public')
    def crear(self, **kw):
        return "Hello, world"

    @http.route('/idea/listar/', auth='user')
    def listar(self, **kw):
        Idea = http.request.env['idea.idea']
        return http.request.render('idea.listar', {
            'ideas': Idea.search([])
        })

    @http.route('/idea/detalle/<int:idObject>/', auth='public')
    def votar(self, idObject):
        Idea = http.request.env['idea.idea']
        print(idObject)
        return http.request.render('idea.votar', {
            'idea': Idea.search([('id', '=', idObject)])[0]
        })

    @http.route('/idea/votar/<int:idObject>/', auth='user', csrf=False)
    def list(self, idObject, **kw):
        Idea = http.request.env['idea.idea']

        idea = Idea.search([('id', '=', idObject)])[0]

        print (kw)
        import pdb; pdb.set_trace()
        return http.request.render('idea.listar', {
            'root': '/idea/listar/',
            'ideas': Idea.search([]),
        })

    # @http.route('/idea/idea/objects/<model("idea.idea"):obj>/', auth='public')
    # def object(self, obj, **kw):
    #     return http.request.render('idea.object', {
    #         'object': obj
    #     })