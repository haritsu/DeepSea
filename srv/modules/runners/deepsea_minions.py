# -*- coding: utf-8 -*-

import salt.client
import sys
import os
import logging

log = logging.getLogger(__name__)

class DeepseaMinions(object):
    """
    """

    def __init__(self, **kwargs):
        """
        """
        self.local = salt.client.LocalClient()
        self.deepsea_minions = self._query()
        self.matches = self._matches()
       

    def _query(self):
        """
        """
        # When search matches no minions, salt prints to stdout.  
        # Suppress stdout.
        _stdout = sys.stdout
        sys.stdout = open(os.devnull, 'w')

        ret = self.local.cmd('*' , 'saltutil.pillar_refresh')
        minions = self.local.cmd('*' , 'pillar.get', [ 'deepsea_minions' ], 
                            expr_form="compound")
        sys.stdout = _stdout
        for minion in minions:
            if minions[minion]:
                return minions[minion]
           
        
        log.error("deepsea_minions is not set")
        return []

    def _matches(self):
        """
        """
        if self.deepsea_minions:
            # When search matches no minions, salt prints to stdout.  
            # Suppress stdout.
            _stdout = sys.stdout
            sys.stdout = open(os.devnull, 'w')
            matches = self.local.cmd(self.deepsea_minions , 'pillar.get', [ 'id' ], 
                                expr_form="compound")
            sys.stdout = _stdout
            return matches.keys()
        return []

def help():
    """
    Usage
    """
    usage = ('salt-run deepsea_minions.show:\n\n'
             '    Displays deepsea_minions value\n'
             '\n\n'
             'salt-run deepsea_minions.matches:\n\n'
             '    Returns an array of matched minions\n'
             '\n\n'
    )
    print usage
    return ""


def show(**kwargs):
    """
    Returns deepsea_minions value
    """
    target = DeepseaMinions()
    return target.deepsea_minions

def matches(**kwargs):
    """
    Returns array of matched minions
    """
    target = DeepseaMinions()
    return target.matches
