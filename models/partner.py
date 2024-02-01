from odoo import tools,fields, models, api, _




class ResPartner(models.Model):
    _inherit = "res.partner"
    old_id = fields.Integer("old id")





    
