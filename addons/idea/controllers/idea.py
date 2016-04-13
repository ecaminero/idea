# -*- coding: utf-8 -*-
from openerp import http


class Idea(http.Controller):
    
    @http.route('/idea/idea/', auth='public')
    def index(self, **kw):
        return "Hello, world"

#     @http.route('/idea/idea/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('idea.listing', {
#             'root': '/idea/idea',
#             'objects': http.request.env['idea.idea'].search([]),
#         })

#     @http.route('/idea/idea/objects/<model("idea.idea"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('idea.object', {
#             'object': obj
#         })