from time import sleep
from ctrlibrary.threatresponse.enrich import enrich_observe_observables


def test_smoke_integrations_errors(observables, module_headers):
    """Perform testing for enrich observe observable endpoint to check that all
    modules, which installed in organization, doesn't throw errors on formed
    dataset

    ID: CCTRI-1696-5cbc9224-0653-498a-af9a-afe1a0d379b0

    Steps:
        1. Send request to enrich observe observable endpoint with provided
        dataset

    Expectedresults:
        1. Response body contains from all modules doesn't contains errors

    Importance: Critical
    """
    response_from_all_modules = enrich_observe_observables(
        payload=[observables],
        **{'headers': module_headers}
    )

    errors = response_from_all_modules.get('errors', [])
    errors_info = dict()
    
    sleep(30)

    if errors:
        for module in errors:
            if module["code"] != 'too many requests':
                errors_info[module["module"]] = module["message"]

        if errors_info:
            raise AssertionError(f'There was an error in such module/modules '
                                 f'{list(errors_info.items())}'
                                 )
