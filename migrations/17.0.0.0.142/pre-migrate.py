# -*- coding: utf-8 -*-
"""v0.0.142: drop the two STALE Studio extension views of x_misc_charge_codes
so the v141 file (trio fields removed) can load.

What happened on upgrade to v141 (target 2026-10-02):

    ParseError: while parsing BugFix-Accounting/views/x_misc_charge_codes_studio_ported_v2.xml:16
    Field "x_studio_charges_line_id" does not exist in model "x_misc_charge_codes"

The file holds 5 views. The three link fields were only ever referenced by
the two EXTENSION views (ported_view_2684 form / ported_view_2685 tree), which
inherit the primaries (ported_view_2682 / 2681). Odoo loads records in file
order: when it rewrites the primary (first record) it validates the COMBINED
arch, i.e. with the extension views as they still are IN THE DATABASE -- the
old arch, still carrying the trio -- against a registry where the fields no
longer exist (they moved to BugFix-Purchase v0.1.0.176). So the primary's
write fails before the file ever reaches the extension records that would
have fixed it.

Fix: unlink the two extension views here, before this module's data loads.
ir.model.data._lookup_xmlids LEFT JOINs the target table; a dangling xmlid
makes _load_records drop the old pointer and CREATE the record afresh from
the new file arch (models.py _load_records: `else: imd.browse(d_id).unlink();
to_create.append(data)`). Net effect: same xmlids, new ids, new arch, no
stale child at primary-validation time. Nothing depends on these two view
ids (no inheriting views; verified via RPC: the model has exactly 5 views).

ORM only (ir.ui.view.unlink), no cr.execute. Idempotent: no-op on fresh
installs (version is None) and when the views are already gone.
"""
import logging

from odoo import api, SUPERUSER_ID

_logger = logging.getLogger(__name__)

STALE_EXTENSION_VIEWS = (
    'BugFix-Accounting.ported_view_2684_odoo_studio_default_2389c30f_1a37_4097_87d2_180fcdcddcb0',
    'BugFix-Accounting.ported_view_2685_odoo_studio_default_f4328649_f0ce_4d1a_9a3b_45e7f1c2e802',
)


def migrate(cr, version):
    if not version:
        return
    env = api.Environment(cr, SUPERUSER_ID, {})
    View = env['ir.ui.view'].sudo().with_context(active_test=False)
    for xmlid in STALE_EXTENSION_VIEWS:
        view = env.ref(xmlid, raise_if_not_found=False)
        if not view:
            continue
        view = View.browse(view.id)
        _logger.info(
            "BugFix-Accounting v0.0.142: unlinking stale extension view %s "
            "(id=%s, model=%s) so the trio-less arch can load",
            xmlid, view.id, view.model,
        )
        view.unlink()
