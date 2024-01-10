from odoo import api, fields, models

class HtmlEditor(models.Model):
    _name = "html.editor"
    _inherit = ['mail.thread']

    name = fields.Char(string="Name")
    body_arch = fields.Html(string='Body', translate=False, sanitize=False)
    body_html = fields.Html(string='Body converted', render_engine='qweb', sanitize=False)

    # def compute_body_html(self):
    #     for record in self:
    #         record.body_html = str(self.body_arch)
