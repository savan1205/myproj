from odoo import fields, models,api

class HospitalDegrees(models.Model):
    _name = "hospital.degrees"
    _description = "hospital degrees"

    degrees = fields.Char(string="degrees")
    from_city=fields.Char(string="From city")

    def action_test(self):
        print("__----------------button clicked")

    