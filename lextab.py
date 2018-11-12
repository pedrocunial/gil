# lextab.py. This file automatically created by PLY (version 3.11). Don't edit!
_tabversion   = '3.10'
_lextokens    = set(('ASSIGNER', 'CLOSE_BRACKET', 'CLOSE_PARENT', 'COMMENT', 'DIV', 'ELSE', 'EQ', 'GT', 'ID', 'IF', 'LOOP', 'LT', 'MINUS', 'MULT', 'NUMBER', 'OPEN_BRACKET', 'OPEN_PARENT', 'PLUS'))
_lexreflags   = 64
_lexliterals  = ''
_lexstateinfo = {'INITIAL': 'inclusive'}
_lexstatere   = {'INITIAL': [('(?P<t_ID>[a-zA-Z_][a-zA-Z_0-9]*)|(?P<t_COMMENT>\\#.*)|(?P<t_NUMBER>\\d+)|(?P<t_newline>\\n+)|(?P<t_ASSIGNER>\\:=)|(?P<t_EQ>\\==)|(?P<t_PLUS>\\+)|(?P<t_MINUS>\\-)|(?P<t_MULT>\\*)|(?P<t_DIV>\\/)|(?P<t_OPEN_PARENT>\\()|(?P<t_CLOSE_PARENT>\\))|(?P<t_OPEN_BRACKET>\\{)|(?P<t_CLOSE_BRACKET>\\})|(?P<t_LT>\\<)|(?P<t_GT>\\>)', [None, ('t_ID', 'ID'), ('t_COMMENT', 'COMMENT'), ('t_NUMBER', 'NUMBER'), ('t_newline', 'newline'), (None, 'ASSIGNER'), (None, 'EQ'), (None, 'PLUS'), (None, 'MINUS'), (None, 'MULT'), (None, 'DIV'), (None, 'OPEN_PARENT'), (None, 'CLOSE_PARENT'), (None, 'OPEN_BRACKET'), (None, 'CLOSE_BRACKET'), (None, 'LT'), (None, 'GT')])]}
_lexstateignore = {'INITIAL': ' \t'}
_lexstateerrorf = {'INITIAL': 't_error'}
_lexstateeoff = {}
