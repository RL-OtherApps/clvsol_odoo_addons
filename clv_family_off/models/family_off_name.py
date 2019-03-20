# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import api, fields, models


class FamilyOff(models.Model):
    _inherit = 'clv.family_off'

    suggested_name = fields.Char(
        string="Suggested Name", required=False, store=True,
        compute="_get_suggested_name",
        help='Suggested Name for the Family (Off).'
    )
    automatic_set_name = fields.Boolean(
        string='Automatic Name',
        help="If checked, the Family (Off) Name will be set automatically.",
        default=True
    )

    @api.depends('street', 'street2')
    def _get_suggested_name(self):
        for record in self:
            if record.street:
                record.suggested_name = record.street
                if record.street2:
                    record.suggested_name = record.suggested_name + ' - ' + record.street2
            elif record.name:
                record.suggested_name = record.name
            else:
                record.suggested_name = 'x'
            # else:
            #     if not record.suggested_name:
            #         if record.code:
            #             record.suggested_name = record.code

    @api.multi
    def write(self, values):
        ret = super().write(values)
        for record in self:
            if record.suggested_name is not False:
                if record.automatic_set_name:
                    if record.name != record.suggested_name:
                        values['name'] = record.suggested_name
                        super().write(values)
                else:
                    if ('name' in values and values['name'] == '/') or \
                       (record.name == '/'):
                        values['name'] = record.suggested_name
                        super().write(values)
        return ret
