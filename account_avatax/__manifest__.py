{
    "name": "Taxes using Avalara Avatax API",
    "version": "13.0.1.0.4",
    "author": "Open Source Integrators, Fabrice Henrion, Odoo SA,"
    " Odoo Community Association (OCA)",
    "summary": "Automatic Tax application using the Avalara Avatax Service",
    "license": "AGPL-3",
    "category": "Accounting",
    "depends": ["account", "sale_stock", "base_geolocalize"],
    "data": [
        "security/avalara_salestax_security.xml",
        "security/ir.model.access.csv",
        "data/avalara_salestax_data.xml",
        "data/avalara_salestax_exemptions.xml",
        "wizard/avalara_salestax_ping_view.xml",
        "wizard/avalara_salestax_address_validate_view.xml",
        "views/avalara_salestax_view.xml",
        "views/partner_view.xml",
        "views/product_view.xml",
        "views/account_move_action.xml",
        "views/account_move_view.xml",
        "views/account_tax_view.xml",
        "views/account_fiscal_position_view.xml",
    ],
    "image": ["static/description/avatax_icon.png"],
    "installable": True,
    "application": True,
    "external_dependencies": {"python": ["Avalara"]},
    "development_status": "Beta",
    "maintainers": ["dreispt"],
}
