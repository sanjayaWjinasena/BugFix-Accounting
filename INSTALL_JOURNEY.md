# BugFix-Accounting — Install Journey (v0.0.22 → v0.0.32)

Comprehensive record of the install-unblock arc for BugFix-Accounting
on the standalone `repair-test-101` fresh-install target. Written
2026-08-29 after v0.0.32 (`61ddb91`) reached a clean install.

Every deferred item and every stripped tab has a **restore path**
documented below — this file is the checklist for future work to
close the ~10% gap left after the arc.

---

## Install now clean — `v0.0.32` = commit `61ddb91`

- Fresh install completes end-to-end on `repair-test-101`.
- All 40 model files load, all 140+ view records validate.
- ~90% of the Clear-DB form-UI surface is Python-owned.
- Remaining gaps are all documented below with restore paths.

---

## What did NOT ship (deferred, tracked)

### 1. Server action stubs (5 raise `UserError('port pending')`)

| Clear-DB id | xmlid | Description | Code size on Clear-DB |
|---|---|---|---|
| 2176 | `srv_rug_account_update_in_si` | RR - RUG Account Update in SI | 862 B |
| 2762 | `srv_update_advance_payment_account_vendor_bill` | Project - Update Advance Payment Account - Vendor Bill | ~1 KB |
| 1370 | `srv_imp_update_consignment_pi` | IMP - Update Consignment - PI | **31 KB** (biggest) |
| 2366 | `srv_imp_vendor_bill_currency_rate` | IMP - Vendor Bill Currency Rate | ~2 KB |
| 1854 | `srv_sls_view_credit_limit_validation` | SLS - View Credit Limit Validation | 607 B |
| 1851 | `srv_sls_send_bank_guarantee_notification` | SLS - Send BG Notification | ~1 KB |
| 1852 | `srv_sls_view_bank_guarantee_validation` | SLS - View BG Validation | ~1 KB |

**Why deferred:** Each is 600 B – 31 KB of Studio Python with its own
depends chain. Full ports risk breaking install if any dependency is
missing. Stubs raise `UserError` so the gap is visible in UI.

**Restore:** Port each Python code block from Clear-DB one at a time.
Smallest first (1854, 862 B → 2176 → 2762 → 2366 → 1851 → 1852 →
1370 last, 31 KB).

### 2. Multi-state approval actions (2 stubs)

| id | xmlid | Notes |
|---|---|---|
| 1493 | `srv_sls_request_credit_note_approval` | `state='multi'` with `child_ids=[1491, 1489]` on Clear-DB |
| 1495 | `srv_sls_credit_note_approval_main` | `state='multi'` with `child_ids=[2537, 2539]` on Clear-DB |

**Why deferred:** Multi-state actions need their child actions ported
first, then the parent flipped to `state='multi'` + `child_ids` wired.

**Restore:** Port 4 child actions (1489, 1491, 2537, 2539), then
update these 2 records.

### 3. QWeb reports (14 total)

Six live in `reports/reports.xml` TODOs:
- Payment Receipt
- Journal Entry (×2)
- Pro-forma Invoice
- account.payment (×2)

Eight more scattered on `x_sales_report_model` + `crossovered.budget`.

**Why deferred:** Each needs full QWeb template + report action ported.
High business value, high effort. Not blocking install.

**Restore:** Port each report as a proper `ir.actions.report` +
`report.report_name` QWeb template. Prioritize by business use.

### 4. Six form tabs stripped from `x_sales_report_model`

| Tab | Field referenced | Cycle owner |
|---|---|---|
| MO - WIP | `x_studio_related_field_oeTJK` → mrp.production | BugFix-MRP |
| Slow Moving Items | `x_studio_related_field_XCKXu` → stock.move.line | BugFix-Stock |
| Sales - Prod. - Purch. | `x_studio_related_field_NsCKm` → stock.move.line | BugFix-Stock |
| Prod. Summary Split | `x_studio_related_field_bCtVj` → stock.move.line | BugFix-Stock |
| Production Variance | `x_studio_related_field_PaCjA` → stock.move | BugFix-Stock |
| Pump Price Costing | `x_studio_pump_price_costing_ids` → x_pump_price_costing | model doesn't exist on-disk |

