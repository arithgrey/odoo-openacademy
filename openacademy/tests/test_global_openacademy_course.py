from psycopg2 import IntegrityError
from odoo.tests.common import TransactionCase
from odoo.tools import mute_logger


class GlobalTestOpenAcademyCourse(TransactionCase):

    def setUp(self):
        super(GlobalTestOpenAcademyCourse, self).setUp()
        self.course = self.env['openacademy.course']

    @mute_logger('odoo.sql_db')
    def create_course(self, name, description, responsible_id):
        course_id = self.course.create({
            'name': name,
            'description': description,
            'responsible_id': responsible_id
        })
        return course_id

    @mute_logger('odoo.sql_db')
    def test_01_same_name_course(self):

        part_msj = 'new row for relation "openacademy_course" violates check constraint '
        message_error = part_msj + '"openacademy_course_name_description_check"'
        with self.assertRaisesRegexp(IntegrityError, message_error):
            self.create_course('test', 'test', None)

    def test_duplicate_course(self):

        course = self.env.ref('openacademy.course0')
        course_id = course.copy()
        print ('course_id', course_id)
