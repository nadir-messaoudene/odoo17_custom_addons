from odoo import api, fields, models, _
import logging

_logger = logging.getLogger('odoo')


class Task(models.Model):
    _inherit = 'project.task'

    delay = fields.Char('Retard', readonly=True, compute='_compute_is_deadline_exceeded')
    note = fields.Html(string='Note')

    def action_send_email(self):
        self.env.ref('project.mail_template_data_project_task').send_mail(self.id)

    @api.depends('date_deadline')
    def _compute_is_deadline_exceeded(self):
        pass
        # for task in self:
        #     deadline = task.date_deadline.date().strftime('%Y-%m-%d')
        #     today = fields.Date.context_today(self).strftime('%Y-%m-%d')
        #     if deadline < today:
        #         delay = str((today - deadline).days)
        #         if delay == '1':
        #             self.delay = _('one days')
        #         else:
        #             self.delay = delay + _(' days')
        #     else:
        #         self.delay = "0"
