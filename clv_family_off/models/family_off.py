# -*- coding: utf-8 -*-
# Copyright 2008 Luis Falcon <lfalcon@gnusolidario.org>
# Copyright 2016 LasLabs Inc.
# License GPL-3.0 or later (http://www.gnu.org/licenses/gpl.html).

import logging

from odoo import api, fields, models
from odoo.modules import get_module_resource

_logger = logging.getLogger(__name__)


class FamilyOff(models.Model):

    _name = 'clv.family_off'
    _description = 'Family (Off)'
    _inherit = 'clv.abstract.partner_entity'

    code = fields.Char(string='Family (Off) Code', required=False)

    notes = fields.Text(string='Notes:')

    @api.model
    def _create_vals(self, vals):
        vals = super()._create_vals(vals)
        vals.update({
            'customer': True,
        })
        vals.update({
            'type': self._name,
        })
        return vals

    @api.model_cr_context
    def _get_default_image_path(self, vals):
        res = super()._get_default_image_path(vals)
        if res:
            return res
        image_path = get_module_resource(
            'clv_family_off', 'static/src/img', 'family_off-avatar.png',
        )
        return image_path

    @api.multi
    def do_family_off_clear_address_data(self):

        for family_off in self:

            # _logger.info(u'>>>>> %s', family_off.ref_address_id)

            # if (family_off.reg_state in ['draft', 'revised']):

            data_values = {}

            data_values['street'] = False
            data_values['street2'] = False
            data_values['zip'] = False
            data_values['city'] = False
            data_values['state_id'] = False
            data_values['country_id'] = False
            # data_values['phone'] = False
            # data_values['mobile'] = False

            _logger.info(u'>>>>>>>>>> %s', data_values)

            family_off.write(data_values)
