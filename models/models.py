# -*- coding: utf-8 -*-
import debugpy
debugpy.listen(("0.0.0.0", 5678))
from odoo import models

class Partner(models.Model):
    _inherit = 'res.partner'
