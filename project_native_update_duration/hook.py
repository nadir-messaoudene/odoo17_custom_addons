from odoo import api, SUPERUSER_ID

def post_init_hook(cr, registry):
    # copy data to native_duration and drop column duration from project_task if exist bouth columns
    update = False

    cr.execute("SELECT column_name FROM information_schema.columns WHERE table_name='project_task' AND "
               "column_name='duration'")

    if cr.fetchone():
        update = True

    if update:
        cr.execute("SELECT column_name FROM information_schema.columns WHERE table_name='project_task' AND "
                   "column_name='native_duration'")
        if cr.fetchone():
            cr.execute("UPDATE project_task SET native_duration=duration WHERE duration IS NOT NULL")
            cr.execute("ALTER TABLE project_task DROP COLUMN duration")

