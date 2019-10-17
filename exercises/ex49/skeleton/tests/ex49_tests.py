# -*- coding: utf-8 -*-
from nose.tools import *
from ex49.ex49 import *


def test_sentence():
    sentence = Sentence(('noun', 'apple'), ('verb', 'eat'), ('direction', 'good'))
    assert_equal(sentence.subject, 'apple')


def test_peek():
    peek1 = peek([('noun', 'apple'), ('verb', 'eat'), ('direction', 'good')])
    peek2 = peek([('direction', 'good')])
    peek3 = peek([])
    assert_equal(peek1, 'noun')
    assert_equal(peek2, 'direction')
    assert_equal(peek3, None)


def test_match():
    match1 = match([('verb', 'eat'), ('noun', 'apple')], 'verb')
    assert_equal(match1, ('verb', 'eat'))


def test_parse_subject():
    last_sentence = parse_subject([('verb', 'eat'), ('direction', 'nice')], ('noun', 'apple'))
    assert_equal(last_sentence.verb, 'eat')
