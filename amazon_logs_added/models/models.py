# -*- coding: utf-8 -*-

from odoo import models, fields, api
import logging

_logger = logging.getLogger(__name__)

class amazon_logs_added(models.Model):
    _inherit = 'amazon.account'


    def action_update_available_marketplaces(self):
        _logger.warning("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        for account in self:
            available_marketplaces = account._get_available_marketplaces()
            new_marketplaces = available_marketplaces - account.available_marketplace_ids
        _logger.warning("fetched marketplaces")
        for a_m in available_marketplaces:
            _logger.warning(a_m.name)
        _logger.warning("new marketplaces")
        for n_m in new_marketplaces:
            _logger.warning(n_m.name)
        _logger.warning("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")

        res = super(amazon_logs_added, self).action_update_available_marketplaces()
        return res

    def _process_order_data(self, order_data):
        _logger.warning("Process order data begin")
        _logger.warning(order_data)
        _logger.warning("Process order data end")
        res = super(amazon_logs_added, self)._process_order_data()
        return res



