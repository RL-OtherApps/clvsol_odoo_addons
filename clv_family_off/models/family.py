# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

import logging

from odoo import api, fields, models

_logger = logging.getLogger(__name__)


class FamilyOff(models.Model):
    _inherit = 'clv.family_off'

    related_family_id = fields.Many2one(comodel_name='clv.family', string='Related Family', ondelete='restrict')
    related_family_name = fields.Char(string='Related Family Name', related='related_family_id.name')
    related_family_code = fields.Char(string='Related Family Code', related='related_family_id.code')
    related_family_category_ids = fields.Many2many(
        comodel_name='clv.family.category',
        string='Related Family Categories',
        related='related_family_id.category_ids'
    )
    related_family_ref_address_id = fields.Many2one(
        comodel_name='clv.address',
        string='Related Family Address',
        related='related_family_id.ref_address_id'
    )
    related_family_ref_address_code = fields.Char(
        string='Related Family Address Code',
        related='related_family_id.ref_address_id.code'
    )
    related_family_ref_address_category_ids = fields.Many2many(
        comodel_name='clv.address.category',
        string='Related Family Address Categories',
        related='related_family_id.ref_address_id.category_ids'
    )

    @api.multi
    def do_family_off_get_related_family_data(self):

        for family_off in self:

            _logger.info(u'>>>>> %s', family_off.related_family_id)

            if (family_off.reg_state in ['draft', 'revised']) and \
               (family_off.related_family_id.id is not False):

                data_values = {}
                data_values['name'] = family_off.related_family_id.name
                data_values['code'] = family_off.related_family_id.code
                data_values['gender'] = family_off.related_family_id.gender
                data_values['birthday'] = family_off.related_family_id.birthday
                data_values['responsible_id'] = family_off.related_family_id.responsible_id.id
                data_values['caregiver_id'] = family_off.related_family_id.caregiver_id.id

                if self.related_family_id.ref_address_id.id is not False:

                    data_values['ref_address_id'] = family_off.related_family_id.ref_address_id.id

                    data_values['street'] = family_off.related_family_id.ref_address_id.street
                    data_values['street2'] = family_off.related_family_id.ref_address_id.street2
                    data_values['zip'] = family_off.related_family_id.ref_address_id.zip
                    data_values['city'] = family_off.related_family_id.ref_address_id.city
                    data_values['state_id'] = family_off.related_family_id.ref_address_id.state_id.id
                    data_values['country_id'] = family_off.related_family_id.ref_address_id.country_id.id
                    # data_values['phone'] = family_off.related_family_id.ref_address_id.phone
                    # data_values['mobile'] = family_off.related_family_id.ref_address_id.mobile

                if family_off.related_family_id.family_id.id is not False:

                    data_values['family_id'] = family_off.related_family_id.family_id.id

                _logger.info(u'>>>>>>>>>> %s', data_values)

                family_off.write(data_values)

        return True