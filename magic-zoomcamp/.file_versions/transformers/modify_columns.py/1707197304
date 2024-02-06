if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    COLUMN_MAP = {
        'VendorID': 'vendor_id'
    }
    data.rename(columns=COLUMN_MAP, inplace=True)
    data['lpep_pickup_date'] = data['lpep_pickup_datetime'].dt.date
    return data


@test
def test_output(output, *args):
    assert output['passenger_count'].isin([0]).sum() == 0, 'There are rides with zero passengers'
