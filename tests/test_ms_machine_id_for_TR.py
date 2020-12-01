from ctrlibrary.threatresponse.enrich import enrich_observe_observables
from pytest import mark


@mark.skip(reason='Deprecated')
def test_ms_machine_id_doesnt_support_by_TR(module_headers):
    """Perform testing for verifying that 'ms_machine_id' type doesn't
    support by TR.

    ID: CCTRI-1957-f67174f1-6932-4247-bad4-807b5c31e486

    Steps:
        1. Send request to enrich observe observable endpoint

    Expectedresults:
        1. Check that response body doesn't contain data.

    Importance: Minor
    """
    observable = [{'type': 'ms_machine_id', 'value': 'test12345'}]
    response_from_all_modules = enrich_observe_observables(
        payload=observable,
        **{'headers': module_headers}
    )

    assert not response_from_all_modules.get('data')

    errors_with_ms_id = []
    for error in response_from_all_modules.get('errors'):
        if 'module_name' not in error:
            if 'ms_machine_id' in error['type']:
                errors_with_ms_id.append(error)
    assert errors_with_ms_id
