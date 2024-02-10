# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class project_task(models.Model):
    _inherit = 'project.task'
    _rec_name = 'name'

    sequence_name = fields.Char("Sequence", readonly=True, copy=False)
    delay = fields.Char("Retard", readonly=True, compute='_compute_is_deadline_exceeded', store=True)
    start_date = fields.Datetime(_("Date debut"))

    @api.onchange('date_deadline', 'start_date')
    def _check_date_start(self):
        if self.start_date:
            if self.start_date > self.date_deadline:
                raise ValidationError(_("Date start superior to date deadline"))

    @api.depends('date_deadline')
    def _compute_is_deadline_exceeded(self):
        for task in self:
            deadline = task.date_deadline.date()
            today = fields.Date.context_today(self)
            if deadline < today:
                delay = str((today - deadline).days)
                if delay == '1':
                    self.delay = _('one days')
                else:
                    self.delay = delay + _(' days')
            else:
                self.delay = "0"

    @api.model
    def create(self, vals):
        if vals.get('sequence_name', _('New')) == _('New'):
            vals['sequence_name'] = self.env['ir.sequence'].next_by_code('project.tasks') or _('New')
        res = super(project_task, self).create(vals)
        return res

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
