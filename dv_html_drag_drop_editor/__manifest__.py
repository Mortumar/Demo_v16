{
    'name': "custom editor for html templates",

    'summary': """
        html editor with preview
    """,

    'description': """
        DESCRIPTION. |
    """,

    'author': 'Develogers',
    'website': 'https://develogers.com',
    'support': 'https://develogers.com/helpdesk',
    'live_test_url': 'https://wa.link/2cc9dn',
    'license': 'LGPL-3',

    'sequence':  1,

    'category': 'Invoice',
    'version': '1.0',

    'depends': [
        'base',
        'contacts',
        'mass_mailing'
    ],

    'data': [
        'security/ir.model.access.csv',
        'views/html_editor_views.xml',
        'views/menu_item_views.xml',
        # 'views/mailing_mailing_views_menus.xml',
        # 'views/mailing_trace_views.xml',
        # 'views/link_tracker_views.xml',
        # 'views/mailing_contact_views.xml',
        # 'views/mailing_list_views.xml',
        # 'views/mailing_mailing_views.xml',
        # 'views/res_config_settings_views.xml',
        # 'views/utm_campaign_views.xml',
        # 'views/assets.xml',
        # 'views/mass_mailing_templates_portal.xml',
        # 'views/themes_templates.xml',
        # 'views/snippets_themes.xml',
        # 'views/snippets/s_alert.xml',
        # 'views/snippets/s_blockquote.xml',
        # 'views/snippets/s_call_to_action.xml',
        # 'views/snippets/s_coupon_code.xml',
        # 'views/snippets/s_cover.xml',
        # 'views/snippets/s_color_blocks_2.xml',
        # 'views/snippets/s_company_team.xml',
        # 'views/snippets/s_comparisons.xml',
        # 'views/snippets/s_features.xml',
        # 'views/snippets/s_features_grid.xml',
        # 'views/snippets/s_hr.xml',
        # 'views/snippets/s_image_text.xml',
        # 'views/snippets/s_masonry_block.xml',
        # 'views/snippets/s_media_list.xml',
        # 'views/snippets/s_numbers.xml',
        # 'views/snippets/s_picture.xml',
        # 'views/snippets/s_product_list.xml',
        # 'views/snippets/s_rating.xml',
        # 'views/snippets/s_references.xml',
        # 'views/snippets/s_showcase.xml',
        # 'views/snippets/s_text_block.xml',
        # 'views/snippets/s_text_highlight.xml',
        # 'views/snippets/s_text_image.xml',
        # 'views/snippets/s_three_columns.xml',
        # 'views/snippets/s_title.xml',
    ],

    'images': ['static/description/banner.png'],

    'application': True,
    'installable': True,
    'auto_install': False,
}
