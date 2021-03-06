# -*- coding: utf-8 -*-
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Address (Aux)',
    'summary': 'Address (Aux) Module used by CLVsol Solutions.',
    'version': '12.0.4.0',
    'author': 'Carlos Eduardo Vercelino - CLVsol',
    'category': 'CLVsol Solutions',
    'license': 'AGPL-3',
    'website': 'https://github.com/CLVsol',
    'depends': [
        'clv_base',
        'clv_global_log',
        'clv_partner_entity',
        'clv_address',
        'clv_global_tag',
    ],
    'data': [
        'security/address_aux_security.xml',
        'security/ir.model.access.csv',
        'views/address_aux_view.xml',
        'views/address_aux_log_view.xml',
        'views/aux_instance_view.xml',
        'views/address_aux_category_view.xml',
        'views/address_aux_marker_view.xml',
        'views/res_partner_view.xml',
        'views/global_tag_view.xml',
        'views/address_aux_name_view.xml',
        'views/address_view.xml',
        'wizard/address_aux_mass_edit_view.xml',
        'wizard/address_associate_to_address_aux_view.xml',
    ],
    'demo': [],
    'test': [],
    'init_xml': [],
    'test': [],
    'update_xml': [],
    'installable': True,
    'application': False,
    'active': False,
    'css': [],
}