Each stripped tab replaced with empty `<page invisible="1"/>` stub so
notebook tab-bar stays intact and restoration is search-and-replace.

**Why deferred:** BugFix-Stock and BugFix-MRP declare
`Many2one('x_sales_report_type')` — that model is defined in
BugFix-Accounting. Adding either as a dep forces it to load FIRST,
and its M2O fails because `x_sales_report_type` isn't registered
yet. **Circular dependency.**

**Restore:** Upstream `x_sales_report_type` + `x_sales_report_model`
to `studio_usermodel_migration` (or a new shared root). All BugFix-*
depend on that upstream. Cycle disappears. Restore the 5 stock/mrp
tabs by reverting the strip in `views/x_sales_report_model_studio_ported_v2.xml`.

For Pump Price Costing tab specifically: port `x_pump_price_costing`
model + fields first, then restore the tab.

### 5. Five tree columns stripped from `x_sales_report_type` tree

`x_studio_production_order_id`, `x_studio_slow_moving_item_id`,
`x_studio_sales_prod_purch_id`, `x_studio_prod_summary_split_id`,
`x_studio_production_variance_id`.

Same cycle as tabs above. Same restore path.

### 6. Six TODO O2M fields on `x_sales_report_model` model

- `x_studio_pump_price_costing_ids`
- `x_studio_related_field_NsCKm`
- `x_studio_related_field_PaCjA`
- `x_studio_related_field_XCKXu`
- `x_studio_related_field_bCtVj`
- `x_studio_related_field_oeTJK`

### 7. Five TODO O2M fields on `x_sales_report_type` model

- `x_studio_production_order_id`
- `x_studio_slow_moving_item_id`
- `x_studio_sales_prod_purch_id`
- `x_studio_prod_summary_split_id`
- `x_studio_production_variance_id`

### 8. HR menu on `bank-data` (sibling repo)

`menu_employee_bank_accounts` under Payroll/Configuration preserved
as `bank-data/_disabled/hr_menu_employee_bank_accounts.xml` (not
loaded by manifest).

**Why deferred:** Clear-DB has ZERO `ir.ui.menu` pins on bank-data —
this menu was added to the repo AFTER Clear-DB was installed, so it
never got processed there. Also had broken parent xmlid
`hr_payroll.menu_payroll_configuration` (correct one lives in
`hr_work_entry_contract_enterprise`).

**Restore:** File already has re-enable instructions in its own
comment header. Add file to bank-data's `__manifest__.py` `data`
list + add `hr_work_entry_contract_enterprise` to `depends`.

---

## Install-error iteration log (11 versions)

### v0.0.22 — Cross-record ordering + broken inherit_id refs

**Error:** `External ID not found: BugFix-Accounting.ported_view_8293_...`

**Root cause:** Two classes of issue found via install-failure trace
+ audit script:

1. `ported_view_8297` referenced `ported_view_8293` (its primary
   parent) but the parent was defined LATER in the same file. Odoo's
   XML loader processes records top-down; `inherit_id` ref must
   resolve at record-parse time.

2. 18 `inherit_id` refs pointed to `BugFix-Accounting.ported_view_NNNN_...`
   xmlids the porter guessed but never emitted. The real primary
   records were in earlier `_studio_ported.xml` files under different
   xmlids (pattern `ported_...` without the `_NNNN_` segment).

**Fix:** Moved `ported_view_8293` above its child. Wrote UUID→xmlid
mapping script that built a lookup from earlier `_studio_ported.xml`
files and rewrote each broken ref to the real record. 19 fixes across
13 files.

**Cost:** 1 commit, ~30 min

---

### v0.0.23 — Routing miss on bank-data fields

**Error:** `Field "x_dest_bank_micr" does not exist in model "account.move.line"`

**Root cause:** 19 bare `x_` fields on account.move.line + 17 on
hr.payslip pinned to `bank-data` module per Clear-DB `ir.model.data`.
Natural instinct said "account.move.line → BugFix-Accounting → add
fields to `models/account_move_line.py`". That would have been WRONG.
Model prefix is a **hint**; `ir.model.data.module` is **ground truth**.

**Fix:** Added `bank-data` to `depends`. Also discovered bank-data
itself had a ~78% content gap vs Clear-DB (someone else pushed 13
commits with the ports; we pulled and used those). Added Jinasena
app rename + icon to bank-data. Deferred the broken HR menu.

