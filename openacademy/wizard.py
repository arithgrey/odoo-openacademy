from odoo import models, fields


class Wizard(models.TransientModel):
    _name = 'openacademy.wizard'

    def _default_session(self):
        session_obj = self.env['openacademy.session']
        session_id = self._context.get('active_id')
        session_record = session_obj.browse(session_id)
        # import pdb; pdb.set_trace()
        return session_record

    session_id = fields.Many2one('openacademy.session',
                                 required=True, default=_default_session)
    attendee_ids = fields.Many2many('res.partner')
