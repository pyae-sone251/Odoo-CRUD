# -*- coding: utf-8 -*-
{
    'name': 'CRUD Practice (create / write / unlink / read)',
    'version': '17.0.1.0.0',
    'summary': 'create, write, unlink, read - ORM method 4 ခုကိုပဲ practice လုပ်ရန်',
    'description': """
        ဒီ module ထဲမှာ model 1 ခုတည်းပါတယ် - "Practice Note"

        Button 4 ခု ရှိပါတယ်:
        1. Create Note      -> create() method ကို ခေါ်သုံးတယ်
        2. Update Note      -> write() method ကို ခေါ်သုံးတယ်
        3. Read Note Info   -> read() method ကို ခေါ်သုံးပြီး popup ပြတယ်
        4. Delete Note      -> unlink() method ကို ခေါ်သုံးတယ်

        Concept တခြားဘာမှ (compute, constrains, onchange) မထည့်ထားပါ -
        ဒီ ၄ ခုကို focus လုပ်ဖို့ပါ
    """,
    'category': 'Tools',
    'author': 'Odoo Learner',
    'depends': ['base'],
    'data': [
        'security/ir.model.access.csv',
        'views/practice_note_views.xml',
        'views/menu.xml',
    ],
    # 'installable': True,
    # 'application': True,
    'license': 'LGPL-3',
}
