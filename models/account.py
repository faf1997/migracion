from odoo import tools,fields, models, api, _




class AccountJournal(models.Model):
    _inherit = "account.journal"
    old_id = fields.Integer("old id")





    
