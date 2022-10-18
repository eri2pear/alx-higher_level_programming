#!/usr/bin/python3
"""This module is the the class LocckdClass"""


class LockedClass():
    """ prevents creating new instance attributes, \
        except if the new instance is called first_name"""
	__slots__ = ["first_name"]
	def __init__(self, first_name=''):
	        self.first_name = first_name
