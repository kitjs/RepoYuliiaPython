import pytest
import mensa_lu_explicilty as mensa
import mensa_lu_implicilty as m_i


def fill_in_all_test():
    mensa.start_win()
    mensa.fill_in_fields()

def fill_in_all_test_impl():
    m_i.start_win_2()
    m_i.fill_in_fields_2()


# fill_in_all_test()
fill_in_all_test_impl()