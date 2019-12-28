from utils.data_format import *

test_data = [{'_id': {'$oid': '5df1bfa0ed520428cd56ac86'}, 'name': 'San Diego Smile Dentistry', 'abbreviation': 'SD Smile', 'address': '7710 Balboa Ave', 'address2': '', 'city': 'San Diego', 'state': 'ca', 'postal_code': '92111', 'area': 'sd', 'phone': '(619) 737-6453', 'website': 'https://sd-smile.com', 'latitude': 32.82225, 'longitude': -117.157913, 'cleaning': 95, 'filling': 140, 'extraction': 110, 'root_canal': 725, 'crown': 850, 'mock_data': True, 'is_active': True},
            {'_id': {'$oid': '5df1c076ed520428cd56ac87'}, 'name': 'Great Smile Dental', 'abbreviation': 'Great Smile', 'address': '5210 Balboa Ave', 'address2': '', 'city': 'San Diego', 'state': 'ca', 'postal_code': '92117', 'area': 'sd', 'phone': '(858) 598-5842', 'website': 'https://great-smile-dental-orthodontics-and-periodontics.business.site/', 'latitude': 32.81897, 'longitude': -117.183968, 'cleaning': 105, 'filling': 120, 'extraction': 110, 'root_canal': 765, 'crown': 1105, 'mock_data': True, 'is_active': True},
            {'_id': {'$oid': '5dfce6692fa10ed564c1c264'}, 'name': 'Advanced Smiles Dentistry', 'abbreviation': 'Adv Smiles', 'address': 'German Gedovius 10489', 'address2': '', 'city': 'Zona Rio', 'state': 'baja', 'postal_code': '22010', 'area': 'tj', 'phone': '(619) 488-1557', 'website': 'https://advancedsmilesdentistry.com/', 'latitude': 32.519606, 'longitude': -117.011157, 'cleaning': 40, 'filling': 40, 'extraction': 90, 'root_canal': 250, 'crown': 450, 'mock_data': False, 'is_active': True},
            {'_id': {'$oid': '5dfce77e2fa10ed564c1c265'}, 'name': 'I Love My Dentist', 'abbreviation': 'Love', 'address': 'Av Revolucion 868', 'address2': '', 'city': 'Zona Centro', 'state': 'baja', 'postal_code': '22000', 'area': 'tj', 'phone': '(619) 452-2823', 'website': 'https://ilovemydentist.com.mx', 'latitude': 32.526848, 'longitude': -117.036049, 'cleaning': 45, 'filling': 75, 'extraction': 80, 'root_canal': 400, 'crown': 398, 'mock_data': False, 'is_active': True}]



result = restructure_dental_json(test_data)

assert result == [{'_id': {'$oid': '5df1bfa0ed520428cd56ac86'}, 'name': 'San Diego Smile Dentistry', 'abbreviation': 'SD Smile', 'address': '7710 Balboa Ave', 'address2': '', 'city': 'San Diego', 'state': 'CA', 'postal_code': '92111', 'area': 'sd', 'phone': '(619) 737-6453', 'website': 'https://sd-smile.com', 'latitude': 32.82225, 'longitude': -117.157913, 'cleaning': 95, 'filling': 140, 'extraction': 110, 'root_canal': 725, 'crown': 850, 'is_active': True, 'fake_data': 'Mock Data'},\
                  {'_id': {'$oid': '5df1c076ed520428cd56ac87'}, 'name': 'Great Smile Dental', 'abbreviation': 'Great Smile', 'address': '5210 Balboa Ave', 'address2': '', 'city': 'San Diego', 'state': 'CA', 'postal_code': '92117', 'area': 'sd', 'phone': '(858) 598-5842', 'website': 'https://great-smile-dental-orthodontics-and-periodontics.business.site/', 'latitude': 32.81897, 'longitude': -117.183968, 'cleaning': 105, 'filling': 120, 'extraction': 110, 'root_canal': 765, 'crown': 1105, 'is_active': True, 'fake_data': 'Mock Data'},\
                  {'_id': {'$oid': '5dfce6692fa10ed564c1c264'}, 'name': 'Advanced Smiles Dentistry', 'abbreviation': 'Adv Smiles', 'address': 'German Gedovius 10489', 'address2': '', 'city': 'Tijuana', 'state': 'baja', 'postal_code': '22010', 'area': 'tj', 'phone': '(619) 488-1557', 'website': 'https://advancedsmilesdentistry.com/', 'latitude': 32.519606, 'longitude': -117.011157, 'cleaning': 40, 'filling': 40, 'extraction': 90, 'root_canal': 250, 'crown': 450, 'is_active': True, 'fake_data': 'Actual Data'},\
                  {'_id': {'$oid': '5dfce77e2fa10ed564c1c265'}, 'name': 'I Love My Dentist', 'abbreviation': 'Love', 'address': 'Av Revolucion 868', 'address2': '', 'city': 'Tijuana', 'state': 'baja', 'postal_code': '22000', 'area': 'tj', 'phone': '(619) 452-2823', 'website': 'https://ilovemydentist.com.mx', 'latitude': 32.526848, 'longitude': -117.036049, 'cleaning': 45, 'filling': 75, 'extraction': 80, 'root_canal': 400, 'crown': 398, 'is_active': True, 'fake_data': 'Actual Data'}], 'result matches expectation'