**Rule captured:** [`feedback-pin-source-verification`](../../../../../Users/sanjaya/.claude/projects/D--Odoo-Playwright-Tests-PlayWrite-Testings/memory/feedback_pin_source_verification.md)

**Cost:** 2 commits (BugFix-Accounting + bank-data), ~45 min

---

### v0.0.24 — Hardcoded numeric action ids in view arch (comprehensive sweep)

**Error:** `Action 2739 (id: 2739) does not exist for button of type action`

**Root cause:** View arch pulled byte-verbatim from Clear-DB contained
`type="action" name="NNNN"` numeric refs. Auto-assigned action ids
don't survive fresh install. Grep sweep across all `_v2.xml` files
found 7 total (previous v0.0.20 fix caught 11 in account_move, missed
these 7 elsewhere).

**Fix:** Ported 4 actions verbatim as records with stable xmlids:
- `srv_advance_payment_acc_update` (2739, ~60 lines)
- `srv_tp_invoice_apply_charges` (1378, 2.6 KB — full consignment/TP
  invoice workflow)
- `act_custom_currency_rates` (1310, window action)
- `act_tp_invoice_vendor_bill` (1386, window action)
- `srv_sales_report_sample_button` (1676, no-op template)

Plus reused standard `account.action_view_account_move_reversal` for
Reverse buttons (id 281, referenced twice).

Rewrote all 7 view refs to `%(BugFix-Accounting.xmlid)d` interpolation.

**Rule captured:** [`feedback-hardcoded-action-ids`](../../../../../Users/sanjaya/.claude/projects/D--Odoo-Playwright-Tests-PlayWrite-Testings/memory/feedback_hardcoded_action_ids.md)

**Cost:** 1 commit, ~40 min

---

### v0.0.25 — Missing mail.thread inherit on 20 x_ models

**Error:** `Field "message_follower_ids" does not exist in model "x_consignment_charge_h"`

**Root cause:** Ported Studio views contain `<div class="oe_chatter">`
blocks that reference `message_follower_ids`, `message_ids`,
`activity_ids`. Those fields come from `mail.thread` +
`mail.activity.mixin`. Our on-disk model ports missed the inherit
lines. Clear-DB has the mixin on all 20 models — RPC-verified for
every one; visually confirmed via Playwright on `x_tp_invoice_line`
form (Send message / Log note / Activities / Follow buttons render).

**Fix:** Batch-added `_inherit = ['mail.thread', 'mail.activity.mixin']`
to 19 existing model files. Created new `models/x_journal_types.py`
(missing entirely). Added `model_x_journal_types` pin to
`security/ir_model_pins.xml`. Fixed 2 latent bugs where
`x_rm_gross_margin_esti.py` + `x_rm_gross_margin_esti_line_7e86d.py`
existed on-disk but were never imported by `models/__init__.py`.

**Change scope:** purely additive — new fields, new chatter UI panel.
Zero existing functionality touched.

**Cost:** 1 commit, ~35 min (biggest edit — 22 files)

---

### v0.0.26 — Auto-porter dropped header buttons on x_lc_header

**Error:** `xpath //button[@name='1404'] cannot be located in parent view`

**Root cause:** Clear-DB's primary form for x_lc_header had 2 header
buttons (Post LC = action 1404, Amend LC = action 1405). Auto-porter
stripped them when it fetched the arch, leaving `<header></header>`
empty. Studio extension view expected them via xpath anchor.

**Fix:** Ported both actions verbatim from Clear-DB
(`srv_lc_post_lc` = 180 chars, `srv_lc_amend_lc` = 2.9 KB — real LC
clone/version-increment workflow). Restored buttons in primary view
header with xmlid interpolation (`%(BugFix-Accounting.srv_lc_post_lc)d`).

Changed extension's xpath anchor from `//button[@name='1404']` to
`//button[@string='Post LC']` (thinking string-based selectors are
DB-stable).

**Cost:** 1 commit, ~25 min

---

### v0.0.27 — Odoo denylist blocks `@string` xpath selector

**Error:** `View inheritance may not use attribute 'string' as a selector`

**Root cause:** My clever fix in v0.0.26 used `@string=` in xpath.
Odoo's arch validator denies `string` because translated UI text
would silently break in different locales.

