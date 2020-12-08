
def gen_quiz(qpool, *args, altcodes, quiz):
    """qpool - seznam dvojic otázka a seznam odpovědí libovolný počet indexů do seznamu qpool
        sekvence, přes kterou lze projít konstrukcí for a která vrací řetězce, jež se mají ve výsledku předřadit (spolu s ': ') před každou z odpovědí 
        vstupní podoba kvízu ve formě seznamu dvojic otázka a seznam formátovaných odpovědí.
        >>> test_qpool1 = [('Question1', ['Answer1', 'Answer2', 'Answer3', 'Answer4']), ('Question2', ['Answer1', 'Answer2', 'Answer3']), ('Question3', ['Answer1', 'Answer2', 'Answer3', 'Answer4']), ('Question4', ['Answer1', 'Answer2'])]
    >>> existing_quiz1 = [('ExistingQuestion1', ['1: Answer1', '2: Answer2', '3: Answer3']), ('ExistingQuestion2', ['1: Answer1', '2: Answer2'])]
    >>> gen_quiz(test_qpool1, -2, 0, altcodes = ('10', '20', '30'), quiz = existing_quiz1)
    [('ExistingQuestion1', ['1: Answer1', '2: Answer2', '3: Answer3']), ('ExistingQuestion2', ['1: Answer1', '2: Answer2']), ('Question3', ['10: Answer1', '20: Answer2', '30: Answer3']), ('Question1', ['10: Answer1', '20: Answer2', '30: Answer3'])]
    """
    for arg in args:
        if (arg > len(qpool)):
            print("Ignoring index ",qpool," - <text výjimky>");
    for i in qpool:
        if(len(i[1]) > len(altcodes)):

if __name__ == "__main__":
    import doctest
    doctest.testmod()
