from psycopg2 import IntegrityError
from odoo import exceptions
from odoo.tests import common
from odoo.tools import mute_logger


class GlobalTestOpenAcademySession(common.TransactionCase):
    # Global test for openacademy module,
    # Test session

    # Pseudo-constructor method of test setUp
    def setUp(self):
        # Define global variables to test methods
        super(GlobalTestOpenAcademySession, self).setUp()
        self.session = self.env['openacademy.session']
        self.course = self.env.ref('openacademy.course0')
        self.partner = self.env.ref('base.res_partner_1')
        self.attendee = self.env.ref('base.res_partner_2')

    # Class methods (Isn't a test)

    # Create session function
    def create_session(self, session_name, session_seats,
                       session_instructor_id, session_attendee_ids, session_course_id):
        session_id = self.session.create({
            'name': session_name,
            'seats': session_seats,
            'instructor_id': session_instructor_id,
            'attendee_ids': session_attendee_ids,
            'course_id': session_course_id,
        })
        return session_id

    # Tests methods (starts with: 'test_')

    def test_10_instructor_is_attendee(self):
        # Test: Create a session without instructor as attendee
        # Python constraint for instructor as attendee

        with self.assertRaisesRegexp(exceptions.ValidationError, 'A session\'s instructor can\'t'
                                                                 ' be an attendee'):
            self.create_session('Session Test Name', 2, self.partner.id,
                                [(6, 0, [self.partner.id])], self.course.id)

        print ("************" * 10, "OK SE COMPLETA EL TEST -> test_10_instructor_is_attendee")

    # Mute SQL error
    @mute_logger('odoo.sql_db')
    def test_20_session_without_course(self):
        # Test: Create a session without course
        # Python constraint for session without course

        with self.assertRaisesRegexp(IntegrityError, 'null value in column "course_id"'
                                                     ' violates not-null constraint'):
            self.create_session('Session Test Name', 2, self.partner.id,
                                [(6, 0, [self.partner.id])], None)

        print ("************" * 10, "OK SE COMPLETA EL TEST -> test_20_session_without_course")

    @mute_logger('odoo.sql_db')
    def test_30_create_valid_session(self):
        # Test: Create a session with valid parameters

        session = self.create_session('Session Test Name', 2, self.partner.id,
                                      [(6, 0, [self.attendee.id])], self.course.id)

        session_id = session.id
        new_session = self.session.search([('id', '=', "{}".format(session_id))])
        #import pdb;
        pdb.set_trace()
        self.assertTrue(new_session.id == session_id)

    print ("************" * 10, "OK SE COMPLETA EL TEST -> test_30_create_valid_session")
