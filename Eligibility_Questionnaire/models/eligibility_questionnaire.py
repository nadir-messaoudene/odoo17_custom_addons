from odoo import models, fields, api

class EligibilityQuestionnaire(models.Model):
    _name = 'eligibility.questionnaire'
    _description = 'Eligibility Questionnaire'

    age = fields.Integer(string='Age', required=True)
    residence = fields.Char(string='Residence', required=True)
    income = fields.Float(string='Annual Income', required=True)

    @api.model
    def check_eligibility(self, age, residence, income):
        if age >= 18 and income >= 20000:
            return True
        return False