assert result[0]['city'] == 'San Diego', 'Got expected value of San Diego'
assert result[3]['city'] == 'Tijuana', 'Got expected value of Tijuana'

new_json = expand_data(result)

assert new_json == [{'_id': {'$oid': '5df1bfa0ed520428cd56ac86'}, 'name': 'San Diego Smile Dentistry', 'abbreviation': 'SD Smile', 'address': '7710 Balboa Ave', 'address2': '', 'city': 'San Diego', 'state': 'CA', 'postal_code': '92111', 'area': 'sd', 'phone': '(619) 737-6453', 'website': 'https://sd-smile.com', 'latitude': 32.82225, 'longitude': -117.157913, 'cleaning': 95, 'filling': 140, 'extraction': 110, 'root_canal': 725, 'crown': 850, 'is_active': True, 'fake_data': 'Mock Data', 'procedure': 'Adult Cleaning', 'cost': 95},\
                    {'_id': {'$oid': '5df1bfa0ed520428cd56ac86'}, 'name': 'San Diego Smile Dentistry', 'abbreviation': 'SD Smile', 'address': '7710 Balboa Ave', 'address2': '', 'city': 'San Diego', 'state': 'CA', 'postal_code': '92111', 'area': 'sd', 'phone': '(619) 737-6453', 'website': 'https://sd-smile.com', 'latitude': 32.82225, 'longitude': -117.157913, 'cleaning': 95, 'filling': 140, 'extraction': 110, 'root_canal': 725, 'crown': 850, 'is_active': True, 'fake_data': 'Mock Data', 'procedure': 'Composite Filling', 'cost': 140},\
                    {'_id': {'$oid': '5df1bfa0ed520428cd56ac86'}, 'name': 'San Diego Smile Dentistry', 'abbreviation': 'SD Smile', 'address': '7710 Balboa Ave', 'address2': '', 'city': 'San Diego', 'state': 'CA', 'postal_code': '92111', 'area': 'sd', 'phone': '(619) 737-6453', 'website': 'https://sd-smile.com', 'latitude': 32.82225, 'longitude': -117.157913, 'cleaning': 95, 'filling': 140, 'extraction': 110, 'root_canal': 725, 'crown': 850, 'is_active': True, 'fake_data': 'Mock Data', 'procedure': 'Extraction', 'cost': 110},\
                    {'_id': {'$oid': '5df1bfa0ed520428cd56ac86'}, 'name': 'San Diego Smile Dentistry', 'abbreviation': 'SD Smile', 'address': '7710 Balboa Ave', 'address2': '', 'city': 'San Diego', 'state': 'CA', 'postal_code': '92111', 'area': 'sd', 'phone': '(619) 737-6453', 'website': 'https://sd-smile.com', 'latitude': 32.82225, 'longitude': -117.157913, 'cleaning': 95, 'filling': 140, 'extraction': 110, 'root_canal': 725, 'crown': 850, 'is_active': True, 'fake_data': 'Mock Data', 'procedure': 'Root Canal', 'cost': 725},\
                    {'_id': {'$oid': '5df1bfa0ed520428cd56ac86'}, 'name': 'San Diego Smile Dentistry', 'abbreviation': 'SD Smile', 'address': '7710 Balboa Ave', 'address2': '', 'city': 'San Diego', 'state': 'CA', 'postal_code': '92111', 'area': 'sd', 'phone': '(619) 737-6453', 'website': 'https://sd-smile.com', 'latitude': 32.82225, 'longitude': -117.157913, 'cleaning': 95, 'filling': 140, 'extraction': 110, 'root_canal': 725, 'crown': 850, 'is_active': True, 'fake_data': 'Mock Data', 'procedure': 'Porcelain Crown', 'cost': 850},\
                    {'_id': {'$oid': '5df1c076ed520428cd56ac87'}, 'name': 'Great Smile Dental', 'abbreviation': 'Great Smile', 'address': '5210 Balboa Ave', 'address2': '', 'city': 'San Diego', 'state': 'CA', 'postal_code': '92117', 'area': 'sd', 'phone': '(858) 598-5842', 'website': 'https://great-smile-dental-orthodontics-and-periodontics.business.site/', 'latitude': 32.81897, 'longitude': -117.183968, 'cleaning': 105, 'filling': 120, 'extraction': 110, 'root_canal': 765, 'crown': 1105, 'is_active': True, 'fake_data': 'Mock Data', 'procedure': 'Adult Cleaning', 'cost': 105},\
                    {'_id': {'$oid': '5df1c076ed520428cd56ac87'}, 'name': 'Great Smile Dental', 'abbreviation': 'Great Smile', 'address': '5210 Balboa Ave', 'address2': '', 'city': 'San Diego', 'state': 'CA', 'postal_code': '92117', 'area': 'sd', 'phone': '(858) 598-5842', 'website': 'https://great-smile-dental-orthodontics-and-periodontics.business.site/', 'latitude': 32.81897, 'longitude': -117.183968, 'cleaning': 105, 'filling': 120, 'extraction': 110, 'root_canal': 765, 'crown': 1105, 'is_active': True, 'fake_data': 'Mock Data', 'procedure': 'Composite Filling', 'cost': 120},\
                    {'_id': {'$oid': '5df1c076ed520428cd56ac87'}, 'name': 'Great Smile Dental', 'abbreviation': 'Great Smile', 'address': '5210 Balboa Ave', 'address2': '', 'city': 'San Diego', 'state': 'CA', 'postal_code': '92117', 'area': 'sd', 'phone': '(858) 598-5842', 'website': 'https://great-smile-dental-orthodontics-and-periodontics.business.site/', 'latitude': 32.81897, 'longitude': -117.183968, 'cleaning': 105, 'filling': 120, 'extraction': 110, 'root_canal': 765, 'crown': 1105, 'is_active': True, 'fake_data': 'Mock Data', 'procedure': 'Extraction', 'cost': 110},\
                    {'_id': {'$oid': '5df1c076ed520428cd56ac87'}, 'name': 'Great Smile Dental', 'abbreviation': 'Great Smile', 'address': '5210 Balboa Ave', 'address2': '', 'city': 'San Diego', 'state': 'CA', 'postal_code': '92117', 'area': 'sd', 'phone': '(858) 598-5842', 'website': 'https://great-smile-dental-orthodontics-and-periodontics.business.site/', 'latitude': 32.81897, 'longitude': -117.183968, 'cleaning': 105, 'filling': 120, 'extraction': 110, 'root_canal': 765, 'crown': 1105, 'is_active': True, 'fake_data': 'Mock Data', 'procedure': 'Root Canal', 'cost': 765},\
                    {'_id': {'$oid': '5df1c076ed520428cd56ac87'}, 'name': 'Great Smile Dental', 'abbreviation': 'Great Smile', 'address': '5210 Balboa Ave', 'address2': '', 'city': 'San Diego', 'state': 'CA', 'postal_code': '92117', 'area': 'sd', 'phone': '(858) 598-5842', 'website': 'https://great-smile-dental-orthodontics-and-periodontics.business.site/', 'latitude': 32.81897, 'longitude': -117.183968, 'cleaning': 105, 'filling': 120, 'extraction': 110, 'root_canal': 765, 'crown': 1105, 'is_active': True, 'fake_data': 'Mock Data', 'procedure': 'Porcelain Crown', 'cost': 1105},\
                    {'_id': {'$oid': '5dfce6692fa10ed564c1c264'}, 'name': 'Advanced Smiles Dentistry', 'abbreviation': 'Adv Smiles', 'address': 'German Gedovius 10489', 'address2': '', 'city': 'Tijuana', 'state': 'baja', 'postal_code': '22010', 'area': 'tj', 'phone': '(619) 488-1557', 'website': 'https://advancedsmilesdentistry.com/', 'latitude': 32.519606, 'longitude': -117.011157, 'cleaning': 40, 'filling': 40, 'extraction': 90, 'root_canal': 250, 'crown': 450, 'is_active': True, 'fake_data': 'Actual Data', 'procedure': 'Adult Cleaning', 'cost': 40},\
                    {'_id': {'$oid': '5dfce6692fa10ed564c1c264'}, 'name': 'Advanced Smiles Dentistry', 'abbreviation': 'Adv Smiles', 'address': 'German Gedovius 10489', 'address2': '', 'city': 'Tijuana', 'state': 'baja', 'postal_code': '22010', 'area': 'tj', 'phone': '(619) 488-1557', 'website': 'https://advancedsmilesdentistry.com/', 'latitude': 32.519606, 'longitude': -117.011157, 'cleaning': 40, 'filling': 40, 'extraction': 90, 'root_canal': 250, 'crown': 450, 'is_active': True, 'fake_data': 'Actual Data', 'procedure': 'Composite Filling', 'cost': 40},\
                    {'_id': {'$oid': '5dfce6692fa10ed564c1c264'}, 'name': 'Advanced Smiles Dentistry', 'abbreviation': 'Adv Smiles', 'address': 'German Gedovius 10489', 'address2': '', 'city': 'Tijuana', 'state': 'baja', 'postal_code': '22010', 'area': 'tj', 'phone': '(619) 488-1557', 'website': 'https://advancedsmilesdentistry.com/', 'latitude': 32.519606, 'longitude': -117.011157, 'cleaning': 40, 'filling': 40, 'extraction': 90, 'root_canal': 250, 'crown': 450, 'is_active': True, 'fake_data': 'Actual Data', 'procedure': 'Extraction', 'cost': 90},\
                    {'_id': {'$oid': '5dfce6692fa10ed564c1c264'}, 'name': 'Advanced Smiles Dentistry', 'abbreviation': 'Adv Smiles', 'address': 'German Gedovius 10489', 'address2': '', 'city': 'Tijuana', 'state': 'baja', 'postal_code': '22010', 'area': 'tj', 'phone': '(619) 488-1557', 'website': 'https://advancedsmilesdentistry.com/', 'latitude': 32.519606, 'longitude': -117.011157, 'cleaning': 40, 'filling': 40, 'extraction': 90, 'root_canal': 250, 'crown': 450, 'is_active': True, 'fake_data': 'Actual Data', 'procedure': 'Root Canal', 'cost': 250},\
                    {'_id': {'$oid': '5dfce6692fa10ed564c1c264'}, 'name': 'Advanced Smiles Dentistry', 'abbreviation': 'Adv Smiles', 'address': 'German Gedovius 10489', 'address2': '', 'city': 'Tijuana', 'state': 'baja', 'postal_code': '22010', 'area': 'tj', 'phone': '(619) 488-1557', 'website': 'https://advancedsmilesdentistry.com/', 'latitude': 32.519606, 'longitude': -117.011157, 'cleaning': 40, 'filling': 40, 'extraction': 90, 'root_canal': 250, 'crown': 450, 'is_active': True, 'fake_data': 'Actual Data', 'procedure': 'Porcelain Crown', 'cost': 450},\
                    {'_id': {'$oid': '5dfce77e2fa10ed564c1c265'}, 'name': 'I Love My Dentist', 'abbreviation': 'Love', 'address': 'Av Revolucion 868', 'address2': '', 'city': 'Tijuana', 'state': 'baja', 'postal_code': '22000', 'area': 'tj', 'phone': '(619) 452-2823', 'website': 'https://ilovemydentist.com.mx', 'latitude': 32.526848, 'longitude': -117.036049, 'cleaning': 45, 'filling': 75, 'extraction': 80, 'root_canal': 400, 'crown': 398, 'is_active': True, 'fake_data': 'Actual Data', 'procedure': 'Adult Cleaning', 'cost': 45},\
                    {'_id': {'$oid': '5dfce77e2fa10ed564c1c265'}, 'name': 'I Love My Dentist', 'abbreviation': 'Love', 'address': 'Av Revolucion 868', 'address2': '', 'city': 'Tijuana', 'state': 'baja', 'postal_code': '22000', 'area': 'tj', 'phone': '(619) 452-2823', 'website': 'https://ilovemydentist.com.mx', 'latitude': 32.526848, 'longitude': -117.036049, 'cleaning': 45, 'filling': 75, 'extraction': 80, 'root_canal': 400, 'crown': 398, 'is_active': True, 'fake_data': 'Actual Data', 'procedure': 'Composite Filling', 'cost': 75},\
                    {'_id': {'$oid': '5dfce77e2fa10ed564c1c265'}, 'name': 'I Love My Dentist', 'abbreviation': 'Love', 'address': 'Av Revolucion 868', 'address2': '', 'city': 'Tijuana', 'state': 'baja', 'postal_code': '22000', 'area': 'tj', 'phone': '(619) 452-2823', 'website': 'https://ilovemydentist.com.mx', 'latitude': 32.526848, 'longitude': -117.036049, 'cleaning': 45, 'filling': 75, 'extraction': 80, 'root_canal': 400, 'crown': 398, 'is_active': True, 'fake_data': 'Actual Data', 'procedure': 'Extraction', 'cost': 80},\
                    {'_id': {'$oid': '5dfce77e2fa10ed564c1c265'}, 'name': 'I Love My Dentist', 'abbreviation': 'Love', 'address': 'Av Revolucion 868', 'address2': '', 'city': 'Tijuana', 'state': 'baja', 'postal_code': '22000', 'area': 'tj', 'phone': '(619) 452-2823', 'website': 'https://ilovemydentist.com.mx', 'latitude': 32.526848, 'longitude': -117.036049, 'cleaning': 45, 'filling': 75, 'extraction': 80, 'root_canal': 400, 'crown': 398, 'is_active': True, 'fake_data': 'Actual Data', 'procedure': 'Root Canal', 'cost': 400},\
                    {'_id': {'$oid': '5dfce77e2fa10ed564c1c265'}, 'name': 'I Love My Dentist', 'abbreviation': 'Love', 'address': 'Av Revolucion 868', 'address2': '', 'city': 'Tijuana', 'state': 'baja', 'postal_code': '22000', 'area': 'tj', 'phone': '(619) 452-2823', 'website': 'https://ilovemydentist.com.mx', 'latitude': 32.526848, 'longitude': -117.036049, 'cleaning': 45, 'filling': 75, 'extraction': 80, 'root_canal': 400, 'crown': 398, 'is_active': True, 'fake_data': 'Actual Data', 'procedure': 'Porcelain Crown', 'cost': 398}], 'result matches expectation'

assert len(new_json) == 20, 'Expected 4 json objects to be expanded into 20'
assert new_json[4]['procedure'] == 'Porcelain Crown'
assert new_json[8]['cost'] == 765

