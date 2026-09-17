from odoo import models,fields,api

class PracticleNote(models.Model):
    _name = 'practicle.note'
    _description = 'Practicle Note'

    name = fields.Char('Title')
    content = fields.Text('Context')
    last_read_result = fields.Text('Last Read Result',readonly=True)

    def action_create(self):
        self.ensure_one

        new = self.create({
            'name' : f'{self.name} /Copy',
            'content' : self.content,
        })

        return {
            'type' : 'ir.actions.client',
            'tag' : 'display_notification',
            'params' : {
                'title' : 'Create Success',
                'message' : 'Create Succcess',
                'type' : 'success',
            },
        }

    def action_write(self):
        self.ensure_one()

        old_content = self.content or ''
        self.write({
            'content' : f'{old_content}\n[Reviewed at write()]',
        })
        return{
            'type':'ir.actions.client',
            'tag':'display_notification',
            'params' : {
                'title' : 'Write Success',
                'message' : 'Content field update',
                'type' : 'success',
            },
        }

    def action_read(self):
        self.ensure_one()

        result = self.read(['name','content'])
        self.write({'last_read_result':str(result[0])})

        return{
            'type' : 'ir.actions.client',
            'tag' : 'display_notification',
            'params' : {
                'title' : 'Read Success',
                'message' : 'Result Success',
                'type' : 'success'
            }
        }

    def action_delete(self):
        self.ensure_one()
        d_name = self.name
        d_content = self.content

        self.unlink()
        return{
            'type' : 'ir.actions.client',
            'tag' : 'display_notification',
            'params' : {
                'title' : 'Success Unlink',
                'message' : 'Unlink record',
                'type' : 'danger',
                'next' : {'type':'ir.actions.act_window_close'},
            }
        }
    