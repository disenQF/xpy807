"""
面试题：

    synonyms = [
       ('beautiful', 'pretty'),
       ('mom', 'mommy'),
       ('quite', 'very'),
       ...
    ]

    输入两个句子，判断它们表达的意思是不是相同，相同返回True, 否则返回False
    例如：输入 "My mom is very beautiful" 和 "My mommy is quite pretty" , 返回True
          输入 "My dad is very pretty" 和 "My mommy is quite beautiful" , 返回 False

    请编写函数 is_synonymous(str1, str2),  synonyms 列表是给定的
"""

synonyms = [
    ('beautiful', 'pretty'),
    ('mom', 'mommy'),
    ('quite', 'very')
]


def is_synonymous(str1, str2):
    word_pairs = zip(str1.split(), str2.split())
    for word1, word2 in word_pairs:
        if word1 == word2:
            continue
        else:
            print(word1, word2, '查询是否为近意词')
            if (word1, word2) in synonyms or \
               (word2, word1) in synonyms:
                continue
            else:
                return False

    return True


if __name__ == '__main__':
    print(is_synonymous('My mom is very beautiful',
                  'My mommy is quite pretty'))

    print(is_synonymous('My dad is very pretty',
                  'My mommy is quite pretty'))
