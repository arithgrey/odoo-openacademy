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
        message_error= 'new row for relation "openacademy_course" violates check constraint "openacademy_course_name_description_check"'
        with self.assertRaisesRegexp(IntegrityError, message_error):
            self.create_course('test', 'test' , None)


    def test_duplicate_course(self):
        '''
        Test Verifica que un curso se copie de fora correcta
        '''
        course = self.env.ref('openacademy.course0')
        #import  pdb; pdb.set_trace()
        course_id = course.copy()
        print ('course_id', course_id)