**Fix:** Switched to positional xpath `//header[1]/button[1]` — no
attribute selector, no denylist concern, no DB-instance dependency.
Post LC is the first button in the (now-restored) header, so
positional works.

**Cost:** 1 commit, ~10 min

---

### v0.0.28 — Missing sentinel field for button modifier

**Error:** `Field 'x_studio_status' used in modifier 'invisible' must be present in view but is missing`

**Root cause:** Restored Post/Amend LC buttons had `invisible="x_studio_status not in ['Draft']"` modifiers. The
`x_studio_status` field is declared visibly in the extension view,
but Odoo validates the primary view arch STANDALONE before applying
extensions on fresh install. Primary needed the field accessible.

**Fix:** Added `<field name="x_studio_status" invisible="1"/>`
sentinel to primary view arch. Zero UI impact (`invisible=1`), zero
functional change (extension still declares visibly).

Same pattern used successfully on Fix-repair (v292-v295) where dozens
of sentinels were injected via `_get_view` runtime patch.

**Cost:** 1 commit, ~10 min

---

### v0.0.29 — Two more stripped-button xpath anchors

**Error:** (Broader grep sweep after v0.0.28 install failure surfaced
2 more `//button[@name='NNNN']` xpath anchors.)

**Root cause:** Same class as v0.0.26 — `x_sales_report_model_studio_ported_v2.xml`
had `//button[@name='1676']` and `x_tp_invoice_header_studio_ported_v2.xml`
had `//button[@name='1384']`. Both anchored to buttons the porter
dropped from the primary view.

**Fix:**
- `x_sales_report_model`: primary already had the Clear Data button
  (v0.0.24 already ported action 1676). Just switched xpath to
  positional.
- `x_tp_invoice_header`: full treatment.
  - Ported action 1384 (IMP - Post TP Invoice, **8 KB** — cost-allocation
    by weight/volume/amount + stock valuation-layer updates +
    account.move creation for the TP reversal) verbatim.
  - Restored Post button in primary header.
  - Added `x_studio_status` sentinel.
  - Switched xpath to positional.

**Post-fix invariant:** grep confirmed **zero live numeric xpath
anchors** remain across the module.

**Cost:** 1 commit, ~30 min

---

### v0.0.30 — First TODO field cascade

**Error:** `Field "x_studio_journal_item_ids" does not exist in model "x_sales_report_model"`

**Root cause:** Field was TODO-commented by auto-porter (couldn't
determine O2M inverse). It's a related O2M navigating through
`x_studio_report_type.x_studio_journal_items_id` which was ALSO
TODO'd on x_sales_report_type.

**Fix:** Un-TODO'd both fields (cascade):
- `x_sales_report_type.x_studio_journal_items_id = fields.One2many('account.move.line', 'x_studio_sales_report_type', ...)`
  (inverse M2O already exists on account.move.line)
- `x_sales_report_model.x_studio_journal_item_ids = fields.One2many('account.move.line', related='x_studio_report_type.x_studio_journal_items_id', ...)`

Kept tight — didn't batch other TODO fields yet.

**Cost:** 1 commit, ~15 min

---

### v0.0.31 — Whack-a-mole → batch un-TODO + cross-repo cycle discovery

**Error:** `Field "x_studio_related_field_DqBBB" does not exist in model "x_sales_report_model"` (next TODO field surfaced)

**Root cause:** 25 TODO fields on x_sales_report_model + 6 on
x_sales_report_type referenced by v2 views. Deep dive revealed a
**cross-repo dependency cycle**:

- Related O2Ms navigate through x_sales_report_type
- x_sales_report_type would need to declare O2Ms with inverses on
  `stock.move.line.x_studio_report_type_sales_prod_purch` etc.
- Those inverse M2Os live in BugFix-Stock / BugFix-MRP
- Adding BugFix-Stock as dep of BugFix-Accounting forces it to load
  FIRST
- But BugFix-Stock's M2Os declare `Many2one('x_sales_report_type')` —
  and `x_sales_report_type` is defined in BugFix-Accounting
- **Cycle**

**Fix (user chose pragmatic path):** Un-TODO 19 safe fields, strip 6
cycle-blocked fields from view. Preserve ~90% of form functionality.

- 16 direct O2Ms on x_sales_report_model (local x_rm_* target inverses,
  safe) un-TODO'd
