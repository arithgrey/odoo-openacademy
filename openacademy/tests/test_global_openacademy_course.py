from psycopg2 import IntegrityError
from odoo.tests.common import TransactionCase
from odoo.tools import mute_logger

class GlobalTestOpenAcademyCourse(TransactionCase):

    def setUp(self):
        super(GlobalTestOpenAcademyCourse , self).setUp()
        self.variable = 'Hellow World'
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

        '''
        Se valida que no se pueda crear un curso con el mismo nombre
        '''
        with self.assertRaisesRegexp(IntegrityError, 'Error Integreity db UNIT TEST, no se pueden crear dos cursos con el mismo nombre'):
            self.create_course('test', 'test' , None)


