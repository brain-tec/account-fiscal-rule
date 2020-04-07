import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo13-addons-oca-account-fiscal-rule",
    description="Meta package for oca-account-fiscal-rule Odoo addons",
    version=version,
    install_requires=[
        'odoo13-addon-account_fiscal_position_rule',
        'odoo13-addon-account_fiscal_position_rule_sale',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
    ]
)
