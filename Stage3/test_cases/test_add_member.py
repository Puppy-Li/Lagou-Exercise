import pytest

from Stage3.po.main_page import MainPage


class TestAddMember:
    @pytest.mark.parametrize("name", ["皮城女警"])
    def test_add_member(self, name):
        main_page = MainPage()
        # 1. go to add member page
        # 2. add a member, click and save then navigate to contact page
        # 3. get member list as assertion
        assert name in main_page.goto_add_member().add_member(name).get_member_list()

