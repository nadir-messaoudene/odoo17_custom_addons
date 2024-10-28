from odoo import http
from odoo.http import request

class WebsiteEligibility(http.Controller):

    @http.route('/eligibility', type='http', auth='public', website=True)
    def eligibility_form(self):
        return request.render('Eligibility_Questionnaire.eligibility_form_page')

    @http.route('/eligibility/check', type='http', auth='public', methods=['POST'], website=True)
    def check_eligibility(self, **kwargs):
        age = int(kwargs.get('age'))
        residence = kwargs.get('residence')
        income = float(kwargs.get('income'))
        eligibility_model = request.env['eligibility.questionnaire']
        is_eligible = eligibility_model.check_eligibility(age, residence, income)
        if is_eligible:
            return "Vous êtes éligible!"
        else:
            return "Vous n'êtes pas éligible."