- 3 related O2Ms on x_sales_report_model with same-repo or already-
  depended-on inverse un-TODO'd
  (`x_studio_related_field_DqBBB` sale.order.line via BugFix-Sales dep,
  `x_studio_related_field_n589a` same account.move.line path as
  journal_item_ids, `x_studio_related_field_nfrkz` account.move via
  BugFix-Accounting's own inherit)
- 2 cascade fields on x_sales_report_type un-TODO'd
  (`x_studio_sales_lines_id`, `x_studio_journal_entry_id`)
- 6 view pages stripped and replaced with empty `<page invisible="1"/>`
  stubs

**Cost:** 1 commit, ~60 min (biggest cognitive lift)

---

### v0.0.32 — Same cascade on x_sales_report_type view

**Error:** `Field "x_studio_test" does not exist in model "x_sales_report_type"`

**Root cause:** x_sales_report_type's own v2 view had 6 TODO fields
referenced. Same cycle pattern as v0.0.31.

**Fix:**
- Un-TODO'd `x_studio_test` (safe — account.move.line inverse via
  `x_studio_many2one_field_kiSUJ` already on our port)
- Stripped 5 cycle-blocked field references from tree extension:
  `x_studio_production_order_id`, `x_studio_slow_moving_item_id`,
  `x_studio_sales_prod_purch_id`, `x_studio_prod_summary_split_id`,
  `x_studio_production_variance_id`

**Cost:** 1 commit, ~10 min

---

## Durable rules captured to project memory this arc

- **`feedback-pin-source-verification`** — Before landing any Studio-
  ported field/view/action in ANY repo, RPC-query Clear-DB's
  `ir.model.data` to find the pinning module. Cost of the lesson:
  nearly dumped 19 bank-data fields into BugFix-Accounting.

- **`feedback-hardcoded-action-ids`** — Byte-verbatim Clear-DB view
  arch contains `type="action" name="NNNN"` numeric refs. Always
  rewrite to `%(module.xmlid)d` xmlid interpolation BEFORE landing.

Companion insights (in commit messages rather than memory):

- xpath anchors targeting numeric action-id buttons also need xmlid
  or positional treatment — not just button `name` attrs
- Primary view arch gets stripped of Studio buttons by the porter —
  restore them from Clear-DB with xmlid interpolation
- Primary views are validated standalone before extensions merge —
  add sentinel fields for any modifier field that only the extension
  provides
- Odoo denylist blocks `@string` as an xpath selector — use
  positional xpath or `@name` with xmlid interpolation
- Auto-porter dedup emits xmlids for records it then skips — cross-
  check with an audit script before pushing

---

## Session stats

- **11 install-error iterations** (v0.0.22 → v0.0.32)
- **~8 fundamentally different error classes** (routing miss,
  hardcoded ids, missing mixins, stripped buttons, xpath denylist,
  extension-field modifiers, xpath numeric anchors, cross-repo cycles)
- **11 commits** to BugFix-Accounting + **3 commits** to bank-data
- **6 full Python action ports** (~50 KB of Studio code moved from
  Clear-DB to disk)
- **~110 XML lines stripped** with restore-path comments preserving
  future work

---

## Follow-up priority order

1. **Upstream `x_sales_report_type` + `x_sales_report_model`** to
   `studio_usermodel_migration`. Unlocks: 5 stock/mrp form tabs +
   5 tree columns + 11 TODO O2M fields (across 2 models). Biggest
   single restore win.

2. **Port the 9 server action stubs** — replaces `raise UserError`
   stubs with real Clear-DB Python code. Order by size: 1854 (607 B)
   → 2176 → 2762 → 2366 → 1851 → 1852 → 1370 (31 KB last).

3. **Port the 2 multi-state approvals** (1493, 1495) + their 4 child
   actions (1489, 1491, 2537, 2539).

4. **Port the 14 QWeb reports.** High business value — user-facing
   documents. Full QWeb template + report action each.

5. **Port the `x_pump_price_costing` model.** Unlocks the Pump Price
   Costing tab on x_sales_report_model.

6. **Re-enable bank-data's HR menu.** File already exists at
   `bank-data/_disabled/hr_menu_employee_bank_accounts.xml` with
   re-enable instructions.
