from cnt_ruleseg import sentseg


def test_sentseg():
    text = (
        '测试句子一， 测试。  测试 句子二。 测试句子三！！！'
    )
    sents = sentseg(text)

    assert 3 == len(sents)

    sent1_text, sent1_range = sents[0]
    assert '测试句子一， 测试。' == sent1_text
    assert '测试句子一， 测试。' == text[sent1_range[0]:sent1_range[1]]

    sent2_text, sent2_range = sents[1]
    assert '测试 句子二。' == sent2_text
    assert '测试 句子二。' == text[sent2_range[0]:sent2_range[1]]

    sent3_text, sent3_range = sents[2]
    assert '测试句子三！！！' == sent3_text
    assert '测试句子三！！！' == text[sent3_range[0]:sent3_range[1]]