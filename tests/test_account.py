import pytest
from data import atm_data
from dsl.atm_check_methods import Atm
from home_work.hw6_api import HttpbinAPI, RestfulBookerAPI, ReqRes, SwaggerPet



@pytest.mark.sanity
def test_atm_flow():
    test = (Atm().check_account_is_created().
            check_money_added_to_account().
            check_money_withdrawal().
            check_pin())


@pytest.mark.regression
@pytest.mark.parametrize("add_value, withdraw_value, exp_result", [atm_data["pack1"],atm_data["pack2"],atm_data["pack3"]])
def test_atm_withdraw(account, add_value, withdraw_value, exp_result):
    account.add_money(add_value)
    assert account.withdraw(withdraw_value, "1234") == exp_result


@pytest.mark.contribution
def test_verify_contribution_amounts_are_correct():
    test = (Atm().
            verify_contribution_amounts_are_correct()
    )


# @pytest.mark.httpbin
def test_httpbin_API():
    test = (HttpbinAPI().
            get_auth_token().
            get_page().
            add_info()
    )


# @pytest.mark.api
def test_restful_booker_API():
    token = RestfulBookerAPI().auth_token()
    print(token)
    booking_id = RestfulBookerAPI().create_booking()
    print(booking_id)
    test = (RestfulBookerAPI().
            get_booking(booking_id, 1234).
            update_booking(booking_id, token)
    )
    print(test)


# @pytest.mark.api
def test_reqres_API(id=2):
    test = (
        ReqRes().get_user(id).create_user()
    )
    print(test.id)
    # user_id = test.id
    # test = test.get_user()


@pytest.mark.api
def test_swagger_pet():
    test = SwaggerPet().create_pet()
    id = test.id
    test = test.get_pet(id)
    previous_name = test.pet_name
    test = test.change_name()
    current_name = test.pet_name
    assert previous_name != current_name
    test.delete_item(id)