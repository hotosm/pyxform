# -*- coding: utf-8 -*-
"""
Test setting form name to data.
"""
from pyxform.tests_v1.pyxform_test_case import PyxformTestCase

class InlineTranslationsTest(PyxformTestCase):

    def test_inline_translations(self):
        """
        Test using data as the name of the form which will generate <data />.
        """
        self.assertPyxformXform(
            md="""
               | survey  |                   |          |            |               |
               |         | type              | name     | label      | choice_filter |
               |         | select_one states | state    | State Name | state != ''   |
               | choices |                   |          |            |
               |         | list name         | name     | label      |
               |         | states            | option a | a          |
               |         | states            | option b | b          |
               |         | states            | option c | c          |
               """,
            name='data',
            id_string='some-id',
            model__contains=['<label>a</label>', '<label>b</label>', '<label>c</label>'],
            model__excludes=['<text id="static_instance-states-0">',
                             '<text id="static_instance-states-1">',
                             '<text id="static_instance-states-2">',
                             '<itextId>static_instance-states-0</itextId>',
                             '<itextId>static_instance-states-1</itextId>',
                             '<itextId>static_instance-states-2</itextId>'],
            xml__contains=['<label ref="label"/>'],
            xml__excludes=['<label ref="jr:itext(itextId)"/>'],
        )

    def test_multiple_translations(self):
        """
        Test using data as the name of the form which will generate <data />.
        """
        self.assertPyxformXform(
            md="""
               | survey  |                   |          |            |               |
               |         | type              | name     | label      | choice_filter |
               |         | select_one states | state    | State Name | state != ''   |
               | choices |                   |          |            |
               |         | list name         | name     | label::English(en)|
               |         | states            | option a | a                 |
               |         | states            | option b | b                 |
               |         | states            | option c | c                 |
               """,
            name='data',
            id_string='some-id',
            model__contains=['<text id="static_instance-states-0">',
                             '<text id="static_instance-states-1">',
                             '<text id="static_instance-states-2">',
                             '<itextId>static_instance-states-0</itextId>',
                             '<itextId>static_instance-states-1</itextId>',
                             '<itextId>static_instance-states-2</itextId>'],
            model__excludes=['<label>a</label>', '<label>b</label>', '<label>c</label>'],
            xml__contains=['<label ref="jr:itext(itextId)"/>'],
            xml__excludes=['<label ref="label"/>'],
        )
