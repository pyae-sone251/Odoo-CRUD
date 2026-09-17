# -*- coding: utf-8 -*-
from odoo import models, fields, api


class PracticeNote(models.Model):
    _name = 'practice.note'
    _description = 'Practice Note (CRUD Demo)'

    name = fields.Char(string='Title', required=True)
    content = fields.Text(string='Content')

    # ဒီ field ကို read() method ရဲ့ result ကို user မြင်ရအောင်
    # screen ပေါ်မှာ ပြသဖို့အတွက်ပဲ ထားထားတာပါ
    last_read_result = fields.Text(string='Last read() Result', readonly=True)

    # =========================================================
    # 1) CREATE demo
    # =========================================================
    # ဒီ button ကို နှိပ်လိုက်ရင် "self" (ရှိပြီးသား record) ရဲ့
    # name/content ကို copy ယူပြီး create() နဲ့ record အသစ်တစ်ခု
    # ဖန်တီးမယ် - "Duplicate" ပုံစံ
    def action_demo_create(self):
        self.ensure_one()

        # create() ကို dictionary payload ({field: value}) နဲ့ပဲ
        # ခေါ်ရတယ် - ဒါက record အသစ်တစ်ခု database ထဲ INSERT လုပ်တာပါ
        new_note = self.create({
            'name': f'{self.name} (Copy)',
            'content': self.content,
        })

        # create() ရဲ့ return value က record (recordset) ဖြစ်တဲ့အတွက်
        # new_note.id ကို တိုက်ရိုက် access လုပ်လို့ရတယ်
        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'title': 'create() ခေါ်ပြီးပါပြီ',
                'message': f'Record အသစ် ID={new_note.id} ကို create() နဲ့ ဖန်တီးလိုက်ပါပြီ',
                'type': 'success',
            },
        }

    # =========================================================
    # 2) WRITE demo
    # =========================================================
    # ဒီ button ကို နှိပ်လိုက်ရင် content field ရဲ့ နောက်ဆုံးမှာ
    # "[Reviewed]" ဆိုတဲ့ text ကို write() နဲ့ ထပ်ဆင့်ထည့်ပေးမယ်
    def action_demo_write(self):
        self.ensure_one()

        old_content = self.content or ''

        # write() ကို "ရှိပြီးသား" record (self) ပေါ်မှာပဲ ခေါ်ရတယ်
        # create() လိုမျိုး record အသစ် ဖန်တီးတာ မဟုတ်ဘဲ
        # database ထဲက row ရှိပြီးသားကို UPDATE လုပ်ခြင်းသာ ဖြစ်တယ်
        self.write({
            'content': f'{old_content}\n[Reviewed at write()]',
        })

        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'title': 'write() ခေါ်ပြီးပါပြီ',
                'message': 'Content field ကို write() နဲ့ update လုပ်လိုက်ပါပြီ',
                'type': 'success',
            },
        }

    # =========================================================
    # 3) READ demo
    # =========================================================
    # read() ရဲ့ return value ဟာ recordset မဟုတ်ဘဲ
    # dictionary list ဖြစ်ကြောင်း တိုက်ရိုက် မြင်ရအောင် ပြထားတာ
    def action_demo_read(self):
        self.ensure_one()

        # read() ကို field name list ပေးပြီးခေါ်ရတယ်
        # result က [{'id': 3, 'name': '...', 'content': '...'}]
        # ပုံစံ dictionary list ဖြစ်တယ် (recordset မဟုတ်ပါ)
        result = self.read(['name', 'content'])

        # result[0] နဲ့ ပထမဆုံး (တစ်ခုတည်းရှိတဲ့) dictionary ကို ယူတယ်
        # ဒီ data ကို last_read_result field ထဲ ထည့်ပြီး
        # user မြင်အောင် ပြထားတာ - ORM method ဆိုတာ python object
        # မဟုတ်ဘဲ raw dict/list ပြန်တာလည်း ရှိတယ်ဆိုတာ ပြချင်လို့
        self.write({'last_read_result': str(result[0])})

        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'title': 'read() ခေါ်ပြီးပါပြီ',
                'message': 'Result ကို "Last read() Result" field မှာ ကြည့်ပါ',
                'type': 'info',
            },
        }

    # =========================================================
    # 4) UNLINK demo
    # =========================================================
    def action_demo_unlink(self):
        self.ensure_one()

        note_name = self.name

        # unlink() ကို parameter မလိုဘဲ ဒီ record ပေါ်မှာ ခေါ်ရုံပါပဲ
        # ခေါ်လိုက်ပြီးရင် database ထဲက row ကို အပြီးတိုင် ဖျက်ပစ်မယ်
        # (ပြန်ယူလို့ မရတော့ပါ)
        self.unlink()

        # unlink() လုပ်ပြီးတာနဲ့ self ဟာ database ထဲ မရှိတော့ပါ
        # ဒီတော့ form ကို ပိတ်ပြီး list view ကို ပြန်ပို့ရတယ်
        return {
            'type': 'ir.actions.client',
            'tag': 'display_notification',
            'params': {
                'title': 'unlink() ခေါ်ပြီးပါပြီ',
                'message': f'"{note_name}" ကို database ကနေ ဖျက်လိုက်ပါပြီ',
                'type': 'warning',
                'next': {'type': 'ir.actions.act_window_close'},
            },
        }
