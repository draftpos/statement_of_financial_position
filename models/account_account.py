from odoo import models, fields

class AccountAccount(models.Model):
    _inherit = 'account.account'

    financial_position_category = fields.Selection([
        ('fp_prop_equip', 'Property and equipment'),
        ('fp_fin_investments', 'Financial investments'),
        ('fp_def_acq_costs', 'Deferred acquisition costs asset'),
        ('fp_other_non_current', 'Other non-current assets'),
        ('fp_contrib_receivables', 'Contribution receivables'),
        ('fp_reinsurance_contract_assets', 'Reinsurance contract assets'),
        ('fp_cash', 'Cash and cash equivalents'),
        ('fp_prepayments', 'Prepayments'),
        ('fp_other_receivables', 'Other Receivables'),
        ('fp_other_current_assets', 'Other (Specify)'),
        ('fp_accum_fund_bf', 'Accumulated Fund brought forward'),
        ('fp_surplus_period', 'Surplus/(Deficit) for the period'),
        ('fp_invest_res_bf', 'Investment Reserve brought forward'),
        ('fp_transfer_invest_res', 'Transfer to/(from) Investment Reserve'),
        ('fp_reval_res_bf', 'Revaluation Reserve brought forward'),
        ('fp_reval_prop_equip', 'Revaluation of property and equipment'),
        ('fp_non_dist_res_bf', 'Non-Distributable Reserve brought forward'),
        ('fp_transfer_non_dist_res', 'Transfer to/(from) Non-Distributable Reserve'),
        ('fp_liab_remain_cov', 'Liability for remaining coverage (LRC)'),
        ('fp_liab_incur_claims_be', 'Liability for incurred claims (LIC) - best estimate'),
        ('fp_liab_incur_claims_risk', 'Liability for incurred claims (LIC) - risk adjustment'),
        ('fp_reins_contract_liab', 'Reinsurance Contract Liabilities'),
        ('fp_rel_party_payables', 'Related party payables'),
        ('fp_lease_liab', 'Lease liability (IFRS 16)'),
        ('fp_long_term_borrow', 'Long-term loans / borrowings'),
        ('fp_trade_payables', 'Trade and other payables'),
    ], string='Financial Position Category')